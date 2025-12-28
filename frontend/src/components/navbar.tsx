// src/components/Navbar.tsx
import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        {/* Logo */}
        <Link href="/" className="text-2xl font-black tracking-tighter text-blue-600">
          MUN<span className="text-slate-900">GLOBAL</span>
        </Link>

        {/* Links */}
        <div className="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-600">
          <Link href="/" className="hover:text-blue-600 transition">News</Link>
          <Link href="/conferences" className="hover:text-blue-600 transition">Conferences</Link>
          <Link href="/news/add" className="bg-blue-600 text-white px-5 py-2.5 rounded-full hover:bg-blue-700 transition shadow-lg shadow-blue-200">
            + Add News
          </Link>
        </div>

        {/* Profile */}
        <Link href="/profile" className="flex items-center gap-3 group">
          <div className="text-right hidden sm:block">
            <p className="text-xs font-bold text-slate-900">Fidel Akilah</p>
            <p className="text-[10px] text-slate-500">Senior Delegate</p>
          </div>
          <div className="w-10 h-10 rounded-full bg-slate-200 border-2 border-white shadow-sm overflow-hidden group-hover:border-blue-400 transition-all" />
        </Link>
      </div>
    </nav>
  );
}