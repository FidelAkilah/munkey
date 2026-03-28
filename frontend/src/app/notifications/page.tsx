"use client";
import { useState, useEffect } from 'react';
import { useSession } from 'next-auth/react';
import Link from 'next/link';
import { motion } from 'framer-motion';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "https://mun-global.onrender.com";

interface Notification {
  id: number;
  type: string;
  type_display: string;
  title: string;
  message: string;
  is_read: boolean;
  link: string;
  created_at: string;
}

interface ExtendedUser {
  accessToken?: string;
}

const NOTIF_ICONS: Record<string, string> = {
  ARTICLE_APPROVED: '✅', ARTICLE_REJECTED: '📝', NEW_COMMENT: '💬',
  AI_FEEDBACK_READY: '🤖', STREAK_MILESTONE: '🔥', SYSTEM: '📢',
};

const NotificationsPage = () => {
  const { data: session, status } = useSession();
  const user = session?.user as ExtendedUser | undefined;
  const accessToken = user?.accessToken;

  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [fetchDone, setFetchDone] = useState(false);
  const [nextPage, setNextPage] = useState<string | null>(null);
  const [filter, setFilter] = useState<'all' | 'unread'>('all');
  const loading = !fetchDone && status !== 'unauthenticated';

  useEffect(() => {
    if (!accessToken) return;
    const headers = { 'Authorization': `Bearer ${accessToken}` };
    let cancelled = false;
    fetch(`${API_BASE}/api/notifications/`, { headers })
      .then((r) => r.ok ? r.json() : null)
      .then((data) => {
        if (cancelled || !data) return;
        setNotifications(Array.isArray(data) ? data : data.results || []);
        setNextPage(data.next || null);
        setFetchDone(true);
      })
      .catch(() => { if (!cancelled) setFetchDone(true); });
    return () => { cancelled = true; };
  }, [accessToken]);

  const loadMore = () => {
    if (!nextPage || !accessToken) return;
    fetch(nextPage, { headers: { 'Authorization': `Bearer ${accessToken}` } })
      .then((r) => r.ok ? r.json() : null)
      .then((data) => {
        if (!data) return;
        const items = Array.isArray(data) ? data : data.results || [];
        setNotifications((prev) => [...prev, ...items]);
        setNextPage(data.next || null);
      })
      .catch(() => {});
  };

  const markAsRead = (id: number) => {
    if (!accessToken) return;
    fetch(`${API_BASE}/api/notifications/${id}/read/`, {
      method: 'PATCH',
      headers: { 'Authorization': `Bearer ${accessToken}` },
    }).then(() => {
      setNotifications((prev) => prev.map((n) => n.id === id ? { ...n, is_read: true } : n));
    }).catch(() => {});
  };

  const markAllRead = () => {
    if (!accessToken) return;
    fetch(`${API_BASE}/api/notifications/read-all/`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${accessToken}` },
    }).then(() => {
      setNotifications((prev) => prev.map((n) => ({ ...n, is_read: true })));
    }).catch(() => {});
  };

  const filtered = filter === 'unread'
    ? notifications.filter((n) => !n.is_read)
    : notifications;

  const unreadCount = notifications.filter((n) => !n.is_read).length;

  if (status === 'loading' || loading) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="w-8 h-8 border-3 border-slate-200 border-t-[#C66810] rounded-full animate-spin" />
      </div>
    );
  }

  if (status !== 'authenticated') {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-lg font-semibold text-slate-700">Please log in to view notifications</p>
          <Link href="/login" className="mt-4 inline-block px-6 py-2.5 bg-[#C66810] text-white font-bold rounded-lg">
            Log In
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="bg-white border-b border-slate-200">
        <div className="max-w-3xl mx-auto px-6 py-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-slate-900">Notifications</h1>
              {unreadCount > 0 && (
                <p className="text-sm text-slate-500 mt-1">{unreadCount} unread</p>
              )}
            </div>
            {unreadCount > 0 && (
              <button
                onClick={markAllRead}
                className="px-4 py-2 text-sm font-semibold text-[#C66810] bg-orange-50 hover:bg-orange-100 rounded-lg transition-colors"
              >
                Mark all as read
              </button>
            )}
          </div>

          <div className="flex gap-2 mt-4">
            {(['all', 'unread'] as const).map((f) => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className={`px-4 py-1.5 text-sm font-semibold rounded-lg transition-colors ${
                  filter === f ? 'bg-[#C66810] text-white' : 'text-slate-600 hover:bg-slate-100'
                }`}
              >
                {f === 'all' ? 'All' : 'Unread'}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="max-w-3xl mx-auto px-6 py-6">
        {filtered.length === 0 ? (
          <div className="text-center py-16">
            <p className="text-4xl mb-3">🔔</p>
            <p className="text-lg font-semibold text-slate-700">
              {filter === 'unread' ? 'No unread notifications' : 'No notifications yet'}
            </p>
            <p className="text-sm text-slate-500 mt-1">
              {filter === 'unread' ? "You're all caught up!" : "Notifications will appear here when something happens"}
            </p>
          </div>
        ) : (
          <div className="space-y-2">
            {filtered.map((notif, i) => (
              <motion.div
                key={notif.id}
                initial={{ opacity: 0, y: 8 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.03 }}
              >
                <Link
                  href={notif.link || '#'}
                  onClick={() => { if (!notif.is_read) markAsRead(notif.id); }}
                  className={`flex items-start gap-4 p-5 rounded-xl border transition-all hover:shadow-md ${
                    !notif.is_read
                      ? 'bg-white border-[#C66810]/20 shadow-sm'
                      : 'bg-white border-slate-200 hover:border-slate-300'
                  }`}
                >
                  <span className="text-2xl mt-0.5">{NOTIF_ICONS[notif.type] || '📢'}</span>
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2">
                      <h3 className={`text-sm ${!notif.is_read ? 'font-bold text-slate-900' : 'font-medium text-slate-700'}`}>
                        {notif.title}
                      </h3>
                      {!notif.is_read && (
                        <span className="w-2.5 h-2.5 bg-[#C66810] rounded-full shrink-0" />
                      )}
                    </div>
                    <p className="text-sm text-slate-600 mt-1">{notif.message}</p>
                    <p className="text-xs text-slate-400 mt-2">
                      {new Date(notif.created_at).toLocaleDateString('en-US', {
                        month: 'long', day: 'numeric', year: 'numeric',
                        hour: '2-digit', minute: '2-digit',
                      })}
                    </p>
                  </div>
                </Link>
              </motion.div>
            ))}
          </div>
        )}

        {nextPage && (
          <div className="text-center mt-6">
            <button
              onClick={loadMore}
              className="px-6 py-2.5 text-sm font-semibold text-[#C66810] bg-orange-50 hover:bg-orange-100 rounded-lg transition-colors"
            >
              Load more
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default NotificationsPage;
