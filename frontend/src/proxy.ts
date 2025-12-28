import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

// In Next.js 16, use 'proxy' as the function name
export function proxy(request: NextRequest) {
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};