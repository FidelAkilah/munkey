# MUNKEY — Product Requirements Document (PRD)

**Product Name:** MUNKEY (MUN Global)
**Version:** 1.0 (Current State)
**Last Updated:** 2026-03-15
**Owner:** Fidel Akilah

---

## 1. Product Overview

### 1.1 What is MUNKEY?

MUNKEY is an AI-powered Model United Nations (MUN) learning platform built for Indonesia's MUN circuit. It serves as an all-in-one hub where MUN delegates can learn, practice, get AI coaching, read community news, find conferences, and watch skill tutorials.

### 1.2 Vision

To become the go-to digital platform for MUN delegates in Indonesia (and eventually Southeast Asia), making high-quality MUN training accessible to anyone — from first-time junior delegates to competitive senior delegates aiming for awards at national and international conferences.

### 1.3 Target Users

| User Type | Description | Role Code |
|-----------|-------------|-----------|
| **Junior Delegates** | Elementary & middle school students, new to MUN | `JR` |
| **Senior Delegates** | High school & college students, 1+ conferences of experience | `SR` |
| **Admins/Moderators** | Content moderators, platform managers | `AD` |

### 1.4 Core Value Proposition

- **AI Tutoring (DiplomAI)** — Personalized coaching and feedback on speeches, draft resolutions, and negotiation skills, available 24/7
- **Structured Curriculum** — Organized learning paths from beginner to advanced across all MUN skill areas
- **Community Hub** — MUN news, delegate interviews, preparation guides, and discussion forums
- **Conference Discovery** — Interactive map of MUN conferences across Indonesia

---

## 2. Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Backend | Django 5.1, Django REST Framework 3.15 | Python REST API |
| Frontend | Next.js 16, React 19, TypeScript 5 | SPA with file-based routing |
| Styling | Tailwind CSS 4, Framer Motion | Utility-first CSS, animation library |
| Database | PostgreSQL (Supabase) | Pooled connection on port 6543 |
| AI Engine | OpenAI API (gpt-4o-mini) | Powers DiplomAI coaching |
| Auth | NextAuth 4 + Django SimpleJWT | JWT-based, 24hr token lifetime |
| Frontend Hosting | Vercel | Auto-deploy on push to main |
| Backend Hosting | Render | Gunicorn + WhiteNoise for static files |

---

## 3. Features — Current State

### 3.1 Authentication & User Management

**Status:** Implemented

- Custom `User` model extending Django `AbstractUser`
- Three roles: Junior (`JR`), Senior (`SR`), Admin (`AD`)
- Junior users are auto-restricted (`is_restricted = True`) for content safety
- JWT authentication: NextAuth CredentialsProvider → Django SimpleJWT
- Login, signup, profile pages on frontend
- 24-hour access token lifetime, sliding refresh tokens

**Pages:** `/login`, `/signup`, `/profile`

**Endpoints:**
- `POST /auth/jwt/create/` — Get JWT tokens
- `POST /auth/jwt/refresh/` — Refresh access token
- `POST /auth/users/` — Register new user

### 3.2 DiplomAI — AI Learning Platform (Curriculum)

**Status:** Implemented — Core Feature

The AI-powered curriculum is the flagship feature. It consists of:

#### 3.2.1 Curriculum Categories (6 total)

| Category | Code | Description |
|----------|------|-------------|
| Speech & Public Speaking | `SPEECH` | Opening/closing speeches, delivery, rhetoric |
| Draft Resolution Writing | `DRAFT` | UN formatting (PP/OP clauses), policy, language |
| Negotiation & Diplomacy | `NEGOTIATION` | Bloc building, compromise, caucus strategy |
| Research & Position Papers | `RESEARCH` | Country research, policy analysis, sourcing |
| Rules of Procedure | `PROCEDURE` | Motions, points of order, parliamentary flow |
| General MUN Skills | `GENERAL` | Conference prep, etiquette, mixed exercises |

#### 3.2.2 Lessons

