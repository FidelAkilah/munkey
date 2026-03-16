/**
 * API fetch wrapper with rate limit (429) handling.
 *
 * Wraps the native fetch() and returns a RateLimitError when the backend
 * responds with HTTP 429, so callers can show the toast.
 */

export class RateLimitError extends Error {
  retryAfter: number;
  customMessage?: string;

  constructor(retryAfter: number, customMessage?: string) {
    super(customMessage || "Rate limit exceeded");
    this.name = "RateLimitError";
    this.retryAfter = retryAfter;
    this.customMessage = customMessage;
  }
}

/**
 * Thin wrapper around fetch() that detects 429 responses and throws
 * a RateLimitError with the retry_after value from the response body.
 *
 * Usage:
 *   try {
 *     const res = await apiFetch("/api/curriculum/chat/", { method: "POST", ... });
 *     const data = await res.json();
 *   } catch (err) {
 *     if (err instanceof RateLimitError) {
 *       showRateLimitToast(err.retryAfter, err.customMessage);
 *       return;
 *     }
 *     // handle other errors
 *   }
 */
export async function apiFetch(
  url: string,
  options?: RequestInit,
): Promise<Response> {
  const res = await fetch(url, options);

  if (res.status === 429) {
    let retryAfter = 60;
    let customMessage: string | undefined;

    try {
      const body = await res.json();
      retryAfter = body.retry_after ?? 60;
      // The daily limit message comes through as the error detail
      if (body.detail && body.detail.includes("resting for today")) {
        customMessage = body.detail;
      }
    } catch {
      // If we can't parse the body, fall back to the Retry-After header
      const headerVal = res.headers.get("Retry-After");
      if (headerVal) retryAfter = parseInt(headerVal, 10) || 60;
    }

    throw new RateLimitError(retryAfter, customMessage);
  }

  return res;
}
