/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { useSession } from "next-auth/react";

const API_BASE = "https://mun-global.onrender.com";

const difficultyLabel: Record<string, { label: string; color: string }> = {
  BEG: { label: "Beginner", color: "bg-green-100 text-green-700" },
  INT: { label: "Intermediate", color: "bg-amber-100 text-amber-700" },
  ADV: { label: "Advanced", color: "bg-red-100 text-red-700" },
};

const typeLabel: Record<string, { label: string; icon: string }> = {
  SPEECH: { label: "Speech Prompt", icon: "🎤" },
  DRAFT: { label: "Draft Resolution", icon: "📜" },
  NEGOTIATION: { label: "Negotiation Scenario", icon: "🤝" },
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

  // Fetch categories
  useEffect(() => {
    fetch(`${API_BASE}/api/curriculum/categories/`)
      .then((r) => r.json())
      .then(setCategories)
      .catch(() => {});
  }, []);

  // Fetch questions
  useEffect(() => {
    async function fetchQuestions() {
      setLoading(true);
      try {
        const params = new URLSearchParams();
        if (selectedCategory) params.append("category", selectedCategory);
        if (selectedDifficulty) params.append("difficulty", selectedDifficulty);
        
        const res = await fetch(`${API_BASE}/api/curriculum/questions/?${params}`);
        if (res.ok) setQuestions(await res.json());
      } catch (err) {
        console.error("Failed to fetch questions", err);
      } finally {
        setLoading(false);
      }
    }
    fetchQuestions();
  }, [selectedCategory, selectedDifficulty]);

  // Generate AI questions
  const handleGenerate = async () => {
    if (!session) {
      alert("Please log in to generate AI practice questions.");
      return;
    }
    setGenerating(true);
    try {
      const token = (session as any)?.user?.accessToken;
      const cat = categories.find((c: any) => c.slug === selectedCategory);
      const categoryType = cat?.category_type || "GENERAL";

      const res = await fetch(`${API_BASE}/api/curriculum/generate-questions/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
        },
        body: JSON.stringify({
          category_type: categoryType,
          difficulty: selectedDifficulty || "INT",
          count: 3,
        }),
      });
      if (res.ok) {
        const data = await res.json();
        setAiQuestions(data.questions || []);
      }
    } catch (err) {
      console.error("Generate failed:", err);
    } finally {
      setGenerating(false);
    }
  };

  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <section className="bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 pt-32 pb-16">
        <div className="max-w-6xl mx-auto px-6">
          <Link href="/curriculum" className="text-slate-400 hover:text-white text-sm font-medium mb-4 inline-block">
            ← Back to Curriculum
          </Link>
          <div className="flex items-center gap-4 mb-4">
            <span className="text-5xl">🎯</span>
            <div>
              <h1 className="text-4xl font-black text-white">Practice Arena</h1>
              <p className="text-slate-400">Challenge yourself with exercises reviewed by DiplomAI</p>
            </div>
          </div>
        </div>
      </section>

      <main className="max-w-6xl mx-auto px-6 py-12">
        {/* Filters */}
        <div className="flex flex-wrap gap-4 mb-10 items-center">
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
            className="px-4 py-2 rounded-xl border border-slate-200 text-sm font-medium text-slate-700 bg-white focus:ring-2 focus:ring-amber-500 focus:border-amber-500"
          >
            <option value="">All Categories</option>
            {categories.map((cat: any) => (
              <option key={cat.id} value={cat.slug}>{cat.name}</option>
            ))}
          </select>
          <select
            value={selectedDifficulty}
            onChange={(e) => setSelectedDifficulty(e.target.value)}
            className="px-4 py-2 rounded-xl border border-slate-200 text-sm font-medium text-slate-700 bg-white focus:ring-2 focus:ring-amber-500 focus:border-amber-500"
          >
            <option value="">All Levels</option>
            <option value="BEG">Beginner</option>
            <option value="INT">Intermediate</option>
            <option value="ADV">Advanced</option>
          </select>

          <button
            onClick={handleGenerate}
            disabled={generating}
            className="ml-auto px-6 py-2 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-bold rounded-xl shadow-md hover:shadow-lg disabled:opacity-60 transition-all duration-300 text-sm"
          >
            {generating ? "🦉 Bongo is thinking..." : "✨ Generate AI Questions"}
          </button>
        </div>

        {/* AI-Generated Questions */}
        {aiQuestions.length > 0 && (
          <div className="mb-12">
            <div className="flex items-center gap-3 mb-6">
              <span className="text-3xl">🦉</span>
              <div>
                <h2 className="text-xl font-bold text-slate-900">Bongo&apos;s Custom Challenges</h2>
                <p className="text-sm text-slate-500">Freshly generated by DiplomAI just for you</p>
              </div>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {aiQuestions.map((q: any, i: number) => (
                <div key={i} className="bg-gradient-to-br from-amber-50 to-orange-50 rounded-2xl p-6 border border-amber-200 shadow-sm">
                  <div className="flex items-center gap-2 mb-3">
                    <span>{typeLabel[q.question_type]?.icon || "💬"}</span>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-amber-600 bg-amber-100 px-2 py-0.5 rounded-full">
                      {typeLabel[q.question_type]?.label || q.question_type}
                    </span>
                  </div>
                  <h3 className="font-bold text-slate-900 mb-2">{q.title}</h3>
                  <p className="text-sm text-slate-600 mb-4 line-clamp-4">{q.prompt}</p>
                  {q.hints && (
                    <p className="text-xs text-amber-600 bg-amber-100/50 p-2 rounded-lg">💡 {q.hints}</p>
                  )}
                  <Link
                    href={`/curriculum/submit?prompt=${encodeURIComponent(q.prompt)}&type=${q.question_type}`}
                    className="mt-4 inline-block text-sm font-bold text-amber-700 hover:text-amber-900 transition-colors"
                  >
                    Attempt this →
                  </Link>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Stored Questions */}
        <h2 className="text-2xl font-black text-slate-900 mb-6">Exercise Library</h2>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {[...Array(4)].map((_, i) => (
              <div key={i} className="h-40 bg-slate-100 rounded-2xl animate-pulse" />
            ))}
          </div>
        ) : questions.length === 0 ? (
          <div className="text-center py-20 bg-slate-50 rounded-2xl">
            <div className="text-5xl mb-4">🦉</div>
            <h3 className="text-xl font-bold text-slate-700">No exercises yet</h3>
            <p className="text-slate-500 mt-2">Try generating some with DiplomAI above, or check back soon!</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {questions.map((q: any) => {
              const type = typeLabel[q.question_type] || typeLabel.OPEN;
              const diff = difficultyLabel[q.difficulty] || difficultyLabel.BEG;
              return (
                <div key={q.id} className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all duration-300">
                  <div className="flex items-center gap-2 mb-3">
                    <span className="text-xl">{type.icon}</span>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500 bg-slate-100 px-2 py-0.5 rounded-full">
                      {type.label}
                    </span>
                    <span className={`text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded-full ${diff.color}`}>
                      {diff.label}
                    </span>
                  </div>
                  <h3 className="font-bold text-lg text-slate-900 mb-2">{q.title}</h3>
                  <p className="text-sm text-slate-500 line-clamp-3 mb-4">{q.prompt}</p>
                  {q.hints && (
                    <p className="text-xs text-blue-600 bg-blue-50 p-2 rounded-lg mb-4">💡 {q.hints}</p>
                  )}
                  <Link
                    href={`/curriculum/submit?question=${q.id}&category=${q.category_name}`}
                    className="text-sm font-bold text-amber-600 hover:text-amber-800 transition-colors"
                  >
                    Attempt this exercise →
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
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center"><div className="text-4xl">🦉</div></div>}>
      <PracticeContent />
    </Suspense>
  );
}
