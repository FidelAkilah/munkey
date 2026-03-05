/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, Suspense, useRef } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { useSession } from "next-auth/react";
import { motion, useInView, AnimatePresence } from "framer-motion";

const API_BASE = "https://mun-global.onrender.com";

const difficultyLabel: Record<string, { label: string; color: string }> = {
  BEG: { label: "Beginner", color: "bg-green-100 text-green-700" },
  INT: { label: "Intermediate", color: "bg-orange-100 text-[#C66810]" },
  ADV: { label: "Advanced", color: "bg-red-100 text-red-700" },
};

const typeLabel: Record<string, { label: string; icon: string }> = {
  SPEECH: { label: "Speech Prompt", icon: "🎤" },
  DRAFT: { label: "Draft Resolution", icon: "📜" },
  NEGOTIATION: { label: "Negotiation", icon: "🤝" },
  QUIZ: { label: "Quiz", icon: "❓" },
  OPEN: { label: "Open-Ended", icon: "💬" },
};

function AnimatedCard({ children, className = "", delay = 0 }: { children: React.ReactNode; className?: string; delay?: number }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-40px" });
  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 20 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1], delay }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

function PracticeContent() {
  const searchParams = useSearchParams();
  const categorySlug = searchParams.get("category");
  const [questions, setQuestions] = useState<any[]>([]);
  const [categories, setCategories] = useState<any[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>(categorySlug || "");
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [generating, setGenerating] = useState(false);
  const [aiQuestions, setAiQuestions] = useState<any[]>([]);
  const { data: session } = useSession();

  useEffect(() => {
    fetch(`${API_BASE}/api/curriculum/categories/`).then((r) => r.json()).then(setCategories).catch(() => {});
  }, []);

  useEffect(() => {
    async function fetchQuestions() {
      setLoading(true);
      try {
        const params = new URLSearchParams();
        if (selectedCategory) params.append("category", selectedCategory);
        if (selectedDifficulty) params.append("difficulty", selectedDifficulty);
        const res = await fetch(`${API_BASE}/api/curriculum/questions/?${params}`);
        if (res.ok) setQuestions(await res.json());
      } catch (err) { console.error("Failed to fetch questions", err); }
      finally { setLoading(false); }
    }
    fetchQuestions();
  }, [selectedCategory, selectedDifficulty]);

  const handleGenerate = async () => {
    if (!session) { alert("Please log in to generate AI practice questions."); return; }
    setGenerating(true);
    try {
      const token = (session as any)?.user?.accessToken;
      const cat = categories.find((c: any) => c.slug === selectedCategory)
        || categories.find((c: any) => String(c.id) === selectedCategory);
      const categoryType = cat?.category_type || "GENERAL";
      const res = await fetch(`${API_BASE}/api/curriculum/generate-questions/`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...(token ? { Authorization: `Bearer ${token}` } : {}) },
        body: JSON.stringify({ category_type: categoryType, difficulty: selectedDifficulty || "INT", count: 3 }),
      });
      if (res.ok) {
        const data = await res.json();
        setAiQuestions(data.questions || []);
      } else {
        const errData = await res.json().catch(() => ({}));
        alert(errData.detail || "Failed to generate questions. Please try logging out and back in.");
      }
    } catch (err) { console.error("Generate failed:", err); alert("Network error generating questions. Please try again."); }
    finally { setGenerating(false); }
  };

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero Header */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="max-w-5xl mx-auto px-6 pt-28 pb-12 relative z-10">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
            <Link href="/curriculum" className="text-slate-400 hover:text-[#C66810] text-sm font-medium mb-4 inline-flex items-center gap-1 transition-colors">&larr; Back to Curriculum</Link>
            <div className="flex items-center gap-4 mb-3">
              <div className="w-14 h-14 rounded-xl bg-[#C66810]/20 text-[#C66810] flex items-center justify-center text-3xl">🎯</div>
              <div>
                <h1 className="text-3xl md:text-4xl font-black text-white">Practice <span className="font-playfair italic text-[#C66810]">Arena</span></h1>
                <p className="text-slate-400 text-sm">Challenge yourself with exercises reviewed by DiplomAI</p>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      <main className="max-w-5xl mx-auto px-6 py-10">
        {/* Filters */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="flex flex-wrap gap-3 mb-8 items-center"
        >
          <select value={selectedCategory} onChange={(e) => setSelectedCategory(e.target.value)}
            className="px-4 py-2.5 rounded-xl border border-slate-200 text-sm font-medium text-slate-700 bg-white focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] shadow-sm">
            <option value="">All Categories</option>
            {categories.map((cat: any) => (<option key={cat.id} value={cat.slug}>{cat.name}</option>))}
          </select>
          <select value={selectedDifficulty} onChange={(e) => setSelectedDifficulty(e.target.value)}
            className="px-4 py-2.5 rounded-xl border border-slate-200 text-sm font-medium text-slate-700 bg-white focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] shadow-sm">
            <option value="">All Levels</option>
            <option value="BEG">Beginner</option>
            <option value="INT">Intermediate</option>
            <option value="ADV">Advanced</option>
          </select>
          <button onClick={handleGenerate} disabled={generating}
            className="ml-auto px-6 py-2.5 bg-[#C66810] text-white font-bold rounded-xl shadow-sm shadow-orange-200 hover:bg-[#A05200] disabled:opacity-60 transition-all text-sm hover:-translate-y-0.5">
            {generating ? "🦊 Thinking..." : "✨ Generate AI Questions"}
          </button>
        </motion.div>

        {/* AI Generated Questions */}
        <AnimatePresence>
          {aiQuestions.length > 0 && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              exit={{ opacity: 0, height: 0 }}
              className="mb-10 overflow-hidden"
            >
              <div className="flex items-center gap-2 mb-4">
                <span className="text-2xl">🐵</span>
                <div>
                  <h2 className="text-lg font-bold text-slate-900">Bongo&apos;s Custom Challenges</h2>
                  <p className="text-xs text-slate-500">Freshly generated by DiplomAI</p>
                </div>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {aiQuestions.map((q: any, i: number) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, y: 16 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.1 }}
                    whileHover={{ y: -4 }}
                    className="bg-orange-50 rounded-xl p-5 border border-orange-200 hover:shadow-md transition-all"
                  >
                    <div className="flex items-center gap-2 mb-2">
                      <span>{typeLabel[q.question_type]?.icon || "💬"}</span>
                      <span className="text-[9px] font-bold uppercase tracking-widest text-[#C66810] bg-orange-100 px-2 py-0.5 rounded">
                        {typeLabel[q.question_type]?.label || q.question_type}
                      </span>
                    </div>
                    <h3 className="font-bold text-slate-900 text-sm mb-1.5">{q.title}</h3>
                    <p className="text-xs text-slate-600 mb-3 line-clamp-4">{q.prompt}</p>
                    {q.hints && (<p className="text-[10px] text-[#C66810] bg-orange-100/50 p-1.5 rounded mb-3">💡 {q.hints}</p>)}
                    <div className="flex gap-3 items-center">
                      <Link href={`/curriculum/submit?prompt=${encodeURIComponent(q.prompt)}&type=${q.question_type}`}
                        className="text-xs font-bold text-[#C66810] hover:text-[#A05200] transition-colors">
                        Quick Submit &rarr;
                      </Link>
                      <span className="text-slate-300">|</span>
                      <button
                        onClick={() => {
                          // Store AI question in sessionStorage for detail page
                          sessionStorage.setItem('ai_question', JSON.stringify(q));
                          window.location.href = `/curriculum/submit?prompt=${encodeURIComponent(q.prompt)}&type=${q.question_type}`;
                        }}
                        className="text-xs font-bold text-slate-500 hover:text-[#C66810] transition-colors"
                      >
                        View Details + Chat 🐵
                      </button>
                    </div>
                  </motion.div>
                ))}
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        <h2 className="text-xl font-black text-slate-900 mb-5 font-playfair">Exercise Library</h2>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {[...Array(4)].map((_, i) => (<div key={i} className="h-36 bg-white rounded-xl border border-slate-200 animate-pulse" />))}
          </div>
        ) : questions.length === 0 ? (
          <div className="text-center py-16 bg-white rounded-2xl border border-slate-200">
            <div className="text-4xl mb-3">🐵</div>
            <h3 className="text-lg font-bold text-slate-700">No exercises yet</h3>
            <p className="text-slate-500 text-sm mt-1">Try generating some with DiplomAI above!</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {questions.map((q: any, idx: number) => {
              const type = typeLabel[q.question_type] || typeLabel.OPEN;
              const diff = difficultyLabel[q.difficulty] || difficultyLabel.BEG;
              return (
                <AnimatedCard key={q.id} delay={idx * 0.05}>
                  <motion.div
                    whileHover={{ y: -4 }}
                    transition={{ type: "spring", stiffness: 300, damping: 20 }}
                    className="bg-white rounded-xl p-5 border border-slate-200 hover:shadow-md hover:border-orange-200 transition-all h-full"
                  >
                    <div className="flex items-center gap-2 mb-2">
                      <span className="text-lg">{type.icon}</span>
                      <span className="text-[9px] font-bold uppercase tracking-widest text-slate-500 bg-slate-100 px-2 py-0.5 rounded">{type.label}</span>
                      <span className={`text-[9px] font-bold uppercase tracking-widest px-2 py-0.5 rounded ${diff.color}`}>{diff.label}</span>
                    </div>
                    <h3 className="font-bold text-base text-slate-900 mb-1.5">{q.title}</h3>
                    <p className="text-xs text-slate-500 line-clamp-3 mb-3">{q.prompt}</p>
                    {q.hints && (<p className="text-[10px] text-[#C66810] bg-orange-50 p-1.5 rounded mb-3">💡 {q.hints}</p>)}
                    <div className="flex gap-3 items-center">
                      <Link href={`/curriculum/question/${q.id}`}
                        className="text-xs font-bold text-[#C66810] hover:text-[#A05200] transition-colors">
                        View Details + Chat 🐵
                      </Link>
                      <span className="text-slate-300">|</span>
                      <Link href={`/curriculum/submit?question=${q.id}&category=${q.category_name}`}
                        className="text-xs font-bold text-slate-500 hover:text-[#C66810] transition-colors">
                        Quick Submit &rarr;
                      </Link>
                    </div>
                  </motion.div>
                </AnimatedCard>
              );
            })}
          </div>
        )}
      </main>
    </div>
  );
}

export default function PracticePage() {
  return (
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center bg-slate-50"><div className="text-4xl animate-bounce">🐵</div></div>}>
      <PracticeContent />
    </Suspense>
  );
}
