/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef } from "react";
import Link from "next/link";
import { useSession } from "next-auth/react";
import { motion, useInView } from "framer-motion";

const API_BASE = "https://mun-global.onrender.com";

const categoryIcons: Record<string, string> = {
  SPEECH: "🎤",
  DRAFT: "📜",
  NEGOTIATION: "🤝",
  RESEARCH: "🔍",
  PROCEDURE: "⚖️",
  GENERAL: "📚",
};

const categoryColors: Record<string, { bg: string; border: string; text: string; iconBg: string }> = {
  SPEECH: { bg: "bg-white", border: "hover:border-orange-300", text: "text-slate-700", iconBg: "bg-orange-100 text-orange-600" },
  DRAFT: { bg: "bg-white", border: "hover:border-blue-300", text: "text-slate-700", iconBg: "bg-blue-100 text-blue-600" },
  NEGOTIATION: { bg: "bg-white", border: "hover:border-emerald-300", text: "text-slate-700", iconBg: "bg-emerald-100 text-emerald-600" },
  RESEARCH: { bg: "bg-white", border: "hover:border-purple-300", text: "text-slate-700", iconBg: "bg-purple-100 text-purple-600" },
  PROCEDURE: { bg: "bg-white", border: "hover:border-rose-300", text: "text-slate-700", iconBg: "bg-rose-100 text-rose-600" },
  GENERAL: { bg: "bg-white", border: "hover:border-slate-300", text: "text-slate-700", iconBg: "bg-slate-100 text-slate-600" },
};

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

