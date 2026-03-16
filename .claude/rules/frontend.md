# Frontend Rules — Next.js / React / TypeScript

## Components
- Functional components with arrow functions only (no class components)
- PascalCase filenames for components (e.g., `Navbar.tsx`, `MUNMap.tsx`)
- Add `"use client"` directive at the top of any component that uses hooks, event handlers, or browser APIs
- Keep server components as the default — only opt into client when necessary

## Styling
- Tailwind CSS utility classes only — no Bootstrap, no CSS modules, no inline style objects
- Use Tailwind CSS 4 syntax (the project uses v4)
- Framer Motion for animations

## Data Fetching
- For endpoints that are rate-limited (AI, submissions, news create), use `apiFetch()` from `src/lib/api.ts` instead of raw `fetch`
- `apiFetch()` detects 429 responses and throws `RateLimitError` — catch it and call `showRateLimitToast()` from the `useRateLimitToast()` hook
- For read-only GET endpoints that don't need 429 handling, raw `fetch` is fine
- Always include `Authorization: Bearer {accessToken}` for authenticated endpoints
- Handle loading and error states in the UI
- `RateLimitToastProvider` is already in the root layout — just use the `useRateLimitToast()` hook in any client component

## Authentication
- NextAuth with CredentialsProvider handles login
- Session contains `accessToken` and `refreshToken` from Django SimpleJWT
- Protected routes use middleware in `src/proxy.ts`
- Token types are extended in `src/types/next-auth.d.ts`

## Routing
- Next.js App Router with file-based routing in `src/app/`
- Dynamic routes use bracket notation: `[slug]`, `[id]`
- API routes live in `src/app/api/`

## Imports
- Vercel is case-sensitive — always match exact filename casing in imports
- Use relative imports (e.g., `../../../lib/api`) — the `@/*` alias maps to the frontend root, not `src/`, so `@/src/lib/api` would be needed. Relative imports are simpler and match existing patterns.
