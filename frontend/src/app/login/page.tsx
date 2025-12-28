
"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/auth/jwt/create/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (res.ok) {
      const data = await res.json();
      // Store token in a cookie for the Next.js 16 Proxy to see
      document.cookie = `session_token=${data.access}; path=/; max-age=3600; SameSite=Lax`;
      router.push("/news/add");
      router.refresh();
    } else {
      alert("Invalid MUN Credentials.");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-slate-50">
      <form onSubmit={handleLogin} className="bg-white p-10 rounded-3xl shadow-xl w-96 border">
        <h1 className="text-2xl font-bold mb-6 text-center">Delegate Login</h1>
        <input 
          type="text" // Change from email to text
          placeholder="Username" 
          className="w-full p-4 mb-4 bg-slate-100 rounded-xl"
          onChange={(e) => setUsername(e.target.value)} 
        />
        <input 
          type="password" placeholder="Password" 
          className="w-full p-4 mb-6 bg-slate-100 rounded-xl"
          onChange={(e) => setPassword(e.target.value)} 
        />
        <button className="w-full bg-blue-600 text-white p-4 rounded-xl font-bold">Sign In</button>
        <p className="text-center mt-6 text-slate-500 text-sm">
            Don&apos;t have an account? <Link href="/signup" className="text-blue-600 font-bold">Sign up here</Link>
        </p>
      </form>
      
    </div>
  );
}