- Each category contains ordered lessons with markdown content
- Three difficulty tiers: Beginner, Intermediate, Advanced
- Includes estimated reading time
- User progress tracked per lesson (`UserProgress` model)

#### 3.2.3 Practice Questions

- AI-generated practice exercises using OpenAI API
- Questions are scenario-based and tied to a specific category
- Include: title, prompt (2-3 paragraphs), hints, sample approach, key concepts
- Question types: `SPEECH`, `DRAFT`, `NEGOTIATION`, `QUIZ`, `OPEN`
- Generated dynamically by `generate_practice_questions()` in `ai_service.py`

#### 3.2.4 Submissions & AI Feedback

- Students submit work as: text, file upload (PDF/TXT), or video URL
- Submissions are reviewed synchronously by DiplomAI on creation
- AI returns structured feedback as JSON:
  ```json
  {
    "overall_score": 0-100,
    "strengths": "bullet points of what's done well",
    "improvements": "bullet points with fix examples",
    "detailed_feedback": "paragraph-form analysis",
    "suggestions": "numbered actionable next steps"
  }
  ```
- One-to-one relationship: each Submission has exactly one AIFeedback
- Category-specific review functions: `review_speech()`, `review_draft_resolution()`, `review_negotiation()`, `review_general()`

#### 3.2.5 DiplomAI Chat (Bongo the Strategist)

- Real-time conversational AI coaching
- Persona: "Bongo the Strategist" — wise, encouraging MUN expert
- Persistent chat sessions via `session_id`
- Context-aware: can reference the specific practice question the user is working on
- Keeps last 20 messages for conversation context
- Responses capped at 300 words (unless deep dive requested)

**Pages:** `/curriculum`, `/curriculum/practice`, `/curriculum/question/[id]`, `/curriculum/submit`

**Endpoints:**
- `GET /api/curriculum/categories/` — List all categories
- `GET /api/curriculum/lessons/` — List lessons
- `GET /api/curriculum/questions/` — List practice questions
- `POST /api/curriculum/submissions/create/` — Submit work + get AI feedback
- `POST /api/curriculum/chat/` — Chat with DiplomAI
- `POST /api/curriculum/generate-questions/` — Generate new AI questions

### 3.3 News & Articles

**Status:** Implemented

- Users can write and submit articles
- Three article categories: Global News (`NW`), Preparation Guides (`GD`), Delegate Interviews (`IN`)
- Admin approval workflow: articles start as `PENDING`, admins approve or reject
- Breaking news flag (`is_breaking`)
- Junior safety flag (`is_junior_safe`) for content filtering
- Rejection includes a reason field for author feedback
- Image support via URL field

**Pages:** `/` (home/feed), `/news`, `/news/[slug]`, `/news/add`, `/news/my-articles`

**Endpoints:**
- `GET /api/news/` — List approved articles
- `GET /api/news/<slug>/` — Article detail
- `POST /api/news/create/` — Submit new article
- `PATCH /api/news/<id>/approve/` — Admin approve
- `PATCH /api/news/<id>/reject/` — Admin reject

### 3.4 Community / Discussion Forum

**Status:** Implemented (Basic)

- Comment system on articles
- Comments tied to articles and users
- Moderation via `is_approved` flag (defaults to `False`)
- Placeholder for AI content moderation (noted in code but not yet implemented)

**Endpoints:**
- `GET /api/community/comments/?article=<id>` — List comments for an article
- `POST /api/community/comments/` — Post a comment

### 3.5 Conference Directory

**Status:** Implemented

- Database of MUN conferences with name, city, country
- Latitude/longitude coordinates for map display
- Active/inactive status and start date
- Google Maps integration on frontend (`MUNMap` component)

**Endpoints:**
- `GET /api/directory/conferences/` — List conferences

### 3.6 Skill Videos (MasterSkills)

**Status:** Implemented

- Categorized YouTube video tutorials
- Categories organized by MUN skill area
- Each video has: title, YouTube URL, video ID, description, difficulty level
- Three difficulty tiers: Beginner, Intermediate, Advanced

