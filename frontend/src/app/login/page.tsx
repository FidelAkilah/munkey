"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { signIn, useSession } from "next-auth/react";
import { motion } from "framer-motion";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isCheckingSession, setIsCheckingSession] = useState(true);
  const router = useRouter();
  const { data: session, status } = useSession();

  useEffect(() => {
    const checkSession = async () => {
      await new Promise(resolve => setTimeout(resolve, 100));
      setIsCheckingSession(false);
      if (status === "authenticated" && session?.user) {
        const params = new URLSearchParams(window.location.search);
        const callbackUrl = params.get("callbackUrl") || "/";
        router.replace(callbackUrl);
      }
    };
    checkSession();
  }, [status, session, router]);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError("");
    try {
      const result = await signIn("credentials", {
        username,
        password,
        redirect: false,
      });
      if (result?.error) {
        setError("Invalid username or password");
        setIsSubmitting(false);
      } else {
        const params = new URLSearchParams(window.location.search);
        const callbackUrl = params.get("callbackUrl") || "/";
        window.location.href = callbackUrl;
      }
    } catch {
      setIsSubmitting(false);
      setError("An error occurred. Please try again.");
    }
  };

  if (isCheckingSession || status === "loading") {
    return (
      <div className="flex items-center justify-center min-h-screen bg-[#070e1c]">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-2 border-[#C66810] border-t-transparent mx-auto mb-4" />
          <p className="text-slate-400">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex">
      {/* Left panel — brand */}
      <div className="hidden lg:flex lg:w-1/2 relative bg-[#070e1c] overflow-hidden items-center justify-center">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_40%,#1e3a6e_0%,transparent_70%)]" />
        <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.025)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.025)_1px,transparent_1px)] bg-[size:60px_60px]" />
        <div className="absolute inset-0 grain" />

        {/* Decorative circles */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] rounded-full border border-white/[0.05]" />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[350px] h-[350px] rounded-full border border-white/[0.06]" />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[200px] h-[200px] rounded-full bg-[#C66810]/10 blur-3xl" />

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="relative z-10 text-center px-12"
        >
          <Image src="/MunKey Main Logo.png" alt="MunKey" width={64} height={64} className="mx-auto mb-8" />
          <h1 className="font-playfair text-5xl font-black text-white leading-tight mb-4">
            Welcome back,<br />
            <span className="text-[#C66810]">Delegate.</span>
          </h1>
          <p className="text-slate-400 text-lg max-w-sm mx-auto leading-relaxed">
            Sign in to access your DiplomAI training, submit stories, and track your MUN journey.
          </p>
        </motion.div>
      </div>

      {/* Right panel — form */}
      <div className="flex-1 flex items-center justify-center bg-white px-6 py-12">
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          className="w-full max-w-md"
        >
          {/* Mobile brand */}
          <div className="lg:hidden text-center mb-10">
            <Image src="/MunKey Main Logo.png" alt="MunKey" width={48} height={48} className="mx-auto mb-4" />
            <h1 className="font-playfair text-3xl font-black text-slate-900">
              Delegate <span className="text-[#C66810]">Login</span>
            </h1>
          </div>

          <div className="hidden lg:block mb-10">
            <h2 className="font-playfair text-3xl font-black text-slate-900 mb-2">Sign In</h2>
            <p className="text-slate-500">Enter your credentials to continue</p>
          </div>

          {error && (
            <motion.div
              initial={{ opacity: 0, y: -8 }}
              animate={{ opacity: 1, y: 0 }}
              className="mb-6 p-4 bg-red-50 text-red-600 text-sm rounded-xl border border-red-100 font-medium"
            >
              {error}
            </motion.div>
          )}

          <form onSubmit={handleLogin} className="space-y-5">
            <div>
              <label className="block text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">Username</label>
              <input
                type="text"
                placeholder="Enter your username"
                className="w-full p-4 bg-slate-50 rounded-xl border border-slate-200 text-slate-900 font-medium focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] transition-all outline-none"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div>
              <label className="block text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">Password</label>
              <input
                type="password"
                placeholder="Enter your password"
                className="w-full p-4 bg-slate-50 rounded-xl border border-slate-200 text-slate-900 font-medium focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] transition-all outline-none"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full bg-[#C66810] text-white p-4 rounded-xl font-bold text-base hover:bg-[#A05200] disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 shadow-lg shadow-orange-200 hover:shadow-xl hover:-translate-y-0.5"
            >
              {isSubmitting ? "Signing in..." : "Sign In"}
            </button>
          </form>

          <p className="text-center mt-8 text-slate-500 text-sm">
            Don&apos;t have an account?{" "}
            <Link href="/signup" className="text-[#C66810] font-bold hover:text-[#A05200] transition-colors">
              Sign up here
            </Link>
          </p>
        </motion.div>
      </div>
    </div>
  );
}
