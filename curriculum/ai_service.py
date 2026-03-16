"""
DiplomAI — AI Service for MUN curriculum feedback.
Powered by OpenAI. Mascot: Bongo the Strategist.
"""
import json
import logging
import io
from django.conf import settings
from rest_framework.exceptions import Throttled

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


def check_daily_token_limit():
    """Check if we've exceeded the daily OpenAI token limit.

    Raises Throttled if the limit is exceeded so DRF returns a proper 429.
    """
    from .models import APIUsageLog
    ok, used = APIUsageLog.check_daily_limit()
    if not ok:
        raise Throttled(
            wait=None,
            detail="Our AI tutor is resting for today. Please try again tomorrow!",
        )


def log_api_usage(user, endpoint, estimated_tokens, model_name='gpt-4o-mini'):
    """Log an OpenAI API call for cost tracking."""
    from .models import APIUsageLog
    try:
        APIUsageLog.objects.create(
            user=user,
            endpoint=endpoint,
            estimated_tokens=estimated_tokens,
            model_name=model_name,
        )
    except Exception as e:
        logger.error(f"Failed to log API usage: {e}")


def get_client():
    """Get OpenAI client with API key from settings."""
    api_key = getattr(settings, 'OPENAI_API_KEY', None)
    if not api_key:
        raise ValueError("OPENAI_API_KEY not configured in settings.")
    if OpenAI is None:
        raise ImportError("openai package is not installed. Run: pip install openai")
    return OpenAI(api_key=api_key)


def review_draft_resolution(text_content: str, question_prompt: str = "", user=None) -> dict:
    """Review a draft resolution submission against a detailed rubric."""
    client = get_client()

    user_prompt = f"""Please review this MUN draft resolution submission.

{f'Exercise prompt: {question_prompt}' if question_prompt else ''}

=== DRAFT RESOLUTION ===
{text_content}
=== END ===

Score this submission against EACH of these rubric criteria:
1. UN Format Compliance (0-20): Correct preambulatory/operative clause structure? Proper formatting (italicized PP verbs, numbering, sponsor/signatory block)?
2. Clause Quality (0-25): Are operative clauses specific, actionable, and measurable? Do PP clauses cite real precedents?
3. Legal Language (0-15): Proper UN terminology used correctly ("Requests", "Urges", "Decides", "Reaffirming", "Noting with concern")? Diplomatic register maintained?
4. Feasibility (0-20): Are proposals realistic, implementable, and fundable? Do they respect state sovereignty?
5. Comprehensiveness (0-20): Does it address root causes, multiple dimensions, and affected stakeholders?

Return your review as JSON with these exact keys:
- "overall_score": integer 0-100 (sum of rubric scores; a solid beginner draft might be 40-55, intermediate 55-75, excellent advanced 80-95)
- "rubric_scores": object where each key is the criterion name and value is {{"score": integer, "max": integer, "comment": "1-2 sentence explanation"}}. Use these exact keys: "un_format_compliance", "clause_quality", "legal_language", "feasibility", "comprehensiveness"
- "strengths": array of 3-5 specific strength bullet points (quote exact phrases from the submission)
- "improvements": array of 3-5 specific improvement bullet points (include concrete examples of how to fix each)
- "detailed_feedback": string with paragraph-form detailed analysis covering structure, content, formatting, and strategy
- "suggestions": array of 3-5 numbered actionable next steps
- "example_revision": string showing a rewritten version of the student's WEAKEST section, demonstrating how to improve it. Pick the lowest-scoring rubric area and rewrite their actual text to show what a stronger version looks like.

If the student is clearly a beginner, be encouraging and focus on 2-3 key improvements rather than overwhelming them."""

    return _call_openai(client, user_prompt, user=user, endpoint="review_draft")