**Pages:** `/skills`

**Endpoints:**
- `GET /api/skills/categories/` — List skill categories with videos

### 3.7 Admin Dashboard

**Status:** Implemented (Basic)

- Article review queue for admins
- Approve/reject articles with reasons
- Accessible only to users with `AD` role

**Pages:** `/admin/dashboard`

---

## 4. Data Model Summary

```
User (AbstractUser)
├── role: JR / SR / AD
├── is_restricted: bool (auto-set for JR)
│
├── Article (author)
│   ├── category: NW / GD / IN
│   ├── status: PENDING / APPROVED / REJECTED
│   ├── is_junior_safe, is_breaking
│   └── Comment (many)
│       └── is_approved: bool
│
├── Submission (user)
│   ├── question: FK → PracticeQuestion (optional)
│   ├── category: FK → CurriculumCategory
│   ├── type: TEXT / FILE / VIDEO_URL
│   └── AIFeedback (one-to-one)
│       └── overall_score, strengths, improvements, detailed_feedback, suggestions
│
├── UserProgress (user + lesson)
│   └── completed: bool
│
└── ChatMessage (user)
    ├── session_id, role (user/assistant), content
    └── question: FK → PracticeQuestion (optional)

CurriculumCategory
├── Lesson (ordered, difficulty)
└── PracticeQuestion (type, difficulty, hints, sample_answer)

Conference (name, city, country, lat, lng, start_date, is_active)

SkillCategory
└── SkillVideo (youtube_url, video_id, difficulty)
```

---

## 5. Authentication & Authorization Matrix

| Action | Junior (JR) | Senior (SR) | Admin (AD) |
|--------|:-----------:|:-----------:|:----------:|
| View approved articles | Filtered (junior-safe only) | All | All |
| Write articles | ? | Yes | Yes |
| Approve/reject articles | No | No | Yes |
| Post comments | ? | Yes | Yes |
| Access curriculum | Yes | Yes | Yes |
| Submit work for AI feedback | Yes | Yes | Yes |
| Chat with DiplomAI | Yes | Yes | Yes |
| View skill videos | Yes | Yes | Yes |
| View conference directory | Yes | Yes | Yes |
| Access admin dashboard | No | No | Yes |

> **Note:** Cells marked `?` indicate that role-based restrictions for Juniors are not yet fully enforced on all endpoints.

---

## 6. Infrastructure & Deployment

### 6.1 Architecture Diagram

```
┌──────────────────┐         ┌──────────────────┐
│   Vercel          │         │   Render          │
│   (Frontend)      │  HTTP   │   (Backend)       │
│   Next.js 16      │◄───────►│   Django 5.1      │
│   React 19        │  JWT    │   DRF 3.15        │
│   TypeScript      │         │   Gunicorn        │
│   Tailwind CSS 4  │         │   WhiteNoise      │
└──────────────────┘         └────────┬───────────┘
                                      │
                              ┌───────▼──────────┐
                              │   Supabase        │
                              │   PostgreSQL      │
                              │   (AWS ap-south-1)│
                              └──────────────────┘
                                      │
                              ┌───────▼──────────┐
                              │   OpenAI API      │
                              │   (gpt-4o-mini)   │
                              └──────────────────┘
```

### 6.2 Deployment Flow

1. Push to `main` → Vercel auto-deploys frontend
2. Push to `main` → Render auto-deploys backend (`build.sh`: pip install → collectstatic → migrate)
3. Database migrations run automatically on deploy

### 6.3 URLs

- **Frontend (Production):** https://munkey-zeta.vercel.app
- **Backend API (Production):** https://mun-global.onrender.com
- **Frontend (Development):** http://localhost:3000
- **Backend (Development):** http://localhost:8000

---

## 7. Current Limitations & Known Issues

### 7.1 Missing Features / Gaps

