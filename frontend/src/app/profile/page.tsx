/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef } from "react";
import Link from "next/link";
import { useSession } from "next-auth/react";
import { motion, useInView, AnimatePresence } from "framer-motion";

const API_BASE = "https://mun-global.onrender.com";

function AnimatedSection({ children, className = "", delay = 0 }: { children: React.ReactNode; className?: string; delay?: number }) {
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

const skillLevelConfig: Record<string, { color: string; bg: string; icon: string }> = {
  "New Delegate": { color: "text-slate-600", bg: "bg-slate-100", icon: "🌱" },
  Beginner: { color: "text-green-700", bg: "bg-green-100", icon: "📗" },
  Intermediate: { color: "text-[#C66810]", bg: "bg-orange-100", icon: "📙" },
  Advanced: { color: "text-red-700", bg: "bg-red-100", icon: "🏆" },
};

export default function ProfilePage() {
  const { data: session, status } = useSession();
  const user = session?.user as any;
  const token = user?.accessToken;
  const isAuthenticated = status === "authenticated";

  const [activeTab, setActiveTab] = useState<"progress" | "submissions" | "articles">("progress");
  const [stats, setStats] = useState<any>(null);
  const [submissions, setSubmissions] = useState<any[]>([]);
  const [articles, setArticles] = useState<any[]>([]);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [loadingStats, setLoadingStats] = useState(true);
  const [loadingSubs, setLoadingSubs] = useState(false);
  const [loadingArticles, setLoadingArticles] = useState(false);

  // Fetch curriculum stats
  useEffect(() => {
    if (!token) return;
    async function fetchStats() {
      try {
        const res = await fetch(`${API_BASE}/api/curriculum/stats/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (res.ok) setStats(await res.json());
      } catch (err) {
        console.error("Failed to fetch stats:", err);
      } finally {
        setLoadingStats(false);
      }
    }
    fetchStats();
  }, [token]);

  // Fetch submissions
  useEffect(() => {
    if (!token || activeTab !== "submissions") return;
    setLoadingSubs(true);
    fetch(`${API_BASE}/api/curriculum/submissions/`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then(setSubmissions)
      .catch(() => {})
      .finally(() => setLoadingSubs(false));
  }, [token, activeTab]);

  // Fetch articles
  useEffect(() => {
    if (!token || activeTab !== "articles") return;
    setLoadingArticles(true);
    fetch(`${API_BASE}/api/news/my-articles/`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then((data) => setArticles(Array.isArray(data) ? data : data.results || []))
      .catch(() => {})
      .finally(() => setLoadingArticles(false));
  }, [token, activeTab]);

  if (status === "loading") {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="text-4xl animate-bounce">🐵</div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen bg-slate-50">
        <section className="relative overflow-hidden bg-[#0a1628] grain">
          <div className="max-w-4xl mx-auto px-6 pt-32 pb-16 text-center relative z-10">
            <div className="text-5xl mb-4">🔒</div>
            <h1 className="text-3xl font-black text-white mb-4">Sign In Required</h1>
            <p className="text-slate-400 mb-8">Log in to see your profile and track your DiplomAI progress.</p>
            <Link
              href="/login"
              className="px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl shadow-lg hover:bg-[#A05200] transition-all"
            >
              Log In
            </Link>
          </div>
        </section>
      </div>
    );
  }

  const skillCfg = skillLevelConfig[stats?.skill_level || "New Delegate"];
  const scorePercent = stats?.average_score || 0;

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Profile Hero */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="absolute bottom-0 left-0 -ml-32 -mb-32 w-[400px] h-[400px] bg-blue-500/5 rounded-full blur-[80px]" />

        <div className="max-w-5xl mx-auto px-6 pt-28 pb-14 relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="flex flex-col md:flex-row items-start md:items-center gap-6"
          >
            {/* Avatar */}
            <div className="w-20 h-20 rounded-2xl bg-[#C66810] flex items-center justify-center text-white text-3xl font-black shadow-lg">
              {user?.name?.charAt(0)?.toUpperCase() || user?.username?.charAt(0)?.toUpperCase() || "U"}
            </div>

            <div className="flex-1">
              <h1 className="text-3xl md:text-4xl font-black text-white mb-1">
                {user?.name || user?.username || "Delegate"}
              </h1>
              <p className="text-slate-400 text-sm mb-3">{user?.email}</p>
              <div className="flex flex-wrap gap-2">
                <span className={`text-[10px] font-bold uppercase tracking-widest px-3 py-1 rounded-full ${skillCfg.bg} ${skillCfg.color}`}>
                  {skillCfg.icon} {stats?.skill_level || "New Delegate"}
                </span>
                <span className="text-[10px] font-bold uppercase tracking-widest px-3 py-1 rounded-full bg-white/10 text-white/70">
                  {user?.role === "AD" ? "Administrator" : user?.role === "JR" ? "Junior Delegate" : "Senior Delegate"}
                </span>
              </div>
            </div>

            {/* Quick Score */}
            {stats && stats.average_score > 0 && (
              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.3 }}
                className="bg-white/[0.07] backdrop-blur-sm rounded-2xl p-6 border border-white/10 text-center min-w-[140px]"
              >
                <div className="text-4xl font-black text-[#C66810]">{stats.average_score}</div>
                <div className="text-xs text-slate-400 font-medium">Avg Score</div>
              </motion.div>
            )}
          </motion.div>
        </div>
      </section>

      {/* Progress Overview Cards */}
      <section className="max-w-5xl mx-auto px-6 -mt-6 relative z-20">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {[
            {
              label: "Submissions",
              value: stats?.total_submissions || 0,
              icon: "📤",
              sub: `${stats?.reviewed_submissions || 0} reviewed`,
              color: "bg-blue-50 border-blue-200",
            },
            {
              label: "Avg Score",
              value: stats?.average_score || "—",
              icon: "📊",
              sub: stats?.best_score ? `Best: ${stats.best_score}` : "No scores yet",
              color: "bg-orange-50 border-orange-200",
            },
            {
              label: "Lessons Done",
              value: stats?.completed_lessons || 0,
              icon: "📚",
              sub: `${stats?.completion_percentage || 0}% complete`,
              color: "bg-green-50 border-green-200",
            },
            {
              label: "Skill Level",
              value: stats?.skill_level || "New",
              icon: skillCfg.icon,
              sub: "Based on performance",
              color: "bg-purple-50 border-purple-200",
              isText: true,
            },
          ].map((card, i) => (
            <AnimatedSection key={i} delay={i * 0.08}>
              <div className={`rounded-xl p-5 border shadow-sm bg-white ${card.color.split(" ")[1]}`}>
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-lg">{card.icon}</span>
                  <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500">{card.label}</span>
                </div>
                <div className={`font-black text-slate-900 ${card.isText ? "text-lg" : "text-2xl"}`}>
                  {card.value}
                </div>
                <p className="text-[11px] text-slate-500 mt-1">{card.sub}</p>
              </div>
            </AnimatedSection>
          ))}
        </div>
      </section>

      {/* Score Trend + Category Breakdown */}
      {stats && (stats.recent_scores?.length > 0 || stats.category_breakdown?.length > 0) && (
        <section className="max-w-5xl mx-auto px-6 mt-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Score Trend */}
            {stats.recent_scores?.length > 1 && (
              <AnimatedSection delay={0.1}>
                <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
                  <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
                    <span>📈</span> Recent Score Trend
                  </h3>
                  <div className="flex items-end gap-2 h-32">
                    {[...stats.recent_scores].reverse().map((score: number, i: number) => (
                      <motion.div
                        key={i}
                        initial={{ height: 0 }}
                        animate={{ height: `${Math.max(score, 5)}%` }}
                        transition={{ duration: 0.6, delay: i * 0.08 }}
                        className="flex-1 rounded-t-lg relative group"
                        style={{
                          backgroundColor:
                            score >= 80 ? "#22c55e" : score >= 60 ? "#C66810" : score >= 40 ? "#f59e0b" : "#ef4444",
                          minHeight: "6px",
                        }}
                      >
                        <div className="absolute -top-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-slate-500 opacity-0 group-hover:opacity-100 transition-opacity">
                          {score}
                        </div>
                      </motion.div>
                    ))}
                  </div>
                  <div className="flex justify-between mt-2 text-[9px] text-slate-400 font-medium">
                    <span>Oldest</span>
                    <span>Latest</span>
                  </div>
                </div>
              </AnimatedSection>
            )}

            {/* Category Breakdown */}
            {stats.category_breakdown?.length > 0 && (
              <AnimatedSection delay={0.2}>
                <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
                  <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
                    <span>🎯</span> Performance by Category
                  </h3>
                  <div className="space-y-3">
                    {stats.category_breakdown.map((cat: any, i: number) => (
                      <div key={i}>
                        <div className="flex justify-between items-center mb-1">
                          <span className="text-sm font-medium text-slate-700">
                            {cat.category__name || cat.category__category_type}
                          </span>
                          <span className="text-sm font-bold text-[#C66810]">
                            {Math.round(cat.avg_score || 0)}
                          </span>
                        </div>
                        <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                          <motion.div
                            initial={{ width: 0 }}
                            animate={{ width: `${cat.avg_score || 0}%` }}
                            transition={{ duration: 0.8, delay: 0.3 + i * 0.1 }}
                            className="h-2 rounded-full bg-[#C66810]"
                          />
                        </div>
                        <div className="flex justify-between mt-0.5">
                          <span className="text-[10px] text-slate-400">{cat.count} submission{cat.count !== 1 ? "s" : ""}</span>
                          <span className="text-[10px] text-slate-400">Best: {cat.best_score || "—"}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </AnimatedSection>
            )}
          </div>
        </section>
      )}

      {/* Overall Progress Bar */}
      {stats && (
        <section className="max-w-5xl mx-auto px-6 mt-8">
          <AnimatedSection delay={0.15}>
            <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-bold text-slate-900 flex items-center gap-2">
                  <span>🏅</span> Overall Progress
                </h3>
                <span className="text-sm font-bold text-[#C66810]">{scorePercent}/100</span>
              </div>
              <div className="w-full bg-slate-100 rounded-full h-4 overflow-hidden mb-3">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: `${scorePercent}%` }}
                  transition={{ duration: 1.2, ease: [0.22, 1, 0.36, 1] }}
                  className="h-4 rounded-full bg-gradient-to-r from-[#C66810] to-[#E8913A]"
                />
              </div>
              <div className="flex justify-between text-[10px] font-bold uppercase tracking-widest text-slate-400">
                <span>🌱 Beginner</span>
                <span>📗 Intermediate</span>
                <span>🏆 Advanced</span>
              </div>
            </div>
          </AnimatedSection>
        </section>
      )}

      {/* Tabs: Submissions & Articles */}
      <section className="max-w-5xl mx-auto px-6 mt-10 mb-16">
        <div className="flex gap-1 bg-white rounded-xl p-1.5 border border-slate-200 shadow-sm inline-flex mb-6">
          {[
            { key: "progress" as const, label: "📈 Progress Track" },
            { key: "submissions" as const, label: "📤 My Submissions" },
            { key: "articles" as const, label: "📝 My Articles" },
          ].map((tab) => (
            <button
              key={tab.key}
              onClick={() => setActiveTab(tab.key)}
              className={`px-5 py-2.5 rounded-lg text-sm font-bold transition-all ${
                activeTab === tab.key
                  ? "bg-[#C66810] text-white shadow-sm"
                  : "text-slate-600 hover:bg-slate-50 hover:text-slate-800"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        <AnimatePresence mode="wait">
          {/* Progress Track Tab */}
          {activeTab === "progress" && (
            <motion.div
              key="progress"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              className="space-y-4"
            >
              {!stats || stats.total_submissions === 0 ? (
                <div className="bg-white rounded-2xl p-12 border border-slate-200 text-center">
                  <div className="text-4xl mb-3">🐵</div>
                  <h3 className="text-lg font-bold text-slate-700 mb-2">Start Your Journey</h3>
                  <p className="text-slate-500 text-sm mb-6">
                    Complete practice exercises with DiplomAI to begin tracking your progress.
                  </p>
                  <Link
                    href="/curriculum/practice"
                    className="inline-block px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors"
                  >
                    Go to Practice Arena
                  </Link>
                </div>
              ) : (
                <div className="space-y-4">
                  {/* Milestones */}
                  <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
                    <h3 className="font-bold text-slate-900 mb-4">🏅 Milestones</h3>
                    <div className="space-y-3">
                      {[
                        { label: "First Submission", target: 1, current: stats.total_submissions, icon: "🚀" },
                        { label: "5 Submissions", target: 5, current: stats.total_submissions, icon: "📝" },
                        { label: "10 Submissions", target: 10, current: stats.total_submissions, icon: "💪" },
                        { label: "Score 70+", target: 70, current: stats.best_score, icon: "⭐" },
                        { label: "Score 85+", target: 85, current: stats.best_score, icon: "🏆" },
                        { label: "Score 95+", target: 95, current: stats.best_score, icon: "👑" },
                      ].map((milestone, i) => {
                        const achieved = milestone.current >= milestone.target;
                        return (
                          <div
                            key={i}
                            className={`flex items-center gap-3 p-3 rounded-xl transition-all ${
                              achieved ? "bg-green-50 border border-green-200" : "bg-slate-50 border border-slate-200"
                            }`}
                          >
                            <span className="text-xl">{achieved ? "✅" : milestone.icon}</span>
                            <span className={`flex-1 text-sm font-medium ${achieved ? "text-green-700" : "text-slate-500"}`}>
                              {milestone.label}
                            </span>
                            {achieved && (
                              <span className="text-[10px] font-bold text-green-600 bg-green-100 px-2 py-0.5 rounded">
                                ACHIEVED
                              </span>
                            )}
                          </div>
                        );
                      })}
                    </div>
                  </div>

                  {/* Recommended Next Steps */}
                  <div className="bg-orange-50 rounded-2xl p-6 border border-orange-200">
                    <h3 className="font-bold text-[#C66810] mb-3 flex items-center gap-2">
                      <span>🐵</span> Bongo&apos;s Recommendation
                    </h3>
                    <p className="text-sm text-slate-700 mb-4">
                      {stats.average_score >= 85
                        ? "Outstanding work! You're performing like a seasoned diplomat. Try advanced exercises and challenge yourself with new categories."
                        : stats.average_score >= 65
                        ? "Strong progress! Focus on your weaker categories and aim for consistency above 80 in all areas."
                        : stats.average_score > 0
                        ? "You're building a solid foundation. Keep practicing regularly and review Bongo's feedback carefully after each submission."
                        : "Welcome! Start with beginner exercises to build confidence, then work your way up."}
                    </p>
                    <Link
                      href="/curriculum/practice"
                      className="inline-block px-5 py-2 bg-[#C66810] text-white font-bold rounded-lg text-sm hover:bg-[#A05200] transition-colors"
                    >
                      Continue Training →
                    </Link>
                  </div>
                </div>
              )}
            </motion.div>
          )}

          {/* Submissions Tab */}
          {activeTab === "submissions" && (
            <motion.div
              key="submissions"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
            >
              {loadingSubs ? (
                <div className="space-y-3">
                  {[1, 2, 3].map((i) => (
                    <div key={i} className="h-24 bg-white rounded-xl border border-slate-200 animate-pulse" />
                  ))}
                </div>
              ) : submissions.length === 0 ? (
                <div className="bg-white rounded-2xl p-12 border border-slate-200 text-center">
                  <div className="text-4xl mb-3">📤</div>
                  <h3 className="text-lg font-bold text-slate-700 mb-2">No Submissions Yet</h3>
                  <p className="text-slate-500 text-sm mb-6">Submit your first exercise for AI review!</p>
                  <Link
                    href="/curriculum/practice"
                    className="inline-block px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors"
                  >
                    Practice Now
                  </Link>
                </div>
              ) : (
                <div className="space-y-3">
                  {submissions.map((sub: any, i: number) => (
                    <AnimatedSection key={sub.id} delay={i * 0.05}>
                      <div className="bg-white rounded-xl p-5 border border-slate-200 shadow-sm hover:shadow-md hover:border-orange-200 transition-all">
                        <div className="flex items-start justify-between">
                          <div className="flex-1">
                            <div className="flex items-center gap-2 mb-1.5">
                              <span className="text-[9px] font-bold uppercase tracking-widest text-slate-500 bg-slate-100 px-2 py-0.5 rounded">
                                {sub.category_name}
                              </span>
                              <span
                                className={`text-[9px] font-bold uppercase tracking-widest px-2 py-0.5 rounded ${
                                  sub.status === "REVIEWED" ? "bg-green-100 text-green-700" : "bg-orange-100 text-[#C66810]"
                                }`}
                              >
                                {sub.status === "REVIEWED" ? "Reviewed" : "Pending"}
                              </span>
                            </div>
                            <p className="text-sm text-slate-700 line-clamp-2">
                              {sub.text_content?.substring(0, 150) || `${sub.submission_type} submission`}
                              {sub.text_content?.length > 150 ? "..." : ""}
                            </p>
                            <p className="text-[10px] text-slate-400 mt-1">
                              {new Date(sub.created_at).toLocaleDateString("en-US", {
                                year: "numeric",
                                month: "short",
                                day: "numeric",
                              })}
                            </p>
                          </div>
                          {sub.feedback && (
                            <div className="ml-4 text-center flex-shrink-0">
                              <div className="text-2xl font-black text-[#C66810]">{sub.feedback.overall_score}</div>
                              <div className="text-[9px] text-slate-400 font-medium">/100</div>
                            </div>
                          )}
                        </div>
                      </div>
                    </AnimatedSection>
                  ))}
                </div>
              )}
            </motion.div>
          )}

          {/* Articles Tab */}
          {activeTab === "articles" && (
            <motion.div
              key="articles"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
            >
              {loadingArticles ? (
                <div className="space-y-3">
                  {[1, 2, 3].map((i) => (
                    <div key={i} className="h-24 bg-white rounded-xl border border-slate-200 animate-pulse" />
                  ))}
                </div>
              ) : articles.length === 0 ? (
                <div className="bg-white rounded-2xl p-12 border border-slate-200 text-center">
                  <div className="text-4xl mb-3">📝</div>
                  <h3 className="text-lg font-bold text-slate-700 mb-2">No Articles Yet</h3>
                  <p className="text-slate-500 text-sm mb-6">Write your first MUN news article!</p>
                  <Link
                    href="/news/add"
                    className="inline-block px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors"
                  >
                    Write Article
                  </Link>
                </div>
              ) : (
                <div className="space-y-3">
                  {articles.map((article: any, i: number) => (
                    <AnimatedSection key={article.id || i} delay={i * 0.05}>
                      <Link
                        href={`/news/${article.slug || article.id}`}
                        className="block bg-white rounded-xl p-5 border border-slate-200 shadow-sm hover:shadow-md hover:border-orange-200 transition-all"
                      >
                        <div className="flex items-center gap-2 mb-1.5">
                          <span
                            className={`text-[9px] font-bold uppercase tracking-widest px-2 py-0.5 rounded ${
                              article.status === "approved"
                                ? "bg-green-100 text-green-700"
                                : article.status === "rejected"
                                ? "bg-red-100 text-red-700"
                                : "bg-orange-100 text-[#C66810]"
                            }`}
                          >
                            {article.status || "draft"}
                          </span>
                          <span className="text-[10px] text-slate-400">
                            {article.created_at &&
                              new Date(article.created_at).toLocaleDateString("en-US", {
                                year: "numeric",
                                month: "short",
                                day: "numeric",
                              })}
                          </span>
                        </div>
                        <h3 className="font-bold text-slate-900 text-sm">{article.title}</h3>
                        {article.summary && (
                          <p className="text-xs text-slate-500 mt-1 line-clamp-2">{article.summary}</p>
                        )}
                      </Link>
                    </AnimatedSection>
                  ))}
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </section>
    </div>
  );
}
