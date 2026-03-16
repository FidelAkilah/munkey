"""
Management command to seed the MUNTip table with curated MUN tips.

Usage:
    python manage.py seed_tips          # Add tips (skip duplicates)
    python manage.py seed_tips --flush  # Delete existing tips and re-seed
"""
from django.core.management.base import BaseCommand
from curriculum.models import MUNTip


TIPS = [
    # ── SPEECH ──
    {"content": "Always refer to yourself in third person as 'the delegate of [Country]' during formal debate — never say 'I' or 'we'.", "category": "SPEECH", "difficulty": "BEG"},
    {"content": "Start your opening speech with a powerful statistic or quote that directly relates to the agenda item. A strong hook makes delegates pay attention.", "category": "SPEECH", "difficulty": "BEG"},
    {"content": "Keep opening speeches under 90 seconds. Committees have short attention spans — make every sentence count.", "category": "SPEECH", "difficulty": "BEG"},
    {"content": "Use the Rule of Three: group your arguments into three key points. 'This resolution addresses prevention, intervention, and recovery.'", "category": "SPEECH", "difficulty": "INT"},
    {"content": "End every speech with a clear call to action. Tell the committee exactly what you want them to do: 'We urge all delegations to support this amendment.'", "category": "SPEECH", "difficulty": "INT"},
    {"content": "Vary your vocal pace — slow down for emphasis on key points, speed up slightly during supporting evidence. Monotone kills persuasion.", "category": "SPEECH", "difficulty": "ADV"},

    # ── DRAFT ──
    {"content": "When writing PPs (preambulatory clauses), use italicized action words: Noting, Recognizing, Bearing in mind, Reaffirming. Each PP must end with a comma.", "category": "DRAFT", "difficulty": "BEG"},
    {"content": "Operative clauses must start with action verbs: Requests, Urges, Decides, Calls upon, Encourages. Each OP is numbered and ends with a semicolon (last one ends with a period).", "category": "DRAFT", "difficulty": "BEG"},
    {"content": "Every operative clause should answer: Who does what, by when, how, and with what funding? Vague clauses get torn apart in debate.", "category": "DRAFT", "difficulty": "INT"},
    {"content": "Reference existing UN resolutions by number in your PPs (e.g., 'Recalling General Assembly resolution 70/1'). It shows research depth and adds legitimacy.", "category": "DRAFT", "difficulty": "INT"},
    {"content": "Include a sunset clause — a built-in review date for your proposals. It shows foresight and makes skeptical delegates more willing to support.", "category": "DRAFT", "difficulty": "ADV"},
    {"content": "Avoid the word 'should' in operative clauses — use 'Requests', 'Urges', or 'Decides' depending on the strength of your intent.", "category": "DRAFT", "difficulty": "BEG"},

    # ── NEGOTIATION ──
    {"content": "In an unmod, approach the strongest opposition first — if you can convince them, others will follow.", "category": "NEGOTIATION", "difficulty": "INT"},
    {"content": "Never negotiate against yourself. State your position clearly and let the other side make the first concession.", "category": "NEGOTIATION", "difficulty": "INT"},
    {"content": "Build a bloc of at least 3-4 countries before presenting a working paper. Solo resolutions rarely pass.", "category": "NEGOTIATION", "difficulty": "BEG"},
    {"content": "Use 'Yes, and...' instead of 'No, but...' when negotiating. Acknowledge the other delegate's point, then add your condition.", "category": "NEGOTIATION", "difficulty": "BEG"},
    {"content": "Map the room early: identify potential allies, swing votes, and opposition. Know who to approach and in what order.", "category": "NEGOTIATION", "difficulty": "INT"},
    {"content": "When merging working papers, focus on compatible operative clauses first. Save contentious points for last when you have momentum.", "category": "NEGOTIATION", "difficulty": "ADV"},

    # ── RESEARCH ──
    {"content": "Check your country's actual UN voting record before the conference. Your position paper should align with how your country has historically voted.", "category": "RESEARCH", "difficulty": "BEG"},
    {"content": "Use primary sources: UN reports, WHO data, World Bank statistics, official government statements. Wikipedia is a starting point, not a source.", "category": "RESEARCH", "difficulty": "BEG"},
    {"content": "A strong position paper has three sections: background on the issue from your country's perspective, past UN actions your country supported, and specific policy proposals.", "category": "RESEARCH", "difficulty": "INT"},
    {"content": "Research your committee's mandate carefully. The UNHRC can't deploy peacekeepers, and the GA can only recommend, not mandate. Stay in scope.", "category": "RESEARCH", "difficulty": "INT"},
    {"content": "Study your country's regional alliances (EU, ASEAN, AU, G77). In MUN, bloc voting is powerful — know who your natural partners are.", "category": "RESEARCH", "difficulty": "ADV"},

    # ── PROCEDURE ──
    {"content": "A Motion to Set the Agenda is usually the first motion — prepare a short (30-second) speech for why your preferred topic should be discussed first.", "category": "PROCEDURE", "difficulty": "BEG"},
    {"content": "A Point of Order can only be raised when a rule is being broken. Don't use it to disagree with a delegate — that's what right of reply is for.", "category": "PROCEDURE", "difficulty": "BEG"},
    {"content": "Know the difference: a moderated caucus has a speakers' list set by the chair; an unmoderated caucus is free-form negotiation with no formal speakers.", "category": "PROCEDURE", "difficulty": "BEG"},
    {"content": "When proposing a moderated caucus, always specify the total time and individual speaking time. Example: '10-minute moderated caucus with 1-minute speaking time on the topic of...'", "category": "PROCEDURE", "difficulty": "INT"},
    {"content": "A Motion to Close Debate ends discussion and moves to voting. Use it strategically when you have the votes — never when debate is still productive.", "category": "PROCEDURE", "difficulty": "INT"},
    {"content": "Use a Motion to Divide the Question to vote on controversial operative clauses separately. This can save a resolution that would otherwise fail as a whole.", "category": "PROCEDURE", "difficulty": "ADV"},

    # ── GENERAL ──
    {"content": "Dress formally and professionally. First impressions matter — other delegates take well-dressed delegates more seriously.", "category": "GENERAL", "difficulty": "BEG"},
    {"content": "Always bring a pen, notepad, and printed copies of your position paper. Digital devices are often restricted in committee.", "category": "GENERAL", "difficulty": "BEG"},
    {"content": "Take notes during other delegates' speeches. Reference their exact words later — it shows you're listening and builds rapport.", "category": "GENERAL", "difficulty": "INT"},
    {"content": "Awards are typically based on: position paper quality, speaking ability, negotiation skill, resolution writing, and overall diplomacy. Balance all five.", "category": "GENERAL", "difficulty": "INT"},
    {"content": "If your resolution fails, don't get discouraged. Pivot to amending the winning resolution — showing adaptability impresses chairs.", "category": "GENERAL", "difficulty": "ADV"},
    {"content": "Introduce yourself to the committee chair before the first session. A brief, professional introduction helps you stand out.", "category": "GENERAL", "difficulty": "BEG"},
]


class Command(BaseCommand):
    help = "Seed the database with curated MUN tips for Bongo's Tip of the Day."

    def add_arguments(self, parser):
        parser.add_argument(
            '--flush',
            action='store_true',
            help='Delete all existing tips before seeding.',
        )

    def handle(self, *args, **options):
        if options['flush']:
            deleted, _ = MUNTip.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Flushed {deleted} existing tips."))

        created_count = 0
        skipped_count = 0

        for tip_data in TIPS:
            _, created = MUNTip.objects.get_or_create(
                content=tip_data["content"],
                defaults={
                    "category": tip_data["category"],
                    "difficulty": tip_data["difficulty"],
                },
            )
            if created:
                created_count += 1
            else:
                skipped_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {created_count} new tips, skipped {skipped_count} duplicates. "
            f"Total tips in DB: {MUNTip.objects.count()}"
        ))
