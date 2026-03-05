/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef } from "react";
import Link from "next/link";
import { motion, useInView, AnimatePresence } from "framer-motion";

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
    case "NW": return "bg-orange-100 text-[#C66810]";
    case "GD": return "bg-purple-100 text-purple-700";
    case "IN": return "bg-orange-100 text-[#C66810]";
    default: return "bg-slate-100 text-slate-700";
  }
};

const getImageUrl = (post: any) => {
  return post.image_url || null;
};

function AnimatedCard({ children, className = "", delay = 0 }: { children: React.ReactNode; className?: string; delay?: number }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-40px" });
  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 24 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1], delay }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

export default function NewsPage() {
  const [articles, setArticles] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState<string>("ALL");

  useEffect(() => {
    async function fetchArticles() {
      try {
        const res = await fetch("https://mun-global.onrender.com/api/news/", {
          cache: "no-store",
        });
        if (res.ok) {
          const data = await res.json();
          setArticles(data);
        }
      } catch (error) {
        console.error("Failed to fetch articles:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchArticles();
  }, []);

  const categories = [
    { key: "ALL", label: "All Stories" },
    { key: "NW", label: "Global News" },
    { key: "GD", label: "Preparation Guides" },
    { key: "IN", label: "Delegate Interviews" },
  ];

  const filtered =
    activeCategory === "ALL"
      ? articles
      : articles.filter((a) => a.category === activeCategory);

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero Header */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="absolute bottom-0 left-0 -ml-32 -mb-32 w-[400px] h-[400px] bg-blue-500/5 rounded-full blur-[80px]" />

        <div className="max-w-7xl mx-auto px-6 pt-32 pb-16 relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <p className="text-[11px] font-black uppercase tracking-[0.3em] text-[#C66810] mb-4">The Wire</p>
            <h1 className="text-5xl md:text-6xl font-black text-white tracking-tight leading-[1.1] mb-4">
              All <span className="font-playfair italic text-[#C66810]">Stories</span>
            </h1>
            <p className="text-slate-400 text-lg max-w-xl">
              The latest from Indonesia&apos;s MUN circuit.
            </p>
          </motion.div>
        </div>
      </section>

      <main className="max-w-7xl mx-auto px-6 py-12">
        {/* Category Filter Tabs */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="flex gap-3 mb-12 overflow-x-auto pb-2 scrollbar-hide"
        >
          {categories.map((cat) => (
            <button
              key={cat.key}
              onClick={() => setActiveCategory(cat.key)}
              className={`px-6 py-2.5 rounded-full font-bold text-sm transition-all whitespace-nowrap ${
                activeCategory === cat.key
                  ? "bg-[#C66810] text-white shadow-lg shadow-orange-200"
                  : "bg-white text-slate-600 hover:bg-slate-100 border border-slate-200"
              }`}
            >
              {cat.label}
            </button>
          ))}
        </motion.div>

        {/* Articles Grid */}
        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[1, 2, 3, 4, 5, 6].map(i => (
              <div key={i} className="bg-white rounded-2xl h-80 border border-slate-200 animate-pulse" />
            ))}
          </div>
        ) : filtered.length === 0 ? (
          <div className="text-center py-20 bg-white rounded-2xl border border-slate-200">
            <div className="text-5xl mb-4 opacity-30">📰</div>
            <h3 className="text-lg font-bold text-slate-700 mb-2">No stories found</h3>
            <p className="text-slate-500 text-sm">No articles in this category yet.</p>
          </div>
        ) : (
          <AnimatePresence mode="wait">
            <motion.div
              key={activeCategory}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.3 }}
              className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
            >
              {filtered.map((post, idx) => (
                <AnimatedCard key={post.id} delay={idx * 0.06}>
                  <Link
                    href={`/news/${post.slug}`}
                    className="group block h-full"
                  >
                    <motion.div
                      whileHover={{ y: -6 }}
                      transition={{ type: "spring", stiffness: 300, damping: 20 }}
                      className="bg-white rounded-2xl overflow-hidden border border-slate-200 hover:shadow-xl hover:border-transparent transition-all h-full flex flex-col"
                    >
                      {getImageUrl(post) ? (
                        <div className="relative w-full h-48 overflow-hidden">
                          <img
                            src={getImageUrl(post)}
                            alt={post.title}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                          />
                          <div className="absolute inset-0 bg-gradient-to-t from-black/10 to-transparent" />
                        </div>
                      ) : (
                        <div className="w-full h-48 bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center">
                          <span className="text-5xl opacity-20">📰</span>
                        </div>
                      )}

                      <div className="p-6 flex flex-col flex-grow">
                        <span
                          className={`inline-block w-fit px-3 py-1 rounded-md text-[10px] font-bold uppercase tracking-widest mb-3 ${getCategoryColor(
                            post.category
                          )}`}
                        >
                          {getCategoryLabel(post.category)}
                        </span>

                        <h3 className="font-bold text-xl text-slate-900 group-hover:text-[#C66810] transition-colors mb-2">
                          {post.title}
                        </h3>
                        <p className="text-slate-500 text-sm line-clamp-3 flex-grow">
                          {post.content}
                        </p>

                        <div className="mt-4 pt-4 border-t border-slate-100 flex items-center gap-2 text-xs text-slate-400">
                          <span className="font-semibold text-slate-600">{post.author_name}</span>
                          <span>&middot;</span>
                          <span>
                            {new Date(post.created_at).toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" })}
                          </span>
                        </div>
                      </div>
                    </motion.div>
                  </Link>
                </AnimatedCard>
              ))}
            </motion.div>
          </AnimatePresence>
        )}
      </main>
    </div>
  );
}
