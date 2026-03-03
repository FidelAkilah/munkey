"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import Link from "next/link";

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
      <main className="max-w-5xl mx-auto px-6 pt-28">
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-10 w-10 border-2 border-[#C66810] border-t-transparent"></div>
        </div>
      </main>
    );
  }

  return (
    <main className="max-w-5xl mx-auto px-6 pt-28 pb-16">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-black text-slate-900 mb-1">Editorial Dashboard</h1>
          <p className="text-slate-500 text-sm">Review and approve article submissions</p>
        </div>
        <Link href="/" className="px-5 py-2 bg-slate-100 text-slate-700 font-bold rounded-lg hover:bg-slate-200 transition text-sm">
          &larr; Back to Home
        </Link>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="bg-white border border-slate-200 rounded-xl p-5">
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1">Pending Review</p>
          <p className="text-3xl font-black text-[#C66810]">{pendingArticles.length}</p>
        </div>
      </div>

      {pendingArticles.length === 0 ? (
        <div className="text-center py-16 bg-slate-50 rounded-xl border border-slate-200">
          <div className="text-5xl mb-3">{"\u2705"}</div>
          <h2 className="text-xl font-bold text-slate-700 mb-2">All Caught Up!</h2>
          <p className="text-slate-500 text-sm">No articles pending review at the moment.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {pendingArticles.map((article) => (
            <div key={article.id} className="bg-white border border-slate-200 rounded-xl p-5 hover:shadow-md hover:border-orange-200 transition-all">
              <div className="flex items-start justify-between gap-6">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-[9px] font-bold text-slate-500 uppercase tracking-widest">
                      {getCategoryLabel(article.category)}
                    </span>
                    <span className="px-2 py-0.5 bg-orange-100 text-[#C66810] rounded text-[9px] font-bold uppercase tracking-widest">
                      PENDING
                    </span>
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 mb-1.5">{article.title}</h3>
                  <p className="text-sm text-slate-600 mb-3 line-clamp-3">{article.content}</p>
                  <div className="flex items-center gap-3 text-xs text-slate-400">
                    <span>By {article.author_name}</span>
                    <span>&middot;</span>
                    <span>{new Date(article.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
                <div className="flex flex-col gap-2">
                  <button onClick={() => handleApprove(article.id)} disabled={processingId === article.id}
                    className="px-5 py-2 bg-green-600 text-white font-bold rounded-lg hover:bg-green-700 transition disabled:opacity-50 text-sm">
                    {processingId === article.id ? "..." : "Approve"}
                  </button>
                  <button onClick={() => handleReject(article.id)} disabled={processingId === article.id}
                    className="px-5 py-2 bg-red-600 text-white font-bold rounded-lg hover:bg-red-700 transition disabled:opacity-50 text-sm">
                    Reject
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}
