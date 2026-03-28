"use client";
import { useSearchParams } from 'next/navigation';
import { useState, useEffect, Suspense } from 'react';
import { useSession } from 'next-auth/react';
import Link from 'next/link';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "https://mun-global.onrender.com";

interface SearchResult {
  id: number;
  title?: string;
  name?: string;
  slug?: string;
  snippet?: string;
  type: string;
  category?: string;
  city?: string;
  country?: string;
}

interface ExtendedUser {
  accessToken?: string;
}

const TYPE_CONFIG: Record<string, { label: string; icon: string; link: (r: SearchResult) => string }> = {
  articles: {
    label: 'Articles',
    icon: '📰',
    link: (r) => `/news/${r.slug}`,
  },
  lessons: {
    label: 'Lessons',
    icon: '📖',
    link: (r) => `/curriculum/practice?category=${r.slug}`,
  },
  questions: {
    label: 'Exercises',
    icon: '🎯',
    link: (r) => `/curriculum/question/${r.id}`,
  },
  conferences: {
    label: 'Conferences',
    icon: '🌍',
    link: () => `/conferences`,
  },
};

const highlightMatch = (text: string, query: string) => {
  if (!text || !query) return text;
  const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const parts = text.split(new RegExp(`(${escaped})`, 'gi'));
  return parts.map((part, i) =>
    part.toLowerCase() === query.toLowerCase() ? (
      <mark key={i} className="bg-yellow-200 text-slate-900 rounded px-0.5">{part}</mark>
    ) : (
      <span key={i}>{part}</span>
    )
  );
};

const SearchContent = () => {
  const searchParams = useSearchParams();
  const query = searchParams.get('q') || '';
  const { data: session } = useSession();
  const user = session?.user as ExtendedUser | undefined;

  const [results, setResults] = useState<Record<string, SearchResult[]>>({});
  const [fetchCount, setFetchCount] = useState(0);
  const [activeTab, setActiveTab] = useState('all');
  const accessToken = user?.accessToken;
  const loading = query.length >= 2 && fetchCount === 0 && Object.keys(results).length === 0;

  useEffect(() => {
    if (!query || query.length < 2) return;
    const headers: Record<string, string> = {};
    if (accessToken) headers['Authorization'] = `Bearer ${accessToken}`;
    let cancelled = false;
    fetch(`${API_BASE}/api/search/?q=${encodeURIComponent(query)}`, { headers })
      .then((r) => r.ok ? r.json() : {})
      .then((data) => { if (!cancelled) { setResults(data); setFetchCount((c) => c + 1); } })
      .catch(() => { if (!cancelled) { setResults({}); setFetchCount((c) => c + 1); } });
    return () => { cancelled = true; };
  }, [query, accessToken]);

  const allTypes = Object.keys(TYPE_CONFIG);
  const tabs = [
    { key: 'all', label: 'All Results' },
    ...allTypes.map((t) => ({ key: t, label: TYPE_CONFIG[t].label })),
  ];

  const totalResults = Object.values(results).reduce((sum, arr) => sum + arr.length, 0);

  const filteredTypes = activeTab === 'all'
    ? allTypes.filter((t) => (results[t]?.length || 0) > 0)
    : [activeTab].filter((t) => (results[t]?.length || 0) > 0);

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="bg-white border-b border-slate-200">
        <div className="max-w-5xl mx-auto px-6 py-8">
          <h1 className="text-2xl font-bold text-slate-900">
            Search results for &ldquo;{query}&rdquo;
          </h1>
          {!loading && (
            <p className="text-sm text-slate-500 mt-1">
              {totalResults} result{totalResults !== 1 ? 's' : ''} found
            </p>
          )}
        </div>
      </div>

      <div className="max-w-5xl mx-auto px-6 py-6">
        {/* Tabs */}
        <div className="flex gap-1 overflow-x-auto pb-4 mb-6 border-b border-slate-200">
          {tabs.map((tab) => {
            const count = tab.key === 'all' ? totalResults : (results[tab.key]?.length || 0);
            return (
              <button
                key={tab.key}
                onClick={() => setActiveTab(tab.key)}
                className={`px-4 py-2 text-sm font-semibold rounded-lg whitespace-nowrap transition-colors ${
                  activeTab === tab.key
                    ? 'bg-[#C66810] text-white'
                    : 'text-slate-600 hover:bg-slate-100'
                }`}
              >
                {tab.label} {count > 0 && <span className="ml-1 opacity-70">({count})</span>}
              </button>
            );
          })}
        </div>

        {/* Loading */}
        {loading && (
          <div className="flex items-center justify-center py-20">
            <div className="w-8 h-8 border-3 border-slate-200 border-t-[#C66810] rounded-full animate-spin" />
          </div>
        )}

        {/* No results */}
        {!loading && totalResults === 0 && query.length >= 2 && (
          <div className="text-center py-20">
            <p className="text-5xl mb-4">🔍</p>
            <p className="text-lg font-semibold text-slate-700">No results found</p>
            <p className="text-sm text-slate-500 mt-1">
              Try different keywords or check your spelling
            </p>
          </div>
        )}

        {/* Results */}
        {!loading && filteredTypes.map((type) => (
          <div key={type} className="mb-8">
            <div className="flex items-center gap-2 mb-3">
              <span className="text-lg">{TYPE_CONFIG[type]?.icon}</span>
              <h2 className="text-lg font-bold text-slate-800">{TYPE_CONFIG[type]?.label}</h2>
              <span className="text-xs font-medium text-slate-400 bg-slate-100 px-2 py-0.5 rounded-full">
                {results[type]?.length}
              </span>
            </div>
            <div className="space-y-3">
              {results[type]?.map((item) => (
                <Link
                  key={`${item.type}-${item.id}`}
                  href={TYPE_CONFIG[type]?.link(item) || '#'}
                  className="block bg-white rounded-xl border border-slate-200 p-5 hover:border-[#C66810]/30 hover:shadow-md transition-all"
                >
                  <div className="flex items-start gap-4">
                    <span className="text-2xl mt-0.5">{TYPE_CONFIG[type]?.icon}</span>
                    <div className="min-w-0 flex-1">
                      <h3 className="text-base font-bold text-slate-900">
                        {highlightMatch(item.title || item.name || '', query)}
                      </h3>
                      {item.snippet && (
                        <p className="text-sm text-slate-600 mt-1 line-clamp-3">
                          {highlightMatch(item.snippet, query)}
                        </p>
                      )}
                      <div className="flex items-center gap-3 mt-2">
                        {item.category && (
                          <span className="text-xs font-medium text-slate-500 bg-slate-100 px-2 py-0.5 rounded-full">
                            {item.category}
                          </span>
                        )}
                        {item.city && item.country && (
                          <span className="text-xs text-slate-400">
                            📍 {item.city}, {item.country}
                          </span>
                        )}
                      </div>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

const SearchPage = () => {
  return (
    <Suspense fallback={
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="w-8 h-8 border-3 border-slate-200 border-t-[#C66810] rounded-full animate-spin" />
      </div>
    }>
      <SearchContent />
    </Suspense>
  );
};

export default SearchPage;
