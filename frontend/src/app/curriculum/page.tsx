/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useSession } from "next-auth/react";

const API_BASE = "https://mun-global.onrender.com";

const categoryIcons: Record<string, string> = {
  SPEECH: "🎤",
  DRAFT: "📜",
  NEGOTIATION: "🤝",
  RESEARCH: "🔍",
  PROCEDURE: "⚖️",
  GENERAL: "📚",
};

const categoryColors: Record<string, { bg: string; border: string; text: string; glow: string }> = {
  SPEECH: { bg: "bg-orange-50", border: "border-orange-200", text: "text-[#C66810]", glow: "hover:shadow-orange-200/60" },
  DRAFT: { bg: "bg-orange-50", border: "border-orange-200", text: "text-[#C66810]", glow: "hover:shadow-orange-200/60" },
  NEGOTIATION: { bg: "bg-emerald-50", border: "border-emerald-200", text: "text-emerald-700", glow: "hover:shadow-emerald-200/60" },
  RESEARCH: { bg: "bg-purple-50", border: "border-purple-200", text: "text-purple-700", glow: "hover:shadow-purple-200/60" },
  PROCEDURE: { bg: "bg-rose-50", border: "border-rose-200", text: "text-rose-700", glow: "hover:shadow-rose-200/60" },
  GENERAL: { bg: "bg-slate-50", border: "border-slate-200", text: "text-slate-700", glow: "hover:shadow-slate-200/60" },
};