def review_speech(text_content: str = "", video_url: str = "", question_prompt: str = "", user=None) -> dict:
    """Review a speech submission against a detailed rubric."""
    client = get_client()

    content_desc = text_content if text_content else f"Speech video submitted at: {video_url}"

    user_prompt = f"""Please review this MUN speech submission.

{f'Exercise prompt: {question_prompt}' if question_prompt else ''}

=== SPEECH CONTENT ===
{content_desc}
=== END ===

Score this submission against EACH of these rubric criteria:
1. Hook/Opening (0-15): Does it grab attention? Is it relevant to the topic? Does it set the tone?
2. Country Position Clarity (0-20): Is the national policy clearly stated? Does the delegate speak authentically from their country's perspective?
3. Evidence & Examples (0-20): Are there specific facts, statistics, treaties, or precedents cited? Are sources credible?
4. Structure & Flow (0-15): Logical progression from problem → position → solution? Smooth transitions?
5. Call to Action (0-15): Clear, actionable proposals for the committee? Does it inspire collaboration?
6. Delivery Notes (0-15): Language appropriate for diplomatic setting? Persuasive tone without aggression? Rhetorical devices used effectively?

Return your review as JSON with these exact keys:
- "overall_score": integer 0-100 (sum of rubric scores; a decent first speech might score 40-55, strong intermediate 60-75, award-winning 85-100)
- "rubric_scores": object where each key is the criterion name and value is {{"score": integer, "max": integer, "comment": "1-2 sentence explanation"}}. Use these exact keys: "hook_opening", "country_position_clarity", "evidence_examples", "structure_flow", "call_to_action", "delivery_notes"
- "strengths": array of 3-5 specific strength bullet points (quote exact phrases from the speech)
- "improvements": array of 3-5 specific improvement bullet points (include concrete rewrites where helpful)
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": array of 3-5 numbered actionable next steps
- "example_revision": string showing a rewritten version of the student's WEAKEST section. Pick the lowest-scoring rubric area and rewrite their actual text to show what a stronger version looks like. If the hook scored lowest, rewrite their opening. If evidence scored lowest, show how to weave in specific data.

Assess whether the speech would be effective in a real MUN committee."""

    return _call_openai(client, user_prompt, user=user, endpoint="review_speech")


def review_negotiation(text_content: str, question_prompt: str = "", user=None) -> dict:
    """Review a negotiation scenario response against a detailed rubric."""
    client = get_client()

    user_prompt = f"""Please review this MUN negotiation/diplomacy exercise response.

{f'Scenario: {question_prompt}' if question_prompt else ''}

=== RESPONSE ===
{text_content}
=== END ===

Score this submission against EACH of these rubric criteria:
1. Strategy Clarity (0-20): Is the negotiation approach well-defined? Are goals and red lines clear?
2. Stakeholder Awareness (0-20): Understanding of other parties' positions, interests, and constraints?
3. Compromise Proposals (0-25): Creative, mutually beneficial solutions? Are trade-offs realistic?
4. Communication Tactics (0-20): Diplomatic language, persuasion techniques, framing? Avoids alienating potential allies?
5. Adaptability (0-15): Contingency plans if initial approach fails? Flexibility without abandoning core interests?

Return your review as JSON with these exact keys:
- "overall_score": integer 0-100 (sum of rubric scores)
- "rubric_scores": object where each key is the criterion name and value is {{"score": integer, "max": integer, "comment": "1-2 sentence explanation"}}. Use these exact keys: "strategy_clarity", "stakeholder_awareness", "compromise_proposals", "communication_tactics", "adaptability"
- "strengths": array of 3-5 specific strength bullet points (reference specific diplomatic strategies used)
- "improvements": array of 3-5 specific improvement bullet points (suggest alternative approaches)
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": array of 3-5 numbered actionable next steps
- "example_revision": string showing a rewritten version of the student's WEAKEST section. Pick the lowest-scoring rubric area and rewrite their actual text to demonstrate a stronger approach. For example, if compromise proposals scored lowest, show what a more creative compromise would look like.

Consider whether the approach would realistically achieve the delegate's goals in a committee setting."""

    return _call_openai(client, user_prompt, user=user, endpoint="review_negotiation")


