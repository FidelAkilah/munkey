"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import Link from "next/link";
import { motion } from "framer-motion";

interface Article {
  id: number;
  title: string;
  content: string;
  category: string;
  status: string;
  created_at: string;
}

export default function MyArticlesPage() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);
  const router = useRouter();
  const { data: session, status } = useSession();

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

    if (status === 'authenticated') {
      fetchArticles();
    }
  }, [status, router]);

  const fetchArticles = async () => {
    try {
      const token = (session?.user as { accessToken?: string })?.accessToken;

      if (!token) {
        console.error("No access token found in session");
        setLoading(false);
        return;
      }

      const res = await fetch("https://mun-global.onrender.com/api/news/my-articles/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (res.ok) {
        const data = await res.json();
        setArticles(data);
      } else {
        console.error("Failed to fetch articles:", res.status, res.statusText);
      }
    } catch (error) {
      console.error("Failed to fetch articles:", error);
    } finally {
      setLoading(false);
    }
  };

  const getStatusBadge = (status: string) => {
    switch (status) {
      case 'APPROVED':
        return <span className="px-3 py-1 bg-green-100 text-green-700 rounded-md text-[10px] font-bold uppercase tracking-widest">Approved</span>;
      case 'PENDING':
        return <span className="px-3 py-1 bg-orange-100 text-[#C66810] rounded-md text-[10px] font-bold uppercase tracking-widest">Pending Review</span>;
      case 'REJECTED':
        return <span className="px-3 py-1 bg-red-100 text-red-700 rounded-md text-[10px] font-bold uppercase tracking-widest">Rejected</span>;
      default:
        return <span className="px-3 py-1 bg-gray-100 text-gray-700 rounded-md text-[10px] font-bold uppercase tracking-widest">{status}</span>;
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
      <div className="min-h-screen bg-slate-50">
        <div className="flex items-center justify-center h-64 pt-32">
          <div className="animate-spin rounded-full h-12 w-12 border-2 border-[#C66810] border-t-transparent"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Hero Header */}
      <section className="relative overflow-hidden bg-[#0a1628] grain">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-[500px] h-[500px] bg-[#C66810]/10 rounded-full blur-[100px]" />
        <div className="max-w-4xl mx-auto px-6 pt-28 pb-12 relative z-10">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
            <div className="flex items-center justify-between">
              <div>
                <h1 className="text-4xl font-black text-white mb-2">My <span className="font-playfair italic text-[#C66810]">Submissions</span></h1>
                <p className="text-slate-400">Track the status of your article submissions</p>
              </div>
              <Link
                href="/news/add"
                className="hidden sm:inline-flex px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition shadow-sm shadow-orange-900/30 text-sm"
              >
                + New Submission
              </Link>
            </div>
          </motion.div>
        </div>
      </section>

      <main className="max-w-4xl mx-auto px-6 py-10">
        {articles.length === 0 ? (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center py-16 bg-white rounded-2xl border border-slate-200"
          >
            <div className="text-6xl mb-4">📝</div>
            <h2 className="text-2xl font-bold mb-4 text-slate-900">No Submissions Yet</h2>
            <p className="text-slate-500 mb-8">
              You haven&apos;t submitted any articles yet. Share your MUN experiences with the community!
            </p>
            <Link
              href="/news/add"
              className="inline-block px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition"
            >
              Submit Your First Article
            </Link>
          </motion.div>
        ) : (
          <div className="space-y-4">
            {articles.map((article, idx) => (
              <motion.div
                key={article.id}
                initial={{ opacity: 0, y: 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: idx * 0.06 }}
                whileHover={{ y: -2 }}
                className="bg-white border border-slate-200 rounded-xl p-6 hover:shadow-lg hover:border-orange-200 transition-all"
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">
                        {getCategoryLabel(article.category)}
                      </span>
                      {getStatusBadge(article.status)}
                    </div>
                    <h3 className="text-xl font-bold mb-2 text-slate-900">{article.title}</h3>
                    <p className="text-slate-600 line-clamp-2 mb-4 text-sm">{article.content}</p>
                    <p className="text-xs text-slate-400">
                      Submitted on {new Date(article.created_at).toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" })}
                    </p>
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
