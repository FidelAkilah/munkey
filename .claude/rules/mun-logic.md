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
    "strengths": "bullet points",
    "improvements": "bullet points with examples",
    "detailed_feedback": "paragraph analysis",
    "suggestions": "numbered actionable steps"
  }
  ```
- Practice questions must include: title, prompt, hints, sample_answers
- Chat sessions use a `session_id` for conversation persistence

## Submissions
- Submission → AIFeedback is a **one-to-one** relationship
- Supported file types: PDF (via pypdf), TXT, MD
- DOCX is not supported — prompt users to convert to PDF
- Feedback is generated synchronously in `SubmissionCreateView.perform_create()`
- Submission types: TEXT, FILE, VIDEO_URL

## Content Safety
- Junior (JR) users must only see content flagged `is_junior_safe=True`
- Articles require admin approval before being visible (status: PENDING → APPROVED)
- Comments have an `is_approved` flag for moderation
- Never expose raw user data or API keys to the frontend

## Article Workflow
- Categories: NEWS, GUIDE, INTERVIEW
- Status flow: PENDING → APPROVED or REJECTED
- Only Admin (AD) users can approve/reject articles via the admin dashboard