def review_general(text_content: str, question_prompt: str = "", user=None) -> dict:
    """General review for any MUN-related submission with rubric feedback."""
    client = get_client()

    user_prompt = f"""Please review this MUN practice submission.

{f'Exercise prompt: {question_prompt}' if question_prompt else ''}

=== SUBMISSION ===
{text_content}
=== END ===

Score this submission against these general rubric criteria:
1. Content Quality (0-25): Depth of analysis, accuracy of information, relevance to the topic?
2. MUN Knowledge (0-25): Understanding of MUN procedures, conventions, and best practices?
3. Critical Thinking (0-25): Original analysis, logical reasoning, consideration of multiple perspectives?
4. Communication (0-25): Clarity of writing, organization, appropriate tone and register?

Return your review as JSON with these exact keys:
- "overall_score": integer 0-100 (sum of rubric scores)
- "rubric_scores": object where each key is the criterion name and value is {{"score": integer, "max": integer, "comment": "1-2 sentence explanation"}}. Use these exact keys: "content_quality", "mun_knowledge", "critical_thinking", "communication"
- "strengths": array of 3-5 specific strength bullet points
- "improvements": array of 3-5 specific improvement bullet points
- "detailed_feedback": string with paragraph-form detailed analysis
- "suggestions": array of 3-5 numbered actionable next steps
- "example_revision": string showing a rewritten version of the student's WEAKEST section, demonstrating how to improve it"""

    return _call_openai(client, user_prompt, user=user, endpoint="review_general")


def generate_practice_questions(category_type: str, difficulty: str = "INT", count: int = 3, user=None) -> list:
    """Generate practice questions dynamically using AI."""
    check_daily_token_limit()
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

    # Map category to the question_type the AI must use
    forced_question_type = {
        "SPEECH": "SPEECH",
        "DRAFT": "DRAFT",
        "NEGOTIATION": "NEGOTIATION",
        "RESEARCH": "OPEN",
        "PROCEDURE": "QUIZ",
        "GENERAL": "OPEN",
    }.get(category_type, "OPEN")

    user_prompt = f"""Generate {count} MUN practice exercises.

Category: {category_type}
Difficulty: {difficulty_desc}
Category Guidance: {category_guidance}

IMPORTANT: ALL exercises MUST be strictly about {category_type} only. Do NOT generate exercises for other categories.
Every exercise must have "question_type" set to "{forced_question_type}".

Return as a JSON array where each item has:
- "title": short, engaging exercise title (5-10 words)
- "prompt": detailed exercise prompt/scenario (2-3 paragraphs with specific context, country names, committee names, and realistic details)
- "hints": 2-3 helpful hints for the student, separated by semicolons
- "question_type": MUST be "{forced_question_type}" for all exercises
- "key_concepts": comma-separated list of 3-5 key MUN concepts this exercise tests
- "sample_approach": a brief 2-sentence description of how a strong delegate would approach this

Make them realistic, educational, and based on actual UN committees and real-world issues.
Ensure progressively challenging content within the difficulty tier.
Remember: stay within the {category_type} category ONLY."""

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

        # Log token usage
        usage = response.usage
        total_tokens = usage.total_tokens if usage else 2000
        log_api_usage(user, "generate_questions", total_tokens, 'gpt-4o-mini')

        content = response.choices[0].message.content
        parsed = json.loads(content)
        # Handle both {"questions": [...]} and direct array
        if isinstance(parsed, list):
            return parsed
        return parsed.get("questions", parsed.get("exercises", []))
    except Throttled:
        raise
    except Exception as e:
        logger.error(f"DiplomAI question generation error: {e}")
        return []


def _format_list_field(value) -> str:
    """Convert a list or string field into a bullet-point string for storage."""
    if isinstance(value, list):
        return "\n".join(f"• {item}" for item in value)
    return str(value) if value else ""


def _call_openai(client, user_prompt: str, user=None, endpoint: str = "review") -> dict:
    """Internal helper to call OpenAI and parse rubric-based response."""
    check_daily_token_limit()

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": DIPLOMAI_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.6,
            max_tokens=3000,
        )

        # Log token usage
        usage = response.usage
        total_tokens = usage.total_tokens if usage else 3000
        log_api_usage(user, endpoint, total_tokens, 'gpt-4o-mini')

        content = response.choices[0].message.content
        parsed = json.loads(content)

        return {
            "overall_score": int(parsed.get("overall_score", 0)),
            "rubric_scores": parsed.get("rubric_scores", None),
            "strengths": _format_list_field(parsed.get("strengths", "")),
            "improvements": _format_list_field(parsed.get("improvements", "")),
            "detailed_feedback": parsed.get("detailed_feedback", ""),
            "suggestions": _format_list_field(parsed.get("suggestions", "")),
            "example_revision": parsed.get("example_revision", ""),
        }

    except Throttled:
        raise  # Re-raise daily limit exceeded
    except Exception as e:
        logger.error(f"DiplomAI review error: {e}")
        return {
            "overall_score": 0,
            "rubric_scores": None,
            "strengths": "",
            "improvements": "",
            "detailed_feedback": f"DiplomAI encountered an error processing your submission. Please try again. (Error: {str(e)})",
            "suggestions": "Try resubmitting, or contact support if the issue persists.",
            "example_revision": "",
        }


