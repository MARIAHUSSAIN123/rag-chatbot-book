import os, json, httpx
from http.server import BaseHTTPRequestHandler

G = os.environ["GEMINI_API_KEY"]
QURL, QKEY = os.environ["QDRANT_URL"].rstrip("/"), os.environ["QDRANT_API_KEY"]
BASE = "https://generativelanguage.googleapis.com/v1beta/models"
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")

SYSTEM = """You are a friendly expert teacher for an AI & Data Science course book.
You receive BOOK CONTEXT (excerpts from the book) and the recent chat.

Rules:
1. Book first: if the topic appears in the book context, say what the book covers about it (module/week if visible).
2. Then go in depth using your own knowledge: clear definition, why it matters, key steps or parts, a simple real-life example, and a short Python snippet when useful. You are NOT limited to the book text.
3. Label the two parts. English: "From the book:" and "More detail:". Roman Urdu: "Book ke mutabiq:" and "Tafseel:". If the topic is not in the book at all, skip the first part and say briefly that the book does not cover it, then explain anyway.
4. Reply in the language of the user's latest message: English, or Roman Urdu (Urdu written in English letters) when they write Roman Urdu.
5. Follow-ups like "isky bary mein", "explain more", "iska example" refer to the previous topic in the chat.
6. Format: plain text, **bold** for key terms, "- " bullets. No markdown headers or tables. Code goes in triple-backtick fences.
7. For greetings or small talk, answer in one or two friendly lines."""


def embed(text):
    r = httpx.post(f"{BASE}/gemini-embedding-001:embedContent?key={G}",
                   json={"content": {"parts": [{"text": text}]}, "outputDimensionality": 768}, timeout=30)
    return r.json()["embedding"]["values"]


class handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode())

    def do_POST(self):
        try:
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            q = body["question"]
            history = body.get("history", [])[-6:]

            # Follow-up sawalon ke liye search mein pichla user sawal bhi shamil
            prev_users = [h["text"] for h in history if h.get("role") == "user"][-2:]
            search_text = " ".join(prev_users + [q])[:1500]

            hits = httpx.post(f"{QURL}/collections/book/points/search",
                              headers={"api-key": QKEY},
                              json={"vector": embed(search_text), "limit": 6, "with_payload": True},
                              timeout=30).json().get("result", [])
            ctx = "\n\n".join(h["payload"]["text"] for h in hits) or "(nothing found)"
            chat = "\n".join(("User: " if h.get("role") == "user" else "Assistant: ") + h.get("text", "")[:600]
                             for h in history)
            prompt = f"BOOK CONTEXT:\n{ctx}\n\nRECENT CHAT:\n{chat or '(none)'}\n\nUSER'S LATEST MESSAGE: {q}"

            r = httpx.post(f"{BASE}/{MODEL}:generateContent?key={G}",
                           json={"systemInstruction": {"parts": [{"text": SYSTEM}]},
                                 "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                                 "generationConfig": {"maxOutputTokens": 1800, "temperature": 0.6}},
                           timeout=55).json()
            if "candidates" not in r:
                msg = r.get("error", {}).get("message") or str(r.get("promptFeedback") or r)
                self._send(200, {"answer": "Gemini error: " + msg})
                return
            parts = r["candidates"][0].get("content", {}).get("parts", [])
            answer = "".join(p.get("text", "") for p in parts) or "Jawab nahi mila, dobara try karein."
            self._send(200, {"answer": answer})
        except Exception as e:
            self._send(500, {"answer": "Server error: " + str(e)})
