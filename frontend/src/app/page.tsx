/* eslint-disable @next/next/no-html-link-for-pages */
/* eslint-disable @typescript-eslint/no-explicit-any */
// src/app/page.tsx
import Link from 'next/link';

async function getNews() {
  const res = await fetch('http://localhost:8000/api/news/', { cache: 'no-store' });
  return res.ok ? res.json() : [];
}

export default async function Home() {
  const news = await getNews();

  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold mb-6">Global MUN News</h1>
      
      {news.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {news.map((item: any) => (
            <div key={item.id} className="p-4 border rounded-xl bg-white shadow">
              <h2 className="font-bold">{item.title}</h2>
              <p className="text-sm text-slate-600 mt-2">{item.content.substring(0, 100)}...</p>
            </div>
          ))}
        </div>
      ) : (
        <div className="p-10 text-center bg-slate-100 rounded-3xl">
          <p className="text-slate-500">No news found. Are you sure the Django server is running at 127.0.0.1:8000?</p>
          <a href="/news/add" className="mt-4 inline-block bg-blue-600 text-white px-6 py-2 rounded-full">
            Add First News
          </a>
        </div>
      )}
    </main>
  );
}