DIPLOMAI_SIMULATION_PROMPT = """You are roleplaying as a Model United Nations delegate in a simulation exercise on the MUNKEY platform.

You are NOT Bongo the coach right now. You are fully IN CHARACTER as the delegate described below.

Your role: {role}
Country: {country}
Topic: {topic}
Stance: {stance}

Guidelines for the simulation:
- Stay completely in character as this delegate at all times
- Respond as this delegate would in a real MUN committee — use diplomatic language and refer to yourself as "the delegate of {country}" or "my delegation"
- Push back on the student's arguments with realistic counterpoints based on your country's known positions
- Raise procedural objections, request evidence, and challenge weak proposals
- Be firm but diplomatic — never break character to coach (that's Bongo's job, not yours right now)
- If the student makes a strong argument, acknowledge it grudgingly but pivot to your next concern
- Use real-world facts, policies, and precedents that your country would actually cite
- Keep responses concise (under 200 words) to simulate real committee back-and-forth
- If the student proposes compromise, evaluate it genuinely from your country's perspective
"""


def _build_chat_messages(messages: list) -> list:
    """Build a smart context window from conversation history.

    Strategy:
    - Always include the first message (sets context/tone)
    - Include the last 15 messages for recent context
    - Avoids duplicating the first message if it's within the last 15
    """
    if not messages:
        return []

    if len(messages) <= 16:
        return [{"role": m["role"], "content": m["content"]} for m in messages]

    first = messages[0]
    recent = messages[-15:]

    result = [{"role": first["role"], "content": first["content"]}]
    for msg in recent:
        result.append({"role": msg["role"], "content": msg["content"]})
    return result


def chat_with_diplomai(messages: list, question_context: str = "",
                       mode: str = "general", simulation_config: dict | None = None,
                       user=None) -> str:
    """
    Have a conversation with DiplomAI.

    Args:
        messages: List of dicts with 'role' and 'content' keys (conversation history)
        question_context: Optional context about the current practice question
        mode: 'general' for coaching, 'simulation' for delegate roleplay
        simulation_config: Dict with role, country, topic, stance for simulation mode
        user: The requesting user (for API usage logging)

    Returns:
        The assistant's response text
    """
    check_daily_token_limit()
    client = get_client()

    if mode == "simulation" and simulation_config:
        system_msg = DIPLOMAI_SIMULATION_PROMPT.format(
            role=simulation_config.get("role", "opposing_delegate"),
            country=simulation_config.get("country", "an unnamed country"),
            topic=simulation_config.get("topic", "the current agenda item"),
            stance=simulation_config.get("stance", "a cautious position"),
        )
    else:
        system_msg = DIPLOMAI_CHAT_PROMPT
        if question_context:
            system_msg += f"\n\nThe delegate is currently working on this practice exercise:\n{question_context}\n\nHelp them with this exercise specifically if they ask about it."

    openai_messages = [{"role": "system", "content": system_msg}]
    openai_messages.extend(_build_chat_messages(messages))

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=openai_messages,
            temperature=0.7,
            max_tokens=1000,
        )

        # Log token usage
        usage = response.usage
        total_tokens = usage.total_tokens if usage else 1000
        log_api_usage(user, "chat", total_tokens, 'gpt-4o-mini')

        return response.choices[0].message.content
    except Throttled:
        raise
    except Exception as e:
        logger.error(f"DiplomAI chat error: {e}")
        if mode == "simulation":
            return "The delegate is momentarily indisposed. Please try again shortly."
        return "I'm having trouble processing your message right now. Please try again in a moment! — Bongo 🦉"
