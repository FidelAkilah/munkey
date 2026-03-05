/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { useSession } from "next-auth/react";

const getCategoryLabel = (cat: string) => {
  switch (cat) {
    case "NW": return "Global News";
    case "GD": return "Preparation Guides";
    case "IN": return "Delegate Interviews";
    default: return cat;
  }
};

const getCategoryColor = (cat: string) => {
  switch (cat) {
    case "NW": return "bg-orange-100 text-[#C66810]";
    case "GD": return "bg-purple-100 text-purple-700";
    case "IN": return "bg-blue-100 text-blue-700";
    default: return "bg-slate-100 text-slate-700";
  }
};

const getImageUrl = (post: any) => {
  return post.image_url || null;
};

export default function Home() {
  const [news, setNews] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const { data: session } = useSession();
  const isAuthenticated = session?.user !== undefined;

  useEffect(() => {
    async function fetchNews() {
      try {
        const res = await fetch("https://mun-global.onrender.com/api/news/", {
          cache: "no-store",
        });
        if (res.ok) {
          const data = await res.json();
          setNews(data);
        }
      } catch (error) {
        console.error("Failed to fetch news:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchNews();
  }, []);

  const missionItems = [
    { icon: "🌍", label: "Nationwide Media", desc: "Connecting Indonesia's circuit.", bg: "bg-orange-50", border: "border-orange-200", text: "text-[#C66810]" },
    { icon: "📡", label: "Reliable Intel", desc: "Primary source for upcoming MUNs.", bg: "bg-blue-50", border: "border-blue-200", text: "text-blue-700" },
    { icon: "🎓", label: "Free Learning", desc: "Cost-free skill sharing for all.", bg: "bg-purple-50", border: "border-purple-200", text: "text-purple-700" },
    { icon: "🚀", label: "The Powerhouse", desc: "Building tomorrow's diplomats.", bg: "bg-emerald-50", border: "border-emerald-200", text: "text-emerald-700" },
  ];

  return (
    <div className="min-h-screen bg-slate-50">

      {/* HERO SECTION */}
      <section className="relative overflow-hidden bg-white border-b border-slate-200">
        <div className="absolute inset-0 bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:20px_20px] opacity-40"></div>

        <div className="max-w-7xl mx-auto px-6 lg:px-8 py-24 md:py-32 relative z-10 flex flex-col items-center text-center">
          <div className="inline-flex items-center gap-2 px-3 py-1 mb-8 rounded-full bg-orange-50 text-[#C66810] text-sm font-bold border border-orange-100">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-orange-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-[#C66810]"></span>
            </span>
            Join the Global Circuit
          </div>

          <h1 className="text-5xl md:text-7xl font-black text-slate-900 tracking-tight leading-[1.1] mb-6 max-w-4xl">
            One Stop for{" "}
            <span className="text-[#C66810]">
              MUN Excellence.
            </span>
          </h1>

          <p className="text-lg md:text-xl text-slate-600 leading-relaxed max-w-2xl mb-10 font-medium">
            Elevate your diplomacy with breaking news, skill-sharing resources, and our revolutionary AI-powered practice.
          </p>

          <div className="flex flex-wrap justify-center gap-4">
            <Link
              href="/skills"
              className="px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl shadow-lg shadow-orange-200 hover:bg-[#A05200] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 transform"
            >
              Explore Skills
            </Link>

            {isAuthenticated ? (
              <Link
                href="/news/add"
                className="px-8 py-4 bg-white text-slate-700 font-bold rounded-xl border-2 border-slate-200 hover:border-slate-300 hover:bg-slate-50 transition-all duration-300"
              >
                Submit a Story
              </Link>
            ) : (
              <Link
                href="/login"
                className="px-8 py-4 bg-white text-slate-700 font-bold rounded-xl border-2 border-slate-200 hover:border-slate-300 hover:bg-slate-50 transition-all duration-300"
              >
                Login to Submit
              </Link>
            )}
          </div>
        </div>
      </section>

      {/* CORE PILLARS SECTION */}
      <section className="max-w-7xl mx-auto px-6 lg:px-8 py-20">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-black text-slate-900 mb-4">Our Core Pillars</h2>
          <p className="text-slate-500 text-lg max-w-2xl mx-auto">
            Everything you need to excel in Model United Nations, all in one place.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {missionItems.map((item, idx) => (
            <div
              key={idx}
              className={`group relative bg-white rounded-2xl p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:border-transparent transition-all duration-300 flex flex-col items-start gap-4 overflow-hidden hover:-translate-y-1`}
            >
              <div className={`w-14 h-14 rounded-xl ${item.bg} ${item.text} flex items-center justify-center text-3xl mb-2 group-hover:scale-110 transition-transform duration-300`}>
                {item.icon}
              </div>

              <div>
                <p className={`text-[10px] font-black uppercase tracking-[0.2em] mb-1 ${item.text}`}>
                  {item.label}
                </p>
                <h3 className="text-lg font-bold text-slate-900 leading-snug">
                  {item.desc}
                </h3>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* DIPLOMAI CTA SECTION */}
      <section className="bg-[#0a1628] py-24 relative overflow-hidden my-12 border-y border-slate-800">
         <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-[#C66810]/20 rounded-full blur-3xl pointer-events-none"></div>
         <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

         <div className="max-w-5xl mx-auto px-6 text-center relative z-10">
           <div className="inline-flex items-center justify-center w-20 h-20 rounded-full bg-white mb-6 shadow-2xl">
             <Image
                src="/MunKey Main Logo.png"
                alt="MunKey Logo"
                width={48}
                height={48}
                className="object-contain"
             />
           </div>
           <h2 className="text-4xl md:text-5xl font-black text-white mb-6">
             Meet <span className="text-[#C66810]">DiplomAI</span>
           </h2>
           <p className="text-slate-300 text-lg md:text-xl mb-10 max-w-2xl mx-auto leading-relaxed">
             Practice your speeches, draft resolutions, and receive personalized feedback
             from our AI strategist, Bongo. Elevate your performance before the next conference.
           </p>
           <Link
             href="/curriculum"
             className="inline-flex items-center gap-2 px-10 py-4 bg-[#C66810] text-white font-bold rounded-xl shadow-lg shadow-orange-900/50 hover:bg-[#A05200] hover:-translate-y-1 transition-all duration-300"
           >
             Start Training Now <span aria-hidden="true">&rarr;</span>
           </Link>
         </div>
      </section>

      {/* NEWS FEED */}
      <main className="max-w-7xl mx-auto px-6 lg:px-8 py-20 mb-12">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6 mb-12 border-b border-slate-200 pb-6">
          <div>
            <h2 className="text-3xl font-black text-slate-900 mb-2">Latest from the Circuit</h2>
            <p className="text-slate-500 font-medium">Stories, interviews, and updates from MUN delegates.</p>
          </div>
          <Link href="/news" className="flex items-center gap-2 text-sm font-bold text-[#C66810] hover:text-[#A05200] transition-colors py-2 px-4 rounded-lg bg-orange-50 hover:bg-orange-100">
            View All Stories <span>&rarr;</span>
          </Link>
        </div>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 animate-pulse">
            {[1, 2, 3].map(i => (
              <div key={i} className="bg-white rounded-2xl h-80 border border-slate-200 shadow-sm" />
            ))}
          </div>
        ) : news.length === 0 ? (
          <div className="bg-white rounded-2xl p-16 text-center border border-slate-200 shadow-sm">
             <div className="text-5xl mb-4 opacity-50">📰</div>
             <h3 className="text-xl font-bold text-slate-700 mb-2">No stories found</h3>
             <p className="text-slate-500 mb-6">Be the first delegate to submit a story to the community!</p>
             <Link href="/news/add" className="inline-block px-6 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors">
               Submit a Story
             </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-12 gap-8">
            {news.slice(0, 5).map((post, index) => (
              <Link
                key={post.id}
                href={`/news/${post.slug}`}
                className={`group block ${
                  index === 0 ? "md:col-span-8 md:row-span-2" : "md:col-span-4"
                }`}
              >
                <div className="bg-white rounded-2xl overflow-hidden border border-slate-200 hover:shadow-xl hover:border-transparent transition-all duration-300 h-full flex flex-col relative">

                  {getImageUrl(post) ? (
                    <div className={`relative w-full overflow-hidden ${index === 0 ? "h-72 md:h-96" : "h-48"}`}>
                      <img
                        src={getImageUrl(post)}
                        alt={post.title}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                      />
                    </div>
                  ) : (
                    <div className={`w-full bg-slate-100 flex items-center justify-center ${index === 0 ? "h-72 md:h-96" : "h-48"}`}>
                      <span className="text-5xl opacity-20">📰</span>
                    </div>
                  )}

                  <div className={`flex flex-col flex-grow ${index === 0 ? "p-8 md:p-10" : "p-6"}`}>
                    <div className="mb-4">
                      <span className={`inline-block px-3 py-1 rounded-md text-[10px] font-bold uppercase tracking-widest ${getCategoryColor(post.category)}`}>
                        {getCategoryLabel(post.category)}
                      </span>
                    </div>

                    <h3 className={`font-black text-slate-900 group-hover:text-[#C66810] transition-colors mb-3 ${index === 0 ? "text-3xl md:text-4xl leading-tight" : "text-xl"}`}>
                      {post.title}
                    </h3>

                    <p className={`text-slate-600 mb-6 flex-grow ${index === 0 ? "text-lg line-clamp-3" : "text-sm line-clamp-2"}`}>
                      {post.content}
                    </p>

                    <div className="flex items-center gap-3 text-xs font-medium text-slate-400 mt-auto pt-4 border-t border-slate-100">
                      <span className="text-slate-700 bg-slate-100 px-2 py-1 rounded-md">{post.author_name}</span>
                      <span>&middot;</span>
                      <span>{new Date(post.created_at).toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric'})}</span>
                    </div>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
