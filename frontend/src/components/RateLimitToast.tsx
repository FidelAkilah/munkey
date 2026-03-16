"use client";

import { useState, useCallback, createContext, useContext } from "react";
import { motion, AnimatePresence } from "framer-motion";

interface Toast {
  id: string;
  message: string;
  retryAfter?: number;
}

interface RateLimitContextType {
  showRateLimitToast: (retryAfter?: number, customMessage?: string) => void;
}

const RateLimitContext = createContext<RateLimitContextType>({
  showRateLimitToast: () => {},
});

export const useRateLimitToast = () => useContext(RateLimitContext);

export const RateLimitToastProvider = ({ children }: { children: React.ReactNode }) => {
  const [toasts, setToasts] = useState<Toast[]>([]);

  const showRateLimitToast = useCallback((retryAfter?: number, customMessage?: string) => {
    const minutes = retryAfter ? Math.ceil(retryAfter / 60) : 1;
    const message =
      customMessage ||
      (retryAfter && retryAfter > 3600
        ? "Our AI tutor is resting for today. Please try again tomorrow!"
        : `You've been practicing a lot! Please wait ${minutes} minute${minutes !== 1 ? "s" : ""} before submitting again.`);

    const id = Date.now().toString();
    setToasts((prev) => [...prev, { id, message, retryAfter }]);

    // Auto-dismiss after 8 seconds
    setTimeout(() => {
      setToasts((prev) => prev.filter((t) => t.id !== id));
    }, 8000);
  }, []);

  const dismissToast = (id: string) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  };

  return (
    <RateLimitContext.Provider value={{ showRateLimitToast }}>
      {children}
      <div className="fixed top-4 right-4 z-50 flex flex-col gap-3 max-w-sm">
        <AnimatePresence>
          {toasts.map((toast) => (
            <motion.div
              key={toast.id}
              initial={{ opacity: 0, y: -20, scale: 0.95 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: -20, scale: 0.95 }}
              transition={{ duration: 0.3 }}
              className="bg-amber-50 border border-amber-300 rounded-xl p-4 shadow-lg"
            >
              <div className="flex items-start gap-3">
                <span className="text-2xl flex-shrink-0">&#9203;</span>
                <div className="flex-1">
                  <p className="text-sm font-semibold text-amber-800">Hold on, delegate!</p>
                  <p className="text-sm text-amber-700 mt-1">{toast.message}</p>
                </div>
                <button
                  onClick={() => dismissToast(toast.id)}
                  className="text-amber-400 hover:text-amber-600 transition-colors flex-shrink-0"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>
    </RateLimitContext.Provider>
  );
};
