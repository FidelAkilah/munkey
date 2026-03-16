# MUNKEY - AI-Powered MUN Learning Platform

MUNKEY (MUN Global) is an AI-powered Model United Nations learning platform for Indonesia's MUN circuit. Django REST API backend + Next.js frontend SPA.

## Guiding Principles

- **Tailwind CSS only** for styling — no Bootstrap, no inline styles
- **Functional components with arrow functions** in React
- **TypeScript** for all frontend code
- **Django REST Framework** serializers + viewsets for all API endpoints
- **JWT authentication** via SimpleJWT (backend) + NextAuth (frontend)
- DiplomAI (the AI tutor) uses OpenAI API — keep prompts in `curriculum/ai_service.py`

## Essential Commands

### Development (from project root)

```bash
npm run dev                  # Start both Django + Next.js concurrently
python manage.py runserver   # Django only (port 8000)
cd frontend && npm run dev   # Next.js only (port 3000)
```

### Backend

```bash
python manage.py migrate              # Run database migrations
python manage.py makemigrations       # Generate new migrations
python manage.py collectstatic        # Gather static files
python manage.py shell                # Django interactive shell
python seed_curriculum.py             # Seed curriculum data
python manage.py check_api_usage      # Print today's OpenAI token usage stats
python manage.py check_api_usage --days 7  # Usage stats for last 7 days
```

### Frontend

```bash
cd frontend && npm run build    # Production build
cd frontend && npm run lint     # ESLint check
```

### Deployment

```bash
bash build.sh    # Render deploy script (pip install, collectstatic, migrate)
```

## Codebase Map

```
accounts/        → User auth & profiles (custom User model with JR/SR/AD roles)
community/       → Discussion forum / comments on articles
core/            → Django settings, authentication, URL routing, throttling
curriculum/      → DiplomAI learning platform (AI feedback, chat, questions, API usage tracking)
directory/       → MUN conference locations (lat/long for maps)
frontend/        → Next.js 16 SPA (src/app/ file-based routing)
news/            → Article posting with admin approval workflow
skills/          → YouTube skill video categories & tutorials
```

### Frontend Structure

```
frontend/src/
├── app/                → Pages (file-based routing)
│   ├── curriculum/     → Learning platform pages
│   ├── news/           → Article pages
│   ├── skills/         → Video tutorial pages
│   └── api/auth/       → NextAuth credential provider
├── components/         → Shared components (Navbar, Footer, MUNMap, RateLimitToast)
├── lib/                → Utilities (api.ts — fetch wrapper with 429 handling)
├── proxy.ts            → Middleware for protected routes
└── types/              → TypeScript type definitions
```

## Tech Stack

| Layer      | Technology                              |
|------------|-----------------------------------------|
| Backend    | Django 5.1, DRF 3.15, SimpleJWT        |
| Frontend   | Next.js 16, React 19, TypeScript 5     |
| Styling    | Tailwind CSS 4, Framer Motion           |
| Database   | PostgreSQL (Supabase)                   |
| AI         | OpenAI API (gpt-4o-mini)                |
| Auth       | NextAuth 4 + Django SimpleJWT           |
| Deploy     | Vercel (frontend) + Render (backend)    |

## Authentication Flow

1. Frontend calls `POST /auth/jwt/create/` via NextAuth CredentialsProvider
2. Django returns `accessToken` + `refreshToken`
3. NextAuth stores tokens in JWT session (24hr maxAge)
4. Frontend sends `Authorization: Bearer {token}` on API calls
5. Backend validates via custom `NextAuthJWTAuthentication` class in `core/authentication.py`

## User Roles

- **Junior (JR)**: Elementary/middle school — auto-restricted, filtered content
- **Senior (SR)**: High school/college — default role
- **Admin (AD)**: Moderators — article approval, dashboard access

## Environment Variables (required in .env)

```
DEBUG, SECRET_KEY, DATABASE_URL, SIMPLE_JWT_SECRET_KEY,
NEXTAUTH_SECRET, NEXTAUTH_URL, NEXT_PUBLIC_API_URL,
OPENAI_API_KEY, PYTHON_VERSION, ALLOWED_HOSTS,
DAILY_TOKEN_LIMIT          # Optional, default 500000 — daily OpenAI token cap
```

## Production URLs

- Frontend: https://munkey-zeta.vercel.app
- Backend API: https://mun-global.onrender.com

## Rate Limiting

All API endpoints are rate-limited via DRF throttling (`core/throttling.py`):

| Endpoint Type | Limit | Scope |
|---------------|-------|-------|
| AI endpoints (chat, submissions/create, generate-questions) | 20/hour | per user |
| Auth endpoints (JWT login/refresh, register) | 5/min | per IP |
| News creation | 10/hour | per user |
| All other endpoints (default) | 100/min | per user |

- Daily OpenAI token cap: 500,000 tokens (configurable via `DAILY_TOKEN_LIMIT` env var)
- `APIUsageLog` model in `curriculum/models.py` tracks every OpenAI call
- Custom throttle classes live in `core/throttling.py`; throttled auth wrappers in `core/views.py`
- 429 responses return `{"error": "Rate limit exceeded", "retry_after": <seconds>}` with `Retry-After` header
- Frontend uses `apiFetch()` from `src/lib/api.ts` + `RateLimitToast` for user-friendly 429 handling
- When adding new AI endpoints: apply `AIEndpointThrottle`, call `check_daily_token_limit()`, pass `user=request.user` to AI service functions

## Rules

- After writing code, run lint (`cd frontend && npm run lint`) and fix errors before finishing
- Never commit `.env` files or API keys
- Keep DECISIONS.md updated when solving significant bugs or making architectural changes
- See `.claude/rules/` for domain-specific rules (frontend, MUN logic, API standards)
