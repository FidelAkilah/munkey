// src/app/news/[slug]/page.tsx
export default async function ArticlePage({ params }: { params: { slug: string } }) {
    const { slug } = await params;
    
    // Fetch from your Django API
    const res = await fetch(`http://127.0.0.1:8000/api/news/${slug}/`);
    const article = await res.json();
  
    return (
      <article className="max-w-4xl mx-auto py-20 px-6">
        <header className="mb-8">
          <span className="text-mun-gold font-bold uppercase tracking-widest">{article.category}</span>
          <h1 className="text-5xl font-extrabold mt-2">{article.title}</h1>
          <p className="text-slate-500 mt-4">By {article.author_name} • {new Date(article.created_at).toLocaleDateString()}</p>
        </header>
        
        <div className="prose prose-lg max-w-none text-slate-800 leading-relaxed">
          {article.content}
        </div>
      </article>
    );
  }