# MUN Domain Logic Rules

## Curriculum Categories
There are exactly 6 curriculum categories. Do not add or rename them without updating both backend models and frontend:
- **SPEECH** — Opening/closing speeches, position statements
- **DRAFT** — Draft resolutions (preambulatory + operative clauses)
- **NEGOTIATION** — Bloc formation, compromise strategies
- **RESEARCH** — Country research, policy analysis
- **PROCEDURE** — Rules of procedure, Points of Order, motions
- **GENERAL** — Mixed MUN exercises

## DiplomAI (AI Tutor)
- Persona: "Bongo the Strategist" — wise, encouraging MUN expert
- All AI prompts live in `curriculum/ai_service.py` — keep them centralized
- AI feedback must return this JSON structure:
  ```json
  {
    "overall_score": 0-100,
    "rubric_scores": {
      "criterion_name": {"score": 0, "max": N, "comment": "explanation"}
    },
    "strengths": ["bullet points"],
    "improvements": ["bullet points with examples"],
    "detailed_feedback": "paragraph analysis",
    "suggestions": ["numbered actionable steps"],
    "example_revision": "rewritten version of the student's weakest section"
  }
  ```
- Each review function has its own rubric criteria (speech: 6 criteria, draft: 5, negotiation: 5, general: 4)
- `_format_list_field()` converts array responses to bullet-point strings for DB storage
- Practice questions must include: title, prompt, hints, sample_answers
- Chat sessions use `ChatSession` model (session_id, mode, simulation_config) + `ChatMessage` for individual messages
- Chat modes: `general` (Bongo coaches) and `simulation` (Bongo roleplays as a delegate via `DIPLOMAI_SIMULATION_PROMPT`)
- Chat context window: first message + last 15 messages (via `_build_chat_messages()`)
- `MUNTip` model stores curated tips; `GET /api/curriculum/tip-of-the-day/` rotates daily
- Seed tips with `python manage.py seed_tips` (35 tips across all 6 categories)

## Submissions
- Submission → AIFeedback is a **one-to-one** relationship
- Supported file types: PDF (via pypdf), TXT, MD
- DOCX is not supported — prompt users to convert to PDF
- Feedback is generated synchronously in `SubmissionCreateView.perform_create()`
- Submission types: TEXT, FILE, VIDEO_URL
- Submissions/create is rate-limited to 20/hour per user via `AIEndpointThrottle`

## OpenAI Cost Protection
- `APIUsageLog` model tracks every OpenAI API call (user, endpoint, estimated_tokens, model_name, timestamp)
- Before every OpenAI call, `check_daily_token_limit()` in `ai_service.py` checks if daily total exceeds `DAILY_TOKEN_LIMIT` (env var, default 500,000). If exceeded, raises `Throttled` → returns 429 with "Our AI tutor is resting for today."
- All AI service functions (`review_*`, `generate_practice_questions`, `chat_with_diplomai`) accept a `user=` kwarg for logging. Always pass `user=request.user` from views.
- `log_api_usage()` extracts `response.usage.total_tokens` from the OpenAI response after each call
- Management command: `python manage.py check_api_usage [--days N]` prints usage by endpoint and user

## Progress Tracking & UserStats
- `UserStats` model (OneToOne with User) stores aggregated stats: `total_submissions`, `average_score`, `best_score`, `current_streak_days`, `longest_streak_days`, `last_active_date`, `scores_by_category` (JSONField)
- Updated automatically via `post_save` signal on `AIFeedback` in `curriculum/signals.py` — never update manually in views
- Streak logic: increments if user submitted yesterday, resets if gap > 1 day, no-op if same day
- Rank badges computed in `UserStatsSerializer.get_rank_badge()`: Novice (0-44), Junior (45-64), Senior (65-79), Distinguished (80-89), Best Delegate (90+)
- `GET /api/curriculum/user-stats/` — returns full UserStats with rank badge
- `GET /api/curriculum/user-progress/` — lessons/questions per category, score trend, weakest category suggestion
- `GET /api/curriculum/recommendations/` — lessons and questions for weakest category at appropriate difficulty
- Seed command: `python manage.py seed_user_stats` — backfills UserStats for existing users
- Frontend dashboard at `/dashboard` uses Recharts (radar chart + line chart)

## Content Safety
- Junior (JR) users must only see content flagged `is_junior_safe=True`
- Articles require admin approval before being visible (status: PENDING → APPROVED)
- Comments have an `is_approved` flag for moderation
- Never expose raw user data or API keys to the frontend

## Article Workflow
- Categories: NEWS, GUIDE, INTERVIEW
- Status flow: PENDING → APPROVED or REJECTED
- Only Admin (AD) users can approve/reject articles via the admin dashboard
- Article creation is rate-limited to 10/hour per user via `NewsCreateThrottle`

## Global Search
- `GET /api/search/?q=<query>&type=<all|articles|lessons|questions|conferences>` in `core/views.py`
- Uses PostgreSQL `SearchVector` + `SearchRank` + `SearchQuery` (websearch type) with GIN indexes
- Searchable models: `Article` (title+content), `Lesson` (title+content), `PracticeQuestion` (title+prompt), `Conference` (name+city+country)
- Only `APPROVED` articles appear in search results
- JR users only see articles with `is_junior_safe=True`
- `AllowAny` permission — anonymous users can search
- When adding a new searchable model: add `GinIndex(SearchVector(...))` in model Meta, create a `_search_<type>` helper in `core/views.py`, add the type to the dispatch map in `global_search`
- Frontend: Navbar dropdown (300ms debounce) + `/search` results page with tabs per content type
