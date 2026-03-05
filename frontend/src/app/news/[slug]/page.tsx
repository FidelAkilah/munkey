import Link from "next/link";

const getCategoryLabel = (cat: string) => {
  switch (cat) {
    case "NW": return "Global News";
    case "GD": return "Preparation Guides";
    case "IN": return "Delegate Interviews";
    default: return cat;
  }
};

const getCategoryColor = (cat: string) => {
  switch (cat) {
    case "NW": return "bg-[#C66810] text-white";
    case "GD": return "bg-purple-600 text-white";
    case "IN": return "bg-blue-600 text-white";
    default: return "bg-slate-600 text-white";
  }
};

export default async function ArticlePage({ params }: { params: { slug: string } }) {
  const { slug } = await params;

  const res = await fetch(`https://mun-global.onrender.com/api/news/${slug}/`, {
    cache: "no-store",
  });

  if (!res.ok) {
    return (
      <main className="max-w-4xl mx-auto pt-32 pb-20 px-6 text-center">
        <div className="text-6xl mb-6 opacity-30">📰</div>
        <h1 className="font-playfair text-4xl font-black mb-4 text-slate-900">Article Not Found</h1>
        <p className="text-slate-500 mb-8 text-lg">
          This article may have been removed or is pending review.
        </p>
        <Link
          href="/news"
          className="inline-flex items-center gap-2 px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors"
        >
          &larr; Back to All Stories
        </Link>
      </main>
    );
  }

  const article = await res.json();
  const imageUrl = article.image_url || null;

  return (
    <article className="min-h-screen bg-white">
      {/* Hero image */}
      {imageUrl && (
        <div className="relative w-full h-[450px] bg-[#070e1c] overflow-hidden">
          <img
            src={imageUrl}
            alt={article.title}
            className="w-full h-full object-cover opacity-80"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-white via-white/20 to-transparent" />
          <div className="absolute inset-0 bg-gradient-to-r from-black/30 to-transparent" />
        </div>
      )}

      <div className={`max-w-3xl mx-auto px-6 ${imageUrl ? "-mt-20 relative z-10 py-8" : "pt-32 pb-16"}`}>
        <Link
          href="/news"
          className="text-sm text-slate-400 hover:text-[#C66810] transition-colors mb-8 inline-flex items-center gap-1 font-medium"
        >
          &larr; Back to All Stories
        </Link>

        <header className="mb-12">
          <span className={`inline-block px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest mb-4 ${getCategoryColor(article.category)}`}>
            {getCategoryLabel(article.category)}
          </span>
          <h1 className="font-playfair text-4xl md:text-5xl font-black text-slate-900 leading-tight mb-6">
            {article.title}
          </h1>
          <div className="flex items-center gap-4 text-slate-500 border-b border-slate-100 pb-6">
            <div className="w-10 h-10 rounded-full bg-[#C66810]/15 text-[#C66810] flex items-center justify-center font-black text-sm">
              {article.author_name?.[0]?.toUpperCase() || "A"}
            </div>
            <div>
              <p className="font-bold text-slate-700">{article.author_name}</p>
              <p className="text-sm">
                {new Date(article.created_at).toLocaleDateString("en-US", {
                  year: "numeric",
                  month: "long",
                  day: "numeric",
                })}
              </p>
            </div>
          </div>
        </header>

        <div className="prose prose-lg max-w-none text-slate-700 leading-[1.85] whitespace-pre-line">
          {article.content}
        </div>

        <div className="mt-16 pt-8 border-t border-slate-100">
          <Link
            href="/news"
            className="text-sm font-bold text-[#C66810] hover:text-[#A05200] transition-colors inline-flex items-center gap-2"
          >
            &larr; All Stories
          </Link>
        </div>
      </div>
    </article>
  );
}
