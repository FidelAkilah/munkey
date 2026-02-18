/* eslint-disable @typescript-eslint/no-explicit-any */
// src/app/skills/page.tsx
"use client";
import { useState, useEffect } from "react";


export default function SkillsPage() {
  const [categories, setCategories] = useState<any[]>([]);
  const [activeTab, setActiveTab] = useState(0);

  useEffect(() => {
    fetch("https://mun-global.onrender.com/api/skills/")
      .then(res => res.json())
      .then(data => setCategories(data));
  }, []);

  return (
    <div className="min-h-screen bg-slate-50">
      
      <main className="max-w-7xl mx-auto px-6 py-12">
        <header className="mb-10">
          <h1 className="text-4xl font-black text-slate-900">Delegate Skill Sharing</h1>
          <p className="text-slate-500 mt-2">Master the art of diplomacy with curated training.</p>
        </header>

        {/* Category Tabs */}
        <div className="flex gap-4 mb-12 overflow-x-auto pb-4 scrollbar-hide">
          {categories.map((cat, idx) => (
            <button
              key={cat.id}
              onClick={() => setActiveTab(idx)}
              className={`px-6 py-2 rounded-full font-bold transition-all whitespace-nowrap ${
                activeTab === idx ? "bg-blue-600 text-white shadow-lg" : "bg-white text-slate-600 hover:bg-slate-100"
              }`}
            >
              {cat.name}
            </button>
          ))}
        </div>

        {/* Video Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {categories[activeTab]?.videos.map((video: any) => (
            <div key={video.id} className="bg-white rounded-[2rem] overflow-hidden border border-slate-200 shadow-sm hover:shadow-xl transition-all">
              {/* YouTube Embed */}
              <div className="aspect-video w-full">
                <iframe
                  className="w-full h-full"
                  src={`https://www.youtube.com/embed/${video.video_id}`}
                  title={video.title}
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                ></iframe>
              </div>
              <div className="p-6">
                <div className="flex justify-between items-start mb-2">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-blue-600 bg-blue-50 px-2 py-1 rounded">
                    {video.difficulty}
                  </span>
                </div>
                <h3 className="font-bold text-lg text-slate-900">{video.title}</h3>
                <p className="text-sm text-slate-500 mt-2 line-clamp-2">{video.description}</p>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}