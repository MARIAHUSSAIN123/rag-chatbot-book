import React, {useState} from 'react';

export default function ChatWidget() {
  const [q, setQ] = useState('');
  const [msgs, setMsgs] = useState([]);
  const [loading, setLoading] = useState(false);

  const ask = async () => {
    if (!q.trim() || loading) return;
    const question = q;
    setQ('');
    setLoading(true);
    setMsgs((m) => [...m, {role: 'user', text: question}]);
    try {
      const r = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question}),
      });
      const d = await r.json();
      setMsgs((m) => [...m, {role: 'bot', text: d.answer}]);
    } catch {
      setMsgs((m) => [...m, {role: 'bot', text: 'Error aa gaya, dobara try karein.'}]);
    }
    setLoading(false);
  };

  return (
    <div style={{border: '1px solid var(--ifm-color-emphasis-300)', borderRadius: 8, padding: 16}}>
      {msgs.map((m, i) => (
        <p key={i}><b>{m.role === 'user' ? 'Aap' : 'Bot'}:</b> {m.text}</p>
      ))}
      {loading && <p>Soch raha hoon...</p>}
      <input
        value={q}
        onChange={(e) => setQ(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && ask()}
        placeholder="Book se sawal poochein..."
        style={{width: '75%', padding: 8, marginRight: 8}}
      />
      <button className="button button--primary" onClick={ask}>Bhejein</button>
    </div>
  );
}