export default function CurriculumPage() {
  const [categories, setCategories] = useState<any[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const { data: session } = useSession();
  const isAuthenticated = !!session?.user;

  useEffect(() => {
    async function fetchData() {
      try {
        const catRes = await fetch(`${API_BASE}/api/curriculum/categories/`);
        if (catRes.ok) {
          const catData = await catRes.json();
          setCategories(catData);
        }
      } catch (err) {
        console.error("Failed to fetch curriculum:", err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  useEffect(() => {
    if (!isAuthenticated) return;
    async function fetchStats() {
      try {
        const token = (session as any)?.user?.accessToken;
        const res = await fetch(`${API_BASE}/api/curriculum/stats/`, {
          headers: token ? { Authorization: `Bearer ${token}` } : {},
        });
        if (res.ok) setStats(await res.json());
      } catch { /* silent */ }
    }
    fetchStats();
  }, [isAuthenticated, session]);

  return (
    <div className="min-h-screen bg-white">
      {/* Hero with Bongo */}
      <section className="relative overflow-hidden bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 pt-32 pb-20">
        {/* Decorative grid */}
        <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:40px_40px]" />
        
        <div className="relative max-w-6xl mx-auto px-6 text-center">
          {/* Bongo Mascot */}
          <div className="inline-flex items-center justify-center w-28 h-28 rounded-full bg-gradient-to-br from-[#C66810] to-[#A05200] shadow-2xl shadow-[#C66810]/30 mb-8 text-6xl">
            🦉
          </div>
          
          <h1 className="text-5xl md:text-6xl font-black text-white mb-4 tracking-tight">
            Meet <span className="text-[#C66810]">Bongo</span>
          </h1>
          <p className="text-xl text-slate-300 mb-2 font-medium">
            Your personal strategist powered by{" "}
            <span className="text-[#C66810] font-bold">
              DiplomAI
            </span>
          </p>
          <p className="text-slate-400 max-w-2xl mx-auto mb-10">
            Master every skill in Model United Nations — from commanding speeches to airtight draft resolutions.
            Bongo the Strategist guides your journey with AI-powered personalized feedback.
          </p>

          <div className="flex flex-wrap gap-4 justify-center">
            <Link
              href="/curriculum/practice"
              className="px-8 py-3 bg-[#C66810] text-white font-bold rounded-xl shadow-sm hover:bg-[#A05200] transition-all duration-300 hover:-translate-y-0.5"
            >
              🎯 Start Practicing
            </Link>
            <Link
              href="/curriculum/submit"
              className="px-8 py-3 bg-white/10 backdrop-blur text-white font-bold rounded-xl border border-white/20 hover:bg-white/20 transition-all duration-300 hover:-translate-y-0.5"
            >
              📤 Submit for Review
            </Link>
          </div>
        </div>
      </section>

      {/* Stats Bar (if authenticated) */}
      {stats && (
        <section className="bg-slate-50 border-b border-slate-200">
          <div className="max-w-6xl mx-auto px-6 py-6">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              {[
                { label: "Lessons Completed", value: `${stats.completed_lessons}/${stats.total_lessons}`, sub: `${stats.completion_percentage}%` },
                { label: "Submissions", value: stats.total_submissions, sub: `${stats.reviewed_submissions} reviewed` },
                { label: "Average Score", value: `${stats.average_score}/100`, sub: "DiplomAI rating" },
                { label: "Progress", value: `${stats.completion_percentage}%`, sub: "overall" },
              ].map((stat, i) => (
                <div key={i} className="text-center">
                  <p className="text-2xl font-black text-slate-900">{stat.value}</p>
                  <p className="text-xs text-slate-500 font-medium uppercase tracking-wider">{stat.label}</p>
                  <p className="text-xs text-slate-400">{stat.sub}</p>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Categories Grid */}
      <section className="max-w-6xl mx-auto px-6 py-16">
        <div className="mb-12">
          <h2 className="text-3xl font-black text-slate-900">Your Curriculum</h2>
          <p className="text-slate-500 mt-2">Choose a track and start leveling up your MUN game.</p>
        </div>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="h-52 bg-slate-100 rounded-2xl animate-pulse" />
            ))}
          </div>
        ) : categories.length === 0 ? (
          <div className="text-center py-20">
            <div className="text-6xl mb-4">🦉</div>
            <h3 className="text-xl font-bold text-slate-700">Curriculum Coming Soon!</h3>
            <p className="text-slate-500 mt-2">Bongo is preparing lessons. Check back soon!</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {categories.map((cat) => {
              const colors = categoryColors[cat.category_type] || categoryColors.GENERAL;
              const icon = categoryIcons[cat.category_type] || "📚";
              return (
                <Link
                  key={cat.id}
                  href={`/curriculum/practice?category=${cat.slug}`}
                  className={`group relative p-6 rounded-2xl border ${colors.border} ${colors.bg} ${colors.glow} shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1`}
                >
                  <div className="flex items-start justify-between mb-4">
                    <span className="text-4xl">{icon}</span>
                    <div className="flex gap-2">
                      <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500 bg-white px-2 py-1 rounded-full">
                        {cat.lesson_count} lessons
                      </span>
                      <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500 bg-white px-2 py-1 rounded-full">
                        {cat.question_count} exercises
                      </span>
                    </div>
                  </div>
                  <h3 className={`text-xl font-bold ${colors.text} mb-2`}>{cat.name}</h3>
                  <p className="text-sm text-slate-500 line-clamp-2">{cat.description || "Master this essential MUN skill with Bongo."}</p>
                  <div className="mt-4 flex items-center gap-2 text-sm font-semibold text-slate-400 group-hover:text-slate-600 transition-colors">
                    <span>Explore →</span>
                  </div>
                </Link>
              );
            })}
          </div>
        )}
      </section>

      {/* How It Works */}
      <section className="bg-slate-50 border-t border-slate-200">
        <div className="max-w-6xl mx-auto px-6 py-16">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-black text-slate-900">How DiplomAI Works</h2>
            <p className="text-slate-500 mt-2">Powered by AI. Guided by Bongo. Built for delegates.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                step: "01",
                icon: "📝",
                title: "Pick a Challenge",
                desc: "Choose from speech prompts, draft resolution exercises, or negotiation scenarios.",
              },
              {
                step: "02",
                icon: "📤",
                title: "Submit Your Work",
                desc: "Upload your draft resolution text, paste your speech, or share a video recording.",
              },
              {
                step: "03",
                icon: "🦉",
                title: "Get AI Feedback",
                desc: "DiplomAI reviews your work and gives detailed scores, strengths, and actionable tips.",
              },
            ].map((item) => (
              <div key={item.step} className="relative bg-white rounded-2xl p-8 border border-slate-200 shadow-sm">
                <span className="absolute -top-3 -left-3 w-8 h-8 bg-slate-900 text-white text-xs font-bold rounded-full flex items-center justify-center">
                  {item.step}
                </span>
                <div className="text-4xl mb-4">{item.icon}</div>
                <h3 className="text-lg font-bold text-slate-900 mb-2">{item.title}</h3>
                <p className="text-sm text-slate-500">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
