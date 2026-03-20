/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef } from "react";
import Link from "next/link";
import { useSession } from "next-auth/react";
import { motion, useInView } from "framer-motion";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
} from "recharts";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "https://mun-global.onrender.com";

const RANK_BADGES = [
  { name: "Novice Delegate", icon: "🌱", min: 0, max: 44, color: "text-slate-600", bg: "bg-slate-100" },
  { name: "Junior Delegate", icon: "📗", min: 45, max: 64, color: "text-green-700", bg: "bg-green-100" },
  { name: "Senior Delegate", icon: "📙", min: 65, max: 79, color: "text-[#C66810]", bg: "bg-orange-100" },
  { name: "Distinguished Delegate", icon: "🏆", min: 80, max: 89, color: "text-amber-700", bg: "bg-amber-100" },
  { name: "Best Delegate", icon: "👑", min: 90, max: 100, color: "text-red-700", bg: "bg-red-100" },
];

const CATEGORY_LABELS: Record<string, string> = {
  SPEECH: "Speech",
  DRAFT: "Draft Resolution",
  NEGOTIATION: "Negotiation",
  RESEARCH: "Research",
  PROCEDURE: "Procedure",
  GENERAL: "General",
};

const CATEGORY_COLORS: Record<string, string> = {
  SPEECH: "#C66810",
  DRAFT: "#3b82f6",
  NEGOTIATION: "#10b981",
  RESEARCH: "#8b5cf6",
  PROCEDURE: "#f43f5e",
  GENERAL: "#64748b",
};

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

function getRankBadge(score: number) {
  return RANK_BADGES.find((b) => score >= b.min && score <= b.max) || RANK_BADGES[0];
}

