import os, json, httpx
from http.server import BaseHTTPRequestHandler

G = os.environ["GEMINI_API_KEY"]
QURL, QKEY = os.environ["QDRANT_URL"].rstrip("/"), os.environ["QDRANT_API_KEY"]
BASE = "https://generativelanguage.googleapis.com/v1beta/models"
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")  # naam badalna ho to Vercel env mein GEMINI_MODEL set karein


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
            hits = httpx.post(f"{QURL}/collections/book/points/search",
                              headers={"api-key": QKEY},
                              json={"vector": embed(q), "limit": 4, "with_payload": True},
                              timeout=30).json()["result"]
            ctx = "\n\n".join(h["payload"]["text"] for h in hits)
            prompt = ("You are a helpful assistant for an AI & Data Science book. Answer ONLY from the context below. "
                      "If the answer is not in the context, say it is not in the book. "
                      "Reply in the same language as the question: English, or Roman Urdu (Urdu written in English letters) "
                      "if the question is in Roman Urdu. Keep answers short and clear.\n\n"
                      f"Context:\n{ctx}\n\nSawal: {q}")
            r = httpx.post(f"{BASE}/{MODEL}:generateContent?key={G}",
                           json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=50).json()
            if "candidates" not in r:
                msg = r.get("error", {}).get("message") or str(r.get("promptFeedback") or r)
                self._send(200, {"answer": "Gemini error: " + msg})
                return
            parts = r["candidates"][0].get("content", {}).get("parts", [])
            answer = "".join(p.get("text", "") for p in parts) or "Jawab nahi mila, dobara try karein."
            self._send(200, {"answer": answer})
        except Exception as e:
            self._send(500, {"answer": "Server error: " + str(e)})
