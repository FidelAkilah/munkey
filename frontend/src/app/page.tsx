/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { motion } from "framer-motion";
import { useSession } from "next-auth/react";

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
  if (post.image_url) return post.image_url;
  if (post.featured_image) return post.featured_image;
  return null;
};

export default function Home() {
  const [news, setNews] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const { data: session } = useSession();
  const isAuthenticated = session?.user !== undefined;

  // 1. FETCH NEWS
  useEffect(() => {
    async function fetchNews() {
      try {
        const res = await fetch("https://mun-global.onrender.com/api/news/", {
          cache: "no-store",
        });
        if (res.ok) {
          const data = await res.json();
          setNews(data);
        }
      } catch (error) {
        console.error("Failed to fetch news:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchNews();
  }, []);

  const missionItems = [
    { icon: "🌍", label: "Nationwide Media", desc: "Connecting Indonesia's circuit.", glow: "group-hover:shadow-[0_0_25px_rgba(34,211,238,0.4)]", border: "border-cyan-100", bg: "bg-cyan-50", text: "text-cyan-600" },
    { icon: "📡", label: "Reliable Intel", desc: "Primary source for upcoming MUNs.", glow: "group-hover:shadow-[0_0_25px_rgba(37,99,235,0.4)]", border: "border-blue-100", bg: "bg-blue-50", text: "text-blue-600" },
    { icon: "🎓", label: "Free Learning", desc: "Cost-free skill sharing for all.", glow: "group-hover:shadow-[0_0_25px_rgba(147,51,234,0.4)]", border: "border-purple-100", bg: "bg-purple-50", text: "text-purple-600" },
    { icon: "🚀", label: "The Powerhouse", desc: "Building tomorrow's diplomats.", glow: "group-hover:shadow-[0_0_25px_rgba(219,39,119,0.4)]", border: "border-pink-100", bg: "bg-pink-50", text: "text-pink-600" },
  ];

  return (
    <div className="min-h-screen bg-white selection:bg-cyan-500/20">

      {/* 1. HERO SECTION */}
      <section className="relative pt-44 pb-16 overflow-hidden flex items-center min-h-[600px] bg-slate-900">
        <div className="absolute inset-0 z-0">
          <Image
            src="/UN-HQ-Flagswide.png"
            alt="UN Flags"
            fill
            className="object-cover scale-105"
            priority
          />
          <div className="absolute inset-0 bg-slate-900/60 backdrop-blur-[2px]" />
        </div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="max-w-7xl mx-auto px-6 relative z-10 text-center text-white"
        >
          <h1 className="text-6xl md:text-8xl font-bold mb-8 tracking-tight leading-tight">
            One Stop for{" "}
            <span className="font-serif italic font-light text-blue-300">
              MUN Excellence.
            </span>
          </h1>

          <div className="flex flex-wrap justify-center gap-5">
            <Link
              href="/skills"
              className="px-12 py-4 bg-blue-600 text-white font-bold rounded-2xl hover:bg-blue-500 transition-all"
            >
              Explore Skills
            </Link>

            {/* NEW SUBMISSION FLOW */}
            {isAuthenticated ? (
              <Link
                href="/news/add"
                className="px-12 py-4 border-2 border-white/30 bg-white/10 backdrop-blur-md text-white rounded-2xl font-bold hover:bg-white hover:text-slate-900 transition-all"
              >
                Submit a Story
              </Link>
            ) : (
              <Link
                href="/login"
                className="px-12 py-4 border-2 border-white/30 bg-white/10 backdrop-blur-md text-white rounded-2xl font-bold hover:bg-white hover:text-slate-900 transition-all"
              >
                Login to Submit
              </Link>
            )}
          </div>
        </motion.div>
      </section>

      {/* 2. SUBMISSION CALLOUT */}
      <section className="py-16 bg-blue-50">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <h2 className="text-3xl font-bold text-slate-900 mb-4">
            Have a story from your circuit?
          </h2>
          <p className="text-slate-600 mb-8 leading-relaxed">
            {isAuthenticated 
              ? "Share your MUN experiences with the community. Submit your article below and our editorial team will review it for publication."
              : "We welcome guest contributions from delegates across Indonesia. Login to submit your story for review."
            }
          </p>
          {isAuthenticated ? (
            <Link
              href="/news/add"
              className="inline-block text-blue-600 font-bold border-b-2 border-blue-600 pb-1 hover:text-blue-800 hover:border-blue-800 transition-all"
            >
              Submit Your Article →
            </Link>
          ) : (
            <Link
              href="/login"
              className="inline-block text-blue-600 font-bold border-b-2 border-blue-600 pb-1 hover:text-blue-800 hover:border-blue-800 transition-all"
            >
              Login to Submit →
            </Link>
          )}
        </div>
      </section>

      {/* 3. MISSION BAR */}
      <section className="bg-white py-14 border-b border-slate-100">
        <div className="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-10">
          {missionItems.map((item, idx) => (
            <motion.div
              key={idx}
              whileHover={{ y: -5 }}
              className="flex items-center gap-5 group"
            >
              <div
                className={`w-16 h-16 ${item.bg} border ${item.border} ${item.text} rounded-2xl flex items-center justify-center text-3xl ${item.glow}`}
              >
                {item.icon}
              </div>
              <div>
                <p className="text-[10px] font-black uppercase text-slate-400 tracking-[0.2em]">
                  {item.label}
                </p>
                <p className="text-sm font-bold text-slate-900">{item.desc}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* 4. NEWS FEED */}
      <main className="max-w-7xl mx-auto px-6 py-24">
        <div className="flex items-end justify-between mb-16">
          <h2 className="text-5xl font-bold italic">Latest from the circuit.</h2>
          <Link href="/news" className="text-sm font-bold text-blue-600">
            View All Stories →
          </Link>
        </div>

        {loading ? (
          <div className="h-64 flex items-center justify-center border-2 border-dashed rounded-[3rem] animate-pulse">
            Fetching the latest diplomatic updates...
          </div>
        ) : news.length === 0 ? (
          <div className="h-64 flex items-center justify-center border-2 border-dashed rounded-[3rem]">
            No stories found. Be the first to submit!
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-12 gap-8">
            {news.slice(0, 5).map((post, index) => (
              <Link
                key={post.id}
                href={`/news/${post.slug}`}
                className={`group block ${
                  index === 0 ? "md:col-span-8" : "md:col-span-4"
                }`}
              >
                <motion.div
                  whileHover={{ y: -4 }}
                  className="bg-white rounded-[2.5rem] overflow-hidden border hover:shadow-xl transition-shadow h-full"
                >
                  {getImageUrl(post) ? (
                    <div className={`relative w-full ${index === 0 ? "h-64" : "h-48"} overflow-hidden`}>
                      <img
                        src={getImageUrl(post)}
                        alt={post.title}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                      />
                    </div>
                  ) : (
                    <div className={`w-full ${index === 0 ? "h-64" : "h-48"} bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center`}>
                      <span className="text-5xl opacity-40">📰</span>
                    </div>
                  )}

                  <div className="p-8">
                    <span className={`inline-block px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest ${getCategoryColor(post.category)}`}>
                      {getCategoryLabel(post.category)}
                    </span>

                    <h3 className="font-black text-2xl mt-3 group-hover:text-blue-600 transition-colors">
                      {post.title}
                    </h3>
                    <p className="mt-3 text-slate-600 line-clamp-3">
                      {post.content}
                    </p>

                    <div className="mt-4 flex items-center gap-2 text-xs text-slate-400">
                      <span className="font-semibold">{post.author_name}</span>
                      <span>&middot;</span>
                      <span>{new Date(post.created_at).toLocaleDateString()}</span>
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

