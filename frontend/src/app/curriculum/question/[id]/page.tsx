/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef, useCallback } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { useSession } from "next-auth/react";
import { motion, AnimatePresence } from "framer-motion";

const API_BASE = "https://mun-global.onrender.com";

const QUICK_ACTIONS = [
  { label: "🎤 Practice my opening speech", message: "I want to practice my opening speech for this topic. Can you give me a structure to follow and then let me try?" },
  { label: "🤝 Simulate a moderated caucus", message: "Let's simulate a moderated caucus. You play the chair and other delegates. I'll practice speaking and responding to questions." },
  { label: "📜 Help me write operative clauses", message: "Help me draft operative clauses for a resolution on this topic. Guide me through proper UN formatting and actionable language." },
  { label: "❓ Quiz me on Rules of Procedure", message: "Quiz me on MUN Rules of Procedure. Ask me scenario-based questions about motions, points, and voting procedures." },
  { label: "📝 Review my position paper", message: "I want to share my position paper draft for feedback. What sections should I include, and can you review it when I paste it?" },
];

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

interface ChatMsg {
  id?: number;
  role: "user" | "assistant";
  content: string;
  created_at?: string;
}

export default function QuestionDetailPage() {
  const params = useParams();
  const questionId = params.id as string;
  const { data: session } = useSession();
  const token = (session as any)?.user?.accessToken;

  const [question, setQuestion] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<"details" | "chat" | "submit">("details");

  // Chat state
  const [messages, setMessages] = useState<ChatMsg[]>([]);
  const [chatInput, setChatInput] = useState("");
  const [sending, setSending] = useState(false);
  const [sessionId, setSessionId] = useState("");
  const chatEndRef = useRef<HTMLDivElement>(null);

  // Simulation state
  const [chatMode, setChatMode] = useState<"general" | "simulation">("general");
  const [simConfig, setSimConfig] = useState({ role: "opposing_delegate", country: "", topic: "", stance: "" });
  const [showSimSetup, setShowSimSetup] = useState(false);

  // Tip of the day
  const [tip, setTip] = useState<{ content: string; category: string } | null>(null);
  const [tipDismissed, setTipDismissed] = useState(false);

  // Submit state
  const [textContent, setTextContent] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [feedback, setFeedback] = useState<any>(null);
  const [submitError, setSubmitError] = useState("");

  useEffect(() => {
    async function fetchQuestion() {
      try {
        const res = await fetch(`${API_BASE}/api/curriculum/questions/${questionId}/`);
        if (res.ok) setQuestion(await res.json());
      } catch (err) {
        console.error("Failed to fetch question:", err);
      } finally {
        setLoading(false);
      }
    }
    if (questionId) fetchQuestion();
  }, [questionId]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // Fetch tip of the day
  useEffect(() => {
    fetch(`${API_BASE}/api/curriculum/tip-of-the-day/`)
      .then((r) => r.ok ? r.json() : null)
      .then((data) => { if (data?.tip) setTip(data.tip); })
      .catch(() => {});
  }, []);

  // Initialize chat with a welcome message
  useEffect(() => {
    if (question && messages.length === 0) {
      setMessages([
        {
          role: "assistant",
          content: `Hey there! 👋 I'm **Bongo**, your DiplomAI strategist. I see you're working on **"${question.title}"**.\n\nFeel free to ask me anything about this exercise — I can help you brainstorm approaches, explain concepts, or give you hints. What would you like to know?`,
        },
      ]);
    }
  }, [question, messages.length]);

  const sendMessage = useCallback(async (overrideMessage?: string) => {
    const msgText = overrideMessage || chatInput.trim();
    if (!msgText || sending) return;
    if (!token) {
      alert("Please log in to chat with DiplomAI.");
      return;
    }

    const userMsg: ChatMsg = { role: "user", content: msgText };
    setMessages((prev) => [...prev, userMsg]);
    setChatInput("");
    setSending(true);

    try {
      const payload: any = {
        message: userMsg.content,
        session_id: sessionId || undefined,
        question_id: parseInt(questionId),
        mode: chatMode,
      };
      if (chatMode === "simulation" && simConfig.country) {
        payload.simulation_config = simConfig;
      }

      const res = await fetch(`${API_BASE}/api/curriculum/chat/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        const data = await res.json();
        if (!sessionId) setSessionId(data.session_id);
        setMessages((prev) => [...prev, data.response]);
      } else {
        setMessages((prev) => [
          ...prev,
          { role: "assistant", content: "Sorry, I had trouble processing that. Please try again!" },
        ]);
      }
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Connection error. Please try again in a moment." },
      ]);
    } finally {
      setSending(false);
    }
  }, [chatInput, sending, token, sessionId, questionId, chatMode, simConfig]);

  const startNewConversation = () => {
    setMessages([]);
    setSessionId("");
    setChatMode("general");
    setShowSimSetup(false);
  };

  const handleSubmit = async () => {
    if (!textContent.trim()) {
      setSubmitError("Please write your response before submitting.");
      return;
    }
    if (!token) {
      setSubmitError("Please log in to submit.");
      return;
    }

    setSubmitting(true);
    setSubmitError("");
    setFeedback(null);

    try {
      const res = await fetch(`${API_BASE}/api/curriculum/submissions/create/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          category: question.category,
          submission_type: "TEXT",
          text_content: textContent,
          question: parseInt(questionId),
        }),
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || JSON.stringify(errData) || "Submission failed");
      }

      const data = await res.json();
      if (data.feedback) {
        setFeedback(data.feedback);
      } else {
        // Poll for feedback
        let attempts = 0;
        const pollInterval = setInterval(async () => {
          attempts++;
          try {
            const detailRes = await fetch(`${API_BASE}/api/curriculum/submissions/${data.id}/`, {
              headers: { Authorization: `Bearer ${token}` },
            });
            if (detailRes.ok) {
              const detailData = await detailRes.json();
              if (detailData.feedback) {
                setFeedback(detailData.feedback);
                clearInterval(pollInterval);
              }
            }
          } catch { /* continue */ }
          if (attempts >= 15) clearInterval(pollInterval);
        }, 2000);
      }
    } catch (err: any) {
      setSubmitError(err.message || "Something went wrong.");
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="text-4xl animate-bounce">🐵</div>
      </div>
    );
  }

  if (!question) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-4xl mb-3">🔍</div>
          <h2 className="text-xl font-bold text-slate-700">Question not found</h2>
          <Link href="/curriculum/practice" className="text-[#C66810] font-bold mt-4 inline-block">
            &larr; Back to Practice
          </Link>
        </div>
      </div>
    );
  }

  const type = typeLabel[question.question_type] || typeLabel.OPEN;
  const diff = difficultyLabel[question.difficulty] || difficultyLabel.BEG;

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="max-w-6xl mx-auto px-6 pt-28 pb-10 relative z-10">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
            <Link
              href="/curriculum/practice"
              className="text-slate-400 hover:text-[#C66810] text-sm font-medium mb-4 inline-flex items-center gap-1 transition-colors"
            >
              &larr; Back to Practice Arena
            </Link>
            <div className="flex items-center gap-4 mb-2">
              <div className="w-14 h-14 rounded-xl bg-[#C66810]/20 text-[#C66810] flex items-center justify-center text-3xl">
                {type.icon}
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-[9px] font-bold uppercase tracking-widest text-white/60 bg-white/10 px-2 py-0.5 rounded">
                    {type.label}
                  </span>
                  <span className={`text-[9px] font-bold uppercase tracking-widest px-2 py-0.5 rounded ${diff.color}`}>
                    {diff.label}
                  </span>
                </div>
                <h1 className="text-2xl md:text-3xl font-black text-white">{question.title}</h1>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Tab Navigation */}
      <div className="max-w-6xl mx-auto px-6 mt-6">
        <div className="flex gap-1 bg-white rounded-xl p-1.5 border border-slate-200 shadow-sm inline-flex">
          {[
            { key: "details" as const, label: "📋 Exercise Details", icon: "" },
            { key: "chat" as const, label: "🐵 Ask Bongo", icon: "" },
            { key: "submit" as const, label: "📤 Submit Answer", icon: "" },
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
      </div>

      <main className="max-w-6xl mx-auto px-6 py-8">
        <AnimatePresence mode="wait">
          {/* ── Details Tab ── */}
          {activeTab === "details" && (
            <motion.div
              key="details"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -12 }}
              transition={{ duration: 0.3 }}
              className="space-y-6"
            >
              {/* Main Prompt */}
              <div className="bg-white rounded-2xl p-8 border border-slate-200 shadow-sm">
                <h2 className="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
                  <span className="w-8 h-8 rounded-lg bg-orange-100 text-[#C66810] flex items-center justify-center text-sm">📝</span>
                  Exercise Prompt
                </h2>
                <div className="text-slate-700 leading-relaxed whitespace-pre-line text-[15px]">{question.prompt}</div>
              </div>

              {/* Hints */}
              {question.hints && (
                <div className="bg-orange-50 rounded-2xl p-6 border border-orange-200">
                  <h3 className="font-bold text-[#C66810] mb-3 flex items-center gap-2">
                    <span>💡</span> Hints & Tips
                  </h3>
                  <p className="text-sm text-slate-700 whitespace-pre-line">{question.hints}</p>
                </div>
              )}

              {/* Key Concepts (if available from AI-generated) */}
              {question.key_concepts && (
                <div className="bg-blue-50 rounded-2xl p-6 border border-blue-200">
                  <h3 className="font-bold text-blue-700 mb-3 flex items-center gap-2">
                    <span>🎯</span> Key Concepts Tested
                  </h3>
                  <div className="flex flex-wrap gap-2">
                    {question.key_concepts.split(",").map((concept: string, i: number) => (
                      <span key={i} className="px-3 py-1 bg-blue-100 text-blue-700 text-xs font-bold rounded-full">
                        {concept.trim()}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* Action Buttons */}
              <div className="flex gap-3">
                <button
                  onClick={() => setActiveTab("chat")}
                  className="px-6 py-3 bg-white text-slate-700 font-bold rounded-xl border border-slate-200 hover:border-[#C66810] hover:text-[#C66810] transition-all text-sm"
                >
                  🐵 Ask Bongo for Help
                </button>
                <button
                  onClick={() => setActiveTab("submit")}
                  className="px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl shadow-sm hover:bg-[#A05200] transition-all text-sm"
                >
                  📤 Submit My Answer
                </button>
                <Link
                  href={`/curriculum/submit?prompt=${encodeURIComponent(question.prompt)}&type=${question.question_type}`}
                  className="px-6 py-3 bg-slate-100 text-slate-600 font-bold rounded-xl hover:bg-slate-200 transition-all text-sm flex items-center"
                >
                  Open Full Submit Page &rarr;
                </Link>
              </div>
            </motion.div>
          )}

          {/* ── Chat Tab ── */}
          {activeTab === "chat" && (
            <motion.div
              key="chat"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -12 }}
              transition={{ duration: 0.3 }}
              className="flex flex-col h-[calc(100vh-320px)] min-h-[500px]"
            >
              {/* Tip of the Day Banner */}
              {tip && !tipDismissed && (
                <motion.div
                  initial={{ opacity: 0, y: -8 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="bg-amber-50 border border-amber-200 rounded-xl p-4 mb-4 flex items-start gap-3"
                >
                  <span className="text-xl flex-shrink-0">💡</span>
                  <div className="flex-1">
                    <p className="text-[10px] font-bold uppercase tracking-widest text-amber-600 mb-1">Bongo&apos;s Tip of the Day</p>
                    <p className="text-sm text-slate-700">{tip.content}</p>
                  </div>
                  <button onClick={() => setTipDismissed(true)} className="text-amber-400 hover:text-amber-600 text-lg flex-shrink-0">&times;</button>
                </motion.div>
              )}

              {/* Mode Toggle + New Conversation */}
              <div className="flex items-center gap-2 mb-3">
                <div className="flex bg-white rounded-lg border border-slate-200 p-0.5">
                  <button
                    onClick={() => { setChatMode("general"); setShowSimSetup(false); }}
                    className={`px-3 py-1.5 rounded-md text-xs font-bold transition-all ${chatMode === "general" ? "bg-[#C66810] text-white" : "text-slate-500 hover:text-slate-700"}`}
                  >
                    🐵 Coach Mode
                  </button>
                  <button
                    onClick={() => { setChatMode("simulation"); setShowSimSetup(true); }}
                    className={`px-3 py-1.5 rounded-md text-xs font-bold transition-all ${chatMode === "simulation" ? "bg-blue-600 text-white" : "text-slate-500 hover:text-slate-700"}`}
                  >
                    🎭 Simulation
                  </button>
                </div>
                <button
                  onClick={startNewConversation}
                  className="ml-auto px-3 py-1.5 bg-white text-xs font-medium text-slate-500 border border-slate-200 rounded-lg hover:border-red-300 hover:text-red-500 transition-colors"
                >
                  + New Conversation
                </button>
              </div>

              {/* Simulation Setup Panel */}
              <AnimatePresence>
                {showSimSetup && chatMode === "simulation" && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: "auto" }}
                    exit={{ opacity: 0, height: 0 }}
                    className="bg-blue-50 border border-blue-200 rounded-xl p-4 mb-3 overflow-hidden"
                  >
                    <p className="text-xs font-bold text-blue-700 mb-3">Configure the delegate Bongo will roleplay as:</p>
                    <div className="grid grid-cols-2 gap-3">
                      <div>
                        <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1">Country</label>
                        <input value={simConfig.country} onChange={(e) => setSimConfig((s) => ({ ...s, country: e.target.value }))}
                          placeholder="e.g. United States" className="w-full px-3 py-2 rounded-lg border border-blue-200 text-sm text-slate-700 focus:ring-2 focus:ring-blue-300 focus:border-blue-400 bg-white" />
                      </div>
                      <div>
                        <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1">Role</label>
                        <select value={simConfig.role} onChange={(e) => setSimConfig((s) => ({ ...s, role: e.target.value }))}
                          className="w-full px-3 py-2 rounded-lg border border-blue-200 text-sm text-slate-700 bg-white">
                          <option value="opposing_delegate">Opposing Delegate</option>
                          <option value="ally_delegate">Allied Delegate</option>
                          <option value="committee_chair">Committee Chair</option>
                        </select>
                      </div>
                      <div>
                        <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1">Topic</label>
                        <input value={simConfig.topic} onChange={(e) => setSimConfig((s) => ({ ...s, topic: e.target.value }))}
                          placeholder="e.g. Climate Change Financing" className="w-full px-3 py-2 rounded-lg border border-blue-200 text-sm text-slate-700 focus:ring-2 focus:ring-blue-300 focus:border-blue-400 bg-white" />
                      </div>
                      <div>
                        <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1">Stance</label>
                        <input value={simConfig.stance} onChange={(e) => setSimConfig((s) => ({ ...s, stance: e.target.value }))}
                          placeholder="e.g. against binding commitments" className="w-full px-3 py-2 rounded-lg border border-blue-200 text-sm text-slate-700 focus:ring-2 focus:ring-blue-300 focus:border-blue-400 bg-white" />
                      </div>
                    </div>
                    <button onClick={() => setShowSimSetup(false)} className="mt-3 px-4 py-1.5 bg-blue-600 text-white text-xs font-bold rounded-lg hover:bg-blue-700 transition-colors">
                      Start Simulation
                    </button>
                  </motion.div>
                )}
              </AnimatePresence>

              {/* Chat Messages */}
              <div className="flex-1 overflow-y-auto bg-white rounded-2xl border border-slate-200 p-6 mb-4 space-y-4">
                {messages.map((msg, i) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, y: 8 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.3, delay: i * 0.05 }}
                    className={`flex gap-3 ${msg.role === "user" ? "justify-end" : "justify-start"}`}
                  >
                    {msg.role === "assistant" && (
                      <div className={`w-9 h-9 rounded-full flex items-center justify-center text-lg flex-shrink-0 mt-1 ${chatMode === "simulation" ? "bg-blue-100" : "bg-[#C66810]/10"}`}>
                        {chatMode === "simulation" ? "🎭" : "🐵"}
                      </div>
                    )}
                    <div
                      className={`max-w-[75%] rounded-2xl px-5 py-3.5 ${
                        msg.role === "user"
                          ? "bg-[#C66810] text-white rounded-br-md"
                          : chatMode === "simulation"
                            ? "bg-blue-50 text-slate-700 border border-blue-200 rounded-bl-md"
                            : "bg-slate-50 text-slate-700 border border-slate-200 rounded-bl-md"
                      }`}
                    >
                      <div className="text-sm leading-relaxed whitespace-pre-wrap">
                        {msg.content.split(/(\*\*.*?\*\*)/g).map((part, j) =>
                          part.startsWith("**") && part.endsWith("**") ? (
                            <strong key={j}>{part.slice(2, -2)}</strong>
                          ) : (
                            <span key={j}>{part}</span>
                          )
                        )}
                      </div>
                    </div>
                    {msg.role === "user" && (
                      <div className="w-9 h-9 rounded-full bg-slate-200 flex items-center justify-center text-sm font-bold text-slate-600 flex-shrink-0 mt-1">
                        You
                      </div>
                    )}
                  </motion.div>
                ))}

                {sending && (
                  <div className="flex gap-3 justify-start">
                    <div className={`w-9 h-9 rounded-full flex items-center justify-center text-lg flex-shrink-0 ${chatMode === "simulation" ? "bg-blue-100" : "bg-[#C66810]/10"}`}>
                      {chatMode === "simulation" ? "🎭" : "🐵"}
                    </div>
                    <div className={`rounded-2xl rounded-bl-md px-5 py-4 ${chatMode === "simulation" ? "bg-blue-50 border border-blue-200" : "bg-slate-50 border border-slate-200"}`}>
                      <div className="flex gap-1.5">
                        <div className="w-2 h-2 rounded-full bg-[#C66810] animate-bounce" style={{ animationDelay: "0ms" }} />
                        <div className="w-2 h-2 rounded-full bg-[#C66810] animate-bounce" style={{ animationDelay: "150ms" }} />
                        <div className="w-2 h-2 rounded-full bg-[#C66810] animate-bounce" style={{ animationDelay: "300ms" }} />
                      </div>
                    </div>
                  </div>
                )}

                <div ref={chatEndRef} />
              </div>

              {/* Chat Input */}
              <div className="flex gap-3">
                <input
                  type="text"
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && sendMessage()}
                  placeholder={chatMode === "simulation" ? "Respond to the delegate..." : "Ask Bongo anything about this exercise..."}
                  className="flex-1 px-5 py-3.5 rounded-xl border border-slate-200 text-sm text-slate-700 focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] shadow-sm bg-white"
                  disabled={sending}
                />
                <button
                  onClick={() => sendMessage()}
                  disabled={sending || !chatInput.trim()}
                  className="px-6 py-3.5 bg-[#C66810] text-white font-bold rounded-xl shadow-sm hover:bg-[#A05200] disabled:opacity-50 transition-all text-sm flex items-center gap-2"
                >
                  {sending ? "..." : "Send"}
                  {!sending && <span>&rarr;</span>}
                </button>
              </div>

              {/* Quick Action Buttons */}
              <div className="flex flex-wrap gap-2 mt-3">
                {QUICK_ACTIONS.map((action) => (
                  <button
                    key={action.label}
                    onClick={() => sendMessage(action.message)}
                    disabled={sending}
                    className="px-3 py-1.5 bg-white text-xs font-medium text-slate-500 border border-slate-200 rounded-full hover:border-[#C66810] hover:text-[#C66810] transition-colors disabled:opacity-50"
                  >
                    {action.label}
                  </button>
                ))}
              </div>
            </motion.div>
          )}

          {/* ── Submit Tab ── */}
          {activeTab === "submit" && (
            <motion.div
              key="submit"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -12 }}
              transition={{ duration: 0.3 }}
              className="space-y-6"
            >
              {/* Compact prompt reminder */}
              <div className="bg-orange-50 rounded-xl p-4 border border-orange-200">
                <div className="flex items-center gap-2 mb-1">
                  <span>🐵</span>
                  <span className="font-bold text-[#C66810] text-sm">Exercise Prompt</span>
                </div>
                <p className="text-xs text-slate-600 line-clamp-3">{question.prompt}</p>
              </div>

              {/* Feedback Display */}
              <AnimatePresence>
                {feedback && (
                  <motion.div
                    initial={{ opacity: 0, scale: 0.96 }}
                    animate={{ opacity: 1, scale: 1 }}
                    className="bg-white border border-slate-200 rounded-2xl p-8 shadow-lg"
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
                          transition={{ delay: 0.3, type: "spring" }}
                          className="text-4xl font-black text-[#C66810]"
                        >
                          {feedback.overall_score}
                        </motion.div>
                        <div className="text-xs text-slate-500 font-medium">/ 100</div>
                      </div>
                    </div>

                    <div className="w-full bg-slate-100 rounded-full h-3 mb-6 overflow-hidden">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${feedback.overall_score}%` }}
                        transition={{ duration: 1.2, delay: 0.4 }}
                        className="h-3 rounded-full bg-[#C66810]"
                      />
                    </div>

                    {/* Rubric Breakdown */}
                    {feedback.rubric_scores && (
                      <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.45 }} className="bg-slate-50 rounded-xl p-5 border border-slate-200 mb-5">
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

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                      <div className="bg-green-50 rounded-xl p-5 border border-green-200">
                        <h3 className="font-bold text-green-700 mb-2">Strengths</h3>
                        <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.strengths}</p>
                      </div>
                      <div className="bg-orange-50 rounded-xl p-5 border border-orange-200">
                        <h3 className="font-bold text-[#C66810] mb-2">Areas for Improvement</h3>
                        <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.improvements}</p>
                      </div>
                    </div>

                    {/* Example Revision */}
                    {feedback.example_revision && (
                      <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.65 }} className="bg-blue-50 rounded-xl p-5 border border-blue-200 mb-4">
                        <h3 className="font-bold text-blue-700 mb-2 flex items-center gap-2">
                          <span>✨</span> Here&apos;s How to Improve
                        </h3>
                        <p className="text-xs text-blue-600 mb-3">Bongo rewrote your weakest section to show you what a stronger version looks like:</p>
                        <div className="bg-white rounded-lg p-4 border border-blue-200 text-sm text-slate-700 whitespace-pre-line font-mono leading-relaxed">
                          {feedback.example_revision}
                        </div>
                      </motion.div>
                    )}

                    <div className="bg-slate-50 rounded-xl p-5 border border-slate-200 mb-4">
                      <h3 className="font-bold text-slate-800 mb-2">Detailed Analysis</h3>
                      <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.detailed_feedback}</p>
                    </div>

                    <div className="bg-orange-50 rounded-xl p-5 border border-orange-200">
                      <h3 className="font-bold text-[#C66810] mb-2">Next Steps</h3>
                      <p className="text-sm text-slate-600 whitespace-pre-line">{feedback.suggestions}</p>
                    </div>

                    <div className="mt-6 flex gap-3">
                      <button
                        onClick={() => setActiveTab("chat")}
                        className="px-5 py-2 bg-white text-slate-700 font-bold rounded-lg border border-slate-200 hover:border-[#C66810] hover:text-[#C66810] transition-colors text-sm"
                      >
                        🐵 Discuss with Bongo
                      </button>
                      <button
                        onClick={() => { setFeedback(null); setTextContent(""); }}
                        className="px-5 py-2 bg-slate-100 text-slate-700 font-bold rounded-lg hover:bg-slate-200 transition-colors text-sm"
                      >
                        📝 Try Again
                      </button>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>

              {/* Submit Form */}
              {!feedback && (
                <div className="space-y-4">
                  <div>
                    <label className="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1.5">
                      Your Response *
                    </label>
                    <textarea
                      value={textContent}
                      onChange={(e) => setTextContent(e.target.value)}
                      rows={14}
                      placeholder="Write your response here... Bongo will review it and give you detailed feedback!"
                      className="w-full px-4 py-3 rounded-xl border border-slate-200 text-slate-700 focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] resize-y font-mono text-sm shadow-sm"
                    />
                  </div>

                  {submitError && (
                    <div className="bg-red-50 border border-red-200 text-red-700 rounded-xl p-4 text-sm">
                      ⚠️ {submitError}
                    </div>
                  )}

                  <button
                    onClick={handleSubmit}
                    disabled={submitting || !textContent.trim()}
                    className="w-full py-4 bg-[#C66810] text-white font-bold text-lg rounded-xl shadow-sm hover:bg-[#A05200] disabled:opacity-60 transition-all"
                  >
                    {submitting ? (
                      <span className="flex items-center justify-center gap-3">
                        <span className="animate-bounce">🐵</span>
                        Bongo is reviewing...
                      </span>
                    ) : (
                      "Submit for DiplomAI Review"
                    )}
                  </button>
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </main>
    </div>
  );
}
