import Link from "next/link";
import Image from "next/image";

export default function Footer() {
  return (
    <footer className="bg-white border-t border-slate-200">
      <div className="max-w-7xl mx-auto px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          
          <div className="md:col-span-2 space-y-4">
            <Link href="/" className="flex items-center gap-2">
              <Image 
                src="/MunKey Main Logo.png" 
                alt="MUNKEY Logo" 
                width={32} 
                height={32} 
                className="w-8 h-8 object-contain"
              />
              <span className="text-xl font-black tracking-tight text-slate-900">
                MUN<span className="text-[#C66810]">KEY</span>
              </span>
            </Link>
            <p className="text-slate-500 text-sm leading-relaxed max-w-sm">
              Empowering Model UN delegates worldwide with breaking news, skill-sharing resources, and AI-powered practice simulation tools.
            </p>
          </div>
          
          <div>
            <h3 className="text-xs font-bold uppercase tracking-widest text-slate-900 mb-4">Explore</h3>
            <div className="flex flex-col gap-3">
              <Link href="/news" className="text-sm text-slate-500 hover:text-[#C66810] transition-colors">News</Link>
              <Link href="/skills" className="text-sm text-slate-500 hover:text-[#C66810] transition-colors">Skill Sharing</Link>
              <Link href="/curriculum" className="text-sm text-slate-500 hover:text-[#C66810] transition-colors">DiplomAI</Link>
            </div>
          </div>
          
          <div>
            <h3 className="text-xs font-bold uppercase tracking-widest text-slate-900 mb-4">Account</h3>
            <div className="flex flex-col gap-3">
              <Link href="/login" className="text-sm text-slate-500 hover:text-[#C66810] transition-colors">Log In</Link>
              <Link href="/signup" className="text-sm text-slate-500 hover:text-[#C66810] transition-colors">Sign Up</Link>
            </div>
          </div>
        </div>
        
        <div className="border-t border-slate-100 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
          <p className="text-xs text-slate-400">&copy; {new Date().getFullYear()} MUNKEY. All rights reserved.</p>
          <div className="flex items-center gap-1 text-xs text-slate-500">
            <span>Built for the MUN community</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
