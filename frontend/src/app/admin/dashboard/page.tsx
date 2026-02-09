"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import Link from "next/link";

// Extend the session user type
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
    if (status === 'unauthenticated') {
      router.push('/login');
      return;
    }

// Check if user is admin (role='AD' or isSuperuser=true)
    if (status === 'authenticated' && session?.user?.role !== 'AD' && !session?.user?.isSuperuser) {
      router.push('/');
      return;
    }

    if (status === 'authenticated' && (session?.user?.role === 'AD' || session?.user?.isSuperuser)) {
      fetchPendingArticles();
    }
  }, [status, session, router]);

  const fetchPendingArticles = async () => {
    try {
      const token = getCookie("session_token");
      const res = await fetch("http://localhost:8000/api/news/admin/pending/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (res.ok) {
        const data = await res.json();
        setPendingArticles(data);
      }
    } catch (error) {
      console.error("Failed to fetch pending articles:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleApprove = async (id: number) => {
    setProcessingId(id);
    try {
      const token = getCookie("session_token");
      const res = await fetch(`http://localhost:8000/api/news/admin/${id}/approve/`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (res.ok) {
        // Remove from list
        setPendingArticles(prev => prev.filter(a => a.id !== id));
      } else {
        alert("Failed to approve article");
      }
    } catch (error) {
      console.error("Failed to approve:", error);
    } finally {
      setProcessingId(null);
    }
  };

  const handleReject = async (id: number) => {
    const reason = prompt("Reason for rejection (optional):");
    setProcessingId(id);
    try {
      const token = getCookie("session_token");
      const res = await fetch(`http://localhost:8000/api/news/admin/${id}/reject/`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ reason }),
      });

      if (res.ok) {
        // Remove from list
        setPendingArticles(prev => prev.filter(a => a.id !== id));
      } else {
        alert("Failed to reject article");
      }
    } catch (error) {
      console.error("Failed to reject:", error);
    } finally {
      setProcessingId(null);
    }
  };

  const getCategoryLabel = (category: string) => {
    switch (category) {
      case 'NW': return 'Global News';
      case 'GD': return 'Preparation Guides';
      case 'IN': return 'Delegate Interviews';
      default: return category;
    }
  };

  if (loading) {
    return (
      <main className="max-w-6xl mx-auto p-12">
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        </div>
      </main>
    );
  }

  return (
    <main className="max-w-6xl mx-auto p-12">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-black mb-2">Editorial Dashboard</h1>
          <p className="text-slate-500">Review and approve article submissions</p>
        </div>
        <Link
          href="/"
          className="px-6 py-3 bg-slate-800 text-white font-semibold rounded-xl hover:bg-slate-700 transition"
        >
          ← Back to Home
        </Link>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white border rounded-2xl p-6">
          <p className="text-sm text-slate-500 mb-1">Pending Review</p>
          <p className="text-3xl font-black text-yellow-600">{pendingArticles.length}</p>
        </div>
      </div>

      {pendingArticles.length === 0 ? (
        <div className="text-center py-16 bg-slate-50 rounded-3xl">
          <div className="text-6xl mb-4">✅</div>
          <h2 className="text-2xl font-bold mb-4">All Caught Up!</h2>
          <p className="text-slate-500">
            No articles pending review at the moment.
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {pendingArticles.map((article) => (
            <div
              key={article.id}
              className="bg-white border rounded-2xl p-6 hover:shadow-lg transition-shadow"
            >
              <div className="flex items-start justify-between gap-6">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-2">
                    <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                      {getCategoryLabel(article.category)}
                    </span>
                    <span className="px-3 py-1 bg-yellow-100 text-yellow-700 rounded-full text-xs font-bold">
                      PENDING
                    </span>
                  </div>
                  <h3 className="text-xl font-bold mb-2">{article.title}</h3>
                  <p className="text-slate-600 mb-4">{article.content}</p>
                  <div className="flex items-center gap-4 text-sm text-slate-500">
                    <span>By {article.author_name}</span>
                    <span>•</span>
                    <span>Submitted {new Date(article.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
                <div className="flex flex-col gap-2">
                  <button
                    onClick={() => handleApprove(article.id)}
                    disabled={processingId === article.id}
                    className="px-6 py-2 bg-green-600 text-white font-semibold rounded-xl hover:bg-green-700 transition disabled:opacity-50"
                  >
                    {processingId === article.id ? 'Processing...' : 'Approve'}
                  </button>
                  <button
                    onClick={() => handleReject(article.id)}
                    disabled={processingId === article.id}
                    className="px-6 py-2 bg-red-600 text-white font-semibold rounded-xl hover:bg-red-700 transition disabled:opacity-50"
                  >
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

