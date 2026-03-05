/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef } from "react";
import Link from "next/link";
import Image from "next/image";
import { useSession } from "next-auth/react";
import { motion, useInView } from "framer-motion";

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
    case "IN": return "bg-blue-100 text-blue-700";
    default: return "bg-slate-100 text-slate-700";
  }
};

const getImageUrl = (post: any) => {
  return post.image_url || null;
};

const TICKER = [
  "GENERAL ASSEMBLY IN SESSION",
  "SECURITY COUNCIL BRIEFING",
  "DELEGATE SUBMISSIONS OPEN",
  "DIPLOMAI BETA LIVE",
  "JOIN THE GLOBAL CIRCUIT",
  "NEW SKILL MODULES AVAILABLE",
  "CONFERENCE SEASON 2026",
];

function AnimatedSection({ children, className = "", delay = 0 }: { children: React.ReactNode; className?: string; delay?: number }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-80px" });
  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 40 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1], delay }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

export default function Home() {
  const [news, setNews] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const { data: session } = useSession();
  const isAuthenticated = session?.user !== undefined;

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
    { icon: "🌍", label: "Nationwide Media", desc: "Connecting Indonesia's circuit.", bg: "bg-orange-50", border: "border-orange-200", text: "text-[#C66810]" },
    { icon: "📡", label: "Reliable Intel", desc: "Primary source for upcoming MUNs.", bg: "bg-blue-50", border: "border-blue-200", text: "text-blue-700" },
    { icon: "🎓", label: "Free Learning", desc: "Cost-free skill sharing for all.", bg: "bg-purple-50", border: "border-purple-200", text: "text-purple-700" },
    { icon: "🚀", label: "The Powerhouse", desc: "Building tomorrow's diplomats.", bg: "bg-emerald-50", border: "border-emerald-200", text: "text-emerald-700" },
  ];

  return (
    <div className="min-h-screen bg-slate-50">

      {/* HERO SECTION — dark navy with grain texture */}
      <section className="relative overflow-hidden bg-[#0a1628] min-h-[94vh] flex items-center grain">
        {/* Decorative elements */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] rounded-full border border-white/[0.03]" />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] rounded-full border border-white/[0.05]" />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[400px] h-[400px] rounded-full border border-white/[0.07]" />
        <div className="absolute top-0 right-0 -mr-40 -mt-40 w-[600px] h-[600px] bg-[#C66810]/10 rounded-full blur-[120px]" />
        <div className="absolute bottom-0 left-0 -ml-40 -mb-40 w-[500px] h-[500px] bg-blue-500/5 rounded-full blur-[100px]" />

        <div className="max-w-7xl mx-auto px-6 lg:px-8 py-24 md:py-32 relative z-10 w-full">
          <div className="flex flex-col items-center text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="inline-flex items-center gap-2 px-4 py-1.5 mb-8 rounded-full bg-white/[0.07] text-[#E8913A] text-sm font-bold border border-white/10 backdrop-blur-sm"
            >
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-orange-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-[#C66810]"></span>
              </span>
              Join the Global Circuit
            </motion.div>

            <motion.h1
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.4, ease: [0.22, 1, 0.36, 1] }}
              className="text-5xl md:text-7xl lg:text-8xl font-black text-white tracking-tight leading-[1.05] mb-6 max-w-5xl"
            >
              One Stop for{" "}
              <span className="font-playfair italic text-[#C66810]">
                MUN Excellence.
              </span>
            </motion.h1>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.6 }}
              className="text-lg md:text-xl text-slate-400 leading-relaxed max-w-2xl mb-12 font-medium"
            >
              Elevate your diplomacy with breaking news, skill-sharing resources, and our revolutionary AI-powered practice.
            </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.8 }}
              className="flex flex-wrap justify-center gap-4"
            >
              <Link
                href="/skills"
                className="group px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl shadow-lg shadow-orange-900/30 hover:bg-[#A05200] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 transform"
              >
                Explore Skills
                <span className="inline-block ml-2 group-hover:translate-x-1 transition-transform">&rarr;</span>
              </Link>

              {isAuthenticated ? (
                <Link
                  href="/news/add"
                  className="px-8 py-4 bg-white/[0.07] text-white font-bold rounded-xl border border-white/10 hover:bg-white/[0.12] hover:border-white/20 backdrop-blur-sm transition-all duration-300"
                >
                  Submit a Story
                </Link>
              ) : (
                <Link
                  href="/login"
                  className="px-8 py-4 bg-white/[0.07] text-white font-bold rounded-xl border border-white/10 hover:bg-white/[0.12] hover:border-white/20 backdrop-blur-sm transition-all duration-300"
                >
                  Login to Submit
                </Link>
              )}
            </motion.div>
          </div>
        </div>

        {/* Scroll indicator */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.5 }}
          className="absolute bottom-8 left-1/2 -translate-x-1/2"
        >
          <div className="w-6 h-10 rounded-full border-2 border-white/20 flex items-start justify-center p-1.5">
            <motion.div
              animate={{ y: [0, 12, 0] }}
              transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
              className="w-1.5 h-1.5 rounded-full bg-[#C66810]"
            />
          </div>
        </motion.div>
      </section>

      {/* TICKER BAR */}
      <div className="bg-[#C66810] py-3 overflow-hidden relative">
        <div className="animate-ticker flex whitespace-nowrap">
          {[...TICKER, ...TICKER].map((item, i) => (
            <span key={i} className="mx-8 text-sm font-black text-white/90 uppercase tracking-[0.2em] flex items-center gap-4">
              <span className="w-1.5 h-1.5 bg-white/60 rounded-full" />
              {item}
            </span>
          ))}
        </div>
      </div>

      {/* CORE PILLARS SECTION */}
      <section className="max-w-7xl mx-auto px-6 lg:px-8 py-24">
        <AnimatedSection>
          <div className="text-center mb-16">
            <p className="text-[11px] font-black uppercase tracking-[0.3em] text-[#C66810] mb-3">Why MUNKEY</p>
            <h2 className="text-4xl md:text-5xl font-black text-slate-900 mb-4 font-playfair">Our Core Pillars</h2>
            <p className="text-slate-500 text-lg max-w-2xl mx-auto">
              Everything you need to excel in Model United Nations, all in one place.
            </p>
          </div>
        </AnimatedSection>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {missionItems.map((item, idx) => (
            <AnimatedSection key={idx} delay={idx * 0.1}>
              <motion.div
                whileHover={{ y: -8, scale: 1.02 }}
                transition={{ type: "spring", stiffness: 300, damping: 20 }}
                className="group relative bg-white rounded-2xl p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:border-transparent transition-all duration-300 flex flex-col items-start gap-4 overflow-hidden h-full"
              >
                <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-slate-50 to-transparent rounded-bl-full opacity-0 group-hover:opacity-100 transition-opacity" />
                <div className={`w-14 h-14 rounded-xl ${item.bg} ${item.text} flex items-center justify-center text-3xl mb-2 group-hover:scale-110 transition-transform duration-300`}>
                  {item.icon}
                </div>
                <div>
                  <p className={`text-[10px] font-black uppercase tracking-[0.2em] mb-1 ${item.text}`}>
                    {item.label}
                  </p>
                  <h3 className="text-lg font-bold text-slate-900 leading-snug">
                    {item.desc}
                  </h3>
                </div>
              </motion.div>
            </AnimatedSection>
          ))}
        </div>
      </section>

      {/* DIPLOMAI CTA SECTION */}
      <AnimatedSection>
        <section className="bg-[#0a1628] py-28 relative overflow-hidden my-12 border-y border-slate-800 grain">
          <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-[#C66810]/20 rounded-full blur-3xl pointer-events-none"></div>
          <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

          <div className="max-w-5xl mx-auto px-6 relative z-10">
            <div className="flex flex-col md:flex-row items-center gap-16">
              {/* Left content */}
              <div className="md:w-1/2 text-left">
                <motion.div
                  whileHover={{ scale: 1.05, rotate: 5 }}
                  className="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-white mb-8 shadow-2xl cursor-default"
                >
                  <Image
                    src="/MunKey Main Logo.png"
                    alt="MunKey Logo"
                    width={48}
                    height={48}
                    className="object-contain"
                  />
                </motion.div>
                <h2 className="text-4xl md:text-5xl font-black text-white mb-6 leading-tight">
                  Meet <span className="font-playfair italic text-[#C66810]">DiplomAI</span>
                </h2>
                <p className="text-slate-400 text-lg mb-10 leading-relaxed">
                  Practice your speeches, draft resolutions, and receive personalized feedback
                  from our AI strategist, Bongo. Elevate your performance before the next conference.
                </p>
                <Link
                  href="/curriculum"
                  className="group inline-flex items-center gap-2 px-10 py-4 bg-[#C66810] text-white font-bold rounded-xl shadow-lg shadow-orange-900/50 hover:bg-[#A05200] hover:-translate-y-1 transition-all duration-300"
                >
                  Start Training Now
                  <span className="group-hover:translate-x-1 transition-transform">&rarr;</span>
                </Link>
              </div>

              {/* Right — chat mockup */}
              <div className="md:w-1/2">
                <div className="bg-white/[0.05] backdrop-blur-sm rounded-2xl border border-white/10 p-6 space-y-4">
                  <div className="flex items-center gap-3 pb-4 border-b border-white/10">
                    <div className="w-8 h-8 rounded-full bg-[#C66810] flex items-center justify-center text-white text-sm font-bold">B</div>
                    <div>
                      <p className="text-white text-sm font-bold">Bongo AI</p>
                      <p className="text-emerald-400 text-[10px]">Online</p>
                    </div>
                  </div>
                  <div className="space-y-3">
                    <div className="bg-white/[0.08] rounded-xl rounded-tl-sm p-3 max-w-[85%]">
                      <p className="text-slate-300 text-sm">Your opening speech had strong rhetoric! Consider adding a specific statistic to strengthen your argument on climate policy.</p>
                    </div>
                    <div className="bg-[#C66810]/20 rounded-xl rounded-tr-sm p-3 max-w-[75%] ml-auto">
                      <p className="text-orange-200 text-sm">Can you help me practice my rebuttal for the Security Council?</p>
                    </div>
                    <div className="bg-white/[0.08] rounded-xl rounded-tl-sm p-3 max-w-[85%]">
                      <p className="text-slate-300 text-sm">Of course! Let&apos;s role-play. I&apos;ll take the opposing delegate&apos;s position. Ready when you are.</p>
                    </div>
                  </div>
                  <div className="pt-3 border-t border-white/10">
                    <div className="bg-white/[0.05] rounded-lg px-4 py-2.5 text-slate-500 text-sm">Type your response...</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </AnimatedSection>

      {/* NEWS FEED */}
      <main className="max-w-7xl mx-auto px-6 lg:px-8 py-24 mb-12">
        <AnimatedSection>
          <div className="flex flex-col md:flex-row items-center justify-between gap-6 mb-12 border-b border-slate-200 pb-6">
            <div>
              <p className="text-[11px] font-black uppercase tracking-[0.3em] text-[#C66810] mb-2">The Wire</p>
              <h2 className="text-3xl md:text-4xl font-black text-slate-900 mb-2 font-playfair">Latest from the Circuit</h2>
              <p className="text-slate-500 font-medium">Stories, interviews, and updates from MUN delegates.</p>
            </div>
            <Link href="/news" className="group flex items-center gap-2 text-sm font-bold text-[#C66810] hover:text-[#A05200] transition-colors py-2 px-4 rounded-lg bg-orange-50 hover:bg-orange-100">
              View All Stories
              <span className="group-hover:translate-x-1 transition-transform">&rarr;</span>
            </Link>
          </div>
        </AnimatedSection>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 animate-pulse">
            {[1, 2, 3].map(i => (
              <div key={i} className="bg-white rounded-2xl h-80 border border-slate-200 shadow-sm" />
            ))}
          </div>
        ) : news.length === 0 ? (
          <div className="bg-white rounded-2xl p-16 text-center border border-slate-200 shadow-sm">
             <div className="text-5xl mb-4 opacity-50">📰</div>
             <h3 className="text-xl font-bold text-slate-700 mb-2">No stories found</h3>
             <p className="text-slate-500 mb-6">Be the first delegate to submit a story to the community!</p>
             <Link href="/news/add" className="inline-block px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors">
               Submit a Story
             </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-12 gap-8">
            {news.slice(0, 5).map((post, index) => (
              <AnimatedSection
                key={post.id}
                delay={index * 0.1}
                className={`${index === 0 ? "md:col-span-8 md:row-span-2" : "md:col-span-4"}`}
              >
                <Link
                  href={`/news/${post.slug}`}
                  className="group block h-full"
                >
                  <motion.div
                    whileHover={{ y: -6 }}
                    transition={{ type: "spring", stiffness: 300, damping: 20 }}
                    className="bg-white rounded-2xl overflow-hidden border border-slate-200 hover:shadow-xl hover:border-transparent transition-all duration-300 h-full flex flex-col relative"
                  >
                    {getImageUrl(post) ? (
                      <div className={`relative w-full overflow-hidden ${index === 0 ? "h-72 md:h-96" : "h-48"}`}>
                        <img
                          src={getImageUrl(post)}
                          alt={post.title}
                          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                        />
                        <div className="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent" />
                      </div>
                    ) : (
                      <div className={`w-full bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center ${index === 0 ? "h-72 md:h-96" : "h-48"}`}>
                        <span className="text-5xl opacity-20">📰</span>
                      </div>
                    )}

                    <div className={`flex flex-col flex-grow ${index === 0 ? "p-8 md:p-10" : "p-6"}`}>
                      <div className="mb-4">
                        <span className={`inline-block px-3 py-1 rounded-md text-[10px] font-bold uppercase tracking-widest ${getCategoryColor(post.category)}`}>
                          {getCategoryLabel(post.category)}
                        </span>
                      </div>

                      <h3 className={`font-black text-slate-900 group-hover:text-[#C66810] transition-colors mb-3 ${index === 0 ? "text-3xl md:text-4xl leading-tight font-playfair" : "text-xl"}`}>
                        {post.title}
                      </h3>

                      <p className={`text-slate-600 mb-6 flex-grow ${index === 0 ? "text-lg line-clamp-3" : "text-sm line-clamp-2"}`}>
                        {post.content}
                      </p>

                      <div className="flex items-center gap-3 text-xs font-medium text-slate-400 mt-auto pt-4 border-t border-slate-100">
                        <span className="text-slate-700 bg-slate-100 px-2 py-1 rounded-md">{post.author_name}</span>
                        <span>&middot;</span>
                        <span>{new Date(post.created_at).toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric'})}</span>
                      </div>
                    </div>
                  </motion.div>
                </Link>
              </AnimatedSection>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
