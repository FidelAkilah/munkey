"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function SignupPage() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    re_password: "", // Djoser requires password re-type
    role: "SR",
  });
  const router = useRouter();

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    
    const res = await fetch("http://localhost:8000/auth/users/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    if (res.ok) {
      alert("Account created! You can now log in.");
      router.push("/login");
    } else {
      const errorData = await res.json();
      alert("Error: " + JSON.stringify(errorData));
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-slate-50">
      <form onSubmit={handleSignup} className="bg-white p-10 rounded-3xl shadow-xl w-96 border">
        <h1 className="text-2xl font-bold mb-6 text-center">Join the Circuit</h1>
        
        <input 
          type="text" placeholder="Username" required
          className="w-full p-4 mb-4 bg-slate-100 rounded-xl"
          onChange={(e) => setFormData({...formData, username: e.target.value})} 
        />
        
        <input 
          type="email" placeholder="Email Address" required
          className="w-full p-4 mb-4 bg-slate-100 rounded-xl"
          onChange={(e) => setFormData({...formData, email: e.target.value})} 
        />
        
        <select 
          className="w-full p-4 mb-4 bg-slate-100 rounded-xl"
          onChange={(e) => setFormData({...formData, role: e.target.value})}
        >
          <option value="SR">Senior Delegate (HS/Univ)</option>
          <option value="JR">Junior Delegate (Elem/JH)</option>
        </select>

        <input 
          type="password" placeholder="Password" required
          className="w-full p-4 mb-4 bg-slate-100 rounded-xl"
          onChange={(e) => setFormData({...formData, password: e.target.value})} 
        />
        
        <input 
          type="password" placeholder="Confirm Password" required
          className="w-full p-4 mb-6 bg-slate-100 rounded-xl"
          onChange={(e) => setFormData({...formData, re_password: e.target.value})} 
        />

        <button className="w-full bg-black text-white p-4 rounded-xl font-bold hover:bg-blue-600 transition">
          Create Account
        </button>
      </form>
    </div>
  );
}