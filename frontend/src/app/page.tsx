/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { useSession } from "next-auth/react";

// ─── HELPERS ────────────────────────────────────────────────────────────────

const getCategoryLabel = (cat: string) => {
  switch (cat) {
    case "NW": return "Global News";
    case "GD": return "Preparation Guides";
    case "IN": return "Delegate Interviews";
    default: return cat;
  }
};

const getImageUrl = (post: any) => post.image_url || null;

// ─── TICKER CONTENT ──────────────────────────────────────────────────────────

const TICKER = [
  "📡  Breaking MUN Circuit News",
  "🌍  Conference Coverage Worldwide",
  "🤖  AI-Powered Speech Practice with DiplomAI",
  "📚  Personalized Curriculum for Every Level",
  "🎥  Curated Video Masterclasses",
  "✍️  Delegate Spotlights & Interviews",
  "🏛️  Resolution Drafting & Crisis Guides",
  "🚀  Build Your Delegate Profile",
];

// ─── SAMPLE YOUTUBE VIDEOS ───────────────────────────────────────────────────
// Replace the `id` values with real YouTube video IDs from your content team.

const FEATURED_VIDEOS = [
  {
    id: "REPLACE_VIDEO_ID_1",
    title: "How to Dominate Your First MUN Conference",
    channel: "Best Delegate",
    tag: "Beginner Guide",
    gradient: "from-blue-900 via-slate-900 to-[#0a1628]",
    tagColor: "text-emerald-300 bg-emerald-950 border-emerald-800/50",
  },
  {
    id: "REPLACE_VIDEO_ID_2",
    title: "Crisis Committee Tactics & Strategy",
    channel: "WorldMUN Academy",
    tag: "Crisis",
    gradient: "from-red-950 via-slate-900 to-[#0a1628]",
    tagColor: "text-red-300 bg-red-950 border-red-800/50",
  },
  {
    id: "REPLACE_VIDEO_ID_3",
    title: "Writing the Perfect Position Paper",
    channel: "MUN Institute",
    tag: "Research",
    gradient: "from-purple-950 via-slate-900 to-[#0a1628]",
    tagColor: "text-purple-300 bg-purple-950 border-purple-800/50",
  },
];

// ─── VIDEO CARD ──────────────────────────────────────────────────────────────

function VideoCard({ video }: { video: (typeof FEATURED_VIDEOS)[0] }) {
  const [playing, setPlaying] = useState(false);

  return (
    <div className="group relative rounded-2xl overflow-hidden bg-[#0d1f3c] border border-white/10 hover:border-[#C66810]/50 transition-all duration-300 hover:shadow-2xl hover:shadow-orange-950/40 hover:-translate-y-1">
      {playing ? (
        <div className="aspect-video">
          <iframe
            src={`https://www.youtube-nocookie.com/embed/${video.id}?autoplay=1&rel=0&modestbranding=1`}
            className="w-full h-full"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
            title={video.title}
          />
        </div>
      ) : (
        <button
          onClick={() => setPlaying(true)}
          className="relative w-full aspect-video block cursor-pointer"
          aria-label={`Play: ${video.title}`}
        >
          {/* Gradient thumbnail background */}
          <div className={`absolute inset-0 bg-gradient-to-br ${video.gradient}`} />
          {/* Subtle grid overlay */}
          <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:40px_40px]" />
          {/* Bottom fade */}
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent" />
          {/* Play button */}
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="w-16 h-16 rounded-full bg-[#C66810] flex items-center justify-center shadow-2xl group-hover:scale-110 group-hover:bg-[#E8913A] transition-all duration-200 ring-4 ring-white/10">
              <svg className="w-6 h-6 text-white ml-1" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8 5v14l11-7z" />
              </svg>
            </div>
          </div>
          {/* YouTube logo */}
          <div className="absolute top-3 right-3">
            <svg className="w-7 h-5 text-red-500 opacity-80" fill="currentColor" viewBox="0 0 24 24">
              <path d="M21.582 6.186a2.506 2.506 0 00-1.765-1.77C18.254 4 12 4 12 4s-6.254 0-7.817.416a2.506 2.506 0 00-1.765 1.77C2 7.747 2 12 2 12s0 4.253.418 5.814a2.506 2.506 0 001.765 1.77C5.746 20 12 20 12 20s6.254 0 7.817-.416a2.506 2.506 0 001.765-1.77C22 16.253 22 12 22 12s0-4.253-.418-5.814zM10 15.464V8.536L16 12l-6 3.464z" />
            </svg>
          </div>
        </button>
      )}

      <div className="p-5">
        <span className={`inline-block text-[10px] font-black uppercase tracking-widest px-2.5 py-0.5 rounded border mb-3 ${video.tagColor}`}>
          {video.tag}
        </span>
        <h3 className="text-white font-bold text-base leading-snug mb-1.5 group-hover:text-[#E8913A] transition-colors">
          {video.title}
        </h3>
        <p className="text-slate-400 text-sm">{video.channel}</p>
      </div>
    </div>
  );
}

