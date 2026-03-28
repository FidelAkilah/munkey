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
python manage.py seed_user_stats      # Create/update UserStats for existing users
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
core/            → Django settings, authentication, URL routing, throttling, global search
curriculum/      → DiplomAI learning platform (AI feedback, chat, questions, API usage tracking, UserStats/progress)
directory/       → MUN conference locations (lat/long for maps)
frontend/        → Next.js 16 SPA (src/app/ file-based routing)
news/            → Article posting with admin approval workflow
notifications/   → In-app notification system (signals, bell icon, polling)
skills/          → YouTube skill video categories & tutorials
```

### Frontend Structure

```
frontend/src/
├── app/                → Pages (file-based routing)
│   ├── curriculum/     → Learning platform pages
│   ├── dashboard/      → Progress dashboard (recharts, radar/line charts)
│   ├── news/           → Article pages
│   ├── notifications/  → Notifications history page
│   ├── search/         → Search results page with tabs
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
| Frontend   | Next.js 16, React 19, TypeScript 5, Recharts |
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

## Global Search

- Endpoint: `GET /api/search/?q=<query>&type=<all|articles|lessons|questions|conferences>`
- Uses PostgreSQL full-text search (`SearchVector`, `SearchRank`, `SearchQuery` with `websearch` type)
- GIN indexes on all searchable models for performance
- Returns results grouped by type, max 10 per type, with snippets
- JR users only see `is_junior_safe` articles; only approved articles are searchable
- `AllowAny` permission — works for anonymous users too
- Backend implementation in `core/views.py` (`global_search` + `_search_*` helpers)
- Frontend: Navbar search dropdown (debounced 300ms) + full `/search` results page with tabs
- When adding searchable models: add GIN index, add `_search_<type>` helper in `core/views.py`

## Notifications

- Model in `notifications/models.py` with types: ARTICLE_APPROVED, ARTICLE_REJECTED, NEW_COMMENT, AI_FEEDBACK_READY, STREAK_MILESTONE, SYSTEM
- Triggers via Django signals in `notifications/signals.py` — fires on AIFeedback creation, Article status change (PENDING→APPROVED/REJECTED), Comment creation
- Helper: `notify()` in `notifications/helpers.py` — use this to create notifications
- API endpoints under `/api/notifications/`: list (paginated), `<id>/read/`, `read-all/`, `unread-count/`
- Frontend: Bell icon in Navbar with unread badge, dropdown panel, polls every 60s
- Full notifications page at `/notifications` with all/unread filter
- When adding new notification types: update `Notification.Type` choices, add signal/trigger, update `notifIcons` in Navbar and `NOTIF_ICONS` in notifications page

## Rules

- After writing code, run lint (`cd frontend && npm run lint`) and fix errors before finishing
- Never commit `.env` files or API keys
- Keep DECISIONS.md updated when solving significant bugs or making architectural changes
- See `.claude/rules/` for domain-specific rules (frontend, MUN logic, API standards)
