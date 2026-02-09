import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export async function proxy(request: NextRequest) {
  // Check for NextAuth session by looking for session cookies
  // NextAuth stores session in cookies named next-auth.*
  const nextAuthCookies = request.cookies.getAll().filter(cookie => 
    cookie.name.startsWith("next-auth.")
  );

  // If no NextAuth session cookies, redirect to login
  if (request.nextUrl.pathname.startsWith("/news/add") && nextAuthCookies.length === 0) {
    return NextResponse.redirect(new URL("/login?callbackUrl=/news/add", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/news/add"], // Only run proxy on this specific route
};
