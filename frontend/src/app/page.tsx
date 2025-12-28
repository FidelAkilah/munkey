// src/app/page.tsx
import MUNMap from "../components/MUNMap";
import Link from 'next/link';

// Fetching both News and Conferences from Django
async function getData() {
  const [newsRes, confRes] = await Promise.all([
    fetch('http://localhost:8000/api/news/', { cache: 'no-store' }),
    fetch('http://localhost:8000/api/conferences/', { cache: 'no-store' })
  ]);
  
  return {
    articles: newsRes.ok ? await newsRes.json() : [],
    conferences: confRes.ok ? await confRes.json() : []
  };
}

export default async function Home() {
  const { articles, conferences } = await getData();

  return (
    <main className="max-w-7xl mx-auto p-8 space-y-12">
      {/* 1. Header Section */}
      <header>
        <h1 className="text-5xl font-black text-slate-900 tracking-tight">Global MUN Hub</h1>
        <p className="text-slate-500 mt-2 text-xl">Breaking the silos between city circuits.</p>
      </header>

      {/* 2. Global Map Section (The City Silo Breaker) */}
      <section>
        <div className="flex justify-between items-end mb-4">
          <h2 className="text-2xl font-bold">Live Conference Map</h2>
          <span className="text-sm text-blue-600 font-semibold">{conferences.length} Live Circuits</span>
        </div>
        <MUNMap markers={conferences} />
      </section>

      {/* 3. News Bento Grid */}
      <section>
        <h2 className="text-2xl font-bold mb-6">Latest from the Circuit</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {articles.map((article: any, index: number) => (
            <Link 
              key={article.id} 
              href={`/news/${article.slug}`}
              className={`group relative rounded-3xl overflow-hidden shadow-lg transition-transform hover:scale-[1.02] bg-slate-200 ${index === 0 ? 'md:col-span-2 md:row-span-1 h-[400px]' : 'h-[400px]'}`}
            >
              <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent p-8 flex flex-col justify-end">
                <span className="text-xs font-bold text-amber-400 uppercase mb-2">{article.category}</span>
                <h2 className="text-2xl font-bold text-white">{article.title}</h2>
                <p className="text-slate-300 text-sm mt-2 line-clamp-2">{article.excerpt}</p>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </main>
  );
}