// ─── NEWS CARD ────────────────────────────────────────────────────────────────

function NewsCard({ post, featured = false }: { post: any; featured?: boolean }) {
  const catColors: Record<string, string> = {
    NW: "bg-[#C66810] text-white",
    GD: "bg-purple-600 text-white",
    IN: "bg-blue-600 text-white",
  };

  return (
    <Link href={`/news/${post.slug}`} className="group block h-full">
      <article className="h-full bg-white rounded-2xl overflow-hidden border border-slate-100 shadow-sm hover:shadow-2xl hover:border-orange-200 transition-all duration-300 hover:-translate-y-1 flex flex-col">
        {/* Image */}
        <div className={`relative overflow-hidden ${featured ? "h-64 md:h-80" : "h-48"}`}>
          {getImageUrl(post) ? (
            <Image
              src={getImageUrl(post)}
              alt={post.title}
              fill
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
              className="object-cover group-hover:scale-105 transition-transform duration-500"
            />
          ) : (
            <div className="w-full h-full bg-gradient-to-br from-orange-50 via-amber-50 to-slate-100 flex items-center justify-center">
              <span className="text-5xl opacity-15">📰</span>
            </div>
          )}
          <div className="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent" />
          <div className="absolute top-4 left-4">
            <span className={`inline-block px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest shadow-sm ${catColors[post.category] || "bg-slate-700 text-white"}`}>
              {getCategoryLabel(post.category)}
            </span>
          </div>
        </div>

        {/* Content */}
        <div className={`flex flex-col flex-grow ${featured ? "p-7" : "p-5"}`}>
          <h3 className={`font-playfair font-black text-slate-900 group-hover:text-[#C66810] transition-colors mb-3 leading-tight ${featured ? "text-2xl md:text-3xl" : "text-lg"}`}>
            {post.title}
          </h3>
          {featured && (
            <p className="text-slate-500 text-base mb-4 line-clamp-3 flex-grow leading-relaxed">
              {post.content}
            </p>
          )}
          <div className="flex items-center gap-2 text-xs text-slate-400 mt-auto pt-4 border-t border-slate-100">
            <span className="w-6 h-6 rounded-full bg-[#C66810]/15 text-[#C66810] flex items-center justify-center font-black text-[10px] flex-shrink-0">
              {post.author_name?.[0]?.toUpperCase() || "A"}
            </span>
            <span className="font-semibold text-slate-600 truncate">{post.author_name}</span>
            <span className="text-slate-300 flex-shrink-0">·</span>
            <span className="flex-shrink-0">
              {new Date(post.created_at).toLocaleDateString(undefined, {
                month: "short",
                day: "numeric",
                year: "numeric",
              })}
            </span>
          </div>
        </div>
      </article>
    </Link>
  );
}

// ─── MAIN PAGE ────────────────────────────────────────────────────────────────

