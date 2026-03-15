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
- Use `fetch` with the backend API URL from `NEXT_PUBLIC_API_URL`
- Always include `Authorization: Bearer {accessToken}` for authenticated endpoints
- Handle loading and error states in the UI

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
- Use absolute imports with `@/` prefix when configured
