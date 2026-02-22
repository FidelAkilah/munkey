import Link from "next/link";

const getCategoryLabel = (cat: string) => {
  switch (cat) {
    case "NW": return "Global News";
    case "GD": return "Preparation Guides";
    case "IN": return "Delegate Interviews";
    default: return cat;
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
        <h1 className="text-4xl font-black mb-4">Article Not Found</h1>
        <p className="text-slate-500 mb-8">
          This article may have been removed or is pending review.
        </p>
        <Link
          href="/news"
          className="text-blue-600 font-bold hover:text-blue-800 transition"
        >
          &larr; Back to All Stories
        </Link>
      </main>
    );
  }

  const article = await res.json();
  const imageUrl = article.image_url || article.featured_image || null;

  return (
    <article className="min-h-screen bg-white">
      {imageUrl && (
        <div className="relative w-full h-[400px] bg-slate-900">
          <img
            src={imageUrl}
            alt={article.title}
            className="w-full h-full object-cover opacity-90"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-white via-transparent to-transparent" />
        </div>
      )}

      <div className={`max-w-4xl mx-auto px-6 ${imageUrl ? "py-12" : "pt-32 pb-16"}`}>
        <Link
          href="/news"
          className="text-sm text-slate-400 hover:text-blue-600 transition mb-8 inline-block"
        >
          &larr; Back to All Stories
        </Link>

        <header className="mb-10">
          <span className="text-mun-gold font-bold uppercase tracking-widest text-sm">
            {getCategoryLabel(article.category)}
          </span>
          <h1 className="text-5xl font-extrabold mt-3 leading-tight">
            {article.title}
          </h1>
          <p className="text-slate-500 mt-4">
            By{" "}
            <span className="font-semibold text-slate-700">
              {article.author_name}
            </span>{" "}
            &middot;{" "}
            {new Date(article.created_at).toLocaleDateString("en-US", {
              year: "numeric",
              month: "long",
              day: "numeric",
            })}
          </p>
        </header>

        <div className="prose prose-lg max-w-none text-slate-800 leading-relaxed whitespace-pre-line">
          {article.content}
        </div>
      </div>
    </article>
  );
}
