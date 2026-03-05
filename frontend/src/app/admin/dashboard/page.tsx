"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import Link from "next/link";
import { motion } from "framer-motion";

interface ExtendedUser {
  name?: string | null;
  email?: string | null;
  image?: string | null;
  role?: string;
  username?: string;
  isSuperuser?: boolean;
}

interface ExtendedSession {
  user: ExtendedUser;
}

interface Article {
  id: number;
  title: string;
  content: string;
  category: string;
  author_name: string;
  status: string;
  created_at: string;
}

export default function AdminDashboardPage() {
  const [pendingArticles, setPendingArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);
  const [processingId, setProcessingId] = useState<number | null>(null);
  const router = useRouter();
  const { data: session, status } = useSession() as { data: ExtendedSession | null; status: string };

  const getCookie = (name: string) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop()?.split(";").shift();
  };

  useEffect(() => {
    if (status === "unauthenticated") { router.push("/login"); return; }
    if (status === "authenticated" && session?.user?.role !== "AD" && !session?.user?.isSuperuser) { router.push("/"); return; }
    if (status === "authenticated" && (session?.user?.role === "AD" || session?.user?.isSuperuser)) { fetchPendingArticles(); }
  }, [status, session, router]);

  const fetchPendingArticles = async () => {
    try {
      const token = getCookie("session_token");
      const res = await fetch("https://mun-global.onrender.com/api/news/admin/pending/", {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.ok) setPendingArticles(await res.json());
    } catch (error) { console.error("Failed to fetch pending articles:", error); }
    finally { setLoading(false); }
  };

  const handleApprove = async (id: number) => {
    setProcessingId(id);
    try {
      const token = getCookie("session_token");
      const res = await fetch(`https://mun-global.onrender.com/api/news/admin/${id}/approve/`, {
        method: "POST", headers: { Authorization: `Bearer ${token}` },
      });
      if (res.ok) setPendingArticles(prev => prev.filter(a => a.id !== id));
      else alert("Failed to approve article");
    } catch (error) { console.error("Failed to approve:", error); }
    finally { setProcessingId(null); }
  };

  const handleReject = async (id: number) => {
    const reason = prompt("Reason for rejection (optional):");
    setProcessingId(id);
    try {
      const token = getCookie("session_token");
      const res = await fetch(`https://mun-global.onrender.com/api/news/admin/${id}/reject/`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
        body: JSON.stringify({ reason }),
      });
      if (res.ok) setPendingArticles(prev => prev.filter(a => a.id !== id));
      else alert("Failed to reject article");
    } catch (error) { console.error("Failed to reject:", error); }
    finally { setProcessingId(null); }
  };

  const getCategoryLabel = (category: string) => {
    switch (category) {
      case "NW": return "Global News";
      case "GD": return "Preparation Guides";
      case "IN": return "Delegate Interviews";
      default: return category;
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50">
        <div className="flex items-center justify-center h-64 pt-32">
          <div className="animate-spin rounded-full h-10 w-10 border-2 border-[#C66810] border-t-transparent"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero Header */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="max-w-5xl mx-auto px-6 pt-28 pb-12 relative z-10">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
            <div className="flex items-center justify-between">
              <div>
                <p className="text-[11px] font-black uppercase tracking-[0.3em] text-[#C66810] mb-2">Admin</p>
                <h1 className="text-3xl md:text-4xl font-black text-white mb-1">Editorial <span className="font-playfair italic text-[#C66810]">Dashboard</span></h1>
                <p className="text-slate-400 text-sm">Review and approve article submissions</p>
              </div>
              <Link href="/" className="px-5 py-2 bg-white/[0.07] text-white font-bold rounded-lg hover:bg-white/[0.12] border border-white/10 transition text-sm">
                &larr; Back to Home
              </Link>
            </div>
          </motion.div>
        </div>
      </section>

      <main className="max-w-5xl mx-auto px-6 py-10">
        {/* Stats */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8"
        >
          <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm">
            <p className="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1">Pending Review</p>
            <p className="text-3xl font-black text-[#C66810]">{pendingArticles.length}</p>
          </div>
        </motion.div>

        {pendingArticles.length === 0 ? (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center py-16 bg-white rounded-2xl border border-slate-200"
          >
            <div className="text-5xl mb-3">{"\u2705"}</div>
            <h2 className="text-xl font-bold text-slate-700 mb-2">All Caught Up!</h2>
            <p className="text-slate-500 text-sm">No articles pending review at the moment.</p>
          </motion.div>
        ) : (
          <div className="space-y-4">
            {pendingArticles.map((article, idx) => (
              <motion.div
                key={article.id}
                initial={{ opacity: 0, y: 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: idx * 0.06 }}
                className="bg-white border border-slate-200 rounded-xl p-5 hover:shadow-md hover:border-orange-200 transition-all"
              >
                <div className="flex items-start justify-between gap-6">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <span className="text-[9px] font-bold text-slate-500 uppercase tracking-widest">
                        {getCategoryLabel(article.category)}
                      </span>
                      <span className="px-2 py-0.5 bg-orange-100 text-[#C66810] rounded-md text-[9px] font-bold uppercase tracking-widest">
                        Pending
                      </span>
                    </div>
                    <h3 className="text-lg font-bold text-slate-900 mb-1.5">{article.title}</h3>
                    <p className="text-sm text-slate-600 mb-3 line-clamp-3">{article.content}</p>
                    <div className="flex items-center gap-3 text-xs text-slate-400">
                      <span>By {article.author_name}</span>
                      <span>&middot;</span>
                      <span>{new Date(article.created_at).toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" })}</span>
                    </div>
                  </div>
                  <div className="flex flex-col gap-2">
                    <motion.button
                      whileHover={{ scale: 1.03 }}
                      whileTap={{ scale: 0.97 }}
                      onClick={() => handleApprove(article.id)}
                      disabled={processingId === article.id}
                      className="px-5 py-2 bg-green-600 text-white font-bold rounded-lg hover:bg-green-700 transition disabled:opacity-50 text-sm"
                    >
                      {processingId === article.id ? "..." : "Approve"}
                    </motion.button>
                    <motion.button
                      whileHover={{ scale: 1.03 }}
                      whileTap={{ scale: 0.97 }}
                      onClick={() => handleReject(article.id)}
                      disabled={processingId === article.id}
                      className="px-5 py-2 bg-red-600 text-white font-bold rounded-lg hover:bg-red-700 transition disabled:opacity-50 text-sm"
                    >
                      Reject
                    </motion.button>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