| Area | Gap | Impact |
|------|-----|--------|
| **Testing** | No tests exist — all `tests.py` files are empty, no frontend tests | High — no safety net for regressions |
| **Content Moderation** | Comment `is_approved` defaults to `False` but no AI moderation is implemented | Medium — manual approval not scalable |
| **Junior Safety** | `is_restricted` flag exists but enforcement is incomplete across all endpoints | High — safety gap for younger users |
| **Search** | No search functionality for articles, conferences, or curriculum content | Medium — discoverability issue |
| **User Profiles** | Profile page exists but limited info (no bio, avatar, achievement display) | Low |
| **Notifications** | No notification system for article approvals, comment replies, or AI feedback | Medium |
| **Mobile Responsiveness** | Unknown — no explicit responsive design testing documented | Medium |
| **SEO** | No explicit SEO optimization (meta tags, OG images, sitemap) | Medium — for public content discovery |
| **Analytics** | No user analytics or learning progress dashboards | Medium |
| **Offline Support** | No PWA or offline capabilities | Low |
| **Rate Limiting** | No API rate limiting — OpenAI calls could be abused | High — cost risk |
| **File Storage** | File uploads use local filesystem (`curriculum/uploads/`) — not cloud storage | Medium — won't persist on Render |
| **DOCX Support** | DOCX files flagged as unsupported — users must convert to PDF | Low |
| **Error Monitoring** | No Sentry, LogRocket, or equivalent error tracking | Medium |
| **Email** | No email integration (password reset, article approval notifications) | Medium |
| **i18n** | No internationalization — English only (target market is Indonesia) | Medium — Bahasa Indonesia support needed |

### 7.2 Known Technical Issues

| Issue | Details |
|-------|---------|
| University WiFi blocks Supabase | Use VPN or mobile data for campus development |
| Vercel case-sensitive imports | Must match exact filename casing (e.g., `Navbar.tsx` not `navbar.tsx`) |
| No linting on backend | No flake8, black, or isort configured for Python code |
| No CI/CD pipeline | No GitHub Actions — deploys are push-to-main with no automated checks |

---

## 8. Feature Detail: DiplomAI AI Engine

### 8.1 AI Model Configuration

| Parameter | Value |
|-----------|-------|
| Model | `gpt-4o-mini` |
| Review temperature | 0.6 (more consistent) |
| Question generation temperature | 0.8 (more creative) |
| Chat temperature | 0.7 (balanced) |
| Max tokens (review) | 2,000 |
| Max tokens (chat) | 1,000 |
| Max tokens (questions) | 2,000 |
| Response format | `json_object` (for reviews and questions) |
| Chat context window | Last 20 messages |

### 8.2 Review Pipeline

```
User submits work
    │
    ▼
SubmissionCreateView.perform_create()
    │
    ├── Text submission → use text_content directly
    ├── File upload → extract_text_from_file() (PDF via pypdf, TXT, MD)
    └── Video URL → pass URL as context
    │
    ▼
Category-specific review function
    ├── DRAFT → review_draft_resolution()
    ├── SPEECH → review_speech()
    ├── NEGOTIATION → review_negotiation()
    └── Other → review_general()
    │
    ▼
Parse JSON response → Create AIFeedback record
    │
    ▼
Return submission + feedback to frontend
```

### 8.3 Scoring Guidelines (embedded in prompts)

| Level | Score Range | Description |
|-------|-----------|-------------|
| Beginner | 45–65 | First attempt, fundamentals present |
| Intermediate | 65–80 | Solid structure, room for nuance |
| Advanced | 80–95 | Near award-quality, polished |
| Exceptional | 95–100 | Reserved for truly outstanding work |

---

## 9. Page Inventory

