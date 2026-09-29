# AI & Data Science Book (English + Roman Urdu)

## Local chalana
```bash
npm install
npm start                      # English: http://localhost:3000
npm start -- --locale ur-Latn  # Roman Urdu
npm run build                  # dono languages ka production build
```

## Content badalna
- English: `docs/*.md`
- Roman Urdu: `i18n/ur-Latn/docusaurus-plugin-content-docs/current/*.md` (same file names)
- `python scripts/gen_content.py` sirf shuru ka draft banata hai. Isay dobara chalane se aapki edits overwrite ho jayengi.

## Chatbot
1. Gemini API key (aistudio.google.com) aur Qdrant Cloud cluster (cloud.qdrant.io) banayein.
2. `.env.example` ke variables Vercel > Settings > Environment Variables mein daalein.
3. Local par wahi variables set karke: `pip install httpx && python scripts/ingest.py`
4. Book update ho to ingest dobara chalayen.

## Deploy
GitHub par push karein, Vercel par repo import karein, `url` in `docusaurus.config.js` apne Vercel URL se badal dein.
