/* eslint-disable @typescript-eslint/no-explicit-any */
// src/components/Navbar.tsx
"use client";
import Link from 'next/link';
import { useSession, signOut } from 'next-auth/react';
import { useState } from 'react';

// Extend the session user type
interface ExtendedUser {
  name?: string | null;
  email?: string | null;
  image?: string | null;
  role?: string;
  username?: string;
  isSuperuser?: boolean;
}

interface ExtendedSession {
  user: ExtendedUser;
}

export default function Navbar() {
  const { data: session, status } = useSession();
  const [showUserMenu, setShowUserMenu] = useState(false);
  const isLoading = status === 'loading';
  const isAuthenticated = status === 'authenticated';
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const user = session?.user as ExtendedUser | undefined;
  const isAdmin = user?.role === 'AD' || user?.isSuperuser === true;

  const getUserInitial = () => {
    if (user?.username) {
      return user.username.charAt(0).toUpperCase();
    }
    if (user?.name) {
      return user.name.charAt(0).toUpperCase();
    }
    return 'U';
  };

  return (
    <nav className="sticky top-0 z-[100] w-full bg-[#0a1628]/95 backdrop-blur-xl border-b border-white/5 shadow-[0_4px_20px_rgba(0,0,0,0.3)]">
      <div className="max-w-7xl mx-auto px-6 lg:px-8 h-20 flex items-center justify-between">
        
        {/* Brand - Elegant & Refined */}
        <Link 
          href="/" 
          className="group flex items-center gap-3"
        >
          <span className="text-3xl font-black tracking-tight">
            <span className="text-white">MUN</span>
            <span className="text-transparent bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400 bg-clip-text">KEY</span>
          </span>
          <div className="w-px h-6 bg-gradient-to-b from-transparent via-cyan-400/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
        </Link>

        {/* Navigation Links - Center */}
        <div className="hidden md:flex items-center gap-1">
          <Link 
            href="/" 
            className="px-5 py-2 text-sm font-medium text-slate-300 hover:text-white hover:bg-white/5 rounded-lg transition-all duration-200"
          >
            NEWS
          </Link>
          <Link 
            href="/skills" 
            className="px-5 py-2 text-sm font-medium text-slate-300 hover:text-white hover:bg-white/5 rounded-lg transition-all duration-200"
          >
            SKILL SHARING
          </Link>
        </div>

        {/* CTA & Profile Actions */}
        <div className="flex items-center gap-4">
          {/* Show Add News button only if authenticated */}
          {isAuthenticated && (
            <Link 
              href="/news/add" 
              className="group relative px-5 py-2.5 bg-gradient-to-r from-cyan-500 to-blue-500 text-white text-sm font-semibold rounded-lg overflow-hidden shadow-lg shadow-cyan-500/20 hover:shadow-cyan-500/40 transition-all duration-300"
            >
              <span className="relative z-10 flex items-center gap-2">
                <span className="text-lg leading-none">+</span>
                <span className="hidden sm:inline">ADD NEWS</span>
              </span>
              <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            </Link>
          )}

          {isLoading ? (
            // Loading state
            <div className="w-9 h-9 rounded-full bg-slate-800 animate-pulse" />
          ) : isAuthenticated ? (
            // Authenticated user menu
            <div className="relative">
              <button 
                onClick={() => setShowUserMenu(!showUserMenu)}
                className="w-9 h-9 rounded-full bg-gradient-to-br from-cyan-400 to-blue-500 p-[2px] cursor-pointer group hover:scale-105 transition-transform duration-200"
              >
                <div className="w-full h-full rounded-full bg-slate-800 flex items-center justify-center text-white text-sm font-semibold">
                  {getUserInitial()}
                </div>
              </button>

              {/* Dropdown menu */}
              {showUserMenu && (
                <div className="absolute right-0 mt-2 w-48 bg-slate-800 rounded-lg shadow-xl border border-white/10 py-2">
                  <div className="px-4 py-2 border-b border-white/10">
                    <p className="text-sm font-semibold text-white">
                      {user?.username || user?.name}
                    </p>
                    <p className="text-xs text-slate-400">
                      {isAdmin ? 'Admin' : 'Delegate'}
                    </p>
                  </div>
                  <Link 
                    href="/news/my-articles"
                    className="block px-4 py-2 text-sm text-slate-300 hover:bg-white/5 hover:text-white"
                    onClick={() => setShowUserMenu(false)}
                  >
                    My Submissions
                  </Link>
                  {isAdmin && (
                    <Link 
                      href="/admin/dashboard"
                      className="block px-4 py-2 text-sm text-cyan-400 hover:bg-white/5 hover:text-cyan-300"
                      onClick={() => setShowUserMenu(false)}
                    >
                      Admin Dashboard
                    </Link>
                  )}
                  <button 
                    onClick={() => {
                      setShowUserMenu(false);
                      signOut();
                    }}
                    className="w-full text-left px-4 py-2 text-sm text-red-400 hover:bg-white/5"
                  >
                    Sign Out
                  </button>
                </div>
              )}
            </div>
          ) : (
            // Show login button if not authenticated
            <Link 
              href="/login" 
              className="px-5 py-2 text-sm font-semibold text-white bg-slate-800 hover:bg-slate-700 rounded-lg transition-all duration-200"
            >
              Login
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
}