| Route | Auth Required | Description |
|-------|:------------:|-------------|
| `/` | No | Home page — news feed |
| `/login` | No | NextAuth credential login |
| `/signup` | No | User registration |
| `/profile` | Yes | User profile |
| `/news` | No | Article listing |
| `/news/[slug]` | No | Article detail with comments |
| `/news/add` | Yes | Create new article |
| `/news/my-articles` | Yes | User's submitted articles |
| `/curriculum` | Yes | Curriculum categories overview |
| `/curriculum/practice` | Yes | Practice questions listing |
| `/curriculum/question/[id]` | Yes | Individual question + DiplomAI chat |
| `/curriculum/submit` | Yes | Submit work for AI feedback |
| `/skills` | No | Skill video categories + player |
| `/admin/dashboard` | Yes (Admin) | Article approval queue |

---

## 10. API Endpoint Inventory

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/jwt/create/` | Login — get JWT tokens |
| POST | `/auth/jwt/refresh/` | Refresh access token |
| POST | `/auth/users/` | Register new user |

### Curriculum (DiplomAI)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/curriculum/categories/` | List curriculum categories |
| GET | `/api/curriculum/lessons/` | List lessons |
| GET | `/api/curriculum/questions/` | List practice questions |
| POST | `/api/curriculum/submissions/create/` | Submit work + receive AI feedback |
| POST | `/api/curriculum/chat/` | Chat with DiplomAI |
| POST | `/api/curriculum/generate-questions/` | Generate new AI practice questions |

### News
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/news/` | List approved articles |
| GET | `/api/news/<slug>/` | Article detail |
| POST | `/api/news/create/` | Submit new article |
| PATCH | `/api/news/<id>/approve/` | Admin: approve article |
| PATCH | `/api/news/<id>/reject/` | Admin: reject article |

### Community
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/community/comments/` | List comments |
| POST | `/api/community/comments/` | Post comment |

### Directory
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/directory/conferences/` | List conferences |

### Skills
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/skills/categories/` | List skill categories + videos |

---

## 11. Environment Variables

| Variable | Required | Description |
|----------|:--------:|-------------|
| `DEBUG` | Yes | Django debug mode (`True`/`False`) |
| `SECRET_KEY` | Yes | Django secret key |
| `DATABASE_URL` | Yes | PostgreSQL connection string (Supabase) |
| `SIMPLE_JWT_SECRET_KEY` | Yes | JWT signing secret |
| `NEXTAUTH_SECRET` | Yes | NextAuth encryption secret |
| `NEXTAUTH_URL` | Yes | Frontend URL for NextAuth |
| `NEXT_PUBLIC_API_URL` | Yes | Backend API URL (used by frontend) |
| `OPENAI_API_KEY` | Yes | OpenAI API key for DiplomAI |
| `PYTHON_VERSION` | Yes | Python runtime version (3.11.9) |
| `ALLOWED_HOSTS` | Yes | Comma-separated allowed hostnames |

---

## 12. Summary for AI Improvement Analysis

**What MUNKEY does well:**
- Clear separation of concerns (Django API + Next.js SPA)
- AI-powered curriculum with structured feedback is a strong differentiator
- Role-based access control with safety considerations for younger users
- Modern tech stack (Next.js 16, React 19, Tailwind CSS 4)
- Clean data model design

**Where MUNKEY needs improvement:**
- Zero test coverage — no backend or frontend tests
- No CI/CD pipeline — code goes straight from push to production
- Missing content moderation automation (AI moderation placeholder exists but isn't built)
- No rate limiting on AI endpoints (cost and abuse risk)
- File uploads won't persist on Render's ephemeral filesystem
- No search, notifications, email, or analytics
- Incomplete Junior safety enforcement
- No internationalization (target market speaks Bahasa Indonesia)
- No error monitoring (Sentry or equivalent)
- No backend code linting or formatting enforcement

**Key questions for improvement:**
1. How can the user experience be improved to increase engagement and retention?
2. What features are missing that competing MUN platforms offer?
3. How should the AI tutoring be enhanced (better models, more personalization, progress tracking)?
4. What infrastructure changes are needed before scaling to more users?
5. How should content moderation be automated for safety?
6. What monetization strategies could be explored?
7. How can the platform better serve the Indonesian MUN community specifically?
