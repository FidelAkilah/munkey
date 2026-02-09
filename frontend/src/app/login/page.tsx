"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { signIn, useSession } from "next-auth/react";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isCheckingSession, setIsCheckingSession] = useState(true);
  const router = useRouter();
  const { data: session, status } = useSession();

  // Check session and redirect if already authenticated
  useEffect(() => {
    const checkSession = async () => {
      // Wait a bit for session to initialize
      await new Promise(resolve => setTimeout(resolve, 100));
      setIsCheckingSession(false);
      
      // Redirect if already logged in
      if (status === "authenticated" && session?.user) {
        router.replace("/news/add");
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
        // Use direct navigation instead of router to avoid issues
        window.location.href = "/news/add";
      }
    } catch (err) {
      setIsSubmitting(false);
      setError("An error occurred. Please try again.");
    }
  };

  // Show loading while checking session
  if (isCheckingSession || status === "loading") {
    return (
      <div className="flex items-center justify-center min-h-screen bg-slate-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-slate-600">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-slate-50">
      <form onSubmit={handleLogin} className="bg-white p-10 rounded-3xl shadow-xl w-96 border">
        <h1 className="text-2xl font-bold mb-6 text-center">Delegate Login</h1>
        
        {error && (
          <div className="mb-4 p-3 bg-red-50 text-red-600 text-sm rounded-lg">
            {error}
          </div>
        )}
        
        <input 
          type="text"
          placeholder="Username" 
          className="w-full p-4 mb-4 bg-slate-100 rounded-xl"
          value={username}
          onChange={(e) => setUsername(e.target.value)} 
          required
        />
        <input 
          type="password" 
          placeholder="Password" 
          className="w-full p-4 mb-6 bg-slate-100 rounded-xl"
          value={password}
          onChange={(e) => setPassword(e.target.value)} 
          required
        />
        <button 
          type="submit"
          disabled={isSubmitting}
          className="w-full bg-blue-600 text-white p-4 rounded-xl font-bold hover:bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isSubmitting ? "Signing in..." : "Sign In"}
        </button>
        <p className="text-center mt-6 text-slate-500 text-sm">
            Don&apos;t have an account? <Link href="/signup" className="text-blue-600 font-bold">Sign up here</Link>
        </p>
      </form>
    </div>
  );
}
