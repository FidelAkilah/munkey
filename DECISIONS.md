# DECISIONS.md — Project Memory

This is a living history of significant bugs, fixes, and architectural decisions. Update this file whenever a notable issue is resolved or an important design choice is made, so AI agents and future contributors don't repeat past mistakes.

---

## 2026-03-15 — Context Engineering Setup

**Decision:** Added CLAUDE.md, AGENTS.md, .github/copilot-instructions.md, and .claude/rules/ to provide AI agents with structured project context.
**Why:** AI agents start each session with a blank slate. These files give them a map of the codebase, coding standards, and domain-specific rules so they produce better code from the first prompt.

---

## 2026-03-14 — Auth Fixes (commits f293af6, 78db94b)

**Issue:** Authentication was broken between frontend and backend.
**Fix:** Fixed JWT token handling in NextAuth ↔ Django SimpleJWT integration.
**Rule:** Always test auth flow end-to-end (login → token → API call) after touching `core/authentication.py`, `frontend/src/app/api/auth/[...nextauth]/route.ts`, or JWT settings.

---

## 2026-03-14 — AI Generated Questions Fix (commit ed4b219)

**Issue:** AI-generated practice questions were failing.
**Fix:** Updated question generation logic in `curriculum/ai_service.py`.
**Rule:** When modifying AI prompts, verify the response JSON structure matches what the frontend expects (title, prompt, hints, sample_answers).

---

## 2026-03-14 — Submission Error Fix (commit 6893082)

**Issue:** Submissions were returning errors.
**Fix:** Fixed submission creation flow in curriculum views.
**Rule:** Submission → AIFeedback is a one-to-one relationship. Always ensure feedback is created atomically with the submission in `SubmissionCreateView.perform_create()`.

---

## 2026-03-15 — Practice Question Bank Redesign

**Decision:** Replaced on-the-fly AI question generation with a seeded question bank (180+ curated questions in DB). Added `is_seeded`, `quality_score`, and `key_concepts` fields to `PracticeQuestion`. Created `seed_questions` management command. AI generation kept as supplement (capped at 50 per category+difficulty combo) and now saves to DB.
**Why:** On-the-fly generation via OpenAI was expensive, slow, and produced inconsistent quality. A curated bank gives instant, reliable questions while AI supplements the library.
**Rule:**
- Run `python manage.py seed_questions` after fresh deploys or DB resets to populate the question bank.
- Use `--flush` flag to replace all seeded questions: `python manage.py seed_questions --flush`.
- The question listing API now returns seeded questions first (ordered by `-is_seeded, -created_at`).
- New query params on `/api/curriculum/questions/`: `source=seeded|ai|all`, `difficulty=beginner|intermediate|advanced`, pagination (20/page).
- New endpoint: `GET /api/curriculum/question-of-the-day/` — rotates daily from seeded questions.
- Frontend: Daily Challenge card on `/curriculum` page fetches question-of-the-day.

---

## 2026-03-15 — Curriculum Page Client-Side Crash Fix

**Issue:** The `/curriculum/practice` page threw a client-side exception ("Application error") because the `PracticeQuestionListView` returns paginated JSON (`{count, next, results: [...]}`) but the frontend did `setQuestions(await res.json())` expecting a plain array. Calling `.map()` on the paginated object crashed React.
**Fix:** Updated `practice/page.tsx` and `curriculum/page.tsx` to handle both paginated and plain array responses: `Array.isArray(data) ? data : data.results || []`. Also added optional chaining on `dailyQuestion.question.prompt?.slice()`.
**Rule:** When consuming DRF list endpoints, always check if the response is paginated (`data.results`) or a plain array. Any view with a `pagination_class` returns `{count, next, previous, results}`, not a bare array.

---

## Deployment Notes

**Issue:** University WiFi may block Supabase database connections.
**Fix:** Use VPN or mobile data when developing on campus.

**Issue:** Vercel is case-sensitive for file imports.
**Fix:** Always match exact casing in import paths (e.g., `Navbar.tsx` not `navbar.tsx`).
**Rule:** Use PascalCase for component filenames, lowercase for utility files.

---

## 2026-03-15 — AI Feedback Rubric Upgrade

**Decision:** Overhauled the DiplomAI feedback system with MUN-specific rubrics for each submission type, an `example_revision` field, and a visual rubric breakdown on the frontend.
**What changed:**
- `ai_service.py`: Each review function (`review_speech`, `review_draft_resolution`, `review_negotiation`, `review_general`) now includes a detailed scoring rubric in its prompt. The AI returns per-criterion scores (e.g., Hook/Opening 0-15, Country Position Clarity 0-20, etc.) and a rewritten example of the student's weakest section.
- `AIFeedback` model: Added `rubric_scores` (JSONField, nullable) and `example_revision` (TextField, nullable) — existing records are unaffected.
- `_call_openai()`: Now parses `rubric_scores`, `example_revision`, and converts array-format strengths/improvements/suggestions to bullet-point strings via `_format_list_field()`. Max tokens increased to 3000.
- Serializers & views updated to pass through new fields.
- Frontend (`submit/page.tsx`, `question/[id]/page.tsx`): Added colored progress bars for each rubric criterion and a "Here's How to Improve" example revision box.
**Why:** Generic feedback wasn't actionable enough. Rubric-based scoring tells students exactly where they're strong/weak, and the example revision is the #1 learning tool for MUN delegates.
**Rule:**
- AI feedback JSON must always include `rubric_scores` (object of `{criterion: {score, max, comment}}`) and `example_revision` (string). The `_call_openai` helper handles both gracefully if the AI omits them.
- When adding a new submission category, define its rubric criteria in the review function prompt and use matching snake_case keys in `rubric_scores`.
- Migration `0004_aifeedback_example_revision_aifeedback_rubric_scores` — both fields are nullable so existing data is safe.

