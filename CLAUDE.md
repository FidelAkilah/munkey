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
core/            → Django settings, authentication middleware, URL routing
curriculum/      → DiplomAI learning platform (AI feedback, chat, questions)
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
├── components/         → Shared components (Navbar, Footer, MUNMap)
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
| AI         | OpenAI API (gpt-3.5-turbo / gpt-4)     |
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
OPENAI_API_KEY, PYTHON_VERSION, ALLOWED_HOSTS
```

## Production URLs

- Frontend: https://munkey-zeta.vercel.app
- Backend API: https://mun-global.onrender.com

## Rules

- After writing code, run lint (`cd frontend && npm run lint`) and fix errors before finishing
- Never commit `.env` files or API keys
- Keep DECISIONS.md updated when solving significant bugs or making architectural changes
- See `.claude/rules/` for domain-specific rules (frontend, MUN logic, API standards)
