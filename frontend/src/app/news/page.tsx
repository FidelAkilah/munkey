/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";

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
    case "NW": return "bg-blue-100 text-blue-700";
    case "GD": return "bg-purple-100 text-purple-700";
    case "IN": return "bg-amber-100 text-amber-700";
    default: return "bg-slate-100 text-slate-700";
  }
};

const getImageUrl = (post: any) => {
  return post.image_url || null;
};

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
    <div className="min-h-screen bg-white">
      <main className="max-w-7xl mx-auto px-6 pt-32 pb-16">
        <header className="mb-12">
          <h1 className="text-5xl font-black text-slate-900">All Stories</h1>
          <p className="text-slate-500 mt-3">
            The latest from Indonesia&apos;s MUN circuit.
          </p>
        </header>

        {/* Category Filter Tabs */}
        <div className="flex gap-3 mb-12 overflow-x-auto pb-2">
          {categories.map((cat) => (
            <button
              key={cat.key}
              onClick={() => setActiveCategory(cat.key)}
              className={`px-6 py-2 rounded-full font-bold text-sm transition-all whitespace-nowrap ${
                activeCategory === cat.key
                  ? "bg-blue-600 text-white shadow-lg"
                  : "bg-slate-100 text-slate-600 hover:bg-slate-200"
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>

        {/* Articles Grid */}
        {loading ? (
          <div className="h-64 flex items-center justify-center border-2 border-dashed rounded-[3rem] animate-pulse">
            Loading articles...
          </div>
        ) : filtered.length === 0 ? (
          <div className="h-64 flex items-center justify-center border-2 border-dashed rounded-[3rem]">
            No stories found in this category.
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {filtered.map((post) => (
              <Link
                key={post.id}
                href={`/news/${post.slug}`}
                className="group block"
              >
                <motion.div
                  whileHover={{ y: -4 }}
                  className="bg-white rounded-[2.5rem] overflow-hidden border hover:shadow-xl transition-shadow h-full"
                >
                  {getImageUrl(post) ? (
                    <div className="relative w-full h-48 overflow-hidden">
                      <img
                        src={getImageUrl(post)}
                        alt={post.title}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                      />
                    </div>
                  ) : (
                    <div className="w-full h-48 bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center">
                      <span className="text-5xl opacity-40">📰</span>
                    </div>
                  )}

                  <div className="p-6">
                    <span
                      className={`inline-block px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest ${getCategoryColor(
                        post.category
                      )}`}
                    >
                      {getCategoryLabel(post.category)}
                    </span>

                    <h3 className="font-bold text-xl mt-3 group-hover:text-blue-600 transition-colors">
                      {post.title}
                    </h3>
                    <p className="mt-2 text-slate-600 text-sm line-clamp-3">
                      {post.content}
                    </p>

                    <div className="mt-4 flex items-center gap-2 text-xs text-slate-400">
                      <span className="font-semibold">{post.author_name}</span>
                      <span>&middot;</span>
                      <span>
                        {new Date(post.created_at).toLocaleDateString()}
                      </span>
                    </div>
                  </div>
                </motion.div>
              </Link>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
