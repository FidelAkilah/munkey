/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { useSession } from "next-auth/react";

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
      const cat = categories.find((c: any) => c.slug === selectedCategory);
      const categoryType = cat?.category_type || "GENERAL";
      const res = await fetch(`${API_BASE}/api/curriculum/generate-questions/`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...(token ? { Authorization: `Bearer ${token}` } : {}) },
        body: JSON.stringify({ category_type: categoryType, difficulty: selectedDifficulty || "INT", count: 3 }),
      });
      if (res.ok) { const data = await res.json(); setAiQuestions(data.questions || []); }
    } catch (err) { console.error("Generate failed:", err); }
    finally { setGenerating(false); }
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <section className="relative overflow-hidden bg-white border-b border-slate-200">
        <div className="absolute inset-0 bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:20px_20px] opacity-30"></div>
        <div className="max-w-5xl mx-auto px-6 pt-28 pb-12 relative z-10">
          <Link href="/curriculum" className="text-slate-500 hover:text-[#C66810] text-sm font-medium mb-4 inline-flex items-center gap-1 transition-colors">&larr; Back to Curriculum</Link>
          <div className="flex items-center gap-3 mb-3">
            <div className="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center text-2xl">🎯</div>
            <div>
              <h1 className="text-3xl font-black text-slate-900">Practice Arena</h1>
              <p className="text-slate-500 text-sm">Challenge yourself with exercises reviewed by DiplomAI</p>
            </div>
          </div>
        </div>
      </section>

      <main className="max-w-5xl mx-auto px-6 py-10">
        <div className="flex flex-wrap gap-3 mb-8 items-center">
          <select value={selectedCategory} onChange={(e) => setSelectedCategory(e.target.value)}
            className="px-3 py-2 rounded-lg border border-slate-200 text-sm font-medium text-slate-700 bg-white focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810]">
            <option value="">All Categories</option>
            {categories.map((cat: any) => (<option key={cat.id} value={cat.slug}>{cat.name}</option>))}
          </select>
          <select value={selectedDifficulty} onChange={(e) => setSelectedDifficulty(e.target.value)}
            className="px-3 py-2 rounded-lg border border-slate-200 text-sm font-medium text-slate-700 bg-white focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810]">
            <option value="">All Levels</option>
            <option value="BEG">Beginner</option>
            <option value="INT">Intermediate</option>
            <option value="ADV">Advanced</option>
          </select>
          <button onClick={handleGenerate} disabled={generating}
            className="ml-auto px-5 py-2 bg-[#C66810] text-white font-bold rounded-lg shadow-sm hover:bg-[#A05200] disabled:opacity-60 transition-all text-sm">
            {generating ? "🦊 Thinking..." : "✨ Generate AI Questions"}
          </button>
        </div>

        {aiQuestions.length > 0 && (
          <div className="mb-10">
            <div className="flex items-center gap-2 mb-4">
              <span className="text-2xl">🐵</span>
              <div>
                <h2 className="text-lg font-bold text-slate-900">Bongo&apos;s Custom Challenges</h2>
                <p className="text-xs text-slate-500">Freshly generated by DiplomAI</p>
              </div>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {aiQuestions.map((q: any, i: number) => (
                <div key={i} className="bg-orange-50 rounded-xl p-5 border border-orange-200">
                  <div className="flex items-center gap-2 mb-2">
                    <span>{typeLabel[q.question_type]?.icon || "💬"}</span>
                    <span className="text-[9px] font-bold uppercase tracking-widest text-[#C66810] bg-orange-100 px-2 py-0.5 rounded">
                      {typeLabel[q.question_type]?.label || q.question_type}
                    </span>
                  </div>
                  <h3 className="font-bold text-slate-900 text-sm mb-1.5">{q.title}</h3>
                  <p className="text-xs text-slate-600 mb-3 line-clamp-4">{q.prompt}</p>
                  {q.hints && (<p className="text-[10px] text-[#C66810] bg-orange-100/50 p-1.5 rounded mb-3">💡 {q.hints}</p>)}
                  <Link href={`/curriculum/submit?prompt=${encodeURIComponent(q.prompt)}&type=${q.question_type}`}
                    className="text-xs font-bold text-[#C66810] hover:text-[#A05200] transition-colors">
                    Attempt this &rarr;
                  </Link>
                </div>
              ))}
            </div>
          </div>
        )}

        <h2 className="text-xl font-black text-slate-900 mb-5">Exercise Library</h2>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {[...Array(4)].map((_, i) => (<div key={i} className="h-36 bg-slate-100 rounded-xl animate-pulse" />))}
          </div>
        ) : questions.length === 0 ? (
          <div className="text-center py-16 bg-slate-50 rounded-xl border border-slate-200">
            <div className="text-4xl mb-3">🐵</div>
            <h3 className="text-lg font-bold text-slate-700">No exercises yet</h3>
            <p className="text-slate-500 text-sm mt-1">Try generating some with DiplomAI above!</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {questions.map((q: any) => {
              const type = typeLabel[q.question_type] || typeLabel.OPEN;
              const diff = difficultyLabel[q.difficulty] || difficultyLabel.BEG;
              return (
                <div key={q.id} className="bg-white rounded-xl p-5 border border-slate-200 hover:shadow-md hover:border-orange-200 transition-all">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-lg">{type.icon}</span>
                    <span className="text-[9px] font-bold uppercase tracking-widest text-slate-500 bg-slate-100 px-2 py-0.5 rounded">{type.label}</span>
                    <span className={`text-[9px] font-bold uppercase tracking-widest px-2 py-0.5 rounded ${diff.color}`}>{diff.label}</span>
                  </div>
                  <h3 className="font-bold text-base text-slate-900 mb-1.5">{q.title}</h3>
                  <p className="text-xs text-slate-500 line-clamp-3 mb-3">{q.prompt}</p>
                  {q.hints && (<p className="text-[10px] text-[#C66810] bg-orange-50 p-1.5 rounded mb-3">💡 {q.hints}</p>)}
                  <Link href={`/curriculum/submit?question=${q.id}&category=${q.category_name}`}
                    className="text-xs font-bold text-[#C66810] hover:text-[#A05200] transition-colors">
                    Attempt this exercise &rarr;
                  </Link>
                </div>
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
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center"><div className="text-4xl">🐵</div></div>}>
      <PracticeContent />
    </Suspense>
  );
}