export default function CurriculumPage() {
  const [categories, setCategories] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const { data: session } = useSession();
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const isAuthenticated = !!session?.user;

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(`${API_BASE}/api/curriculum/categories/`);
        if (res.ok) {
          const data = await res.json();
          if (data && data.length > 0) setCategories(data);
        }
      } catch (err) {
        console.error("Failed to fetch curriculum:", err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="absolute bottom-0 left-0 -ml-32 -mb-32 w-[400px] h-[400px] bg-blue-500/5 rounded-full blur-[80px]" />
        <div className="absolute top-1/2 left-1/4 -translate-y-1/2 w-[300px] h-[300px] rounded-full border border-white/[0.03]" />

        <div className="max-w-7xl mx-auto px-6 lg:px-8 py-24 flex flex-col md:flex-row items-center gap-12 relative z-10">
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
            className="md:w-1/2 text-left space-y-6"
          >
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/[0.07] text-[#E8913A] text-sm font-bold border border-white/10 backdrop-blur-sm">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-orange-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-[#C66810]"></span>
              </span>
              DiplomAI Beta
            </div>

            <h1 className="text-5xl md:text-6xl font-black text-white tracking-tight leading-[1.1]">
              Meet <span className="font-playfair italic text-[#C66810]">Bongo</span>,<br />
              Your MUN Strategist
            </h1>

            <p className="text-lg text-slate-400 leading-relaxed max-w-lg">
              Unlock your potential with AI-driven feedback on speeches, resolutions, and strategy.
              Review your performance in real-time and climb the ranks of diplomacy.
            </p>

            <div className="flex flex-wrap gap-4 pt-4">
              <Link
                href="/curriculum/practice"
                className="group px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl shadow-lg shadow-orange-900/30 hover:bg-[#A05200] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 transform"
              >
                Start Training
                <span className="inline-block ml-2 group-hover:translate-x-1 transition-transform">&rarr;</span>
              </Link>
              <Link
                href="#modules"
                className="px-8 py-4 bg-white/[0.07] text-white font-bold rounded-xl border border-white/10 hover:bg-white/[0.12] hover:border-white/20 backdrop-blur-sm transition-all duration-300"
              >
                View Modules
              </Link>
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.3, ease: [0.22, 1, 0.36, 1] }}
            className="md:w-1/2 flex justify-center md:justify-end relative"
          >
            <div className="relative w-80 h-80 md:w-96 md:h-96">
              {/* Decorative ring */}
              <div className="absolute inset-[-12px] rounded-full border-2 border-dashed border-[#C66810]/20 animate-[spin_30s_linear_infinite]" />
              <div className="absolute inset-[-4px] rounded-full bg-gradient-to-br from-[#C66810]/20 to-transparent blur-sm" />
              <video
                src="/munkeyanimation.mp4"
                autoPlay
                loop
                muted
                playsInline
                className="w-full h-full object-cover rounded-full drop-shadow-2xl relative z-10"
              />
            </div>
          </motion.div>
        </div>
      </section>

      {/* Categories / Modules Grid */}
      <section id="modules" className="max-w-7xl mx-auto px-6 lg:px-8 py-24">
        <AnimatedSection>
          <div className="text-center mb-16">
            <p className="text-[11px] font-black uppercase tracking-[0.3em] text-[#C66810] mb-3">Curriculum</p>
            <h2 className="text-3xl md:text-4xl font-black text-slate-900 mb-4 font-playfair">Training Modules</h2>
            <p className="text-slate-500 text-lg max-w-2xl mx-auto">
              Select a skill to focus on. Each module is designed to target specific areas of your Model UN performance.
            </p>
          </div>
        </AnimatedSection>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[1, 2, 3].map((i) => (
              <div key={i} className="h-64 bg-white rounded-2xl border border-slate-200 shadow-sm animate-pulse"></div>
            ))}
          </div>
        ) : categories.length === 0 ? (
          <AnimatedSection>
            <div className="text-center py-16 bg-white rounded-2xl border border-slate-200">
              <div className="text-5xl mb-4">🐵</div>
              <h3 className="text-xl font-bold text-slate-700 mb-2">Modules loading soon</h3>
              <p className="text-slate-500 mb-6">The backend is warming up. Try refreshing in a moment!</p>
              <Link href="/curriculum/practice" className="inline-block px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors">
                Go to Practice Arena
              </Link>
            </div>
          </AnimatedSection>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {categories.map((cat, idx) => {
              const style = categoryColors[cat.type || cat.category_type] || categoryColors.GENERAL;
              return (
                <AnimatedSection key={idx} delay={idx * 0.08}>
                  <Link
                    href={`/curriculum/practice?category=${cat.slug || cat.id}`}
                    className={`group relative bg-white rounded-2xl p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:border-transparent transition-all duration-300 flex flex-col items-start gap-4 overflow-hidden hover:-translate-y-1 ${style.border} block h-full`}
                  >
                    <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-slate-50 to-transparent rounded-bl-full opacity-0 group-hover:opacity-100 transition-opacity" />
                    <div className={`w-14 h-14 rounded-xl ${style.iconBg} flex items-center justify-center text-2xl mb-2 group-hover:scale-110 transition-transform duration-300`}>
                      {categoryIcons[cat.type || cat.category_type] || "📚"}
                    </div>

                    <div>
                      <h3 className="text-xl font-bold text-slate-900 mb-2 group-hover:text-[#C66810] transition-colors">
                        {cat.name}
                      </h3>
                      <p className="text-slate-500 text-sm leading-relaxed">
                        {cat.description || "Enhance your skills with AI feedback."}
                      </p>
                    </div>

                    <div className="mt-auto pt-4 flex items-center text-sm font-bold text-slate-400 group-hover:text-[#C66810] transition-colors">
                      Start Module <span className="ml-2 group-hover:translate-x-1 transition-transform">&rarr;</span>
                    </div>
                  </Link>
                </AnimatedSection>
              );
            })}
          </div>
        )}
      </section>

      {/* CTA Section */}
      <AnimatedSection>
        <section className="bg-[#0a1628] py-24 relative overflow-hidden grain">
          <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-orange-500/20 rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl"></div>

          <div className="max-w-4xl mx-auto px-6 text-center relative z-10">
            <h2 className="text-3xl md:text-4xl font-black text-white mb-6">
              Ready to become a <span className="font-playfair italic text-[#C66810]">Best Delegate</span>?
            </h2>
            <p className="text-slate-300 text-lg mb-10 max-w-2xl mx-auto">
              Join thousands of students enhancing their diplomacy skills with DiplomAI.
              Sign up today to track your progress.
            </p>
            {!isAuthenticated && (
              <Link
                href="/signup"
                className="inline-block px-10 py-4 bg-white text-slate-900 font-bold rounded-xl shadow-lg hover:bg-slate-100 transition-all duration-200"
              >
                Get Started for Free
              </Link>
            )}
          </div>
        </section>
      </AnimatedSection>
    </div>
  );
}
