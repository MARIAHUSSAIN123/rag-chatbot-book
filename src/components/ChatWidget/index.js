import React, {useState, useEffect, useRef} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './styles.module.css';

const TXT = {
  en: {
    title: 'AI Book Assistant', online: 'Ask me anything about the book',
    hello: 'Hi! 👋 I can answer questions from this book. Ask in English or Roman Urdu.',
    ph: 'Type your question...', send: 'Send', typing: 'Thinking',
    err: 'Something went wrong. Please try again.', open: 'Open chat', close: 'Close',
    chips: ['What is in Module 4?', 'How long is the course?', 'Which projects are there?'],
  },
  ur: {
    title: 'AI Book Assistant', online: 'Book ke bare mein kuch bhi poochein',
    hello: 'Assalam o Alaikum! 👋 Main is book se sawalon ke jawab deta hoon. English ya Roman Urdu mein poochein.',
    ph: 'Apna sawal likhein...', send: 'Bhejein', typing: 'Soch raha hoon',
    err: 'Kuch masla aa gaya, dobara try karein.', open: 'Chat kholen', close: 'Band karein',
    chips: ['Module 4 mein kya hai?', 'Course kitne mahine ka hai?', 'Kaun se projects hain?'],
  },
};

// Chhota sa formatter: **bold** aur bullet lines
function Rich({text}) {
  return text.split('\n').map((line, i) => {
    const bullet = /^\s*[*-]\s+/.test(line);
    const clean = line.replace(/^\s*[*-]\s+/, '');
    const parts = clean.split(/(\*\*[^*]+\*\*)/g).map((p, j) =>
      p.startsWith('**') && p.endsWith('**') ? <b key={j}>{p.slice(2, -2)}</b> : p);
    return <div key={i} className={bullet ? styles.li : undefined}>{bullet ? '• ' : ''}{parts}</div>;
  });
}

export default function ChatWidget() {
  const {i18n} = useDocusaurusContext();
  const lang = i18n.currentLocale === 'en' ? 'en' : 'ur';
  const t = TXT[lang];
  const [open, setOpen] = useState(false);
  const [q, setQ] = useState('');
  const [msgs, setMsgs] = useState([]);
  const [loading, setLoading] = useState(false);
  const endRef = useRef(null);

  useEffect(() => {
    const h = () => setOpen(true);
    window.addEventListener('open-chatbot', h);
    return () => window.removeEventListener('open-chatbot', h);
  }, []);
  useEffect(() => { endRef.current && endRef.current.scrollIntoView({behavior: 'smooth'}); }, [msgs, loading, open]);

  const ask = async (text) => {
    const question = (text ?? q).trim();
    if (!question || loading) return;
    setQ('');
    setLoading(true);
    setMsgs((m) => [...m, {role: 'user', text: question}]);
    try {
      const r = await fetch('/api/chat', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question, lang}),
      });
      const d = await r.json();
      setMsgs((m) => [...m, {role: 'bot', text: d.answer}]);
    } catch {
      setMsgs((m) => [...m, {role: 'bot', text: t.err}]);
    }
    setLoading(false);
  };

  return (
    <>
      {!open && (
        <button className={styles.fab} onClick={() => setOpen(true)} aria-label={t.open}>
          <span className={styles.ring} />
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
          </svg>
        </button>
      )}
      {open && (
        <div className={styles.panel} role="dialog" aria-label={t.title}>
          <div className={styles.head}>
            <div className={styles.avatar}>🤖</div>
            <div className={styles.headText}>
              <b>{t.title}</b>
              <span><i className={styles.dot} /> {t.online}</span>
            </div>
            <button className={styles.x} onClick={() => setOpen(false)} aria-label={t.close}>✕</button>
          </div>
          <div className={styles.body}>
            <div className={`${styles.msg} ${styles.bot}`}>{t.hello}</div>
            {msgs.length === 0 && (
              <div className={styles.chips}>
                {t.chips.map((c) => <button key={c} onClick={() => ask(c)}>{c}</button>)}
              </div>
            )}
            {msgs.map((m, i) => (
              <div key={i} className={`${styles.msg} ${m.role === 'user' ? styles.user : styles.bot}`}>
                <Rich text={m.text} />
              </div>
            ))}
            {loading && (
              <div className={`${styles.msg} ${styles.bot}`}>
                {t.typing} <span className={styles.dots}><i /><i /><i /></span>
              </div>
            )}
            <div ref={endRef} />
          </div>
          <div className={styles.foot}>
            <input value={q} onChange={(e) => setQ(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && ask()} placeholder={t.ph} />
            <button onClick={() => ask()} disabled={loading || !q.trim()}>{t.send}</button>
          </div>
        </div>
      )}
    </>
  );
}
