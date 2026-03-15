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

<!-- Add new entries above this line. Format:
## YYYY-MM-DD — Short Title

**Issue:** What went wrong or what decision was being made.
**Fix:** What was done to resolve it.
**Rule:** What to do (or avoid) in the future to prevent recurrence.
-->
