"use client";
import { useState, useEffect, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useSession } from "next-auth/react";

function AddNewsForm() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [imageFile, setImageFile] = useState<File | null>(null);
  const [category, setCategory] = useState("NW");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<'idle' | 'success' | 'error'>('idle');
  const [errorMessage, setErrorMessage] = useState("");
  const router = useRouter();
  const searchParams = useSearchParams();
  const { data: session, status } = useSession();

  // Get callback URL from search params
  const callbackUrl = searchParams.get("callbackUrl") || "/news/my-articles";

  // Get the access token from session
  const getToken = () => {
    // Try session first
    if (session?.user && typeof (session.user as { accessToken?: string }).accessToken === 'string') {
      return (session.user as { accessToken: string }).accessToken;
    }
    return null;
  };

  // Redirect to login if not authenticated (only once session is confirmed)
  useEffect(() => {
    if (status === "unauthenticated") {
      router.push(`/login?callbackUrl=${encodeURIComponent("/news/add")}`);
    }
  }, [status, router]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!session?.user) {
      router.push(`/login?callbackUrl=${encodeURIComponent("/news/add")}`);
      return;
    }

    setIsSubmitting(true);
    setSubmitStatus('idle');
    setErrorMessage("");

    const token = getToken();
    
    if (!token) {
      setSubmitStatus('error');
      setErrorMessage("Session expired. Please log in again.");
      setIsSubmitting(false);
      return;
    }

    // Use FormData instead of JSON
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
    formData.append("category", category);

    if (imageFile) {
      formData.append("featured_image", imageFile);
    }

    try {
      const res = await fetch("http://localhost:8000/api/news/create/", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: formData,
      });

      if (res.ok) {
        setSubmitStatus('success');
        setTimeout(() => {
          router.push(callbackUrl);
        }, 1500);
      } else {
        const errorData = await res.json();
        setSubmitStatus('error');
        setErrorMessage(errorData.detail || JSON.stringify(errorData));
      }
    } catch (error) {
      setSubmitStatus('error');
      setErrorMessage("Network error. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  // Loading state
  if (status === 'loading') {
    return (
      <main className="max-w-4xl mx-auto p-12">
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        </div>
      </main>
    );
  }

  // If not authenticated, show message
  if (status === 'unauthenticated' || !session?.user) {
    return (
      <main className="max-w-4xl mx-auto p-12">
        <div className="text-center py-20">
          <h1 className="text-4xl font-black mb-6">Login Required</h1>
          <p className="text-slate-600 mb-8">
            You need to be logged in to submit an article.
          </p>
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

      {submitStatus === 'success' && (
        <div className="mb-8 p-6 bg-green-50 border border-green-200 rounded-2xl">
          <div className="flex items-center gap-3 text-green-700">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span className="font-semibold">Article submitted successfully! Redirecting to your submissions...</span>
          </div>
        </div>
      )}

      {submitStatus === 'error' && (
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

        {/* Image Upload */}
        <input
          type="file"
          accept="image/*"
          className="w-full p-4 bg-slate-50 border rounded-3xl focus:outline-none focus:ring-2 focus:ring-blue-500"
          onChange={(e) => setImageFile(e.target.files?.[0] || null)}
        />

        <div className="flex gap-4">
          <button
            type="submit"
            disabled={isSubmitting}
            className={`flex-1 bg-blue-600 text-white px-12 py-4 rounded-full font-bold transition ${
              isSubmitting ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-700'
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
              'Submit for Review'
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
      <Suspense fallback={
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        </div>
      }>
        <AddNewsForm />
      </Suspense>
    </main>
  );
}

