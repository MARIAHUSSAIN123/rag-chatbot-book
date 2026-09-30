import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';

const MODULES = [
  ['🐍', 'module-01-python-foundations', 'Python Foundations', 'Python Ki Buniyad', '2-6'],
  ['📊', 'module-02-python-for-data-science', 'Python for Data Science', 'Data Science Ke Liye Python', '7-10'],
  ['📐', 'module-03-statistics-and-math-for-ml', 'Statistics & Math for ML', 'ML Ke Liye Statistics Aur Math', '11-14'],
  ['🤖', 'module-04-machine-learning', 'Machine Learning', 'Machine Learning', '15-21'],
  ['🧠', 'module-05-deep-learning', 'Deep Learning', 'Deep Learning', '22-26'],
  ['🚀', 'module-06-mlops', 'MLOps', 'MLOps', '27-30'],
  ['☁️', 'module-07-big-data-and-cloud', 'Big Data & Cloud', 'Big Data Aur Cloud', '31-34'],
  ['✨', 'module-08-generative-ai-llms', 'Generative AI (LLMs)', 'Generative AI (LLMs)', '35-38'],
  ['🕹️', 'module-09-agentic-ai', 'Agentic AI', 'Agentic AI', '39-41'],
];

const T = {
  en: {
    title: 'AI & Data Science Book',
    sub: 'From Python basics to Generative and Agentic AI, in English and Roman Urdu.',
    start: 'Start Learning', ask: 'Ask the AI Assistant', by: 'Created by Maria Hussain',
    stats: [['10', 'Months'], ['9', 'Modules'], ['41', 'Weeks'], ['2', 'Languages']],
    mods: 'Course Modules', week: 'Weeks',
  },
  ur: {
    title: 'AI aur Data Science Book',
    sub: 'Python ki buniyad se Generative aur Agentic AI tak, English aur Roman Urdu mein.',
    start: 'Parhna Shuru Karein', ask: 'AI Assistant se Poochein', by: 'Created by Maria Hussain',
    stats: [['10', 'Mahine'], ['9', 'Modules'], ['41', 'Haftay'], ['2', 'Zubanein']],
    mods: 'Course Modules', week: 'Haftay',
  },
};

export default function Home() {
  const {i18n} = useDocusaurusContext();
  const t = i18n.currentLocale === 'en' ? T.en : T.ur;
  const i = i18n.currentLocale === 'en' ? 2 : 3;
  return (
    <Layout title={t.title} description={t.sub}>
      <header className={styles.hero}>
        <span className={`${styles.blob} ${styles.b1}`} />
        <span className={`${styles.blob} ${styles.b2}`} />
        <span className={`${styles.blob} ${styles.b3}`} />
        <div className="container">
          <p className={styles.badge}>🎓 SMIT · {t.by}</p>
          <h1 className={styles.title}>{t.title}</h1>
          <p className={styles.sub}>{t.sub}</p>
          <div className={styles.btns}>
            <Link className={`button button--lg ${styles.cta}`} to="/docs/intro">{t.start} →</Link>
            <button className={`button button--lg ${styles.ghost}`}
              onClick={() => window.dispatchEvent(new Event('open-chatbot'))}>💬 {t.ask}</button>
          </div>
          <div className={styles.stats}>
            {t.stats.map(([n, l]) => (
              <div key={l} className={styles.stat}><b>{n}</b><span>{l}</span></div>
            ))}
          </div>
        </div>
      </header>
      <main className="container margin-vert--xl">
        <h2 className={styles.h2}>{t.mods}</h2>
        <div className={styles.grid}>
          {MODULES.map((m, idx) => (
            <Link key={m[1]} to={`/docs/${m[1]}`} className={styles.card} style={{animationDelay: `${idx * 70}ms`}}>
              <span className={styles.icon}>{m[0]}</span>
              <h3>{m[i]}</h3>
              <p>{t.week} {m[4]}</p>
            </Link>
          ))}
        </div>
      </main>
    </Layout>
  );
}
