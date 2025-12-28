import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const token = request.cookies.get("session_token");

  // If trying to add news without a token, redirect to login
  if (request.nextUrl.pathname.startsWith("/news/add") && !token) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/news/add"], // Only run proxy on this specific route
};