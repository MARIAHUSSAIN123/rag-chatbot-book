"""Book ko Qdrant vector DB mein upload karta hai. Local par chalayen:
   GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY set karke  ->  python scripts/ingest.py
   (pehle: pip install httpx)"""
import os, glob, uuid, httpx
G = os.environ["GEMINI_API_KEY"]
QURL = os.environ["QDRANT_URL"].rstrip("/")
H = {"api-key": os.environ["QDRANT_API_KEY"]}
BASE = "https://generativelanguage.googleapis.com/v1beta/models"

def embed(t):
    return httpx.post(f"{BASE}/gemini-embedding-001:embedContent?key={G}",
        json={"content": {"parts": [{"text": t}]}, "outputDimensionality": 768}, timeout=30).json()["embedding"]["values"]

httpx.delete(f"{QURL}/collections/book", headers=H)  # purana data saaf
httpx.put(f"{QURL}/collections/book", headers=H, json={"vectors": {"size": 768, "distance": "Cosine"}})

files = glob.glob("docs/**/*.md*", recursive=True) + glob.glob("i18n/**/*.md*", recursive=True)
points = []
for f in files:
    text = open(f, encoding="utf-8").read()
    for i in range(0, len(text), 1000):
        chunk = text[i:i+1000]
        points.append({"id": str(uuid.uuid4()), "vector": embed(chunk), "payload": {"text": chunk, "file": f}})
for i in range(0, len(points), 50):
    httpx.put(f"{QURL}/collections/book/points", headers=H, json={"points": points[i:i+50]}, timeout=120)
print(len(points), "chunks uploaded")
