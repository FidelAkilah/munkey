import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-slate-900 text-white">
      <div className="max-w-5xl mx-auto px-6 py-10">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <Link href="/" className="text-xl font-black tracking-tight">
              MUN<span className="text-[#C66810]">KEY</span>
            </Link>
            <p className="text-slate-400 text-xs mt-2 leading-relaxed">
              Empowering MUN delegates worldwide with news, skills, and AI-powered practice tools.
            </p>
          </div>
          <div>
            <h3 className="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-3">Explore</h3>
            <div className="flex flex-col gap-1.5">
              <Link href="/news" className="text-sm text-slate-400 hover:text-[#C66810] transition-colors">News</Link>
              <Link href="/skills" className="text-sm text-slate-400 hover:text-[#C66810] transition-colors">Skills</Link>
              <Link href="/curriculum" className="text-sm text-slate-400 hover:text-[#C66810] transition-colors">DiplomAI</Link>
            </div>
          </div>
          <div>
            <h3 className="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-3">Account</h3>
            <div className="flex flex-col gap-1.5">
              <Link href="/login" className="text-sm text-slate-400 hover:text-[#C66810] transition-colors">Log In</Link>
              <Link href="/signup" className="text-sm text-slate-400 hover:text-[#C66810] transition-colors">Sign Up</Link>
            </div>
          </div>
        </div>
        <div className="border-t border-slate-800 mt-8 pt-6 flex flex-col md:flex-row items-center justify-between gap-3">
          <p className="text-xs text-slate-500">&copy; {new Date().getFullYear()} MUNKEY. All rights reserved.</p>
          <p className="text-xs text-slate-600">
            Built with <span className="text-[#C66810]">&#9829;</span> for the MUN community
          </p>
        </div>
      </div>
    </footer>
  );
}
