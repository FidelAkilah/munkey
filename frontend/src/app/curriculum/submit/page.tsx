/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useState, useEffect, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { useSession } from "next-auth/react";
import { motion, AnimatePresence } from "framer-motion";

const API_BASE = "https://mun-global.onrender.com";

function SubmitContent() {
  const searchParams = useSearchParams();
  const questionId = searchParams.get("question");
  const promptParam = searchParams.get("prompt");
  const typeParam = searchParams.get("type");

  const { data: session } = useSession();
  const isAuthenticated = !!session?.user;

  const [categories, setCategories] = useState<any[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>("");
  const [submissionType, setSubmissionType] = useState<string>(
    typeParam === "SPEECH" ? "TEXT" : typeParam === "DRAFT" ? "TEXT" : "TEXT"
  );
  const [textContent, setTextContent] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [fileUpload, setFileUpload] = useState<File | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [feedback, setFeedback] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(`${API_BASE}/api/curriculum/categories/`)
      .then((r) => r.json())
      .then(setCategories)
      .catch(() => {});
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setFeedback(null);

    if (!isAuthenticated) {
      setError("Please log in to submit your work for review.");
      return;
    }

    if (!selectedCategory) {
      setError("Please select a category.");
      return;
    }

    setSubmitting(true);

    try {
      const token = (session as any)?.user?.accessToken;

      let body: any;
      const headers: Record<string, string> = {};
      if (token) headers["Authorization"] = `Bearer ${token}`;

      if (submissionType === "FILE" && fileUpload) {
        const formData = new FormData();
        formData.append("category", selectedCategory);
        formData.append("submission_type", "FILE");
        formData.append("file_upload", fileUpload);
        if (questionId) formData.append("question", questionId);
        body = formData;
      } else {
        headers["Content-Type"] = "application/json";
        body = JSON.stringify({
          category: parseInt(selectedCategory),
          submission_type: submissionType,
          text_content: textContent,
          video_url: videoUrl,
          ...(questionId ? { question: parseInt(questionId) } : {}),
        });
      }

      const res = await fetch(`${API_BASE}/api/curriculum/submissions/create/`, {
        method: "POST",
        headers,
        body,
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || JSON.stringify(errData) || "Submission failed");
      }

      const data = await res.json();

      if (data.feedback) {
        setFeedback(data.feedback);
      } else {
        let attempts = 0;
        const pollInterval = setInterval(async () => {
          attempts++;
          try {
            const detailRes = await fetch(`${API_BASE}/api/curriculum/submissions/${data.id}/`, {
              headers: token ? { Authorization: `Bearer ${token}` } : {},
            });
            if (detailRes.ok) {
              const detailData = await detailRes.json();
              if (detailData.feedback) {
                setFeedback(detailData.feedback);
                clearInterval(pollInterval);
              }
            }
          } catch { /* continue polling */ }
          if (attempts >= 15) clearInterval(pollInterval);
        }, 2000);
      }
    } catch (err: any) {
      setError(err.message || "Something went wrong.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero Header */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="max-w-4xl mx-auto px-6 pt-28 pb-12 relative z-10">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
            <Link href="/curriculum" className="text-slate-400 hover:text-[#C66810] text-sm font-medium mb-4 inline-flex items-center gap-1 transition-colors">
              &larr; Back to Curriculum
            </Link>
            <div className="flex items-center gap-4">
              <div className="w-14 h-14 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-3xl">📤</div>
              <div>
                <h1 className="text-3xl md:text-4xl font-black text-white">Submit for <span className="font-playfair italic text-[#C66810]">Review</span></h1>
                <p className="text-slate-400 text-sm">
                  Upload your work and let <span className="text-[#C66810] font-semibold">Bongo</span> powered by{" "}
                  <span className="text-[#C66810] font-semibold">DiplomAI</span> give you expert feedback
                </p>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      <main className="max-w-4xl mx-auto px-6 py-10">
        {/* Prompt Display */}
        <AnimatePresence>
          {promptParam && (
            <motion.div
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              className="bg-orange-50 border border-orange-200 rounded-xl p-5 mb-8"
            >
              <div className="flex items-center gap-2 mb-2">
                <span className="text-xl">🐵</span>
                <span className="font-bold text-[#C66810]">Exercise Prompt</span>
              </div>
              <p className="text-sm text-slate-700">{promptParam}</p>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Feedback Display */}
        <AnimatePresence>
          {feedback && (
            <motion.div
              initial={{ opacity: 0, scale: 0.96 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
              className="bg-white border border-slate-200 rounded-2xl p-8 mb-10 shadow-lg"
            >
              <div className="flex items-center gap-3 mb-6">
                <span className="text-4xl">🐵</span>
                <div>
                  <h2 className="text-2xl font-black text-slate-900 font-playfair">Bongo&apos;s Feedback</h2>
                  <p className="text-xs text-slate-500">Powered by DiplomAI</p>
                </div>
                <div className="ml-auto text-center">
                  <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ delay: 0.3, type: "spring", stiffness: 200 }}
                    className="text-4xl font-black text-[#C66810]"
                  >
                    {feedback.overall_score}
                  </motion.div>
                  <div className="text-xs text-slate-500 font-medium">/ 100</div>
                </div>
              </div>

              <div className="w-full bg-slate-100 rounded-full h-3 mb-8 overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: `${feedback.overall_score}%` }}
                  transition={{ duration: 1.2, delay: 0.4, ease: [0.22, 1, 0.36, 1] }}
                  className="h-3 rounded-full bg-[#C66810]"
                />
              </div>

              {/* Rubric Breakdown */}
              {feedback.rubric_scores && (
                <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.45 }} className="bg-slate-50 rounded-xl p-5 border border-slate-200 mb-6">
                  <h3 className="font-bold text-slate-800 mb-4 flex items-center gap-2">
                    <span className="w-6 h-6 rounded bg-[#C66810]/10 text-[#C66810] flex items-center justify-center text-xs">📊</span>
                    Rubric Breakdown
                  </h3>
                  <div className="space-y-3">
                    {Object.entries(feedback.rubric_scores).map(([key, val]: [string, any], i: number) => {
                      const pct = val.max > 0 ? (val.score / val.max) * 100 : 0;
                      const barColor = pct >= 75 ? "bg-green-500" : pct >= 50 ? "bg-[#C66810]" : "bg-red-400";
                      const label = key.replace(/_/g, " ").replace(/\b\w/g, (c: string) => c.toUpperCase());
                      return (
                        <motion.div key={key} initial={{ opacity: 0, x: -12 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.5 + i * 0.08 }}>
                          <div className="flex items-center justify-between mb-1">
                            <span className="text-sm font-semibold text-slate-700">{label}</span>
                            <span className="text-sm font-bold text-slate-800">{val.score}/{val.max}</span>
                          </div>
                          <div className="w-full bg-slate-200 rounded-full h-2.5 overflow-hidden mb-1">
                            <motion.div
                              initial={{ width: 0 }}
                              animate={{ width: `${pct}%` }}
                              transition={{ duration: 0.8, delay: 0.6 + i * 0.08 }}
                              className={`h-2.5 rounded-full ${barColor}`}
                            />
                          </div>
                          {val.comment && <p className="text-xs text-slate-500 mt-0.5">{val.comment}</p>}
                        </motion.div>
                      );
                    })}
                  </div>
                </motion.div>
              )}

              <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mb-5">
                <motion.div initial={{ opacity: 0, x: -16 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.5 }} className="bg-green-50 rounded-xl p-5 border border-green-200">
                  <h3 className="font-bold text-green-700 mb-2">Strengths</h3>
                  <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.strengths}</p>
                </motion.div>
                <motion.div initial={{ opacity: 0, x: 16 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.6 }} className="bg-orange-50 rounded-xl p-5 border border-orange-200">
                  <h3 className="font-bold text-[#C66810] mb-2">Areas for Improvement</h3>
                  <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.improvements}</p>
                </motion.div>
              </div>

              {/* Example Revision */}
              {feedback.example_revision && (
                <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.65 }} className="bg-blue-50 rounded-xl p-5 border border-blue-200 mb-5">
                  <h3 className="font-bold text-blue-700 mb-2 flex items-center gap-2">
                    <span>✨</span> Here&apos;s How to Improve
                  </h3>
                  <p className="text-xs text-blue-600 mb-3">Bongo rewrote your weakest section to show you what a stronger version looks like:</p>
                  <div className="bg-white rounded-lg p-4 border border-blue-200 text-sm text-slate-700 whitespace-pre-line font-mono leading-relaxed">
                    {feedback.example_revision}
                  </div>
                </motion.div>
              )}

              <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.7 }} className="bg-slate-50 rounded-xl p-5 border border-slate-200 mb-5">
                <h3 className="font-bold text-slate-800 mb-2">Detailed Analysis</h3>
                <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.detailed_feedback}</p>
              </motion.div>

              <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.8 }} className="bg-orange-50 rounded-xl p-5 border border-orange-200">
                <h3 className="font-bold text-[#C66810] mb-2">Next Steps</h3>
                <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.suggestions}</p>
              </motion.div>

              <div className="mt-6 flex gap-3">
                <Link href="/curriculum/practice"
                  className="px-5 py-2 bg-[#C66810] text-white font-bold rounded-lg hover:bg-[#A05200] transition-colors text-sm">
                  🎯 Try Another Exercise
                </Link>
                <button
                  onClick={() => { setFeedback(null); setTextContent(""); setVideoUrl(""); }}
                  className="px-5 py-2 bg-slate-100 text-slate-700 font-bold rounded-lg hover:bg-slate-200 transition-colors text-sm">
                  📝 Submit Again
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Submission Form */}
        {!feedback && (
          <motion.form
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            onSubmit={handleSubmit}
            className="space-y-7"
          >
            <div>
              <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1.5">Category *</label>
              <select value={selectedCategory} onChange={(e) => setSelectedCategory(e.target.value)} required
                className="w-full px-4 py-3 rounded-xl border border-slate-200 text-slate-700 focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] bg-white shadow-sm">
                <option value="">Select a category...</option>
                {categories.map((cat: any) => (
                  <option key={cat.id} value={cat.id}>{cat.name}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Submission Type</label>
              <div className="flex gap-3">
                {[
                  { value: "TEXT", label: "📝 Text / Draft", desc: "Paste your resolution or speech text" },
                  { value: "VIDEO_URL", label: "🎥 Video URL", desc: "Share a link to your speech recording" },
                  { value: "FILE", label: "📎 File Upload", desc: "Upload a document file" },
                ].map((opt) => (
                  <button key={opt.value} type="button" onClick={() => setSubmissionType(opt.value)}
                    className={`flex-1 p-4 rounded-xl border-2 text-left transition-all ${
                      submissionType === opt.value
                        ? "border-[#C66810] bg-orange-50 shadow-sm"
                        : "border-slate-200 bg-white hover:border-slate-300"
                    }`}>
                    <p className="font-bold text-sm text-slate-800">{opt.label}</p>
                    <p className="text-xs text-slate-500 mt-1">{opt.desc}</p>
                  </button>
                ))}
              </div>
            </div>

            {submissionType === "TEXT" && (
              <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }} transition={{ duration: 0.3 }}>
                <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1.5">Your Work *</label>
                <textarea value={textContent} onChange={(e) => setTextContent(e.target.value)} required rows={14}
                  placeholder={"Paste your draft resolution, speech text, or negotiation response here...\n\nBongo will review your work and provide detailed feedback!"}
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 text-slate-700 focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] resize-y font-mono text-sm shadow-sm" />
              </motion.div>
            )}

            {submissionType === "VIDEO_URL" && (
              <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }} transition={{ duration: 0.3 }}>
                <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1.5">Video URL *</label>
                <input type="url" value={videoUrl} onChange={(e) => setVideoUrl(e.target.value)} required
                  placeholder="https://youtube.com/watch?v=... or Google Drive link"
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 text-slate-700 focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] shadow-sm" />
                <p className="text-xs text-slate-400 mt-2">
                  Upload your speech video to YouTube (unlisted) or Google Drive and paste the link.
                </p>
                <textarea value={textContent} onChange={(e) => setTextContent(e.target.value)} rows={6}
                  placeholder="(Optional) Paste your speech transcript here for more detailed AI feedback..."
                  className="w-full mt-3 px-4 py-3 rounded-xl border border-slate-200 text-slate-700 focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] resize-y font-mono text-sm shadow-sm" />
              </motion.div>
            )}

            {submissionType === "FILE" && (
              <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }} transition={{ duration: 0.3 }}>
                <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1.5">Upload File *</label>
                <div className="border-2 border-dashed border-slate-300 rounded-xl p-8 text-center hover:border-[#C66810] transition-colors">
                  <input type="file" onChange={(e) => setFileUpload(e.target.files?.[0] || null)}
                    accept=".pdf,.doc,.docx,.txt" className="hidden" id="file-input" />
                  <label htmlFor="file-input" className="cursor-pointer">
                    <div className="text-4xl mb-3">📎</div>
                    <p className="font-bold text-slate-700">
                      {fileUpload ? fileUpload.name : "Click to upload or drag and drop"}
                    </p>
                    <p className="text-xs text-slate-400 mt-1">PDF, DOC, DOCX, or TXT (max 10MB)</p>
                  </label>
                </div>
              </motion.div>
            )}

            {error && (
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="bg-red-50 border border-red-200 text-red-700 rounded-xl p-4 text-sm">
                {"\u26a0\ufe0f"} {error}
              </motion.div>
            )}

            <motion.button
              type="submit"
              disabled={submitting || !isAuthenticated}
              whileHover={{ scale: 1.01 }}
              whileTap={{ scale: 0.99 }}
              className="w-full py-4 bg-[#C66810] text-white font-bold text-lg rounded-xl shadow-sm shadow-orange-200 hover:bg-[#A05200] disabled:opacity-60 transition-all"
            >
              {submitting ? (
                <span className="flex items-center justify-center gap-3">
                  <span className="animate-bounce">🐵</span>
                  Bongo is reviewing your work...
                </span>
              ) : (
                "Submit for DiplomAI Review"
              )}
            </motion.button>

            {!isAuthenticated && (
              <p className="text-center text-sm text-slate-500">
                <Link href="/login" className="text-[#C66810] font-bold hover:underline">Log in</Link> to submit your work for AI review.
              </p>
            )}
          </motion.form>
        )}
      </main>
    </div>
  );
}

export default function SubmitPage() {
  return (
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center bg-slate-50"><div className="text-4xl animate-bounce">🐵</div></div>}>
      <SubmitContent />
    </Suspense>
  );
}
