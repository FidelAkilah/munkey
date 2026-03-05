"""
DiplomAI — AI Service for MUN curriculum feedback.
Powered by OpenAI. Mascot: Bongo the Strategist.
"""
import json
import logging
import io
from django.conf import settings

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None
    logging.getLogger(__name__).warning("pypdf not installed. PDF extraction unavailable.")

logger = logging.getLogger(__name__)

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None
    logger.warning("openai package not installed. AI features will be unavailable.")


DIPLOMAI_SYSTEM_PROMPT = """You are DiplomAI (codename "Bongo"), an expert Model United Nations (MUN) strategist and coach.
You are the AI engine behind MUNKEY, a platform dedicated to MUN excellence.

Your persona:
- Wise, encouraging, and deeply knowledgeable about all aspects of MUN
- You use a professional yet approachable tone — think "senior delegate mentoring a newcomer"
- You sign off important feedback as "— Bongo 🦉"

Your expertise covers:
- Speech & Public Speaking: delivery, structure, rhetoric, persuasion, vocal variety, body language cues
- Draft Resolution Writing: UN formatting (PP/OP clauses), policy feasibility, language precision, diplomatic style
- Negotiation & Diplomacy: bloc building, compromise crafting, lobbying tactics, caucus strategy
- Research & Position Papers: depth, accuracy, sourcing, policy proposals, country alignment
- Rules of Procedure: motions, points, parliamentary flow, chairing best practices
- Conference Strategy: award criteria, committee dynamics, crisis response, portfolio management

When providing feedback:
- Always be encouraging but honest — celebrate what's done well before addressing gaps
- Give specific, actionable improvements with examples when possible
- Reference real MUN best practices, UN document styles, and diplomatic conventions
- Tailor difficulty and depth to the user's apparent skill level
- When generating practice questions, make them scenario-based and realistic
"""

DIPLOMAI_CHAT_PROMPT = """You are DiplomAI (codename "Bongo"), an expert MUN coach integrated into the MUNKEY learning platform.
You are chatting with a delegate who wants to improve their MUN skills.

Guidelines for conversation:
- Be concise but thorough — answer questions clearly without unnecessary padding
- If they ask about a specific practice question, reference it directly and help them think through it
- Offer strategic advice, examples, and tips from real MUN conferences
- If they share their work, give quick constructive feedback
- Use markdown formatting for clarity (bold, bullet points, etc.)
- Keep responses under 300 words unless they ask for a deep dive
- Be encouraging and build their confidence while being honest about areas to improve
- If they seem stuck, offer hints and guiding questions rather than giving away answers
"""


def extract_text_from_file(file_field) -> str:
    """Extract text content from an uploaded file (PDF, TXT, etc.)."""
    if not file_field:
        return ""

    try:
        file_field.seek(0)
        filename = file_field.name.lower()

        if filename.endswith('.pdf'):
            if PdfReader is None:
                return "[PDF file uploaded but pypdf is not installed for text extraction]"
            reader = PdfReader(io.BytesIO(file_field.read()))
            text_parts = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
            return "\n\n".join(text_parts) if text_parts else "[PDF contained no extractable text — it may be a scanned image]"

        elif filename.endswith('.txt') or filename.endswith('.md'):
            return file_field.read().decode('utf-8', errors='replace')

        elif filename.endswith('.docx'):
            return "[DOCX file uploaded — please submit as PDF or paste text directly for best results]"

        else:
            return f"[File uploaded: {filename} — unsupported format for text extraction. Please submit as PDF or paste text.]"

    except Exception as e:
        logger.error(f"File text extraction error: {e}")
        return f"[Error extracting text from file: {str(e)}]"
    finally:
        try:
            file_field.seek(0)
        except Exception:
            pass


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
- "overall_score": integer 0-100 (be fair but encouraging — a solid beginner draft might be 50-65, a good intermediate draft 65-80, an excellent advanced draft 80-95)
- "strengths": string with bullet points of what's done well (be specific — quote exact phrases)
- "improvements": string with bullet points of what needs improvement (give examples of how to fix each issue)
- "detailed_feedback": string with paragraph-form detailed analysis covering structure, content, formatting, and strategy
- "suggestions": string with numbered actionable next steps the delegate can take immediately

