/* eslint-disable @typescript-eslint/no-explicit-any */
// src/app/skills/page.tsx
"use client";
import { useState, useEffect, useRef } from "react";
import { motion, useInView, AnimatePresence } from "framer-motion";

function AnimatedSection({ children, className = "", delay = 0 }: { children: React.ReactNode; className?: string; delay?: number }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-60px" });
  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1], delay }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

const difficultyColor: Record<string, string> = {
  BEG: "bg-emerald-100 text-emerald-700",
  INT: "bg-orange-100 text-[#C66810]",
  ADV: "bg-red-100 text-red-700",
  Beginner: "bg-emerald-100 text-emerald-700",
  Intermediate: "bg-orange-100 text-[#C66810]",
  Advanced: "bg-red-100 text-red-700",
};

export default function SkillsPage() {
  const [categories, setCategories] = useState<any[]>([]);
  const [activeTab, setActiveTab] = useState(0);

  useEffect(() => {
    fetch("https://mun-global.onrender.com/api/skills/")
      .then(res => res.json())
      .then(data => setCategories(data));
  }, []);

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
            <p className="text-[11px] font-black uppercase tracking-[0.3em] text-[#C66810] mb-4">Learn & Grow</p>
            <h1 className="text-5xl md:text-6xl font-black text-white tracking-tight leading-[1.1] mb-4">
              Delegate <span className="font-playfair italic text-[#C66810]">Skill Sharing</span>
            </h1>
            <p className="text-slate-400 text-lg max-w-xl">
              Master the art of diplomacy with curated training videos from experienced delegates and coaches.
            </p>
          </motion.div>
        </div>
      </section>

      <main className="max-w-7xl mx-auto px-6 py-12">
        {/* Category Tabs */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="flex gap-3 mb-12 overflow-x-auto pb-4 scrollbar-hide"
        >
          {categories.map((cat, idx) => (
            <button
              key={cat.id}
              onClick={() => setActiveTab(idx)}
              className={`relative px-6 py-2.5 rounded-full font-bold transition-all whitespace-nowrap text-sm ${
                activeTab === idx
                  ? "bg-[#C66810] text-white shadow-lg shadow-orange-200"
                  : "bg-white text-slate-600 hover:bg-slate-100 border border-slate-200"
              }`}
            >
              {cat.name}
              {activeTab === idx && (
                <motion.div
                  layoutId="activeSkillTab"
                  className="absolute inset-0 bg-[#C66810] rounded-full -z-10"
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                />
              )}
            </button>
          ))}
        </motion.div>

        {/* Video Grid */}
        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -16 }}
            transition={{ duration: 0.35 }}
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
          >
            {categories[activeTab]?.videos.map((video: any, idx: number) => (
              <AnimatedSection key={video.id} delay={idx * 0.08}>
                <motion.div
                  whileHover={{ y: -6 }}
                  transition={{ type: "spring", stiffness: 300, damping: 20 }}
                  className="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-xl hover:border-transparent transition-all group"
                >
                  {/* YouTube Embed */}
                  <div className="aspect-video w-full relative overflow-hidden">
                    <iframe
                      className="w-full h-full"
                      src={`https://www.youtube.com/embed/${video.video_id}`}
                      title={video.title}
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowFullScreen
                    ></iframe>
                  </div>
                  <div className="p-6">
                    <div className="flex justify-between items-start mb-3">
                      <span className={`text-[10px] font-bold uppercase tracking-widest px-2.5 py-1 rounded-md ${difficultyColor[video.difficulty] || "bg-slate-100 text-slate-600"}`}>
                        {video.difficulty}
                      </span>
                    </div>
                    <h3 className="font-bold text-lg text-slate-900 group-hover:text-[#C66810] transition-colors">{video.title}</h3>
                    <p className="text-sm text-slate-500 mt-2 line-clamp-2">{video.description}</p>
                  </div>
                </motion.div>
              </AnimatedSection>
            ))}
          </motion.div>
        </AnimatePresence>

        {categories.length === 0 && (
          <div className="text-center py-20">
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-slate-100 flex items-center justify-center">
              <span className="text-3xl">🎬</span>
            </div>
            <h3 className="text-lg font-bold text-slate-700 mb-2">Loading Skills...</h3>
            <p className="text-slate-500 text-sm">Fetching training modules from the server.</p>
          </div>
        )}
      </main>
    </div>
  );
}
