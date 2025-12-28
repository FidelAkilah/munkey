"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AddNewsPage() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const router = useRouter();

  const handlePublish = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // Professional way to get the cookie in the browser
    const getCookie = (name: string) => {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop()?.split(';').shift();
    };

    const token = getCookie('session_token');

    const res = await fetch("http://localhost:8000/api/news/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}` //
      },
      body: JSON.stringify({ 
        title, 
        content, 
        // Django needs a slug; let's generate it from the title
        slug: title.toLowerCase().trim().replace(/[^\w\s-]/g, '').replace(/[\s_-]+/g, '-').replace(/^-+|-+$/g, ''),
        category: "NW" 
      }),
    });

    if (res.ok) {
      router.push("/");
      router.refresh();
    } else {
      const errorData = await res.json();
      console.error("Django Error:", errorData); // This will tell you EXACTLY what field is missing
      alert("Check the console for errors!");
    }
  };

  return (
    <main className="max-w-4xl mx-auto p-12">
      <h1 className="text-4xl font-black mb-8">Post to Global Feed</h1>
      <form onSubmit={handlePublish} className="space-y-6">
        <input 
          className="w-full p-6 text-2xl font-bold bg-slate-50 border rounded-3xl"
          placeholder="Enter Article Title..." 
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <textarea 
          className="w-full p-6 h-96 bg-slate-50 border rounded-3xl"
          placeholder="Start typing the circuit news..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        />
        <button className="bg-black text-white px-12 py-4 rounded-full font-bold hover:bg-blue-600 transition">
          Publish Article
        </button>
      </form>
    </main>
  );
}