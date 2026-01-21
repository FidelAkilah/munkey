"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AddNewsPage() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [imageFile, setImageFile] = useState<File | null>(null);
  const router = useRouter();

  const handlePublish = async (e: React.FormEvent) => {
    e.preventDefault();

    // Professional cookie getter
    const getCookie = (name: string) => {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop()?.split(";").shift();
    };

    const token = getCookie("session_token");

    // 🔥 Use FormData instead of JSON
    const formData = new FormData();
    formData.append("title", title);
    formData.append("content", content);
    formData.append(
      "slug",
      title
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, "")
        .replace(/[\s_-]+/g, "-")
        .replace(/^-+|-+$/g, "")
    );
    formData.append("category", "NW");

    if (imageFile) {
      formData.append("featured_image", imageFile);
    }

    const res = await fetch("http://localhost:8000/api/news/create/", {
      method: "POST",
      headers: {
        // ❌ DO NOT set Content-Type when using FormData
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    if (res.ok) {
      router.push("/");
      router.refresh();
    } else {
      const errorData = await res.json();
      console.error("Django Error:", errorData);
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

        {/* 🖼️ Image Upload */}
        <input
          type="file"
          accept="image/*"
          className="w-full p-4 bg-slate-50 border rounded-3xl"
          onChange={(e) => setImageFile(e.target.files?.[0] || null)}
        />

        <button className="bg-black text-white px-12 py-4 rounded-full font-bold hover:bg-blue-600 transition">
          Publish Article
        </button>
      </form>
    </main>
  );
}