---

## 2026-03-16 — DiplomAI Chat Upgrade: Simulation Mode, Tips, Smart Context

**Decision:** Major upgrade to the DiplomAI chat system with four new features.
**What changed:**
1. **Simulation Mode** — New `ChatSession` model tracks session mode (`general` | `simulation`) and `simulation_config` (JSON: role, country, topic, stance). `DIPLOMAI_SIMULATION_PROMPT` in `ai_service.py` makes Bongo roleplay in-character as a delegate. Chat endpoint accepts `mode` and `simulation_config` parameters.
2. **MUNTip Model + Tip of the Day** — New `MUNTip` model (content, category, difficulty, is_active). Seeded with 35 curated tips via `python manage.py seed_tips`. Endpoint `GET /api/curriculum/tip-of-the-day/` rotates daily. Displayed as a dismissible banner above the chat.
3. **Smart Chat Context** — Replaced "last 20 messages" with `_build_chat_messages()`: always includes the first message (sets context) + last 15 messages. Avoids losing the opening context in long conversations.
4. **Quick Action Buttons** — `QUICK_ACTIONS` constant array in the frontend with 5 preset buttons (practice speech, simulate caucus, write clauses, RoP quiz, review position paper). Each sends a pre-configured message.
5. **New Conversation** — Button clears session state and starts fresh.
**Why:** The generic chatbot wasn't exercising students' skills. Simulation mode forces them to think on their feet against a realistic opponent. Tips provide passive learning. Smart context prevents lost context in long sessions.
**Rule:**
- Chat sessions now persist in `ChatSession` model — the `session_id` foreign key approach is preserved on `ChatMessage` for backward compatibility.
- When adding simulation roles, update the `<select>` options in `question/[id]/page.tsx` and the prompt in `DIPLOMAI_SIMULATION_PROMPT`.
- Run `python manage.py seed_tips` after fresh deploys to populate the tip bank.
- Migration `0005_muntip_chatsession`.

---

## 2026-03-16 — Rate Limiting & OpenAI Cost Protection

**Issue:** No rate limiting on any API endpoints. AI endpoints (chat, submissions, generate-questions) were completely unprotected — risk of abuse and runaway OpenAI costs.
**Decision:** Added comprehensive rate limiting using DRF's built-in throttling framework, plus an `APIUsageLog` model for daily OpenAI spend tracking.
**What changed:**
1. **DRF Throttling** (`core/throttling.py`): Custom throttle classes with proper 429 JSON responses and `Retry-After` / `X-RateLimit-*` headers.
   - AI endpoints (chat, submissions/create, generate-questions): **20 requests/hour** per user
   - Auth endpoints (JWT login/refresh): **5 requests/min** per IP
   - News creation: **10 requests/hour** per user
   - All other GET endpoints: **100 requests/min** per user (default)
2. **OpenAI Cost Protection** (`curriculum/models.py: APIUsageLog`): Every OpenAI call logs user, endpoint, estimated_tokens, timestamp. Before each call, `check_daily_token_limit()` rejects with 429 if daily total exceeds `DAILY_TOKEN_LIMIT` env var (default: 500,000 tokens).
3. **Management Command**: `python manage.py check_api_usage [--days N]` prints token usage stats by endpoint and user.
4. **Frontend 429 Handling**: `RateLimitToastProvider` wraps the app. `apiFetch()` wrapper in `src/lib/api.ts` detects 429 responses and triggers a user-friendly toast: "You've been practicing a lot! Please wait X minutes before submitting again." or "Our AI tutor is resting for today."
5. **Auth Throttling**: Throttled wrappers for djoser JWT views in `core/views.py`, registered before djoser includes in `core/urls.py`.
6. **CORS**: Added `X-RateLimit-*` and `Retry-After` to `CORS_EXPOSE_HEADERS`.
**Why:** Open AI endpoints are a cost and abuse risk. Rate limiting protects both the budget and the user experience. The daily token cap prevents unexpected OpenAI bills.
**Rule:**
- When adding new AI-powered endpoints, apply `AIEndpointThrottle` and call `check_daily_token_limit()` before the OpenAI call.
- Pass `user=request.user` to all AI service functions for usage logging.
- Migration `0006_apiusagelog`.
- New env var: `DAILY_TOKEN_LIMIT` (default 500000). Set in `.env` or Render dashboard.
- Frontend pages that call throttled endpoints must use `apiFetch()` from `src/lib/api.ts` and handle `RateLimitError`.

---

<!-- Add new entries above this line. Format:
## YYYY-MM-DD — Short Title

**Issue:** What went wrong or what decision was being made.
**Fix:** What was done to resolve it.
**Rule:** What to do (or avoid) in the future to prevent recurrence.
-->
