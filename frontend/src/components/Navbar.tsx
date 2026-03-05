/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";
import Link from 'next/link';
import Image from 'next/image';
import { useSession, signOut } from 'next-auth/react';
import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface ExtendedUser {
  name?: string | null;
  email?: string | null;
  image?: string | null;
  role?: string;
  username?: string;
  isSuperuser?: boolean;
}

export default function Navbar() {
  const { data: session, status } = useSession();
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const isLoading = status === 'loading';
  const isAuthenticated = status === 'authenticated';
  const user = session?.user as ExtendedUser | undefined;
  const isAdmin = user?.role === 'AD' || user?.isSuperuser === true;

  const getUserInitial = () => {
    if (user?.username) return user.username.charAt(0).toUpperCase();
    if (user?.name) return user.name.charAt(0).toUpperCase();
    return 'U';
  };

  const navLinks = [
    { href: '/news', label: 'NEWS' },
    { href: '/skills', label: 'SKILL SHARING' },
    { href: '/curriculum', label: 'DIPLOMAI', hasIcon: true },
  ];

  return (
    <nav className="sticky top-0 z-[100] w-full bg-white/95 backdrop-blur-xl border-b border-slate-200 shadow-sm">
      <div className="max-w-7xl mx-auto px-6 lg:px-8 h-20 flex items-center justify-between">

        {/* Brand */}
        <Link href="/" className="group flex items-center gap-3">
          <Image
            src="/MunKey Main Logo.png"
            alt="MUNKEY Logo"
            width={40}
            height={40}
            className="w-10 h-10 object-contain group-hover:scale-105 transition-transform"
          />
          <span className="text-3xl font-black tracking-tight text-slate-900">
            MUN<span className="text-[#C66810]">KEY</span>
          </span>
        </Link>

        {/* Navigation Links - Center (Desktop) */}
        <div className="hidden md:flex items-center gap-1">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="px-5 py-2 text-sm font-bold text-slate-600 hover:text-[#C66810] hover:bg-orange-50 rounded-lg transition-all duration-200 flex items-center gap-2"
            >
              {link.hasIcon && (
                <Image
                  src="/MunKey Main Logo.png"
                  alt="Bongo"
                  width={20}
                  height={20}
                  className="w-5 h-5 object-contain"
                />
              )}
              <span>{link.label}</span>
            </Link>
          ))}
        </div>

        {/* CTA & Profile Actions */}
        <div className="flex items-center gap-3">
          {isAuthenticated && (
            <Link
              href="/news/add"
              className="hidden sm:inline-flex items-center gap-2 px-5 py-2.5 bg-[#C66810] text-white text-sm font-bold rounded-lg shadow-sm hover:bg-[#A05200] transition-all duration-300"
            >
              <span className="text-lg leading-none">+</span>
              <span>ADD NEWS</span>
            </Link>
          )}

          {isLoading ? (
            <div className="w-9 h-9 rounded-full bg-slate-200 animate-pulse" />
          ) : isAuthenticated ? (
            <div className="relative">
              <button
                onClick={() => setShowUserMenu(!showUserMenu)}
                className="w-10 h-10 rounded-full border-2 border-[#C66810]/20 p-[2px] cursor-pointer hover:border-[#C66810] transition-colors duration-200 focus:outline-none"
              >
                <div className="w-full h-full rounded-full bg-[#C66810] flex items-center justify-center text-white text-sm font-bold shadow-md">
                  {getUserInitial()}
                </div>
              </button>

              <AnimatePresence>
                {showUserMenu && (
                  <>
                    <div
                      className="fixed inset-0 z-10"
                      onClick={() => setShowUserMenu(false)}
                    />
                    <motion.div
                      initial={{ opacity: 0, scale: 0.95, y: -4 }}
                      animate={{ opacity: 1, scale: 1, y: 0 }}
                      exit={{ opacity: 0, scale: 0.95, y: -4 }}
                      transition={{ duration: 0.15 }}
                      className="absolute right-0 mt-2 w-56 bg-white rounded-xl shadow-xl border border-slate-100 py-2 z-20 origin-top-right ring-1 ring-black/5"
                    >
                      <div className="px-4 py-3 border-b border-slate-100 bg-slate-50/50">
                        <p className="text-sm font-bold text-slate-900 truncate">
                          {user?.username || user?.name}
                        </p>
                        <p className="text-xs text-slate-500 font-medium">
                          {isAdmin ? 'Administrator' : 'Delegate Account'}
                        </p>
                      </div>

                      <div className="py-1">
                        <Link
                          href="/news/my-articles"
                          className="flex items-center gap-2 px-4 py-2.5 text-sm text-slate-600 hover:bg-orange-50 hover:text-[#C66810] transition-colors font-medium"
                          onClick={() => setShowUserMenu(false)}
                        >
                          <span>📝</span> My Submissions
                        </Link>

                        {isAdmin && (
                          <Link
                            href="/admin/dashboard"
                            className="flex items-center gap-2 px-4 py-2.5 text-sm text-[#C66810] hover:bg-orange-50 font-bold transition-colors"
                            onClick={() => setShowUserMenu(false)}
                          >
                            <span>⚡</span> Admin Dashboard
                          </Link>
                        )}
                      </div>

                      <div className="py-1 border-t border-slate-100">
                        <button
                          onClick={() => {
                            setShowUserMenu(false);
                            signOut();
                          }}
                          className="w-full text-left flex items-center gap-2 px-4 py-2.5 text-sm text-red-600 hover:bg-red-50 font-medium transition-colors"
                        >
                          <span>🚪</span> Sign Out
                        </button>
                      </div>
                    </motion.div>
                  </>
                )}
              </AnimatePresence>
            </div>
          ) : (
            <Link
              href="/login"
              className="px-6 py-2.5 text-sm font-bold text-[#C66810] bg-orange-50 hover:bg-orange-100 rounded-lg transition-all duration-200"
            >
              Log In
            </Link>
          )}

          {/* Mobile Hamburger */}
          <button
            onClick={() => setMobileOpen(!mobileOpen)}
            className="md:hidden w-10 h-10 flex items-center justify-center rounded-lg hover:bg-slate-100 transition-colors"
          >
            <motion.div className="flex flex-col gap-1.5" animate={mobileOpen ? "open" : "closed"}>
              <motion.span
                variants={{ closed: { rotate: 0, y: 0 }, open: { rotate: 45, y: 6 } }}
                className="block w-5 h-0.5 bg-slate-700"
              />
              <motion.span
                variants={{ closed: { opacity: 1 }, open: { opacity: 0 } }}
                className="block w-5 h-0.5 bg-slate-700"
              />
              <motion.span
                variants={{ closed: { rotate: 0, y: 0 }, open: { rotate: -45, y: -6 } }}
                className="block w-5 h-0.5 bg-slate-700"
              />
            </motion.div>
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.25 }}
            className="md:hidden overflow-hidden border-t border-slate-100 bg-white"
          >
            <div className="px-6 py-4 space-y-1">
              {navLinks.map((link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  onClick={() => setMobileOpen(false)}
                  className="block px-4 py-3 text-sm font-bold text-slate-700 hover:text-[#C66810] hover:bg-orange-50 rounded-lg transition-colors"
                >
                  {link.label}
                </Link>
              ))}
              {isAuthenticated && (
                <Link
                  href="/news/add"
                  onClick={() => setMobileOpen(false)}
                  className="block px-4 py-3 text-sm font-bold text-[#C66810] bg-orange-50 rounded-lg"
                >
                  + Add News
                </Link>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
}
