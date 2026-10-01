import os, json, time, httpx
from http.server import BaseHTTPRequestHandler

G = os.environ["GEMINI_API_KEY"]
QURL, QKEY = os.environ["QDRANT_URL"].rstrip("/"), os.environ["QDRANT_API_KEY"]
BASE = "https://generativelanguage.googleapis.com/v1beta/models"
# Pehla model busy ho to agla try hota hai. Vercel env GEMINI_MODEL mein comma se naam de sakte hain.
COLL = os.environ.get("QDRANT_COLLECTION", "book")  # purani AI-DS book ka collection
MODELS = [m.strip() for m in os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite,gemini-3.5-flash,gemini-2.5-flash").split(",") if m.strip()]

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


def generate(payload):
    """Busy ya slow model par foran agla model try karta hai. (data, error) return karta hai."""
    start, last = time.time(), "unknown error"
    for model in MODELS:
        for attempt in range(2):
            left = 52 - (time.time() - start)
            if left < 5:
                return None, last
            try:
                data = httpx.post(f"{BASE}/{model}:generateContent?key={G}", json=payload,
                                  timeout=min(20, left)).json()
            except Exception as e:
                last = str(e) or "timeout"
                break                 # timeout/network: dobara wahi model nahi, seedha agla model
            if "candidates" in data:
                return data, None
            err = data.get("error", {})
            last = err.get("message") or str(data.get("promptFeedback") or data)
            code = err.get("code")
            if code in (429, 500, 503, 504):
                if attempt == 0:
                    time.sleep(1)
                continue              # ek dafa retry, phir agla model
            if code == 404:
                break                 # ye model nahi mila, agla try karo
            return None, last         # key ghalat / content blocked, retry ka faida nahi
    return None, last


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

            hits = httpx.post(f"{QURL}/collections/{COLL}/points/search",
                              headers={"api-key": QKEY},
                              json={"vector": embed(search_text), "limit": 6, "with_payload": True},
                              timeout=30).json().get("result", [])
            ctx = "\n\n".join(h["payload"]["text"] for h in hits) or "(nothing found)"
            chat = "\n".join(("User: " if h.get("role") == "user" else "Assistant: ") + h.get("text", "")[:600]
                             for h in history)
            prompt = f"BOOK CONTEXT:\n{ctx}\n\nRECENT CHAT:\n{chat or '(none)'}\n\nUSER'S LATEST MESSAGE: {q}"

            r, error = generate({"systemInstruction": {"parts": [{"text": SYSTEM}]},
                                 "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                                 "generationConfig": {"maxOutputTokens": 2400, "temperature": 0.6}})
            if error:
                self._send(200, {"answer": "Abhi AI service busy hai, thori der baad dobara try karein. (" + error[:120] + ")"})
                return
            parts = r["candidates"][0].get("content", {}).get("parts", [])
            answer = "".join(p.get("text", "") for p in parts) or "Jawab nahi mila, dobara try karein."
            self._send(200, {"answer": answer})
        except Exception as e:
            self._send(500, {"answer": "Server error: " + str(e)})