export default function Home() {
  const [news, setNews] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const { data: session } = useSession();
  const isAuthenticated = !!session?.user;

  useEffect(() => {
    fetch("https://mun-global.onrender.com/api/news/", { cache: "no-store" })
      .then((res) => (res.ok ? res.json() : []))
      .then((data) => setNews(data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const tickerItems = [...TICKER, ...TICKER];

  return (
    <div className="min-h-screen bg-white">

      {/* ═══════════════════════════════════════════════════════════════════
          HERO — Dark navy editorial, serif headline
      ═══════════════════════════════════════════════════════════════════ */}
      <section className="relative overflow-hidden bg-[#070e1c] min-h-[94vh] flex flex-col">

        {/* Background radial glows */}
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_70%_-10%,#1e3a6e_0%,transparent_70%)]" />
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_60%_50%_at_0%_100%,#3d1a00_0%,transparent_60%)] opacity-70" />

        {/* Fine grid */}
        <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.025)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.025)_1px,transparent_1px)] bg-[size:80px_80px]" />

        {/* Noise grain */}
        <div
          className="absolute inset-0 opacity-[0.04] pointer-events-none"
          style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E")`,
          }}
        />

        {/* Decorative concentric rings */}
        <div className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/4 pointer-events-none hidden lg:block">
          <div className="w-[800px] h-[800px] rounded-full border border-white/[0.04]" />
          <div className="absolute inset-[80px] rounded-full border border-white/[0.05]" />
          <div className="absolute inset-[200px] rounded-full border border-white/[0.06]" />
          <div className="absolute inset-[320px] rounded-full bg-[#C66810]/5 blur-3xl" />
        </div>

        {/* Content */}
        <div className="relative z-10 flex-grow flex items-center">
          <div className="max-w-7xl mx-auto px-6 lg:px-8 py-20 w-full">
            <div className="grid lg:grid-cols-[1fr_420px] gap-16 items-center">

              {/* ── Left: Text block ── */}
              <div>
                {/* Live badge */}
                <div className="inline-flex items-center gap-2.5 px-4 py-2 rounded-full border border-[#C66810]/30 bg-[#C66810]/10 text-[#E8913A] text-sm font-bold mb-10 animate-fade-in">
                  <span className="relative flex h-2 w-2">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#C66810] opacity-75" />
                    <span className="relative inline-flex h-2 w-2 rounded-full bg-[#E8913A]" />
                  </span>
                  Live from the MUN Circuit
                </div>

                {/* Headline */}
                <h1 className="font-playfair text-[clamp(3.5rem,9vw,6.5rem)] font-black text-white leading-[0.93] tracking-tight mb-8 animate-fade-up">
                  Where<br />
                  Diplomats<br />
                  <em className="text-[#C66810] not-italic">Are Made.</em>
                </h1>

                {/* Subtitle */}
                <p className="text-slate-300 text-lg md:text-xl leading-relaxed max-w-lg mb-12 font-light animate-fade-up" style={{ animationDelay: "0.15s" }}>
                  Read breaking circuit stories, train with our personalized AI coach,
                  and master MUN through expert video — all in one place for delegates like you.
                </p>

                {/* CTAs */}
                <div className="flex flex-wrap gap-4 animate-fade-up" style={{ animationDelay: "0.3s" }}>
                  <Link
                    href="/curriculum"
                    className="group inline-flex items-center gap-3 px-8 py-4 bg-[#C66810] text-white font-bold text-base rounded-xl hover:bg-[#E8913A] transition-all duration-200 shadow-lg shadow-orange-950/50 hover:-translate-y-0.5"
                  >
                    Start Training
                    <svg className="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                    </svg>
                  </Link>
                  <Link
                    href="/news"
                    className="inline-flex items-center gap-2 px-8 py-4 bg-white/8 text-white font-bold text-base rounded-xl border border-white/15 hover:bg-white/15 hover:border-white/25 transition-all duration-200 backdrop-blur-sm"
                  >
                    Read the News
                  </Link>
                </div>
              </div>

              {/* ── Right: Feature preview cards ── */}
              <div className="hidden lg:flex flex-col gap-4 animate-fade-up" style={{ animationDelay: "0.2s" }}>

                {/* Stats row */}
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-white/[0.04] border border-white/10 rounded-2xl p-5 backdrop-blur-sm hover:bg-white/[0.07] transition-colors">
                    <p className="font-playfair text-[#E8913A] text-3xl font-black mb-1">∞</p>
                    <p className="text-slate-400 text-xs font-medium leading-snug">Articles &amp; Stories from the Circuit</p>
                  </div>
                  <div className="bg-white/[0.04] border border-white/10 rounded-2xl p-5 backdrop-blur-sm hover:bg-white/[0.07] transition-colors">
                    <p className="font-playfair text-[#E8913A] text-3xl font-black mb-1">AI</p>
                    <p className="text-slate-400 text-xs font-medium leading-snug">Personalized Curriculum Engine</p>
                  </div>
                </div>

                {/* DiplomAI preview card */}
                <div className="bg-white/[0.04] border border-white/10 rounded-2xl p-5 backdrop-blur-sm hover:bg-white/[0.07] transition-colors">
                  <div className="flex items-center gap-3 mb-4">
                    <div className="w-9 h-9 rounded-xl bg-[#C66810]/20 border border-[#C66810]/30 flex items-center justify-center">
                      <Image src="/MunKey Main Logo.png" alt="Bongo" width={22} height={22} className="object-contain" />
                    </div>
                    <div className="flex-grow">
                      <p className="text-white font-bold text-sm">DiplomAI — Bongo</p>
                      <p className="text-slate-400 text-xs">Your personal MUN coach</p>
                    </div>
                    <span className="text-[10px] font-bold text-emerald-400 bg-emerald-900/50 border border-emerald-800/50 px-2 py-0.5 rounded-full">LIVE</span>
                  </div>
                  <div className="space-y-2">
                    <div className="bg-white/[0.05] rounded-xl p-3 text-slate-400 text-sm leading-relaxed">
                      &ldquo;Help me open my UNSC speech on climate displacement...&rdquo;
                    </div>
                    <div className="bg-[#C66810]/12 border border-[#C66810]/20 rounded-xl p-3 text-[#E8913A] text-sm leading-relaxed ml-3">
                      Here&rsquo;s a powerful opening that links climate data to national security...
                    </div>
                  </div>
                </div>

                {/* Video pill */}
                <Link
                  href="#learn"
                  className="group bg-white/[0.04] border border-white/10 rounded-2xl p-5 backdrop-blur-sm hover:bg-white/[0.07] hover:border-red-800/40 transition-all duration-200 flex items-center gap-4"
                >
                  <div className="w-11 h-11 rounded-xl bg-red-900/30 border border-red-800/30 flex items-center justify-center flex-shrink-0">
                    <svg className="w-5 h-5 text-red-400" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M21.582 6.186a2.506 2.506 0 00-1.765-1.77C18.254 4 12 4 12 4s-6.254 0-7.817.416a2.506 2.506 0 00-1.765 1.77C2 7.747 2 12 2 12s0 4.253.418 5.814a2.506 2.506 0 001.765 1.77C5.746 20 12 20 12 20s6.254 0 7.817-.416a2.506 2.506 0 001.765-1.77C22 16.253 22 12 22 12s0-4.253-.418-5.814zM10 15.464V8.536L16 12l-6 3.464z" />
                    </svg>
                  </div>
                  <div>
                    <p className="text-white font-bold text-sm">Video Learning Library</p>
                    <p className="text-slate-400 text-xs">Curated MUN masterclasses</p>
                  </div>
                  <svg
                    className="w-4 h-4 text-slate-500 ml-auto group-hover:translate-x-1 group-hover:text-red-400 transition-all"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24"
                  >
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </Link>

              </div>
            </div>
          </div>
        </div>

        {/* Bottom edge line */}
        <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-white/10 to-transparent" />
      </section>

      {/* ═══════════════════════════════════════════════════════════════════
          TICKER — Orange scrolling banner
      ═══════════════════════════════════════════════════════════════════ */}
      <div className="bg-[#C66810] py-3 overflow-hidden border-b border-orange-700 select-none">
        <div className="flex whitespace-nowrap animate-ticker">
          {tickerItems.map((item, i) => (
            <span key={i} className="inline-flex items-center">
              <span className="text-white text-sm font-semibold tracking-wide px-10">{item}</span>
              <span className="text-orange-200/50 text-xs">◆</span>
            </span>
          ))}
        </div>
      </div>

      {/* ═══════════════════════════════════════════════════════════════════
          THREE PILLARS
      ═══════════════════════════════════════════════════════════════════ */}
      <section className="bg-white py-28 border-b border-slate-100">
        <div className="max-w-7xl mx-auto px-6 lg:px-8">
          <div className="text-center mb-16">
            <p className="text-[#C66810] text-xs font-black uppercase tracking-[0.35em] mb-4">The Platform</p>
            <h2 className="font-playfair text-4xl md:text-5xl font-black text-slate-900 leading-tight">
              Everything you need to<br />
              <em className="text-[#C66810]">dominate the chamber.</em>
            </h2>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: "📰",
                label: "News & Stories",
                tagline: "The Circuit's Voice",
                desc: "Read breaking conference news, personal delegate stories, preparation guides, and interviews from across the global MUN world.",
                href: "/news",
                linkText: "Browse stories",
                bg: "from-orange-50 to-amber-50/60",
                iconBg: "bg-orange-100 text-orange-700",
                border: "border-slate-200 hover:border-orange-300",
                dark: false,
              },
              {
                icon: "🤖",
                label: "DiplomAI",
                tagline: "Your AI MUN Coach",
                desc: "Train with Bongo — our AI strategist that gives personalized speech feedback, resolution drafting help, and debate strategy tailored to you.",
                href: "/curriculum",
                linkText: "Meet DiplomAI",
                bg: "from-slate-900 to-[#0a1628]",
                iconBg: "bg-[#C66810]/20 text-[#E8913A]",
                border: "border-slate-800 hover:border-slate-600",
                dark: true,
              },
              {
                icon: "🎥",
                label: "Video Learning",
                tagline: "Watch & Master",
                desc: "Sharpen your skills through curated YouTube masterclasses — from writing position papers to crisis committee tactics and advanced speech technique.",
                href: "#learn",
                linkText: "Watch now",
                bg: "from-red-50 to-rose-50/60",
                iconBg: "bg-red-100 text-red-700",
                border: "border-slate-200 hover:border-red-300",
                dark: false,
              },
            ].map((pillar) => (
              <div
                key={pillar.label}
                className={`group relative rounded-2xl bg-gradient-to-br ${pillar.bg} border ${pillar.border} p-8 transition-all duration-300 hover:shadow-2xl hover:-translate-y-1`}
              >
                <div className={`w-14 h-14 rounded-2xl ${pillar.iconBg} flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform duration-200`}>
                  {pillar.icon}
                </div>
                <p className={`text-xs font-black uppercase tracking-widest mb-2 ${pillar.dark ? "text-slate-500" : "text-slate-400"}`}>
                  {pillar.label}
                </p>
                <h3 className={`font-playfair text-2xl font-bold mb-4 leading-tight ${pillar.dark ? "text-white" : "text-slate-900"}`}>
                  {pillar.tagline}
                </h3>
                <p className={`leading-relaxed mb-8 text-sm ${pillar.dark ? "text-slate-400" : "text-slate-600"}`}>
                  {pillar.desc}
                </p>
                <Link
                  href={pillar.href}
                  className={`inline-flex items-center gap-2 text-sm font-bold transition-colors ${pillar.dark ? "text-[#E8913A] hover:text-[#C66810]" : "text-[#C66810] hover:text-[#A05200]"}`}
                >
                  {pillar.linkText}
                  <svg className="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                  </svg>
                </Link>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════════════
          LATEST NEWS
      ═══════════════════════════════════════════════════════════════════ */}
      <section className="bg-slate-50 py-28 border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-6 lg:px-8">

          <div className="flex items-end justify-between mb-14">
            <div>
              <p className="text-[#C66810] text-xs font-black uppercase tracking-[0.35em] mb-3">From the Circuit</p>
              <h2 className="font-playfair text-4xl md:text-5xl font-black text-slate-900">Latest Stories</h2>
            </div>
            <Link
              href="/news"
              className="hidden md:inline-flex items-center gap-2 px-5 py-2.5 bg-white border border-slate-200 rounded-xl text-sm font-bold text-slate-700 hover:border-[#C66810] hover:text-[#C66810] transition-all duration-200 shadow-sm"
            >
              All stories
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </Link>
          </div>

          {/* Loading */}
          {loading && (
            <div className="grid md:grid-cols-12 gap-6 animate-pulse">
              <div className="md:col-span-7 bg-white rounded-2xl h-96 border border-slate-200" />
              <div className="md:col-span-5 grid grid-rows-2 gap-6">
                <div className="bg-white rounded-2xl border border-slate-200" />
                <div className="bg-white rounded-2xl border border-slate-200" />
              </div>
            </div>
          )}

          {/* Empty */}
          {!loading && news.length === 0 && (
            <div className="bg-white rounded-2xl p-20 text-center border border-slate-200 shadow-sm">
              <p className="text-5xl mb-5 opacity-20">📰</p>
              <h3 className="font-playfair text-2xl font-bold text-slate-700 mb-2">No stories yet</h3>
              <p className="text-slate-500 mb-8">Be the first delegate to share with the community.</p>
              <Link
                href={isAuthenticated ? "/news/add" : "/login"}
                className="inline-block px-7 py-3 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors"
              >
                {isAuthenticated ? "Submit a Story" : "Login to Submit"}
              </Link>
            </div>
          )}

          {/* News grid */}
          {!loading && news.length > 0 && (
            <>
              <div className="grid md:grid-cols-12 gap-6 mb-6">
                {news[0] && (
                  <div className="md:col-span-7 h-full">
                    <NewsCard post={news[0]} featured />
                  </div>
                )}
                <div className="md:col-span-5 grid grid-rows-2 gap-6">
                  {news[1] && <NewsCard post={news[1]} />}
                  {news[2] && <NewsCard post={news[2]} />}
                </div>
              </div>

              {news.length > 3 && (
                <div className="grid md:grid-cols-3 gap-6">
                  {news.slice(3, 6).map((post) => (
                    <NewsCard key={post.id} post={post} />
                  ))}
                </div>
              )}

              <div className="mt-10 text-center md:hidden">
                <Link
                  href="/news"
                  className="inline-flex items-center gap-2 px-6 py-3 bg-white border border-slate-200 rounded-xl text-sm font-bold text-slate-700 hover:border-[#C66810] hover:text-[#C66810] transition-all duration-200 shadow-sm"
                >
                  View all stories →
                </Link>
              </div>
            </>
          )}
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════════════
          DIPLOMAI SPOTLIGHT
      ═══════════════════════════════════════════════════════════════════ */}
      <section className="relative bg-[#070e1c] py-28 overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_70%_60%_at_0%_50%,#1a3a6b_0%,transparent_60%)] opacity-60" />
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-[#C66810]/8 rounded-full blur-3xl" />
        <div className="absolute bottom-0 left-1/3 w-64 h-64 bg-blue-700/10 rounded-full blur-3xl" />
        <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:60px_60px]" />

        <div className="max-w-7xl mx-auto px-6 lg:px-8 relative z-10">
          <div className="grid lg:grid-cols-2 gap-16 items-center">

            {/* Text */}
            <div>
              <div className="inline-flex items-center gap-2 mb-8 px-4 py-2 rounded-full border border-[#C66810]/30 bg-[#C66810]/10">
                <span className="text-xs font-black uppercase tracking-[0.25em] text-[#E8913A]">DiplomAI</span>
              </div>
              <h2 className="font-playfair text-4xl md:text-5xl xl:text-6xl font-black text-white leading-tight mb-6">
                Meet<br />
                <span className="text-[#C66810]">Bongo.</span><br />
                Your AI Coach.
              </h2>
              <p className="text-slate-300 text-lg leading-relaxed mb-8 max-w-md">
                Practice speeches, draft resolutions, and get instant personalized feedback from Bongo —
                your AI strategist trained to help delegates at every level excel.
              </p>
              <div className="flex flex-wrap gap-3 mb-10">
                {["Speech Coaching", "Resolution Help", "Crisis Strategy", "Personal Feedback"].map((tag) => (
                  <span key={tag} className="px-4 py-1.5 bg-white/5 border border-white/10 rounded-full text-sm text-slate-300 font-medium">
                    {tag}
                  </span>
                ))}
              </div>
              <Link
                href="/curriculum"
                className="inline-flex items-center gap-3 px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#E8913A] transition-all duration-200 shadow-lg shadow-orange-950/40 hover:-translate-y-0.5"
              >
                Train with Bongo
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                </svg>
              </Link>
            </div>

            {/* Chat UI mockup */}
            <div className="relative">
              <div className="bg-white/[0.04] border border-white/10 rounded-2xl p-6 backdrop-blur-sm shadow-2xl">
                {/* Header */}
                <div className="flex items-center gap-3 mb-6 pb-5 border-b border-white/[0.08]">
                  <div className="relative">
                    <div className="w-10 h-10 rounded-full bg-[#C66810]/20 border border-[#C66810]/30 flex items-center justify-center">
                      <Image src="/MunKey Main Logo.png" alt="Bongo" width={24} height={24} className="object-contain" />
                    </div>
                    <span className="absolute -bottom-0.5 -right-0.5 w-3 h-3 bg-emerald-400 rounded-full border-2 border-[#070e1c]" />
                  </div>
                  <div>
                    <p className="text-white font-bold text-sm">Bongo</p>
                    <p className="text-emerald-400 text-xs font-medium">Online · ready to coach</p>
                  </div>
                  <div className="ml-auto flex gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-white/10" />
                    <span className="w-2.5 h-2.5 rounded-full bg-white/10" />
                    <span className="w-2.5 h-2.5 rounded-full bg-white/10" />
                  </div>
                </div>

                {/* Messages */}
                <div className="space-y-4 mb-6">
                  <div className="flex gap-3 items-start">
                    <div className="w-7 h-7 rounded-full bg-[#C66810]/20 flex-shrink-0 flex items-center justify-center text-[11px] mt-0.5">🤖</div>
                    <div className="bg-white/[0.06] rounded-2xl rounded-tl-sm px-4 py-3 text-slate-300 text-sm leading-relaxed max-w-[82%]">
                      Welcome! I&rsquo;m Bongo. Tell me what committee you&rsquo;re in and I&rsquo;ll help you prepare a powerful speech.
                    </div>
                  </div>
                  <div className="flex gap-3 items-start flex-row-reverse">
                    <div className="w-7 h-7 rounded-full bg-slate-700 flex-shrink-0 flex items-center justify-center text-[11px] mt-0.5">👤</div>
                    <div className="bg-[#C66810]/20 border border-[#C66810]/25 rounded-2xl rounded-tr-sm px-4 py-3 text-[#E8913A] text-sm leading-relaxed max-w-[82%]">
                      UNSC debate on climate displacement — I need an opening speech
                    </div>
                  </div>
                  <div className="flex gap-3 items-start">
                    <div className="w-7 h-7 rounded-full bg-[#C66810]/20 flex-shrink-0 flex items-center justify-center text-[11px] mt-0.5">🤖</div>
                    <div className="bg-white/[0.06] rounded-2xl rounded-tl-sm px-4 py-3 text-slate-300 text-sm leading-relaxed max-w-[82%]">
                      Great topic. Let&rsquo;s open with a hook that links climate data to national security threats — here&rsquo;s your first paragraph...
                    </div>
                  </div>
                </div>

                {/* Input */}
                <div className="flex gap-3 items-center bg-white/[0.04] border border-white/10 rounded-xl px-4 py-3">
                  <span className="text-slate-500 text-sm flex-grow">Ask Bongo anything about MUN...</span>
                  <div className="w-8 h-8 rounded-lg bg-[#C66810] flex items-center justify-center flex-shrink-0">
                    <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                    </svg>
                  </div>
                </div>
              </div>
              <div className="absolute -inset-6 bg-[#C66810]/5 rounded-3xl blur-2xl -z-10" />
            </div>

          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════════════
          YOUTUBE LEARNING
      ═══════════════════════════════════════════════════════════════════ */}
      <section id="learn" className="bg-slate-900 py-28">
        <div className="max-w-7xl mx-auto px-6 lg:px-8">

          <div className="flex items-end justify-between mb-14">
            <div>
              <p className="text-[#C66810] text-xs font-black uppercase tracking-[0.35em] mb-3">Video Library</p>
              <h2 className="font-playfair text-4xl md:text-5xl font-black text-white">Learn by Watching</h2>
            </div>
            <div className="hidden md:flex items-center gap-2 text-slate-400 text-sm font-medium">
              <svg className="w-5 h-5 text-red-500" fill="currentColor" viewBox="0 0 24 24">
                <path d="M21.582 6.186a2.506 2.506 0 00-1.765-1.77C18.254 4 12 4 12 4s-6.254 0-7.817.416a2.506 2.506 0 00-1.765 1.77C2 7.747 2 12 2 12s0 4.253.418 5.814a2.506 2.506 0 001.765 1.77C5.746 20 12 20 12 20s6.254 0 7.817-.416a2.506 2.506 0 001.765-1.77C22 16.253 22 12 22 12s0-4.253-.418-5.814zM10 15.464V8.536L16 12l-6 3.464z" />
              </svg>
              Curated MUN Masterclasses
            </div>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {FEATURED_VIDEOS.map((video) => (
              <VideoCard key={video.id + video.title} video={video} />
            ))}
          </div>

          <p className="text-slate-600 text-xs text-center mt-8">
            Update <code className="text-slate-500 bg-slate-800 px-1.5 py-0.5 rounded">FEATURED_VIDEOS</code> in{" "}
            <code className="text-slate-500 bg-slate-800 px-1.5 py-0.5 rounded">page.tsx</code> with real YouTube video IDs.
          </p>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════════════
          FINAL CTA
      ═══════════════════════════════════════════════════════════════════ */}
      <section className="bg-white py-28 border-t border-slate-100">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <div className="mb-8">
            <Image src="/MunKey Main Logo.png" alt="MunKey" width={60} height={60} className="mx-auto" />
          </div>
          <h2 className="font-playfair text-4xl md:text-6xl font-black text-slate-900 leading-tight mb-6">
            Ready to step<br />
            <em className="text-[#C66810]">into the chamber?</em>
          </h2>
          <p className="text-slate-500 text-lg md:text-xl max-w-xl mx-auto mb-12 leading-relaxed">
            Join MunKey — read the news, train with DiplomAI, and build the skills every elite delegate needs. It&rsquo;s free.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            {isAuthenticated ? (
              <>
                <Link href="/curriculum" className="px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors shadow-lg shadow-orange-100">
                  Open DiplomAI →
                </Link>
                <Link href="/news" className="px-8 py-4 bg-slate-100 text-slate-700 font-bold rounded-xl hover:bg-slate-200 transition-colors">
                  Browse News
                </Link>
              </>
            ) : (
              <>
                <Link href="/signup" className="px-8 py-4 bg-[#C66810] text-white font-bold rounded-xl hover:bg-[#A05200] transition-colors shadow-lg shadow-orange-100">
                  Join Free →
                </Link>
                <Link href="/login" className="px-8 py-4 bg-slate-100 text-slate-700 font-bold rounded-xl hover:bg-slate-200 transition-colors">
                  Login
                </Link>
              </>
            )}
          </div>
        </div>
      </section>

    </div>
  );
}
