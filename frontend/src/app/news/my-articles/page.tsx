"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import Link from "next/link";

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
      // Get token from NextAuth session instead of cookies
      const token = (session?.user as { accessToken?: string })?.accessToken;
      
      if (!token) {
        console.error("No access token found in session");
        setLoading(false);
        return;
      }

      const res = await fetch("http://localhost:8000/api/news/my-articles/", {
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
        return <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-bold">APPROVED</span>;
      case 'PENDING':
        return <span className="px-3 py-1 bg-yellow-100 text-yellow-700 rounded-full text-xs font-bold">PENDING REVIEW</span>;
      case 'REJECTED':
        return <span className="px-3 py-1 bg-red-100 text-red-700 rounded-full text-xs font-bold">REJECTED</span>;
      default:
        return <span className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-xs font-bold">{status}</span>;
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
      <main className="max-w-4xl mx-auto p-12">
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        </div>
      </main>
    );
  }

  return (
    <main className="max-w-4xl mx-auto p-12">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-black mb-2">My Submissions</h1>
          <p className="text-slate-500">Track the status of your article submissions</p>
        </div>
        <Link
          href="/news/add"
          className="px-6 py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition"
        >
          + New Submission
        </Link>
      </div>

      {articles.length === 0 ? (
        <div className="text-center py-16 bg-slate-50 rounded-3xl">
          <div className="text-6xl mb-4">📝</div>
          <h2 className="text-2xl font-bold mb-4">No Submissions Yet</h2>
          <p className="text-slate-500 mb-8">
            You haven&apos;t submitted any articles yet. Share your MUN experiences with the community!
          </p>
          <Link
            href="/news/add"
            className="inline-block px-8 py-4 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition"
          >
            Submit Your First Article
          </Link>
        </div>
      ) : (
        <div className="space-y-4">
          {articles.map((article) => (
            <div
              key={article.id}
              className="bg-white border rounded-2xl p-6 hover:shadow-lg transition-shadow"
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-2">
                    <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                      {getCategoryLabel(article.category)}
                    </span>
                    {getStatusBadge(article.status)}
                  </div>
                  <h3 className="text-xl font-bold mb-2">{article.title}</h3>
                  <p className="text-slate-600 line-clamp-2 mb-4">{article.content}</p>
                  <p className="text-xs text-slate-400">
                    Submitted on {new Date(article.created_at).toLocaleDateString()}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}

