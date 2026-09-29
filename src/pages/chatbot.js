import React from 'react';
import Layout from '@theme/Layout';
import ChatWidget from '@site/src/components/ChatWidget';

export default function ChatbotPage() {
  return (
    <Layout title="Chatbot" description="Ask questions from the book">
      <main className="container margin-vert--lg">
        <h1>Book Chatbot</h1>
        <p>English ya Roman Urdu mein sawal poochein.</p>
        <ChatWidget />
      </main>
    </Layout>
  );
}