Focus on: preambulatory clause structure (PP), operative clause structure (OP), UN formatting conventions, policy feasibility, language precision, diplomatic tone, and whether the resolution addresses the actual issue comprehensively.
If the student is clearly a beginner, be encouraging and focus on 2-3 key improvements rather than overwhelming them."""

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
- "overall_score": integer 0-100 (be fair — a decent first speech might score 45-60, a strong intermediate speech 65-80, an award-winning speech 85-100)
- "strengths": string with bullet points of what's done well (quote specific phrases or structural elements)
- "improvements": string with bullet points of what needs improvement (provide concrete examples and rewrites where helpful)
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": string with numbered actionable next steps

Focus on: opening hook effectiveness, argument structure and flow, rhetorical devices (anaphora, tricolon, etc.), diplomatic language vs. aggressive tone, use of evidence and statistics, emotional appeal balance, closing impact and call to action.
Assess whether the speech would be effective in a real MUN committee and suggest committee-specific strategies."""

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
- "strengths": string with bullet points of what's done well (be specific about diplomatic strategy)
- "improvements": string with bullet points of what needs improvement (suggest alternative approaches)
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": string with numbered actionable next steps

Focus on: strategic thinking and long-term planning, coalition/bloc awareness and building, compromise proposals and their feasibility, diplomatic language and tact, realistic policy approaches that align with country positions, understanding of power dynamics within the committee.
Consider whether the approach would realistically achieve the delegate's goals in a committee setting."""

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

    difficulty_desc = {
        "BEG": "Beginner — suitable for first-time or novice MUN delegates. Focus on fundamentals, basic formatting, and introductory scenarios.",
        "INT": "Intermediate — for delegates with 2-5 conferences of experience. Include nuanced scenarios, multi-party dynamics, and more complex topics.",
        "ADV": "Advanced — for experienced delegates competing at national/international level. Include crisis scenarios, advanced drafting, and sophisticated strategy challenges.",
    }.get(difficulty, "Intermediate")

    category_guidance = {
        "SPEECH": "Focus on opening statements, general debate speeches, and caucus interventions. Include specific country positions on real-world issues.",
        "DRAFT": "Focus on resolution drafting with proper PP/OP clause structure. Include real UN topics and require proper formatting.",
        "NEGOTIATION": "Create multi-party negotiation scenarios with conflicting interests and potential compromise zones. Include bloc dynamics.",
        "RESEARCH": "Focus on position paper writing, country research methodology, and policy analysis for specific agenda items.",
        "PROCEDURE": "Cover motions, points of order, voting procedures, and parliamentary flow. Include scenario-based procedural challenges.",
        "GENERAL": "Mix of general MUN skills including conference preparation, committee strategy, and delegate etiquette.",
    }.get(category_type, "General MUN practice exercises.")

    user_prompt = f"""Generate {count} MUN practice exercises.

Category: {category_type}
Difficulty: {difficulty_desc}
Category Guidance: {category_guidance}

Return as a JSON array where each item has:
- "title": short, engaging exercise title (5-10 words)
- "prompt": detailed exercise prompt/scenario (2-3 paragraphs with specific context, country names, committee names, and realistic details)
- "hints": 2-3 helpful hints for the student, separated by semicolons
- "question_type": one of SPEECH, DRAFT, NEGOTIATION, QUIZ, OPEN
- "key_concepts": comma-separated list of 3-5 key MUN concepts this exercise tests
- "sample_approach": a brief 2-sentence description of how a strong delegate would approach this

Make them realistic, educational, and based on actual UN committees and real-world issues.
Ensure progressively challenging content within the difficulty tier."""

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


def chat_with_diplomai(messages: list, question_context: str = "") -> str:
    """
    Have a conversation with DiplomAI.
    
    Args:
        messages: List of dicts with 'role' and 'content' keys (conversation history)
        question_context: Optional context about the current practice question
    
    Returns:
        The assistant's response text
    """
    client = get_client()

    system_msg = DIPLOMAI_CHAT_PROMPT
    if question_context:
        system_msg += f"\n\nThe delegate is currently working on this practice exercise:\n{question_context}\n\nHelp them with this exercise specifically if they ask about it."

    openai_messages = [{"role": "system", "content": system_msg}]
    
    # Include up to last 20 messages for context
    for msg in messages[-20:]:
        openai_messages.append({
            "role": msg["role"],
            "content": msg["content"],
        })

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=openai_messages,
            temperature=0.7,
            max_tokens=1000,
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"DiplomAI chat error: {e}")
        return "I'm having trouble processing your message right now. Please try again in a moment! — Bongo 🦉"
