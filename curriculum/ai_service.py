"""
DiplomAI — AI Service for MUN curriculum feedback.
Powered by OpenAI. Mascot: Bongo the Strategist.
"""
import json
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None
    logger.warning("openai package not installed. AI features will be unavailable.")


DIPLOMAI_SYSTEM_PROMPT = """You are DiplomAI, an expert Model United Nations (MUN) coach and strategist. 
Your mascot is Bongo the Strategist — a wise, encouraging owl who guides delegates toward excellence.

Your role is to provide detailed, constructive, and actionable feedback on MUN-related submissions.
You are an expert on:
- Speech & Public Speaking (delivery, structure, rhetoric, persuasion)
- Draft Resolution Writing (format, operative/preambulatory clauses, UN style)
- Negotiation & Diplomacy (bloc building, compromise, lobbying tactics)
- Research & Position Papers (depth, accuracy, policy proposals)
- Rules of Procedure (motions, points, parliamentary procedure)

Always:
- Be encouraging but honest
- Point out specific strengths
- Give specific, actionable improvements
- Reference MUN best practices
- Use a professional yet approachable tone
- Sign off feedback as "— Bongo 🦉"
"""


def get_client():
    """Get OpenAI client with API key from settings."""
    api_key = getattr(settings, 'OPENAI_API_KEY', None)
    if not api_key:
        raise ValueError("OPENAI_API_KEY not configured in settings.")
    if OpenAI is None:
        raise ImportError("openai package is not installed. Run: pip install openai")
    return OpenAI(api_key=api_key)


def review_draft_resolution(text_content: str, question_prompt: str = "") -> dict:
    """Review a draft resolution submission."""
    client = get_client()

    user_prompt = f"""Please review this MUN draft resolution submission.

{f'Exercise prompt: {question_prompt}' if question_prompt else ''}

=== DRAFT RESOLUTION ===
{text_content}
=== END ===

Provide your review as JSON with these exact keys:
- "overall_score": integer 0-100
- "strengths": string with bullet points of what's done well
- "improvements": string with bullet points of what needs improvement  
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": string with numbered actionable next steps

Focus on: clause structure, UN formatting, policy feasibility, language precision, and diplomatic tone."""

    return _call_openai(client, user_prompt)


def review_speech(text_content: str = "", video_url: str = "", question_prompt: str = "") -> dict:
    """Review a speech submission (text transcript or general feedback on description)."""
    client = get_client()

    content_desc = text_content if text_content else f"Speech video submitted at: {video_url}"

    user_prompt = f"""Please review this MUN speech submission.

{f'Exercise prompt: {question_prompt}' if question_prompt else ''}

=== SPEECH CONTENT ===
{content_desc}
=== END ===

Provide your review as JSON with these exact keys:
- "overall_score": integer 0-100
- "strengths": string with bullet points of what's done well
- "improvements": string with bullet points of what needs improvement
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": string with numbered actionable next steps

Focus on: opening hook, argument structure, rhetorical devices, diplomatic language, persuasiveness, and closing impact."""

    return _call_openai(client, user_prompt)


def review_negotiation(text_content: str, question_prompt: str = "") -> dict:
    """Review a negotiation scenario response."""
    client = get_client()

    user_prompt = f"""Please review this MUN negotiation/diplomacy exercise response.

{f'Scenario: {question_prompt}' if question_prompt else ''}

=== RESPONSE ===
{text_content}
=== END ===

Provide your review as JSON with these exact keys:
- "overall_score": integer 0-100
- "strengths": string with bullet points of what's done well
- "improvements": string with bullet points of what needs improvement
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": string with numbered actionable next steps

Focus on: strategic thinking, coalition awareness, compromise proposals, diplomatic language, and realistic policy approaches."""

    return _call_openai(client, user_prompt)


def review_general(text_content: str, question_prompt: str = "") -> dict:
    """General review for any MUN-related submission."""
    client = get_client()

    user_prompt = f"""Please review this MUN practice submission.

{f'Exercise prompt: {question_prompt}' if question_prompt else ''}

=== SUBMISSION ===
{text_content}
=== END ===

Provide your review as JSON with these exact keys:
- "overall_score": integer 0-100
- "strengths": string with bullet points of what's done well
- "improvements": string with bullet points of what needs improvement
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": string with numbered actionable next steps"""

    return _call_openai(client, user_prompt)


def generate_practice_questions(category_type: str, difficulty: str = "INT", count: int = 3) -> list:
    """Generate practice questions dynamically using AI."""
    client = get_client()

    user_prompt = f"""Generate {count} MUN practice exercises for the category: {category_type}
Difficulty level: {difficulty}

Return as a JSON array where each item has:
- "title": short exercise title
- "prompt": detailed exercise prompt/scenario (2-3 paragraphs)
- "hints": helpful hints for the student
- "question_type": one of SPEECH, DRAFT, NEGOTIATION, QUIZ, OPEN

Make them realistic, educational, and progressively challenging."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": DIPLOMAI_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.8,
            max_tokens=2000,
        )
        content = response.choices[0].message.content
        parsed = json.loads(content)
        # Handle both {"questions": [...]} and direct array
        if isinstance(parsed, list):
            return parsed
        return parsed.get("questions", parsed.get("exercises", []))
    except Exception as e:
        logger.error(f"DiplomAI question generation error: {e}")
        return []


def _call_openai(client, user_prompt: str) -> dict:
    """Internal helper to call OpenAI and parse response."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": DIPLOMAI_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.6,
            max_tokens=2000,
        )

        content = response.choices[0].message.content
        parsed = json.loads(content)

        return {
            "overall_score": int(parsed.get("overall_score", 0)),
            "strengths": parsed.get("strengths", ""),
            "improvements": parsed.get("improvements", ""),
            "detailed_feedback": parsed.get("detailed_feedback", ""),
            "suggestions": parsed.get("suggestions", ""),
        }

    except Exception as e:
        logger.error(f"DiplomAI review error: {e}")
        return {
            "overall_score": 0,
            "strengths": "",
            "improvements": "",
            "detailed_feedback": f"DiplomAI encountered an error processing your submission. Please try again. (Error: {str(e)})",
            "suggestions": "Try resubmitting, or contact support if the issue persists.",
        }