export default function DashboardPage() {
  const { data: session, status } = useSession();
  const user = session?.user as any;
  const token = user?.accessToken;
  const isAuthenticated = status === "authenticated";

  const [stats, setStats] = useState<any>(null);
  const [progress, setProgress] = useState<any>(null);
  const [submissions, setSubmissions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;

    const headers = { Authorization: `Bearer ${token}` };

    Promise.all([
      fetch(`${API_BASE}/api/curriculum/user-stats/`, { headers }).then((r) => r.ok ? r.json() : null),
      fetch(`${API_BASE}/api/curriculum/user-progress/`, { headers }).then((r) => r.ok ? r.json() : null),
      fetch(`${API_BASE}/api/curriculum/submissions/`, { headers }).then((r) => r.ok ? r.json() : null),
    ])
      .then(([statsData, progressData, subsData]) => {
        if (statsData) setStats(statsData);
        if (progressData) setProgress(progressData);
        if (subsData) setSubmissions(Array.isArray(subsData) ? subsData : subsData.results || []);
      })
      .catch((err) => console.error("Dashboard fetch error:", err))
      .finally(() => setLoading(false));
  }, [token]);

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
            <p className="text-slate-400 mb-8">Log in to view your progress dashboard.</p>
            <Link href="/login" className="px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl shadow-lg hover:bg-[#A05200] transition-all">
              Log In
            </Link>
          </div>
        </section>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="text-4xl animate-bounce">🐵</div>
      </div>
    );
  }

  const badge = getRankBadge(stats?.average_score || 0);

  // Build radar chart data from all 6 categories
  const radarData = Object.keys(CATEGORY_LABELS).map((cat) => ({
    category: CATEGORY_LABELS[cat],
    score: stats?.scores_by_category?.[cat]?.avg || 0,
    fullMark: 100,
  }));

  // Score trend for line chart
  const trendData = (progress?.score_trend || []).map((s: any, i: number) => ({
    index: i + 1,
    score: s.score,
    date: s.date ? new Date(s.date).toLocaleDateString("en-US", { month: "short", day: "numeric" }) : `#${i + 1}`,
    category: CATEGORY_LABELS[s.category] || s.category,
  }));

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="absolute bottom-0 left-0 -ml-32 -mb-32 w-[400px] h-[400px] bg-blue-500/5 rounded-full blur-[80px]" />
        <div className="max-w-6xl mx-auto px-6 pt-24 pb-14 relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <p className="text-[11px] font-black uppercase tracking-[0.3em] text-[#E8913A] mb-3">Progress Dashboard</p>
            <h1 className="text-4xl md:text-5xl font-black text-white mb-2">
              Your <span className="font-playfair italic text-[#C66810]">Journey</span>
            </h1>
            <p className="text-slate-400 text-lg max-w-xl">
              Track your growth, spot your strengths, and find what to work on next.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Top Stats Row */}
      <section className="max-w-6xl mx-auto px-6 -mt-6 relative z-20">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {[
            {
              label: "Streak",
              value: `${stats?.current_streak_days || 0}d`,
              icon: "🔥",
              sub: `Longest: ${stats?.longest_streak_days || 0}d`,
              borderColor: "border-orange-200",
            },
            {
              label: "Submissions",
              value: stats?.total_submissions || 0,
              icon: "📤",
              sub: "Total reviewed",
              borderColor: "border-blue-200",
            },
            {
              label: "Average Score",
              value: stats?.average_score || "—",
              icon: "📊",
              sub: stats?.best_score ? `Best: ${stats.best_score}` : "No scores yet",
              borderColor: "border-green-200",
            },
            {
              label: "Rank",
              value: badge.name,
              icon: badge.icon,
              sub: `Score ${stats?.average_score || 0}/100`,
              borderColor: "border-purple-200",
              isText: true,
            },
          ].map((card, i) => (
            <AnimatedSection key={i} delay={i * 0.08}>
              <div className={`rounded-xl p-5 border shadow-sm bg-white ${card.borderColor}`}>
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-lg">{card.icon}</span>
                  <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500">{card.label}</span>
                </div>
                <div className={`font-black text-slate-900 ${card.isText ? "text-base" : "text-2xl"}`}>
                  {card.value}
                </div>
                <p className="text-[11px] text-slate-500 mt-1">{card.sub}</p>
              </div>
            </AnimatedSection>
          ))}
        </div>
      </section>

      {/* Radar + Line Charts */}
      <section className="max-w-6xl mx-auto px-6 mt-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Radar Chart — Category Performance */}
          <AnimatedSection delay={0.1}>
            <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
              <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
                <span>🎯</span> Skills Radar
              </h3>
              {radarData.some((d) => d.score > 0) ? (
                <ResponsiveContainer width="100%" height={300}>
                  <RadarChart data={radarData} cx="50%" cy="50%" outerRadius="70%">
                    <PolarGrid stroke="#e2e8f0" />
                    <PolarAngleAxis
                      dataKey="category"
                      tick={{ fontSize: 11, fill: "#64748b", fontWeight: 600 }}
                    />
                    <PolarRadiusAxis
                      angle={30}
                      domain={[0, 100]}
                      tick={{ fontSize: 10, fill: "#94a3b8" }}
                    />
                    <Radar
                      name="Score"
                      dataKey="score"
                      stroke="#C66810"
                      fill="#C66810"
                      fillOpacity={0.2}
                      strokeWidth={2}
                    />
                  </RadarChart>
                </ResponsiveContainer>
              ) : (
                <div className="h-[300px] flex items-center justify-center text-slate-400 text-sm">
                  Complete exercises to see your skills radar
                </div>
              )}
            </div>
          </AnimatedSection>

          {/* Score Trend Line Chart */}
          <AnimatedSection delay={0.2}>
            <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
              <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
                <span>📈</span> Score Trend
              </h3>
              {trendData.length > 1 ? (
                <ResponsiveContainer width="100%" height={300}>
                  <LineChart data={trendData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                    <XAxis
                      dataKey="date"
                      tick={{ fontSize: 10, fill: "#94a3b8" }}
                      tickLine={false}
                    />
                    <YAxis
                      domain={[0, 100]}
                      tick={{ fontSize: 10, fill: "#94a3b8" }}
                      tickLine={false}
                    />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#fff",
                        border: "1px solid #e2e8f0",
                        borderRadius: "8px",
                        fontSize: "12px",
                      }}
                      formatter={(value) => [`${value}/100`, "Score"]}
                    />
                    <Line
                      type="monotone"
                      dataKey="score"
                      stroke="#C66810"
                      strokeWidth={2.5}
                      dot={{ fill: "#C66810", r: 4 }}
                      activeDot={{ r: 6, fill: "#A05200" }}
                    />
                  </LineChart>
                </ResponsiveContainer>
              ) : (
                <div className="h-[300px] flex items-center justify-center text-slate-400 text-sm">
                  {trendData.length === 1 ? "Submit one more exercise to see your trend" : "Complete exercises to see your score trend"}
                </div>
              )}
            </div>
          </AnimatedSection>
        </div>
      </section>

      {/* Category Breakdown */}
      {stats?.scores_by_category && Object.keys(stats.scores_by_category).length > 0 && (
        <section className="max-w-6xl mx-auto px-6 mt-8">
          <AnimatedSection delay={0.15}>
            <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
              <h3 className="font-bold text-slate-900 mb-5 flex items-center gap-2">
                <span>📋</span> Category Breakdown
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {Object.entries(stats.scores_by_category).map(([cat, data]: [string, any], i: number) => (
                  <div key={cat} className="p-4 rounded-xl border border-slate-100 bg-slate-50/50">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm font-bold text-slate-700">{CATEGORY_LABELS[cat] || cat}</span>
                      <span className="text-sm font-black" style={{ color: CATEGORY_COLORS[cat] || "#64748b" }}>
                        {Math.round(data.avg || 0)}
                      </span>
                    </div>
                    <div className="w-full bg-slate-200 rounded-full h-2 overflow-hidden mb-2">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${data.avg || 0}%` }}
                        transition={{ duration: 0.8, delay: 0.2 + i * 0.1 }}
                        className="h-2 rounded-full"
                        style={{ backgroundColor: CATEGORY_COLORS[cat] || "#64748b" }}
                      />
                    </div>
                    <div className="flex justify-between text-[10px] text-slate-400">
                      <span>{data.count} submission{data.count !== 1 ? "s" : ""}</span>
                      <span>Best: {data.best || "—"}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </AnimatedSection>
        </section>
      )}

      {/* Rank Progress */}
      <section className="max-w-6xl mx-auto px-6 mt-8">
        <AnimatedSection delay={0.2}>
          <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
            <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
              <span>🏅</span> Rank Progress
            </h3>
            <div className="flex items-center gap-1 mb-3">
              {RANK_BADGES.map((b, i) => {
                const isActive = badge.name === b.name;
                const isPassed = (stats?.average_score || 0) >= b.min;
                return (
                  <div key={i} className="flex-1 flex flex-col items-center gap-1">
                    <span className={`text-lg ${isActive ? "scale-125" : isPassed ? "" : "opacity-30"} transition-transform`}>
                      {b.icon}
                    </span>
                    <div className={`w-full h-2 rounded-full ${isPassed ? "bg-[#C66810]" : "bg-slate-200"}`} />
                    <span className={`text-[9px] font-bold text-center ${isActive ? "text-[#C66810]" : "text-slate-400"}`}>
                      {b.name.split(" ")[0]}
                    </span>
                  </div>
                );
              })}
            </div>
            {badge.max < 100 && (
              <p className="text-xs text-slate-500 text-center mt-2">
                {Math.ceil((badge.max + 1) - (stats?.average_score || 0))} more points to reach{" "}
                <span className="font-bold text-slate-700">{RANK_BADGES[RANK_BADGES.indexOf(badge) + 1]?.name}</span>
              </p>
            )}
          </div>
        </AnimatedSection>
      </section>

      {/* Recent Submissions */}
      <section className="max-w-6xl mx-auto px-6 mt-8 mb-16">
        <AnimatedSection delay={0.25}>
          <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
            <div className="flex items-center justify-between mb-5">
              <h3 className="font-bold text-slate-900 flex items-center gap-2">
                <span>📤</span> Recent Submissions
              </h3>
              <Link href="/profile" className="text-sm font-bold text-[#C66810] hover:underline">
                View All &rarr;
              </Link>
            </div>
            {submissions.length === 0 ? (
              <div className="text-center py-10">
                <div className="text-4xl mb-3">🐵</div>
                <p className="text-slate-500 text-sm mb-4">No submissions yet. Start practicing!</p>
                <Link
                  href="/curriculum/practice"
                  className="inline-block px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors"
                >
                  Go to Practice Arena
                </Link>
              </div>
            ) : (
              <div className="space-y-3">
                {submissions.slice(0, 5).map((sub: any) => (
                  <div
                    key={sub.id}
                    className="flex items-center gap-4 p-4 rounded-xl border border-slate-100 hover:border-orange-200 transition-colors"
                  >
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2 mb-1">
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
                      <p className="text-sm text-slate-700 truncate">
                        {sub.text_content?.substring(0, 100) || `${sub.submission_type} submission`}
                      </p>
                      <p className="text-[10px] text-slate-400 mt-0.5">
                        {new Date(sub.created_at).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" })}
                      </p>
                    </div>
                    {sub.feedback && (
                      <div className="text-center flex-shrink-0">
                        <div className="text-2xl font-black text-[#C66810]">{sub.feedback.overall_score}</div>
                        <div className="text-[9px] text-slate-400 font-medium">/100</div>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        </AnimatedSection>
      </section>
    </div>
  );
}
