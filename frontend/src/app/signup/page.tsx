"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { motion } from "framer-motion";

export default function SignupPage() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    re_password: "",
    role: "SR",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState("");
  const router = useRouter();

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError("");

    const res = await fetch("https://mun-global.onrender.com/auth/users/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    if (res.ok) {
      alert("Account created! You can now log in.");
      router.push("/login");
    } else {
      const errorData = await res.json();
      setError(JSON.stringify(errorData));
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen flex">
      {/* Left panel — brand */}
      <div className="hidden lg:flex lg:w-1/2 relative bg-[#070e1c] overflow-hidden items-center justify-center">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_40%,#1e3a6e_0%,transparent_70%)]" />
        <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.025)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.025)_1px,transparent_1px)] bg-[size:60px_60px]" />
        <div className="absolute inset-0 grain" />

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
            Join the<br />
            <span className="text-[#C66810]">Circuit.</span>
          </h1>
          <p className="text-slate-400 text-lg max-w-sm mx-auto leading-relaxed">
            Create your delegate account to access AI training, share stories, and connect with the MUN community.
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
          <div className="lg:hidden text-center mb-10">
            <Image src="/MunKey Main Logo.png" alt="MunKey" width={48} height={48} className="mx-auto mb-4" />
            <h1 className="font-playfair text-3xl font-black text-slate-900">
              Join the <span className="text-[#C66810]">Circuit</span>
            </h1>
          </div>

          <div className="hidden lg:block mb-10">
            <h2 className="font-playfair text-3xl font-black text-slate-900 mb-2">Create Account</h2>
            <p className="text-slate-500">Set up your delegate profile</p>
          </div>

          {error && (
            <motion.div
              initial={{ opacity: 0, y: -8 }}
              animate={{ opacity: 1, y: 0 }}
              className="mb-6 p-4 bg-red-50 text-red-600 text-sm rounded-xl border border-red-100 font-medium break-all"
            >
              {error}
            </motion.div>
          )}

          <form onSubmit={handleSignup} className="space-y-4">
            <div>
              <label className="block text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">Username</label>
              <input
                type="text"
                placeholder="Choose a username"
                required
                className="w-full p-4 bg-slate-50 rounded-xl border border-slate-200 text-slate-900 font-medium focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] transition-all outline-none"
                onChange={(e) => setFormData({ ...formData, username: e.target.value })}
              />
            </div>
            <div>
              <label className="block text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">Email Address</label>
              <input
                type="email"
                placeholder="your@email.com"
                required
                className="w-full p-4 bg-slate-50 rounded-xl border border-slate-200 text-slate-900 font-medium focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] transition-all outline-none"
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              />
            </div>
            <div>
              <label className="block text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">Delegate Level</label>
              <select
                className="w-full p-4 bg-slate-50 rounded-xl border border-slate-200 text-slate-900 font-medium focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] transition-all outline-none"
                onChange={(e) => setFormData({ ...formData, role: e.target.value })}
              >
                <option value="SR">Senior Delegate (HS/Univ)</option>
                <option value="JR">Junior Delegate (Elem/JH)</option>
              </select>
            </div>
            <div>
              <label className="block text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">Password</label>
              <input
                type="password"
                placeholder="Create a password"
                required
                className="w-full p-4 bg-slate-50 rounded-xl border border-slate-200 text-slate-900 font-medium focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] transition-all outline-none"
                onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              />
            </div>
            <div>
              <label className="block text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">Confirm Password</label>
              <input
                type="password"
                placeholder="Re-enter your password"
                required
                className="w-full p-4 bg-slate-50 rounded-xl border border-slate-200 text-slate-900 font-medium focus:ring-2 focus:ring-[#C66810]/30 focus:border-[#C66810] transition-all outline-none"
                onChange={(e) => setFormData({ ...formData, re_password: e.target.value })}
              />
            </div>
            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full bg-[#C66810] text-white p-4 rounded-xl font-bold text-base hover:bg-[#A05200] disabled:opacity-50 transition-all duration-200 shadow-lg shadow-orange-200 hover:shadow-xl hover:-translate-y-0.5"
            >
              {isSubmitting ? "Creating Account..." : "Create Account"}
            </button>
          </form>

          <p className="text-center mt-8 text-slate-500 text-sm">
            Already have an account?{" "}
            <Link href="/login" className="text-[#C66810] font-bold hover:text-[#A05200] transition-colors">
              Sign in here
            </Link>
          </p>
        </motion.div>
      </div>
    </div>
  );
}
