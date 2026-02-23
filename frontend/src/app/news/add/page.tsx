"use client";
import { useState, useEffect, useRef, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useSession } from "next-auth/react";

function compressImage(file: File, maxWidth = 800, quality = 0.7): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const img = new window.Image();
      img.onload = () => {
        const canvas = document.createElement("canvas");
        let w = img.width;
        let h = img.height;
        if (w > maxWidth) {
          h = (h * maxWidth) / w;
          w = maxWidth;
        }
        canvas.width = w;
        canvas.height = h;
        const ctx = canvas.getContext("2d");
        if (!ctx) return reject("Canvas not supported");
        ctx.drawImage(img, 0, 0, w, h);
        resolve(canvas.toDataURL("image/jpeg", quality));
      };
      img.onerror = reject;
      img.src = e.target?.result as string;
    };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

function AddNewsForm() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [imageMode, setImageMode] = useState<"upload" | "url">("url");
  const [imageUrl, setImageUrl] = useState("");
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [isCompressing, setIsCompressing] = useState(false);
  const [category, setCategory] = useState("NW");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<"idle" | "success" | "error">("idle");
  const [errorMessage, setErrorMessage] = useState("");
  const fileInputRef = useRef<HTMLInputElement>(null);
  const router = useRouter();
  const searchParams = useSearchParams();
  const { data: session, status } = useSession();

  const callbackUrl = searchParams.get("callbackUrl") || "/news/my-articles";

  const getToken = () => {
    if (session?.user && typeof (session.user as { accessToken?: string }).accessToken === "string") {
      return (session.user as { accessToken: string }).accessToken;
    }
    return null;
  };

  useEffect(() => {
    if (status === "unauthenticated") {
      router.push(`/login?callbackUrl=${encodeURIComponent("/news/add")}`);
    }
  }, [status, router]);

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsCompressing(true);
    try {
      const compressed = await compressImage(file);
      setImagePreview(compressed);
      setImageUrl(compressed);
    } catch {
      setErrorMessage("Failed to process image. Try a different file.");
    } finally {
      setIsCompressing(false);
    }
  };

  const handleUrlChange = (url: string) => {
    setImageUrl(url);
    setImagePreview(url || null);
  };

  const clearImage = () => {
    setImageUrl("");
    setImagePreview(null);
    if (fileInputRef.current) fileInputRef.current.value = "";
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!session?.user) {
      router.push(`/login?callbackUrl=${encodeURIComponent("/news/add")}`);
      return;
    }

    setIsSubmitting(true);
    setSubmitStatus("idle");
    setErrorMessage("");

    const token = getToken();

    if (!token) {
      setSubmitStatus("error");
      setErrorMessage("Session expired. Please log in again.");
      setIsSubmitting(false);
      return;
    }

    const slug = title
      .toLowerCase()
      .trim()
      .replace(/[^\w\s-]/g, "")
      .replace(/[\s_-]+/g, "-")
      .replace(/^-+|-+$/g, "");

    try {
      const res = await fetch("https://mun-global.onrender.com/api/news/create/", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title,
          content,
          slug,
          category,
          image_url: imageUrl,
        }),
      });

      if (res.ok) {
        setSubmitStatus("success");
        setTimeout(() => {
          router.push(callbackUrl);
        }, 1500);
      } else {
        const errorData = await res.json();
        setSubmitStatus("error");
        setErrorMessage(errorData.detail || JSON.stringify(errorData));
      }
    } catch {
      setSubmitStatus("error");
      setErrorMessage("Network error. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  if (status === "loading") {
    return (
      <main className="max-w-4xl mx-auto p-12">
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        </div>
      </main>
    );
  }

  if (status === "unauthenticated" || !session?.user) {
    return (
      <main className="max-w-4xl mx-auto p-12">
        <div className="text-center py-20">
          <h1 className="text-4xl font-black mb-6">Login Required</h1>
          <p className="text-slate-600 mb-8">You need to be logged in to submit an article.</p>
          <button
            onClick={() => router.push("/login?callbackUrl=/news/add")}
            className="bg-blue-600 text-white px-12 py-4 rounded-full font-bold hover:bg-blue-700 transition"
          >
            Go to Login
          </button>
        </div>
      </main>
    );
  }

  return (
    <>
      <h1 className="text-4xl font-black mb-2">Submit Your Story</h1>
      <p className="text-slate-500 mb-8">
        Share your MUN experiences with the community. Your article will be reviewed by our team before publication.
      </p>

      {submitStatus === "success" && (
        <div className="mb-8 p-6 bg-green-50 border border-green-200 rounded-2xl">
          <div className="flex items-center gap-3 text-green-700">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span className="font-semibold">Article submitted successfully! Redirecting to your submissions...</span>
          </div>
        </div>
      )}

      {submitStatus === "error" && (
        <div className="mb-8 p-6 bg-red-50 border border-red-200 rounded-2xl">
          <div className="flex items-center gap-3 text-red-700">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
            <span className="font-semibold">Error: {errorMessage}</span>
          </div>
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-6">
        <input
          className="w-full p-6 text-2xl font-bold bg-slate-50 border rounded-3xl focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Enter Article Title..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />

        <select
          className="w-full p-6 bg-slate-50 border rounded-3xl focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        >
          <option value="NW">Global News</option>
          <option value="GD">Preparation Guides</option>
          <option value="IN">Delegate Interviews</option>
        </select>

        <textarea
          className="w-full p-6 h-64 bg-slate-50 border rounded-3xl focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Start typing your article... Share your MUN story, conference experience, or helpful tips for other delegates."
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        />

        {/* Image Section */}
        <div className="space-y-4">
          <label className="text-sm font-semibold text-slate-700">Featured Image</label>

          {/* Mode Toggle */}
          <div className="flex gap-2 bg-slate-100 p-1 rounded-full w-fit">
            <button
              type="button"
              onClick={() => { setImageMode("url"); clearImage(); }}
              className={`px-5 py-2 rounded-full text-sm font-semibold transition-all ${
                imageMode === "url"
                  ? "bg-white text-blue-600 shadow-sm"
                  : "text-slate-500 hover:text-slate-700"
              }`}
            >
              Paste URL
            </button>
            <button
              type="button"
              onClick={() => { setImageMode("upload"); clearImage(); }}
              className={`px-5 py-2 rounded-full text-sm font-semibold transition-all ${
                imageMode === "upload"
                  ? "bg-white text-blue-600 shadow-sm"
                  : "text-slate-500 hover:text-slate-700"
              }`}
            >
              Upload from Device
            </button>
          </div>

          {/* URL Input */}
          {imageMode === "url" && (
            <input
              type="url"
              className="w-full p-4 bg-slate-50 border rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="https://example.com/image.jpg"
              value={imageUrl.startsWith("data:") ? "" : imageUrl}
              onChange={(e) => handleUrlChange(e.target.value)}
            />
          )}

          {/* File Upload */}
          {imageMode === "upload" && (
            <div className="relative">
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                className="w-full p-4 bg-slate-50 border rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-600 hover:file:bg-blue-100"
                onChange={handleFileChange}
              />
              {isCompressing && (
                <div className="absolute inset-0 bg-white/80 rounded-2xl flex items-center justify-center">
                  <div className="flex items-center gap-2 text-sm text-slate-600">
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-blue-600"></div>
                    Compressing image...
                  </div>
                </div>
              )}
              <p className="text-xs text-slate-400 mt-2">
                Image will be compressed automatically (max 800px wide, JPEG).
              </p>
            </div>
          )}

          {/* Preview */}
          {imagePreview && (
            <div className="relative rounded-2xl overflow-hidden border bg-slate-50">
              <img
                src={imagePreview}
                alt="Preview"
                className="w-full h-48 object-cover"
                onError={() => setImagePreview(null)}
              />
              <button
                type="button"
                onClick={clearImage}
                className="absolute top-3 right-3 w-8 h-8 bg-black/50 hover:bg-black/70 text-white rounded-full flex items-center justify-center transition"
              >
                &times;
              </button>
            </div>
          )}
        </div>

        <div className="flex gap-4">
          <button
            type="submit"
            disabled={isSubmitting}
            className={`flex-1 bg-blue-600 text-white px-12 py-4 rounded-full font-bold transition ${
              isSubmitting ? "opacity-50 cursor-not-allowed" : "hover:bg-blue-700"
            }`}
          >
            {isSubmitting ? (
              <span className="flex items-center justify-center gap-2">
                <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                </svg>
                Submitting...
              </span>
            ) : (
              "Submit for Review"
            )}
          </button>
        </div>

        <p className="text-sm text-slate-500 text-center">
          By submitting, you agree that your article will be reviewed by our editorial team before publication.
        </p>
      </form>
    </>
  );
}

export default function AddNewsPage() {
  return (
    <main className="max-w-4xl mx-auto p-12">
      <Suspense
        fallback={
          <div className="flex items-center justify-center h-64">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
          </div>
        }
      >
        <AddNewsForm />
      </Suspense>
    </main>
  );
}
