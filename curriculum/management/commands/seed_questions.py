from django.core.management.base import BaseCommand
from curriculum.models import CurriculumCategory, PracticeQuestion


CATEGORIES = [
    {"name": "Speech & Public Speaking", "slug": "speech", "category_type": "SPEECH", "icon": "\U0001f3a4", "order": 1, "description": "Master the art of public speaking in Model United Nations. Learn to deliver compelling opening speeches, craft persuasive arguments, and command the attention of your committee."},
    {"name": "Draft Resolution Writing", "slug": "draft", "category_type": "DRAFT", "icon": "\U0001f4dc", "order": 2, "description": "Learn UN document formatting, operative and preambulatory clause structure, and how to write effective draft resolutions that build consensus and address complex global issues."},
    {"name": "Negotiation & Diplomacy", "slug": "negotiation", "category_type": "NEGOTIATION", "icon": "\U0001f91d", "order": 3, "description": "Build coalitions and craft compromises that advance your country's interests while maintaining diplomatic relationships and achieving workable solutions."},
    {"name": "Research & Position Papers", "slug": "research", "category_type": "RESEARCH", "icon": "\U0001f50d", "order": 4, "description": "Conduct thorough country research and write compelling position papers that demonstrate deep understanding of your assigned nation's policies and priorities."},
    {"name": "Rules of Procedure", "slug": "procedure", "category_type": "PROCEDURE", "icon": "\u2696\ufe0f", "order": 5, "description": "Navigate parliamentary procedure with confidence. Master motions, points, voting procedures, and the flow of debate in Model United Nations."},
    {"name": "General MUN Skills", "slug": "general", "category_type": "GENERAL", "icon": "\U0001f4da", "order": 6, "description": "Develop well-rounded MUN competencies including note-passing strategy, crisis management, awards criteria, and overall conference preparation."},
]

# Map category_type to question_type
CATEGORY_QUESTION_TYPE = {
    "SPEECH": "SPEECH",
    "DRAFT": "DRAFT",
    "NEGOTIATION": "NEGOTIATION",
    "RESEARCH": "OPEN",
    "PROCEDURE": "QUIZ",
    "GENERAL": "OPEN",
}

QUESTIONS = []

# ── SPEECH QUESTIONS ──────────────────────────────────────────────────────────
QUESTIONS += [
    # ── BEGINNER (10) ────────────────────────────────────────────────────────
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Opening Speech on Climate Change",
        "prompt": (
            "You are the delegate of Brazil in the United Nations Environment Programme (UNEP). "
            "The committee topic is 'Combating Deforestation and Promoting Sustainable Land Use.' "
            "This is the first session of committee, and each delegate has been given 90 seconds "
            "to deliver an opening speech.\n\n"
            "Brazil is home to the Amazon rainforest, the largest tropical rainforest in the world, "
            "and has faced significant international pressure regarding deforestation rates. However, "
            "Brazil also views the Amazon as a sovereign resource and has invested in monitoring "
            "programs like PRODES and DETER.\n\n"
            "Write a 90-second opening speech (approximately 200-250 words) that introduces Brazil's "
            "position on deforestation, acknowledges the global importance of the Amazon, and signals "
            "willingness to cooperate while defending national sovereignty over natural resources."
        ),
        "hints": (
            "Start with a hook that captures attention — perhaps a statistic about the Amazon;"
            "Mention Brazil's existing conservation programs to show credibility;"
            "Balance sovereignty concerns with cooperative language;"
            "End with a call to action or invitation for collaboration"
        ),
        "sample_answer": (
            "A strong opening speech would begin with a compelling fact about the Amazon's role in "
            "global carbon absorption, acknowledge Brazil's dual responsibility as steward and sovereign, "
            "reference concrete programs like PRODES, and conclude by inviting fellow delegates to pursue "
            "solutions that respect national sovereignty while addressing the shared climate crisis."
        ),
        "key_concepts": "opening speech, national sovereignty, environmental policy, hook, call to action",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "First-Time Delegate Speech Introduction",
        "prompt": (
            "You are the delegate of Japan in the General Assembly First Committee (DISEC). The topic "
            "is 'Regulation of Autonomous Weapons Systems.' The Chair has opened the Speakers' List "
            "and you have been recognized to speak for 60 seconds.\n\n"
            "Japan is a technologically advanced nation that supports multilateral disarmament efforts. "
            "It has historically aligned with calls for human oversight of weapons systems and has "
            "supported discussions at the Convention on Certain Conventional Weapons (CCW) regarding "
            "lethal autonomous weapons systems (LAWS).\n\n"
            "Write a brief 60-second speech (approximately 130-160 words) that clearly states Japan's "
            "position on autonomous weapons. Keep the language simple, diplomatic, and focused on one "
            "or two key points. This exercise is designed for first-time delegates who are learning to "
            "speak confidently in committee."
        ),
        "hints": (
            "Address the Chair properly: 'Honorable Chair, fellow delegates...';"
            "Focus on just one or two main points rather than trying to cover everything;"
            "Use simple, clear sentences — avoid jargon you cannot explain;"
            "Practice reading aloud to check your timing"
        ),
        "sample_answer": (
            "An effective beginner speech would open with proper diplomatic address, state Japan's "
            "belief in maintaining meaningful human control over weapons systems, reference the CCW "
            "framework, and express willingness to work toward a binding international agreement."
        ),
        "key_concepts": "speakers list, diplomatic address, concise argumentation, autonomous weapons",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Introducing Your Country's Refugee Policy",
        "prompt": (
            "You are the delegate of Germany in the Third Committee of the General Assembly (SOCHUM). "
            "The topic is 'Protecting the Rights of Refugees and Internally Displaced Persons.' You "
            "have 90 seconds on the Speakers' List.\n\n"
            "Germany accepted over one million refugees during the 2015-2016 European migration crisis "
            "and has one of the most comprehensive asylum systems in Europe. The country has experience "
            "with both the benefits and challenges of large-scale refugee integration, including language "
            "training programs, employment initiatives, and community tensions.\n\n"
            "Write a 90-second speech (approximately 200-250 words) that presents Germany's experience "
            "with refugee integration, highlights successful policies, and urges the international "
            "community to share the burden of displacement more equitably."
        ),
        "hints": (
            "Use Germany's real-world experience as evidence of credibility;"
            "Mention specific programs or statistics to strengthen your argument;"
            "The concept of 'burden-sharing' is central to this topic — emphasize it;"
            "Keep your tone empathetic but also pragmatic"
        ),
        "sample_answer": (
            "A well-crafted speech would reference Germany's intake of over one million refugees, "
            "highlight integration successes like language and job training programs, acknowledge "
            "remaining challenges, and call for an equitable global responsibility-sharing framework "
            "consistent with the Global Compact on Refugees."
        ),
        "key_concepts": "refugee rights, burden-sharing, integration, Global Compact on Refugees, empathy in diplomacy",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Speaking on Access to Clean Water",
        "prompt": (
            "You are the delegate of Nigeria in the Economic and Social Council (ECOSOC). The topic is "
            "'Ensuring Universal Access to Clean Water and Sanitation.' You have been placed on the "
            "Speakers' List for a 90-second speech.\n\n"
            "Nigeria is Africa's most populous country, with over 200 million people. Despite being "
            "rich in natural resources, an estimated 60 million Nigerians lack access to basic water "
            "supply, and waterborne diseases remain a leading cause of child mortality. Nigeria has "
            "partnered with UNICEF and the World Bank on water infrastructure projects.\n\n"
            "Write a 90-second speech (approximately 200-250 words) from Nigeria's perspective that "
            "describes the scale of the water crisis, connects it to broader development goals (SDG 6), "
            "and requests increased international support for water infrastructure in developing nations."
        ),
        "hints": (
            "Open with a striking statistic about water access in Nigeria or globally;"
            "Link the water crisis to Sustainable Development Goal 6;"
            "Mention existing partnerships to show Nigeria is already taking action;"
            "Make a specific ask — what kind of international support does Nigeria want?"
        ),
        "sample_answer": (
            "An effective speech would open with a statistic about the 60 million Nigerians lacking "
            "clean water, connect this to SDG 6 targets, reference partnerships with UNICEF and the "
            "World Bank, and conclude with a concrete call for increased financing and technology "
            "transfer for water infrastructure in the developing world."
        ),
        "key_concepts": "SDG 6, water access, development financing, technology transfer, ECOSOC",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Addressing Cybersecurity Threats Briefly",
        "prompt": (
            "You are the delegate of India in the General Assembly First Committee (DISEC). The topic "
            "is 'Establishing Norms for Responsible State Behavior in Cyberspace.' You have 60 seconds "
            "to deliver a speech from the Speakers' List.\n\n"
            "India has the second-largest internet user base in the world and has experienced significant "
            "cyberattacks on its critical infrastructure, including the 2020 attack on its power grid. "
            "India supports the development of international cyber norms through the UN Group of "
            "Governmental Experts (GGE) process and emphasizes the importance of capacity building for "
            "developing nations.\n\n"
            "Write a concise 60-second speech (approximately 130-160 words) that outlines India's "
            "position on cybersecurity norms. Focus on the need for inclusive norm-setting that accounts "
            "for developing countries' perspectives and capacity-building needs."
        ),
        "hints": (
            "Keep it short and focused — 60 seconds is only about 150 words;"
            "Mention India's large digital population to establish relevance;"
            "Reference the GGE process to show familiarity with existing frameworks;"
            "Emphasize inclusivity and capacity building as your core message"
        ),
        "sample_answer": (
            "A strong short speech would note India's massive digital population and vulnerability to "
            "cyberattacks, endorse the GGE framework for norm development, and stress that cyber norms "
            "must be developed inclusively with capacity-building support for developing states."
        ),
        "key_concepts": "cybersecurity, GGE, capacity building, inclusive multilateralism, DISEC",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Speaking on Pandemic Preparedness",
        "prompt": (
            "You are the delegate of Indonesia in the World Health Organization (WHO) committee. The "
            "topic is 'Strengthening Global Pandemic Preparedness and Response.' You have 90 seconds "
            "on the Speakers' List.\n\n"
            "Indonesia is the world's fourth most populous country and an archipelago of over 17,000 "
            "islands, making disease surveillance and healthcare delivery uniquely challenging. During "
            "the COVID-19 pandemic, Indonesia faced difficulties with vaccine distribution, healthcare "
            "infrastructure strain, and economic impacts on its large informal economy.\n\n"
            "Write a 90-second speech (approximately 200-250 words) that highlights the unique "
            "challenges island and developing nations face in pandemic response, advocates for equitable "
            "vaccine distribution, and supports strengthening WHO's role in coordinating global health "
            "emergencies."
        ),
        "hints": (
            "Use Indonesia's geography (archipelago) as a concrete example of logistical challenges;"
            "Reference the COVAX initiative and vaccine equity;"
            "Support strengthening WHO authority without being too aggressive;"
            "Connect pandemic preparedness to economic stability"
        ),
        "sample_answer": (
            "A well-structured speech would describe Indonesia's archipelago challenges for health "
            "delivery, reference the inequities exposed by COVID-19 vaccine distribution, advocate for "
            "strengthening COVAX and WHO coordination mechanisms, and connect pandemic preparedness to "
            "economic resilience for developing nations."
        ),
        "key_concepts": "pandemic preparedness, vaccine equity, COVAX, WHO authority, island nations",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Advocating for Women's Education Rights",
        "prompt": (
            "You are the delegate of Egypt in the UN Human Rights Council (UNHRC). The topic is "
            "'Advancing Gender Equality in Education Worldwide.' You have 90 seconds to deliver "
            "a speech.\n\n"
            "Egypt has made significant strides in improving girls' access to education. The country's "
            "literacy rate for young women has improved substantially over the past two decades, and "
            "Egypt has invested in community schools in rural areas. However, challenges remain, "
            "particularly in Upper Egypt, where cultural barriers and poverty still limit girls' "
            "educational attainment.\n\n"
            "Write a 90-second speech (approximately 200-250 words) that showcases Egypt's progress "
            "on girls' education, acknowledges remaining challenges honestly, and calls for increased "
            "international funding for education programs in developing countries."
        ),
        "hints": (
            "Highlight Egypt's progress to establish credibility before addressing challenges;"
            "Mentioning specific initiatives like community schools makes your speech more convincing;"
            "Be honest about remaining gaps — delegates respect authenticity;"
            "Connect education to broader development outcomes (poverty reduction, health, etc.)"
        ),
        "sample_answer": (
            "An effective speech would celebrate Egypt's improvements in girls' literacy rates, "
            "mention community school initiatives, honestly acknowledge rural barriers in Upper Egypt, "
            "and advocate for international funding mechanisms that target education access in "
            "developing regions, linking girls' education to broader SDG achievement."
        ),
        "key_concepts": "gender equality, education access, UNHRC, SDGs, community schools",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Nuclear Disarmament Opening Statement",
        "prompt": (
            "You are the delegate of South Africa in the General Assembly First Committee (DISEC). The "
            "topic is 'Preventing Nuclear Proliferation and Advancing Disarmament.' You have 90 seconds "
            "to deliver an opening speech.\n\n"
            "South Africa is the only country in history to have voluntarily dismantled its nuclear "
            "weapons program. In the late 1980s, South Africa dismantled six nuclear warheads and "
            "joined the Treaty on the Non-Proliferation of Nuclear Weapons (NPT) as a non-nuclear "
            "weapon state. South Africa is also a signatory of the Treaty on the Prohibition of "
            "Nuclear Weapons (TPNW) and the African Nuclear-Weapon-Free Zone Treaty (Pelindaba Treaty).\n\n"
            "Write a 90-second opening speech (approximately 200-250 words) that leverages South "
            "Africa's unique moral authority on nuclear disarmament to advocate for a world free of "
            "nuclear weapons."
        ),
        "hints": (
            "South Africa's voluntary disarmament is a powerful rhetorical tool — lead with it;"
            "Reference relevant treaties: NPT, TPNW, Pelindaba Treaty;"
            "Use moral authority without being preachy — maintain diplomatic tone;"
            "Call on nuclear-armed states to take concrete disarmament steps"
        ),
        "sample_answer": (
            "A compelling speech would open by invoking South Africa's unique history of voluntary "
            "nuclear disarmament, use this moral authority to challenge nuclear-armed states, reference "
            "the NPT and TPNW frameworks, and call for concrete disarmament timelines and universal "
            "adherence to nuclear-weapon-free zone treaties."
        ),
        "key_concepts": "nuclear disarmament, NPT, TPNW, Pelindaba Treaty, moral authority, voluntary disarmament",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Raising Food Security Concerns",
        "prompt": (
            "You are the delegate of the Philippines in the Food and Agriculture Organization (FAO) "
            "committee. The topic is 'Addressing Food Insecurity in Climate-Vulnerable Nations.' You "
            "have 90 seconds on the Speakers' List.\n\n"
            "The Philippines is one of the most climate-vulnerable countries in the world, regularly "
            "experiencing typhoons, flooding, and drought. Agriculture employs roughly 25% of the "
            "Filipino workforce, and rice is the staple crop. Typhoon Haiyan in 2013 devastated "
            "agricultural regions, and the country continues to face recurring climate-related "
            "disruptions to food production.\n\n"
            "Write a 90-second speech (approximately 200-250 words) that conveys the urgency of food "
            "insecurity in climate-vulnerable nations, uses the Philippines' experience as a case study, "
            "and proposes international cooperation on climate-resilient agriculture."
        ),
        "hints": (
            "Use Typhoon Haiyan as a vivid, specific example to ground your speech;"
            "Connect climate vulnerability directly to food insecurity;"
            "Propose concrete solutions like climate-resilient crop varieties or early warning systems;"
            "Keep your tone urgent but solution-oriented"
        ),
        "sample_answer": (
            "A strong speech would reference the devastation of Typhoon Haiyan on Philippine agriculture, "
            "connect climate vulnerability to food insecurity for millions of Filipinos, and call for "
            "international investment in climate-resilient agricultural practices, early warning systems, "
            "and post-disaster food supply mechanisms."
        ),
        "key_concepts": "food security, climate vulnerability, FAO, climate-resilient agriculture, disaster preparedness",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "BEG",
        "title": "Terrorism and International Cooperation",
        "prompt": (
            "You are the delegate of Mexico in the Sixth Committee of the General Assembly (Legal). "
            "The topic is 'Strengthening the International Legal Framework Against Terrorism.' You "
            "have 60 seconds to deliver a speech.\n\n"
            "Mexico has dealt with significant security challenges from organized crime and drug "
            "cartels, and while these are distinct from terrorism, Mexico recognizes the overlapping "
            "threats of transnational crime and terrorism. Mexico supports the UN Global Counter-"
            "Terrorism Strategy and emphasizes that counter-terrorism measures must respect human rights "
            "and the rule of law.\n\n"
            "Write a concise 60-second speech (approximately 130-160 words) that affirms Mexico's "
            "commitment to fighting terrorism within a human rights framework and calls for stronger "
            "international legal cooperation."
        ),
        "hints": (
            "Keep it brief — 60 seconds is very short, so pick one clear message;"
            "Emphasize the human rights dimension of counter-terrorism;"
            "Reference the UN Global Counter-Terrorism Strategy;"
            "Avoid conflating organized crime with terrorism, but acknowledge overlapping threats"
        ),
        "sample_answer": (
            "An effective short speech would affirm Mexico's commitment to the UN Global Counter-"
            "Terrorism Strategy, emphasize that all counter-terrorism measures must comply with "
            "international human rights law, and call for enhanced legal cooperation and information "
            "sharing between states."
        ),
        "key_concepts": "counter-terrorism, human rights, rule of law, UN Global Counter-Terrorism Strategy",
    },

    # ── INTERMEDIATE (10) ────────────────────────────────────────────────────
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Responding to a Bloc's Counter-Argument",
        "prompt": (
            "You are the delegate of India in the General Assembly Second Committee (ECOFIN). The topic "
            "is 'Bridging the Digital Divide Between Developed and Developing Nations.' A bloc of "
            "Western European delegates has just argued that developing countries should liberalize "
            "their telecommunications markets and allow foreign investment to solve the digital divide, "
            "rather than relying on international aid.\n\n"
            "India disagrees with this framing. While India has a thriving tech sector, it also has "
            "significant digital infrastructure gaps in rural areas and has pursued a mixed model of "
            "public investment (like BharatNet) alongside private sector growth. India believes that "
            "market liberalization alone is insufficient and that targeted public investment and "
            "technology transfer are essential.\n\n"
            "Write a 90-second response speech (approximately 200-250 words) that respectfully counters "
            "the Western European bloc's argument. Acknowledge valid points in their position while "
            "presenting India's alternative approach. Demonstrate intermediate-level debating skills by "
            "using evidence, making concessions, and pivoting to your own argument."
        ),
        "hints": (
            "Begin by acknowledging the other bloc's point — this shows diplomatic maturity;"
            "Use the 'Yes, but...' technique: concede a minor point, then pivot to your stronger argument;"
            "Reference BharatNet as concrete evidence that public investment works;"
            "Frame your argument in terms of equity, not just efficiency"
        ),
        "sample_answer": (
            "A strong response would acknowledge that private investment plays a role in digital "
            "infrastructure, but pivot to argue that market liberalization alone leaves rural and "
            "marginalized communities behind. Referencing BharatNet's success in connecting rural India, "
            "the speech would advocate for blended models that combine public investment, technology "
            "transfer, and private participation."
        ),
        "key_concepts": "rebuttal, concession and pivot, digital divide, BharatNet, technology transfer, ECOFIN",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Moderated Caucus Intervention on AI",
        "prompt": (
            "You are the delegate of Germany in the Special Political and Decolonization Committee "
            "(SPECPOL). The topic is 'Ethical Implications of Artificial Intelligence in Governance.' "
            "A moderated caucus has been set with the sub-topic 'Balancing Innovation and Regulation.' "
            "You have 60 seconds for your intervention.\n\n"
            "Germany and the European Union have been global leaders in AI regulation, having developed "
            "the EU AI Act — the world's first comprehensive AI regulatory framework. Germany believes "
            "in a risk-based approach to AI governance that categorizes AI systems by their potential "
            "harm and applies proportional regulation.\n\n"
            "Write a focused 60-second moderated caucus speech (approximately 130-160 words) that "
            "advances a specific proposal or idea related to the sub-topic. Unlike a Speakers' List "
            "speech, a moderated caucus intervention should be laser-focused on one concrete idea and "
            "should build on the existing discussion rather than restate general positions."
        ),
        "hints": (
            "Moderated caucus speeches are different from Speakers' List speeches — they should advance a specific point;"
            "Propose the risk-based regulatory model as a framework the committee could adopt;"
            "Reference the EU AI Act as a working example;"
            "End with a concrete suggestion for what the committee should include in the working paper"
        ),
        "sample_answer": (
            "An effective moderated caucus intervention would propose that the committee adopt a "
            "risk-based classification system for AI, cite the EU AI Act as a proven model, and "
            "suggest specific language for the working paper that establishes tiered regulatory "
            "requirements based on the level of risk an AI system poses to human rights."
        ),
        "key_concepts": "moderated caucus, EU AI Act, risk-based regulation, working paper, focused intervention",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Right of Reply on Human Rights",
        "prompt": (
            "You are the delegate of Saudi Arabia in the UN Human Rights Council (UNHRC). The topic "
            "is 'Freedom of Expression in the Digital Age.' During a previous speech, the delegate of "
            "Sweden directly criticized Saudi Arabia's record on press freedom and online censorship, "
            "citing the case of detained bloggers and restrictive cybercrime laws.\n\n"
            "Saudi Arabia's Vision 2030 reform agenda includes social and economic modernization, and "
            "the country has taken steps to expand digital access and online services. However, Saudi "
            "Arabia also maintains that certain restrictions on expression are necessary to preserve "
            "social stability and national security, and that different cultural contexts require "
            "different approaches to rights implementation.\n\n"
            "Write a Right of Reply (approximately 200-250 words, 90 seconds) that responds to "
            "Sweden's criticism. You must maintain diplomatic composure, defend your country's position "
            "without being defensive, and redirect the conversation toward broader principles. This "
            "exercise tests your ability to handle direct criticism gracefully in committee."
        ),
        "hints": (
            "Never attack the criticizing delegate personally — address the argument, not the person;"
            "Use cultural relativism arguments carefully and diplomatically;"
            "Mention Vision 2030 reforms to show progress;"
            "Redirect the conversation to a broader principle, like the universality vs. cultural context debate;"
            "Maintain composure — a Right of Reply should be firm but dignified"
        ),
        "sample_answer": (
            "A skilled Right of Reply would thank the delegate for their perspective, note that Saudi "
            "Arabia's Vision 2030 represents meaningful reform, argue that rights implementation must "
            "account for diverse cultural and security contexts, and redirect the conversation toward "
            "the need for all nations to examine their own records before casting judgment."
        ),
        "key_concepts": "right of reply, diplomatic composure, cultural relativism, Vision 2030, press freedom",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Persuading Uncommitted Delegates on Climate",
        "prompt": (
            "You are the delegate of the Maldives in the United Nations Environment Programme (UNEP). "
            "The topic is 'Addressing Sea-Level Rise and Its Impact on Small Island Developing States.' "
            "Committee is in an unmoderated caucus, and you are speaking to a small group of three "
            "uncommitted delegates (Chile, Thailand, and Morocco) trying to convince them to support "
            "your draft resolution.\n\n"
            "Your draft resolution calls for the establishment of a Loss and Damage Fund specifically "
            "for SIDS (Small Island Developing States) affected by sea-level rise, funded by assessed "
            "contributions from the top 20 greenhouse gas emitting nations. Some delegates are "
            "concerned this is too aggressive and prefer voluntary contributions.\n\n"
            "Write an informal but persuasive speech (approximately 200-250 words) that you would "
            "deliver to this small group. The tone should be conversational but compelling. Focus on "
            "building common ground and addressing their likely concerns about the mandatory funding "
            "mechanism."
        ),
        "hints": (
            "Informal caucus speeches should be conversational, not stiff — drop the 'Honorable Chair';"
            "Anticipate objections about mandatory funding and address them preemptively;"
            "Find common ground — Chile, Thailand, and Morocco all have coastal vulnerabilities;"
            "Use emotional appeals alongside logical ones — the Maldives' existential threat is powerful;"
            "Offer a compromise: perhaps phased implementation of assessed contributions"
        ),
        "sample_answer": (
            "A persuasive informal pitch would connect with the delegates' own coastal vulnerabilities, "
            "acknowledge concerns about mandatory funding by proposing phased implementation, use the "
            "Maldives' existential threat as a moral anchor, and frame supporting the resolution as "
            "being on the right side of history."
        ),
        "key_concepts": "informal persuasion, Loss and Damage, SIDS, coalition building, addressing objections",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Defending Your Draft Resolution",
        "prompt": (
            "You are the delegate of Nigeria in the General Assembly Third Committee (SOCHUM). The "
            "topic is 'Combating Human Trafficking in Conflict Zones.' Your bloc has submitted a draft "
            "resolution, and the committee is now in the formal presentation of draft resolutions. You "
            "are the primary sponsor and must introduce your draft to the committee.\n\n"
            "Your draft resolution has three main pillars: (1) strengthening UNODC's mandate to "
            "investigate trafficking networks in conflict zones, (2) establishing regional training "
            "programs for law enforcement in affected areas, and (3) creating a victims' assistance "
            "fund financed through voluntary contributions. A rival bloc has submitted an alternative "
            "draft that focuses solely on border security measures.\n\n"
            "Write a 2-minute speech (approximately 280-330 words) that presents your draft resolution "
            "to the committee. Explain the key provisions, justify why your approach is superior to "
            "alternatives, and urge delegates to support your draft. This is a critical moment — your "
            "speech must be organized, persuasive, and inclusive."
        ),
        "hints": (
            "Structure your speech clearly: briefly overview all three pillars;"
            "Explain why each pillar matters — don't just list provisions, justify them;"
            "Contrast your holistic approach with the rival bloc's narrow focus on border security;"
            "Invite friendly amendments to show openness and attract more sponsors;"
            "End with a strong closing that frames a vote for your resolution as a vote for victims"
        ),
        "sample_answer": (
            "An effective draft presentation would systematically introduce each pillar with brief "
            "justification, contrast the holistic victim-centered approach with the rival draft's "
            "narrow border-security focus, invite friendly amendments to broaden support, and close "
            "with an emotional appeal connecting the resolution to real victims of trafficking."
        ),
        "key_concepts": "draft presentation, UNODC, human trafficking, three-pillar structure, contrast with rivals",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Speaking in Favor of an Amendment",
        "prompt": (
            "You are the delegate of Mexico in the Economic and Social Council (ECOSOC). The topic is "
            "'Reducing Economic Inequality Through Progressive Taxation.' A draft resolution is on the "
            "floor, and an amendment has been proposed by the delegate of South Korea to add an "
            "operative clause establishing a UN advisory body on international tax cooperation.\n\n"
            "Mexico supports this amendment. Mexico has long advocated for stronger international tax "
            "cooperation to combat illicit financial flows and tax evasion by multinational corporations, "
            "which disproportionately harm developing countries. Mexico believes the current OECD-led "
            "framework for tax cooperation is insufficiently inclusive of developing nations.\n\n"
            "Write a 60-second speech (approximately 130-160 words) speaking in favor of the amendment. "
            "Your speech should be concise, directly supportive, and explain why this amendment "
            "strengthens the overall draft resolution."
        ),
        "hints": (
            "When speaking for an amendment, be direct — state your support immediately;"
            "Explain what value the amendment adds to the existing draft;"
            "Reference the inadequacy of the current OECD framework to justify the need;"
            "Urge fellow delegates to vote in favor"
        ),
        "sample_answer": (
            "A well-delivered pro-amendment speech would immediately state support, explain that the "
            "advisory body fills a gap in inclusive international tax governance that the OECD framework "
            "does not address, and urge delegates to vote yes as a step toward equitable economic policy."
        ),
        "key_concepts": "amendment procedures, international tax cooperation, OECD, ECOSOC, speaking for amendments",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Crisis Committee Breaking News Response",
        "prompt": (
            "You are the delegate of France on the UN Security Council. The committee is running a "
            "crisis simulation, and breaking news has just been announced: a large-scale cyberattack "
            "has disabled critical infrastructure in three NATO member states, including power grids "
            "and hospital systems. Intelligence suggests a state actor is responsible, but attribution "
            "is not yet confirmed.\n\n"
            "France, as a permanent member of the Security Council and a NATO ally, must respond "
            "quickly. The Chair has opened an emergency Speakers' List and France has been recognized "
            "for 90 seconds.\n\n"
            "Write a 90-second crisis response speech (approximately 200-250 words) that addresses the "
            "breaking news. You must balance urgency with caution, propose immediate actions the "
            "Security Council can take, and avoid premature attribution while still demonstrating "
            "resolve. This tests your ability to think on your feet and deliver measured, authoritative "
            "speeches under pressure."
        ),
        "hints": (
            "Express concern and solidarity immediately — this is an emergency;"
            "Be careful about attribution — say 'reports suggest' rather than making accusations;"
            "Propose concrete immediate steps: emergency session, investigation, aid coordination;"
            "Reference Article 5 of NATO carefully — acknowledge it without triggering it unilaterally;"
            "Project calm authority, not panic"
        ),
        "sample_answer": (
            "A strong crisis speech would express immediate solidarity with affected states, urge "
            "caution on attribution while calling for a rapid independent investigation, propose "
            "concrete Security Council actions such as an emergency investigation team and humanitarian "
            "coordination, and project measured resolve without escalatory language."
        ),
        "key_concepts": "crisis response, Security Council, cyberattack, attribution, NATO, measured rhetoric",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Closing Speech Summarizing Key Points",
        "prompt": (
            "You are the delegate of South Africa in the Special Political and Decolonization Committee "
            "(SPECPOL). The topic is 'Reforming United Nations Peacekeeping Operations.' The committee "
            "is nearing the end of debate, and you have secured the last slot on the Speakers' List. "
            "This is effectively your closing speech.\n\n"
            "Throughout the conference, South Africa has been a leading voice advocating for: (1) "
            "greater African Union involvement in peacekeeping decisions affecting Africa, (2) improved "
            "training and accountability standards for peacekeepers, and (3) sustainable funding "
            "mechanisms that do not leave troop-contributing countries bearing unfair financial burdens. "
            "South Africa is also the primary sponsor of a draft resolution that has strong but not "
            "universal support.\n\n"
            "Write a closing speech of approximately 200-250 words (90 seconds) that summarizes your "
            "key positions, makes a final appeal for support of your draft resolution, and leaves a "
            "lasting impression on the committee."
        ),
        "hints": (
            "A closing speech should feel like a summary and call to action, not a new argument;"
            "Reference your three main advocacy points briefly;"
            "Acknowledge compromise and collaboration that happened during debate;"
            "Make one final emotional or principled appeal for your draft resolution;"
            "End with a memorable closing line"
        ),
        "sample_answer": (
            "An effective closing speech would briefly recap South Africa's three priorities, acknowledge "
            "productive debates and compromises reached during committee, make a final principled appeal "
            "for the draft resolution, and close with a memorable statement about the responsibility "
            "to protect vulnerable populations through reformed peacekeeping."
        ),
        "key_concepts": "closing speech, peacekeeping reform, AU-UN cooperation, rhetorical conclusion, draft resolution appeal",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Pivot from Defense to Offense in Debate",
        "prompt": (
            "You are the delegate of China in the UN Human Rights Council (UNHRC). The topic is "
            "'Protecting Privacy Rights in the Age of Mass Surveillance.' Multiple Western delegates "
            "have criticized China's social credit system and digital surveillance apparatus during "
            "their speeches. The committee mood has shifted against China's position.\n\n"
            "China's position is that surveillance technologies are legitimate tools for public safety "
            "and social governance when used under the rule of law. China also points out that Western "
            "nations, including the United States and United Kingdom, operate extensive surveillance "
            "programs (as revealed by the Snowden disclosures) and that selective criticism of China "
            "reflects political bias rather than genuine concern for privacy rights.\n\n"
            "Write a 90-second speech (approximately 200-250 words) that pivots from defending China's "
            "position to putting pressure on critics. Use the technique of 'tu quoque' (pointing out "
            "hypocrisy) judiciously while also presenting China's constructive vision for privacy "
            "governance. This tests your ability to seize rhetorical momentum in a hostile environment."
        ),
        "hints": (
            "Acknowledge the importance of privacy as a value — do not dismiss it outright;"
            "Use the Snowden revelations strategically but do not dwell on them too long;"
            "Pivot quickly from defense to your own constructive proposal;"
            "Frame your argument as being about consistent standards, not deflection;"
            "Propose a universal framework rather than selective targeting"
        ),
        "sample_answer": (
            "A skilled pivot speech would briefly acknowledge privacy concerns, redirect attention to "
            "Western surveillance programs revealed by Snowden to establish the hypocrisy of selective "
            "criticism, then pivot constructively to propose a universal surveillance oversight framework "
            "that applies equally to all states, thereby seizing the initiative."
        ),
        "key_concepts": "rhetorical pivot, tu quoque, Snowden disclosures, constructive redirection, surveillance oversight",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "INT",
        "title": "Explaining Vote After Resolution Passes",
        "prompt": (
            "You are the delegate of Japan in the General Assembly Plenary session. A resolution on "
            "'Establishing a Moratorium on Deep-Sea Mining Beyond National Jurisdiction' has just passed "
            "with a vote of 98-35-22. Japan voted against the resolution.\n\n"
            "Japan has significant economic interests in deep-sea mining, particularly for rare earth "
            "minerals needed for its technology and automotive industries. Japan is a member of the "
            "International Seabed Authority (ISA) and believes that regulated deep-sea mining under "
            "ISA oversight is preferable to a blanket moratorium. Japan also invested heavily in "
            "deep-sea mining research and exploration technology.\n\n"
            "Write an Explanation of Vote (approximately 200-250 words, 90 seconds) that explains "
            "Japan's no vote. An Explanation of Vote should be respectful of the committee's decision, "
            "clearly state why Japan could not support the resolution, and express Japan's continued "
            "commitment to responsible ocean governance."
        ),
        "hints": (
            "Begin by respecting the democratic process — acknowledge the majority decision;"
            "Clearly explain your reasoning without being bitter or confrontational;"
            "Distinguish between opposing the moratorium and opposing ocean protection;"
            "Reaffirm Japan's commitment to responsible mining under ISA regulation;"
            "Explanations of Vote are formal — maintain diplomatic register"
        ),
        "sample_answer": (
            "A proper Explanation of Vote would respect the committee's majority decision, clearly "
            "state that Japan opposes a blanket moratorium because it prefers regulated extraction "
            "under ISA oversight, distinguish between opposing the moratorium and opposing environmental "
            "protection, and reaffirm Japan's commitment to responsible ocean governance."
        ),
        "key_concepts": "explanation of vote, deep-sea mining, ISA, voting procedures, diplomatic dissent",
    },

    # ── ADVANCED (10) ────────────────────────────────────────────────────────
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Security Council Veto Justification Speech",
        "prompt": (
            "You are the delegate of Russia on the United Nations Security Council. A draft resolution "
            "has been proposed to authorize a multinational peacekeeping force in a fictional country "
            "experiencing civil conflict. The draft resolution, sponsored by the United States and the "
            "United Kingdom, includes provisions for the use of force under Chapter VII of the UN "
            "Charter and establishes a no-fly zone.\n\n"
            "Russia intends to exercise its veto. Russia opposes the resolution because it views the "
            "Chapter VII authorization and no-fly zone as overreach that could lead to regime change — "
            "similar to what happened in Libya following Resolution 1973 in 2011. Russia supports "
            "diplomatic solutions and believes the conflict can be resolved through mediation under "
            "Chapter VI rather than enforcement under Chapter VII.\n\n"
            "Write a formal veto justification speech of approximately 330-400 words (2-3 minutes) that "
            "explains Russia's decision to veto. This is one of the most consequential speech types in "
            "MUN. You must present a rigorous legal and political argument, reference historical "
            "precedent, propose an alternative path, and maintain gravitas throughout. The committee "
            "and international media are watching."
        ),
        "hints": (
            "A veto justification is one of the most dramatic moments in MUN — the weight of it should be felt in your delivery;"
            "Reference the Libya precedent (Resolution 1973) explicitly — this is your strongest argument;"
            "Distinguish clearly between Chapter VI (peaceful settlement) and Chapter VII (enforcement) approaches;"
            "Propose a concrete alternative: special envoy, regional mediation, ceasefire negotiations;"
            "Anticipate accusations of obstructionism and preemptively address them;"
            "Close with a statement about protecting the integrity of the Security Council"
        ),
        "sample_answer": (
            "A masterful veto justification would invoke the Libya precedent to demonstrate how Chapter "
            "VII authorizations can be misused for regime change, present a detailed legal argument for "
            "Chapter VI mediation, propose a concrete alternative including a special envoy and ceasefire "
            "framework, and conclude by framing the veto as protecting the Security Council's credibility "
            "and the principle of non-intervention."
        ),
        "key_concepts": "veto power, Chapter VII, Chapter VI, Libya precedent, no-fly zone, regime change, P5 responsibility",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Impromptu Response to Unfriendly Amendment",
        "prompt": (
            "You are the delegate of Brazil in the Economic and Financial Committee (ECOFIN). The topic "
            "is 'Reforming International Financial Institutions for Equitable Development.' Your bloc "
            "has submitted a strong draft resolution calling for weighted voting reform at the IMF and "
            "World Bank to give developing nations greater representation.\n\n"
            "An unfriendly amendment has just been introduced by the delegate of the United Kingdom. "
            "The amendment would replace your operative clause calling for mandatory voting share "
            "redistribution with language that merely 'encourages member states to consider voluntary "
            "adjustments to voting share allocation at their discretion.' This effectively guts the "
            "core of your resolution.\n\n"
            "You have not had time to prepare — you have 90 seconds to speak against this amendment "
            "immediately. The vote on the amendment will happen right after speeches for and against.\n\n"
            "Write an impromptu 90-second speech (approximately 200-250 words) opposing the amendment. "
            "You must quickly and clearly explain why the amendment undermines the resolution's purpose, "
            "rally your supporters, and persuade swing votes to vote against the amendment. This tests "
            "advanced impromptu speaking and strategic thinking under pressure."
        ),
        "hints": (
            "Start by framing what is at stake — the core of your resolution is being gutted;"
            "Compare the original language (mandatory redistribution) with the amendment (voluntary consideration);"
            "Point out that 'voluntary adjustments' have been tried for decades and failed to produce change;"
            "Make it personal for developing nations: this is about their voice in global economic governance;"
            "Urge a no vote on the amendment, not a no vote on the resolution — be clear about what you are asking"
        ),
        "sample_answer": (
            "A powerful opposition speech would immediately frame the amendment as gutting the resolution's "
            "core intent, contrast the binding language of the original with the toothless voluntary "
            "language of the amendment, cite the historical failure of voluntary reform approaches at "
            "the IMF, and make a direct appeal to developing nation delegates that their representation "
            "in global economic governance is on the line."
        ),
        "key_concepts": "unfriendly amendment, impromptu speaking, IMF reform, voting share redistribution, strategic urgency",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Bridging Two Rival Blocs as Mediator",
        "prompt": (
            "You are the delegate of Indonesia in the General Assembly Third Committee (SOCHUM). The "
            "topic is 'Protecting Digital Privacy Rights While Combating Online Extremism.' The "
            "committee has fractured into two opposing blocs.\n\n"
            "Bloc A (led by Sweden, Canada, and Germany) has submitted a draft resolution emphasizing "
            "strong data privacy protections, restrictions on government surveillance, and independent "
            "oversight mechanisms. Bloc B (led by Egypt, Russia, and Singapore) has submitted a "
            "competing draft emphasizing state authority to monitor and regulate online content to "
            "combat extremism and terrorism, with minimal restrictions on government surveillance "
            "powers.\n\n"
            "Indonesia is not aligned with either bloc but sees merit in both positions. Indonesia has "
            "experience with both online extremism (domestic terrorist recruitment) and digital rights "
            "advocacy. You want to position yourself as a bridge-builder and propose a compromise "
            "framework.\n\n"
            "Write a 2-minute speech (approximately 280-330 words) that acknowledges the valid concerns "
            "of both blocs, identifies specific areas of potential compromise, and proposes a concrete "
            "merged framework. This tests advanced diplomatic skill, creative problem-solving, and the "
            "ability to rise above bloc politics to serve the committee."
        ),
        "hints": (
            "Begin by acknowledging both blocs' legitimate concerns — extremism IS dangerous, privacy IS fundamental;"
            "Identify specific overlap: both blocs likely agree on transparency and judicial oversight in some form;"
            "Propose a tiered system: stronger surveillance powers require proportionally stronger oversight;"
            "Position Indonesia's own experience with both extremism and digital rights as your credibility;"
            "Invite both blocs to a working group to merge the drafts — offer to facilitate"
        ),
        "sample_answer": (
            "A masterful bridge-building speech would validate both blocs' core concerns, identify "
            "specific areas of overlap such as judicial oversight and transparency requirements, propose "
            "a proportionality framework where surveillance powers are tied to corresponding oversight "
            "mechanisms, cite Indonesia's experience with both extremism and digital rights, and invite "
            "both blocs to a facilitated working group to produce a merged draft."
        ),
        "key_concepts": "bridge-building, bloc mediation, proportionality framework, digital privacy, online extremism, compromise",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Emotional Appeal on Humanitarian Crisis",
        "prompt": (
            "You are the delegate of Jordan in a special emergency session of the General Assembly. The "
            "topic is 'Addressing the Humanitarian Crisis Resulting from the Prolonged Conflict in "
            "Syria.' Jordan has hosted over 650,000 registered Syrian refugees — one of the highest "
            "per-capita refugee populations in the world — straining its water, education, healthcare, "
            "and economic systems.\n\n"
            "The General Assembly is considering a resolution to increase humanitarian funding and "
            "establish new resettlement pathways. Many wealthy nations have been reluctant to increase "
            "their commitments. You have 2 minutes for this critical speech.\n\n"
            "Write a 2-minute speech (approximately 280-330 words) that combines factual argumentation "
            "with emotional appeal. Use specific data about Jordan's refugee burden, personal-scale "
            "narratives (without fabricating individual stories — use representative scenarios), and "
            "moral arguments to compel wealthy nations to act. This tests your ability to move a room "
            "through the combination of logos, pathos, and ethos — the mark of an advanced speaker."
        ),
        "hints": (
            "Use the rhetorical trifecta: logos (data on refugee numbers, economic strain), pathos (human impact), ethos (Jordan's credibility as a host);"
            "Paint a picture: describe what a refugee camp near Amman looks like, the strain on Jordanian schools;"
            "Use a representative scenario — 'Imagine a family of five arriving with nothing...' — without inventing a specific person;"
            "Make the moral argument: those with the most resources bear the greatest responsibility;"
            "Direct your appeal specifically at wealthy nations — name the gap between their capacity and contributions;"
            "End with a line that lingers in delegates' minds"
        ),
        "sample_answer": (
            "An exceptional speech would weave together hard data on Jordan's refugee burden with "
            "vivid representative scenarios of refugee families, establish Jordan's moral authority as "
            "a nation that has shared its limited resources, directly challenge wealthy nations to match "
            "their rhetoric with commitments, and close with a memorable moral appeal that elevates the "
            "debate above politics to human dignity."
        ),
        "key_concepts": "emotional appeal, logos pathos ethos, humanitarian crisis, refugee burden-sharing, rhetorical craft",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Chair's Ruling Challenge Speech",
        "prompt": (
            "You are the delegate of Cuba in the General Assembly First Committee (DISEC). The topic "
            "is 'Preventing an Arms Race in Outer Space.' The Chair has just ruled your proposed "
            "amendment out of order, stating that it falls outside the scope of the topic because it "
            "addresses terrestrial missile defense systems that you argue are directly linked to space "
            "weaponization.\n\n"
            "You believe the Chair's ruling is incorrect. Terrestrial missile defense systems like the "
            "U.S. Ground-based Midcourse Defense (GMD) system rely on space-based sensors and could "
            "be repurposed for anti-satellite operations. You want to challenge the Chair's ruling "
            "through the appropriate procedural mechanism (appealing the decision of the Chair).\n\n"
            "Write a 90-second speech (approximately 200-250 words) that respectfully but firmly "
            "challenges the Chair's ruling. You must present a logical argument for why terrestrial "
            "missile defense falls within the scope of the topic, cite the procedural basis for your "
            "challenge, and persuade the committee to overturn the ruling through a vote. This tests "
            "advanced procedural knowledge, rhetorical precision, and the ability to challenge "
            "authority diplomatically."
        ),
        "hints": (
            "Be scrupulously respectful of the Chair — you are challenging the ruling, not the person;"
            "State the procedural basis: 'I wish to appeal the decision of the Chair pursuant to Rule...';"
            "Make a tight logical argument: space-based sensors are integral to terrestrial missile defense, therefore they fall within the space weapons topic;"
            "Keep your argument narrow and focused — do not ramble;"
            "Address your appeal to fellow delegates, who will vote on whether to sustain the Chair's ruling;"
            "Acknowledge the Chair's authority while exercising your right to appeal"
        ),
        "sample_answer": (
            "An effective challenge speech would respectfully invoke the appeal procedure, present a "
            "concise technical argument connecting ground-based missile defense to space-based components, "
            "argue that excluding terrestrial systems with space-based elements artificially narrows the "
            "topic, and appeal to delegates to overturn the ruling in the interest of comprehensive debate."
        ),
        "key_concepts": "appeal of the Chair, procedural challenge, outer space arms race, missile defense, scope of topic",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Filibuster-Style Extended Debate Speech",
        "prompt": (
            "You are the delegate of the Philippines in the General Assembly Second Committee (ECOFIN). "
            "The topic is 'Ensuring Fair Labor Standards in Global Supply Chains.' A draft resolution "
            "that your bloc opposes is about to come to a vote, and it appears to have majority support. "
            "Your bloc needs more time to negotiate concessions or propose amendments.\n\n"
            "You have secured a 2-minute slot on the Speakers' List and plan to use it strategically — "
            "not to filibuster in the traditional sense, but to deliver a substantive speech that "
            "simultaneously slows the process, introduces new arguments that create doubt, and buys "
            "your allies time to negotiate behind the scenes.\n\n"
            "The Philippines has one of the largest overseas worker populations in the world (over 10 "
            "million OFWs — Overseas Filipino Workers) and has direct experience with labor exploitation "
            "in global supply chains. However, the Philippines also depends on foreign investment in "
            "manufacturing and is cautious about overly rigid labor standards that could drive "
            "investment to competitor nations.\n\n"
            "Write a 2-minute speech (approximately 280-330 words) that is substantive enough to be "
            "legitimate but strategically designed to introduce complexity, raise new questions, and "
            "delay consensus. This tests advanced strategic speaking and the ability to use procedural "
            "awareness to achieve tactical objectives."
        ),
        "hints": (
            "Do not actually filibuster — your speech must have genuine substance to maintain credibility;"
            "Introduce a new dimension the committee has not fully considered: the impact of rigid labor standards on developing country competitiveness;"
            "Ask pointed questions that demand answers before a vote: 'Has this committee considered the unintended consequences of...';"
            "Reference the 10 million OFWs as stakeholders whose livelihoods depend on getting this right;"
            "Suggest that the draft needs further refinement — propose specific concerns that could justify reopening debate;"
            "Your goal is not to kill the resolution but to delay the vote and create space for negotiation"
        ),
        "sample_answer": (
            "A strategically crafted speech would raise legitimate concerns about the impact of rigid "
            "labor standards on developing nations' competitiveness, introduce the OFW perspective as "
            "an underexplored dimension, pose specific unanswered questions that create doubt about the "
            "draft's readiness for a vote, and conclude by suggesting the committee needs more time to "
            "refine the resolution — all while maintaining substantive credibility."
        ),
        "key_concepts": "strategic speaking, delay tactics, OFW, labor standards, supply chains, tactical rhetoric",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Keynote Speech for GA Plenary Session",
        "prompt": (
            "You are the delegate of India in the General Assembly Plenary session. The topic is "
            "'Reforming the United Nations for the 21st Century.' India is a leading candidate for "
            "permanent membership on an expanded Security Council and has long advocated for UN reform "
            "that reflects contemporary geopolitical realities rather than the post-World War II order.\n\n"
            "The General Assembly President has invited select delegates to deliver 3-minute keynote "
            "speeches presenting their vision for UN reform. India has been selected as one of six "
            "keynote speakers. This is a prestigious opportunity and your speech will be the centerpiece "
            "of India's advocacy at this conference.\n\n"
            "Write a 3-minute keynote speech (approximately 400-480 words) that presents India's "
            "comprehensive vision for UN reform. Address Security Council expansion, General Assembly "
            "revitalization, improved representation of the Global South, and the role of emerging "
            "powers. This speech should be visionary, quotable, and demonstrate the highest level of "
            "MUN oratory. It should have a clear narrative arc with an introduction, body, and "
            "memorable conclusion."
        ),
        "hints": (
            "This is a keynote — it should feel like a historic speech, not a committee intervention;"
            "Open with a compelling vision or question that frames the entire speech;"
            "Structure around 3-4 clear reform pillars: Security Council expansion, GA revitalization, Global South representation, emerging powers' role;"
            "Use India's credentials: world's largest democracy, sixth-largest economy, major troop contributor to peacekeeping;"
            "Include at least one quotable line that other delegates might remember;"
            "Build to a crescendo — your conclusion should be the most powerful moment;"
            "Reference specific reform proposals: G4 proposal for Security Council expansion, GA resolution decision-making authority"
        ),
        "sample_answer": (
            "An outstanding keynote would open with a vision of what the UN could be, systematically "
            "address Security Council expansion (citing the G4 proposal), General Assembly revitalization, "
            "and Global South representation, leverage India's credentials as a democracy, economy, and "
            "peacekeeping contributor, include memorable quotable language, and build to an inspiring "
            "conclusion about the UN fulfilling its founding promise for all nations."
        ),
        "key_concepts": "keynote speech, UN reform, Security Council expansion, G4, Global South, narrative arc, visionary rhetoric",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Point of Order with Legal Argumentation",
        "prompt": (
            "You are the delegate of Egypt in the UN Human Rights Council (UNHRC). The committee is "
            "debating 'The Role of Non-State Actors in Human Rights Protection.' A draft resolution "
            "currently under debate includes an operative clause that would grant certain NGOs the "
            "ability to submit independent reports directly to the Human Rights Council, bypassing "
            "the ECOSOC consultative status review process.\n\n"
            "You believe this clause violates ECOSOC Resolution 1996/31, which establishes the "
            "framework for NGO participation in the UN system, and that the Human Rights Council does "
            "not have the authority to unilaterally modify ECOSOC-established procedures.\n\n"
            "You raise a Point of Order. Write the speech (approximately 200-250 words, 90 seconds) "
            "that you would deliver to explain your Point of Order to the Chair. You must cite the "
            "specific procedural and legal basis for your objection, explain clearly why the operative "
            "clause exceeds the committee's authority, and request that the clause be struck or "
            "referred to ECOSOC. This tests advanced legal argumentation and procedural mastery."
        ),
        "hints": (
            "A Point of Order must reference a specific rule or procedural violation — be precise;"
            "Cite ECOSOC Resolution 1996/31 by name and explain its relevance;"
            "Argue that the UNHRC cannot override ECOSOC's authority over NGO consultative status;"
            "Be respectful but legally rigorous — this is a formal procedural intervention;"
            "Request a specific remedy: striking the clause or referring it to ECOSOC for review;"
            "Keep your argument tight and legalistic — Points of Order are not general policy speeches"
        ),
        "sample_answer": (
            "A rigorous Point of Order would cite ECOSOC Resolution 1996/31 as the governing framework "
            "for NGO participation, argue that the UNHRC lacks competence to unilaterally modify ECOSOC "
            "procedures, explain that the operative clause therefore exceeds the committee's mandate, "
            "and request that the Chair either strike the clause or refer it to ECOSOC for consideration."
        ),
        "key_concepts": "point of order, ECOSOC Resolution 1996/31, NGO consultative status, committee competence, legal argumentation",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Multilingual Diplomatic Rhetoric Strategy",
        "prompt": (
            "You are the delegate of Morocco in the General Assembly Plenary. The topic is 'Promoting "
            "Multilingualism and Cultural Diversity Within the United Nations System.' Morocco is a "
            "multilingual nation where Arabic, Amazigh (Berber), French, and increasingly English are "
            "spoken. Morocco is a co-sponsor of a draft resolution that seeks to strengthen the use "
            "of all six official UN languages and promote the inclusion of indigenous languages.\n\n"
            "You have been asked to deliver the keynote introduction of the draft resolution in a "
            "2-minute speech. As an advanced rhetorical exercise, your speech should strategically "
            "incorporate brief phrases or greetings in multiple languages (Arabic, French, and English "
            "at minimum) to demonstrate the very multilingualism the resolution promotes. However, the "
            "substance of the speech must remain in English and be fully comprehensible to all "
            "delegates.\n\n"
            "Write a 2-minute speech (approximately 280-330 words) that uses multilingual rhetorical "
            "flourishes purposefully, presents the draft resolution's key provisions, and argues for "
            "the practical and moral importance of multilingualism in international diplomacy. This "
            "tests advanced rhetorical technique, cultural sensitivity, and the ability to use "
            "language itself as a persuasive tool."
        ),
        "hints": (
            "Open with greetings in Arabic and French before switching to English — this immediately demonstrates your point;"
            "Use multilingual phrases sparingly and purposefully — they should enhance, not distract;"
            "Present 2-3 key provisions of the draft resolution clearly;"
            "Argue that linguistic diversity is not just cultural preservation but practical effectiveness — monolingual diplomacy excludes perspectives;"
            "Reference Morocco's own multilingual identity as evidence that multilingualism strengthens rather than divides;"
            "Use the speech itself as proof of concept for the resolution's vision"
        ),
        "sample_answer": (
            "An exceptional multilingual speech would open with greetings in Arabic and French, use "
            "Morocco's multilingual identity as a living example, present the draft resolution's key "
            "provisions for strengthening all six UN languages and promoting indigenous languages, argue "
            "that linguistic diversity improves the quality of diplomacy, and close with a phrase in "
            "multiple languages that underscores the resolution's message."
        ),
        "key_concepts": "multilingual rhetoric, cultural diversity, UN official languages, rhetorical technique, Morocco, draft presentation",
    },
    {
        "category_type": "SPEECH",
        "difficulty": "ADV",
        "title": "Withdrawing Sponsorship Under Pressure",
        "prompt": (
            "You are the delegate of South Korea in the General Assembly First Committee (DISEC). The "
            "topic is 'Preventing the Militarization of Outer Space.' You were originally a co-sponsor "
            "of a draft resolution led by Canada and Brazil that called for a binding treaty banning "
            "all weapons in outer space.\n\n"
            "However, during negotiations, the draft has been significantly amended to include language "
            "that would restrict the development of satellite-based early warning systems — systems "
            "that South Korea considers essential for monitoring North Korean missile launches. Your "
            "allies in the bloc have been unable or unwilling to remove this language, and you have "
            "decided you must withdraw your co-sponsorship.\n\n"
            "Write a 2-minute speech (approximately 280-330 words) announcing your withdrawal of "
            "co-sponsorship. This is a delicate diplomatic moment: you must explain why you are "
            "withdrawing without burning bridges with your former allies (Canada and Brazil), maintain "
            "your credibility on the broader topic of space weaponization, and signal openness to "
            "rejoining if the problematic language is removed. This tests the highest level of "
            "diplomatic communication — delivering bad news gracefully while preserving relationships "
            "and strategic options."
        ),
        "hints": (
            "Begin by reaffirming your commitment to the broader goal of preventing space weaponization;"
            "Express genuine appreciation for Canada and Brazil's leadership — do not burn bridges;"
            "Clearly but diplomatically identify the specific language that forced your withdrawal;"
            "Explain your national security concern (North Korean missile monitoring) without being provocative;"
            "Frame your withdrawal as principled, not petty — you still support the goal, just not this specific language;"
            "Leave the door open: state the specific condition under which you would rejoin;"
            "End with a forward-looking statement that maintains your diplomatic standing"
        ),
        "sample_answer": (
            "A masterful withdrawal speech would open by reaffirming commitment to preventing space "
            "weaponization, express genuine gratitude to bloc allies, precisely identify the problematic "
            "clause on satellite early warning systems, explain South Korea's security concern regarding "
            "North Korean missile monitoring without inflammatory language, frame the withdrawal as "
            "principled rather than hostile, state the specific change that would allow rejoining, and "
            "close by reaffirming the relationship with former allies and commitment to the broader cause."
        ),
        "key_concepts": "withdrawal of sponsorship, diplomatic grace, national security, space weaponization, preserving alliances, conditional support",
    },
]

# ── DRAFT QUESTIONS ──────────────────────────────────────────
QUESTIONS += [
    # ── BEGINNER (10) ────────────────────────────────────────────────────────
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Writing a Basic Preambulatory Clause on Pandemic Vaccines",
        "prompt": (
            "You are the delegate of Indonesia in the World Health Organization (WHO) committee. "
            "The topic under discussion is 'Ensuring Equitable Global Access to Pandemic Vaccines.' "
            "Your bloc has begun drafting a resolution and you have been asked to contribute a single "
            "preambulatory clause that establishes the context for the resolution.\n\n"
            "Indonesia, as the world's fourth-most-populous country, was heavily affected by COVID-19 "
            "and has been a vocal advocate for the COVAX facility and technology transfer agreements. "
            "The delegation believes that vaccine equity is not merely a moral imperative but a "
            "prerequisite for global economic recovery.\n\n"
            "Write one properly formatted preambulatory clause (PP) that references an existing UN "
            "document or WHO framework, establishes the urgency of equitable vaccine distribution, "
            "and reflects Indonesia's priorities. Remember that preambulatory clauses begin with "
            "italicized participles or adjectives (e.g., 'Recalling,' 'Deeply concerned,' 'Noting "
            "with alarm') and end with a comma."
        ),
        "hints": (
            "Use an appropriate opening participle such as 'Deeply concerned' or 'Recognizing';"
            "Reference a real UN document like WHA resolution 73.1 or the COVAX framework;"
            "Keep the clause to one or two sentences that set the stage for operative action;"
            "End the clause with a comma, not a period or semicolon"
        ),
        "sample_answer": (
            "A strong preambulatory clause might read: 'Deeply concerned that, as of 2024, low-income "
            "countries have received less than 20 percent of global vaccine doses despite bearing a "
            "disproportionate burden of pandemic mortality, and recalling World Health Assembly resolution "
            "73.1 (2020) which called upon Member States to ensure equitable access to diagnostics, "
            "therapeutics, and vaccines,' — This clause effectively references an existing framework, "
            "cites a concrete statistic to establish urgency, and aligns with Indonesia's advocacy for "
            "equitable distribution through multilateral mechanisms."
        ),
        "key_concepts": "preambulatory clause, PP formatting, vaccine equity, referencing UN documents, opening participles",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Writing a Single Operative Clause on Climate Finance",
        "prompt": (
            "You are the delegate of Nigeria in the United Nations Environment Programme (UNEP). "
            "The committee is debating 'Mobilizing Climate Finance for Developing Nations.' Your "
            "working paper group has asked you to draft one operative clause that proposes a concrete "
            "action for the international community.\n\n"
            "Nigeria, as Africa's largest economy, faces severe climate impacts including desertification "
            "in the north, coastal erosion in the south, and increasing frequency of extreme weather "
            "events. Nigeria has called for developed nations to fulfill their $100 billion annual "
            "climate finance pledge and to increase concessional lending through the Green Climate Fund.\n\n"
            "Write one properly formatted operative clause (OP) that proposes a specific, actionable "
            "step related to climate finance. Operative clauses begin with an active verb in the present "
            "tense (e.g., 'Calls upon,' 'Urges,' 'Recommends') and end with a semicolon. Each clause "
            "should be numbered."
        ),
        "hints": (
            "Begin with an appropriate operative verb such as 'Urges,' 'Calls upon,' or 'Requests';"
            "Specify which actors are being asked to do what — avoid vague language;"
            "Include a measurable or concrete action, such as a funding target or timeline;"
            "End the operative clause with a semicolon"
        ),
        "sample_answer": (
            "A well-crafted operative clause might read: '1. Calls upon all developed country Parties "
            "to the United Nations Framework Convention on Climate Change to fulfill and exceed their "
            "collective commitment of mobilizing USD 100 billion annually in climate finance by 2025, "
            "with at least 50 percent allocated to adaptation projects in least developed countries and "
            "small island developing states;' — This clause uses the correct operative verb format, "
            "identifies specific actors and a concrete financial target, includes a timeline, and "
            "prioritizes vulnerable nations."
        ),
        "key_concepts": "operative clause, OP formatting, climate finance, actionable language, specificity in drafting",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Formatting a Simple Single-Topic Resolution on Ocean Pollution",
        "prompt": (
            "You are the delegate of the Philippines in the General Assembly Plenary. The committee "
            "topic is 'Addressing Marine Plastic Pollution in Coastal Developing Nations.' You have "
            "been asked to draft a short, simple resolution containing three preambulatory clauses and "
            "three operative clauses on this single issue.\n\n"
            "The Philippines is one of the top contributors to ocean plastic waste, largely due to "
            "inadequate waste management infrastructure and the prevalence of single-use plastics in "
            "daily commerce. However, the country has also launched initiatives like the Extended "
            "Producer Responsibility Act of 2022 and community-based coastal cleanup programs. The "
            "Philippines seeks international support for waste management infrastructure and technology "
            "transfer.\n\n"
            "Write a properly formatted mini-resolution with a header (committee name, sponsors, "
            "signatories, topic), three preambulatory clauses (PPs), and three operative clauses (OPs). "
            "Focus on one single issue: reducing marine plastic pollution through international "
            "cooperation and infrastructure support."
        ),
        "hints": (
            "Include a proper header with committee, topic, sponsors, and signatories;"
            "Each PP should begin with a different participle or adjective and end with a comma;"
            "Each OP should begin with a different operative verb, be numbered, and end with a semicolon "
            "(except the last, which ends with a period);"
            "Keep the resolution focused on one issue — do not try to solve everything"
        ),
        "sample_answer": (
            "A complete mini-resolution should include: a header identifying the GA Plenary as the "
            "committee and listing the Philippines as sponsor; three PPs referencing relevant frameworks "
            "like UNEA Resolution 5/14, stating the scale of the problem, and acknowledging developing "
            "nations' challenges; three numbered OPs that propose specific actions such as establishing "
            "a technical assistance fund, encouraging technology transfer for recycling infrastructure, "
            "and requesting the Secretary-General to report on implementation progress. The last OP "
            "should end with a period. Formatting must follow standard UN resolution conventions."
        ),
        "key_concepts": "resolution structure, header formatting, PP and OP conventions, single-topic focus, proper punctuation",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Choosing Correct Operative Verbs for a Food Security Resolution",
        "prompt": (
            "You are the delegate of Ethiopia in the Food and Agriculture Organization (FAO) committee. "
            "The topic is 'Strengthening Global Food Security in the Face of Climate Change.' Your bloc "
            "leader has written a draft resolution, but the operative verbs are all incorrect or "
            "inappropriate for the body in question. You have been asked to fix them.\n\n"
            "Ethiopia, located in the Horn of Africa, is highly vulnerable to drought and food "
            "insecurity. The country has experience with the Productive Safety Net Programme and has "
            "advocated for climate-resilient agriculture practices. Ethiopia wants the FAO to take "
            "concrete steps to support smallholder farmers in adapting to changing rainfall patterns.\n\n"
            "Below are five operative clauses with incorrect verbs. Rewrite each clause using the "
            "correct operative verb, keeping in mind that the FAO is a specialized agency (not the "
            "Security Council) and therefore cannot use verbs like 'Demands' or 'Decides' in a binding "
            "sense. Choose from appropriate verbs such as 'Encourages,' 'Recommends,' 'Invites,' "
            "'Requests,' or 'Calls upon.'\n\n"
            "1. Demands all Member States to increase agricultural research funding;\n"
            "2. Orders the FAO Director-General to establish a climate-resilient seed bank network;\n"
            "3. Declares that all nations must adopt drought-resistant crop varieties;\n"
            "4. Commands developed nations to transfer agricultural technology;\n"
            "5. Mandates the creation of a global food reserve system;"
        ),
        "hints": (
            "Remember that GA bodies and specialized agencies use recommendatory language, not binding;"
            "Verbs like 'Demands,' 'Orders,' 'Declares,' 'Commands,' and 'Mandates' are too strong "
            "for the FAO — they imply binding authority that the body does not possess;"
            "'Encourages,' 'Recommends,' 'Invites,' 'Calls upon,' and 'Requests' are appropriate;"
            "Match the verb strength to the action: 'Requests' for asking the Secretariat, 'Encourages' "
            "for suggesting to Member States"
        ),
        "sample_answer": (
            "Corrected clauses should use appropriate recommendatory verbs: 1. 'Encourages all Member "
            "States to increase agricultural research funding;' 2. 'Requests the FAO Director-General "
            "to explore the establishment of a climate-resilient seed bank network;' 3. 'Recommends "
            "that all nations consider adopting drought-resistant crop varieties;' 4. 'Calls upon "
            "developed nations to facilitate the transfer of agricultural technology;' 5. 'Invites "
            "Member States to contribute to the creation of a global food reserve system;' Each verb "
            "reflects the advisory nature of FAO resolutions."
        ),
        "key_concepts": "operative verbs, committee authority, recommendatory vs binding language, FAO powers, verb-body alignment",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Drafting Preambulatory Clauses Referencing Existing Frameworks on Digital Privacy",
        "prompt": (
            "You are the delegate of Germany in the Third Committee (SOCHUM). The topic under "
            "discussion is 'Protecting Digital Privacy Rights in the Age of Mass Surveillance.' You "
            "need to write three preambulatory clauses that reference existing international frameworks "
            "and establish the legal and normative basis for your resolution.\n\n"
            "Germany has a strong tradition of privacy protection, shaped by its historical experience "
            "with surveillance under both the Nazi and East German regimes. Germany was among the "
            "co-sponsors of GA Resolution 68/167 on the right to privacy in the digital age, and "
            "the country's Federal Constitutional Court has established a constitutional right to "
            "informational self-determination. Germany seeks robust international standards for data "
            "protection.\n\n"
            "Write three preambulatory clauses that each reference a different existing document or "
            "framework: (1) a UN General Assembly resolution, (2) the Universal Declaration of Human "
            "Rights or another international human rights instrument, and (3) a report by a UN Special "
            "Rapporteur or other expert body. Each clause should use a different opening participle."
        ),
        "hints": (
            "Use different opening words for each clause: e.g., 'Reaffirming,' 'Guided by,' 'Taking note of';"
            "Reference real documents: GA Res. 68/167, Article 12 of the UDHR, reports by the Special "
            "Rapporteur on the right to privacy;"
            "Each PP should be one to two sentences and end with a comma;"
            "The clauses should build a logical progression from established rights to current concerns"
        ),
        "sample_answer": (
            "Three well-constructed PPs might include: (1) 'Reaffirming General Assembly resolution "
            "68/167 of 18 December 2013, entitled \"The right to privacy in the digital age,\" which "
            "affirmed that the rights held by people offline must also be protected online,' (2) 'Guided "
            "by Article 12 of the Universal Declaration of Human Rights and Article 17 of the "
            "International Covenant on Civil and Political Rights, both of which protect individuals "
            "against arbitrary interference with their privacy, family, home, or correspondence,' "
            "(3) 'Taking note of the report of the Special Rapporteur on the right to privacy "
            "(A/HRC/31/64), which highlighted the need for independent oversight mechanisms to govern "
            "State surveillance programs,' — These clauses reference three distinct frameworks, use "
            "different opening participles, and build a coherent legal foundation."
        ),
        "key_concepts": "preambulatory references, UN document citations, UDHR, Special Rapporteur reports, legal foundations",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Writing an Operative Clause with Sub-Clauses on Refugee Protection",
        "prompt": (
            "You are the delegate of Kenya in the United Nations High Commissioner for Refugees "
            "(UNHCR) Executive Committee simulation. The topic is 'Strengthening the International "
            "Framework for Refugee Protection.' You have been asked to write a single operative clause "
            "that contains two or three sub-clauses (sub-operative points).\n\n"
            "Kenya hosts one of the largest refugee populations in Africa, with the Dadaab and Kakuma "
            "refugee complexes sheltering hundreds of thousands of refugees primarily from Somalia and "
            "South Sudan. Kenya has expressed frustration with the uneven global distribution of refugee "
            "hosting responsibilities and has called for greater burden-sharing under the Global Compact "
            "on Refugees.\n\n"
            "Write one operative clause with the main action, followed by two or three lettered "
            "sub-clauses (a, b, c) that provide specific details or implementation steps. The main "
            "clause should address burden-sharing, and the sub-clauses should specify mechanisms or "
            "targets. Use proper formatting: the main clause begins with a numbered operative verb, "
            "sub-clauses are lettered and indented."
        ),
        "hints": (
            "The main clause should state the overall action, such as 'Calls upon the international "
            "community to enhance burden-sharing mechanisms';"
            "Sub-clauses should elaborate with specifics: e.g., (a) financial contributions, "
            "(b) resettlement quotas, (c) technical assistance;"
            "Sub-clauses use lowercase letters and begin with a gerund or present participle;"
            "The last sub-clause ends with a semicolon (or period if it is the last OP in the resolution)"
        ),
        "sample_answer": (
            "A well-structured operative clause with sub-clauses might read: '1. Calls upon all Member "
            "States to strengthen equitable responsibility-sharing for refugee protection, in accordance "
            "with the Global Compact on Refugees, by: (a) Increasing annual financial contributions to "
            "UNHCR to meet at least 75 percent of the agency's operational budget requirements; "
            "(b) Expanding third-country resettlement programs to accommodate no fewer than 10 percent "
            "of the protracted refugee population annually; (c) Providing technical and logistical "
            "support to host countries for the integration of refugees into national education and "
            "healthcare systems;' — This format correctly uses a main clause with specific, measurable "
            "sub-operative points."
        ),
        "key_concepts": "sub-clauses, operative clause structure, burden-sharing, Global Compact on Refugees, formatting with lettered sub-points",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Identifying Errors in a Draft Resolution on Women's Empowerment",
        "prompt": (
            "You are the delegate of Morocco in the Commission on the Status of Women (CSW), simulated "
            "within the SOCHUM framework. The topic is 'Advancing Women's Economic Empowerment in "
            "Developing Nations.' A fellow delegate has written a short draft resolution, but it "
            "contains several formatting and substantive errors. Your task is to identify and correct them.\n\n"
            "Morocco has made significant strides in women's empowerment, including reforms to the "
            "Moudawana (family code) and the launch of the Maroc Digital 2025 strategy, which includes "
            "provisions for women's digital inclusion. Morocco seeks pragmatic, culturally sensitive "
            "approaches to women's economic empowerment.\n\n"
            "Here is the draft with errors:\n\n"
            "COMMITTEE: SOCHUM\nTOPIC: Women's Empowerment\nSPONSORS: Morocco\n\n"
            "Recalling the Beijing Declaration and Platform for Action.\n"
            "Concerned by the ongoing gender pay gap in developing nations,\n"
            "Aware that women make up the majority of informal sector workers.\n\n"
            "1. Demands all Member States to close the gender pay gap within two years;\n"
            "2. Encourages the creation of women's entrepreneurship programs\n"
            "3. requests the Secretary-General to provide a report on progress.\n\n"
            "Find and explain all formatting, punctuation, substantive, and verb-appropriateness "
            "errors in this draft."
        ),
        "hints": (
            "Check PP punctuation: PPs should end with commas, not periods;"
            "Check OP verbs: 'Demands' is too strong for SOCHUM — use recommendatory language;"
            "Check OP punctuation: each OP should end with a semicolon except the last, which ends "
            "with a period;"
            "Check capitalization: operative verbs should be capitalized;"
            "Check realism: closing the gender pay gap within two years is unrealistic"
        ),
        "sample_answer": (
            "Errors include: (1) PPs 1 and 3 end with periods instead of commas; (2) 'Demands' in OP 1 "
            "is inappropriate for SOCHUM, which has no binding authority — 'Encourages' or 'Urges' "
            "would be correct; (3) The target of closing the gender pay gap within two years is "
            "unrealistic and would not gain consensus; (4) OP 2 is missing its ending semicolon; "
            "(5) OP 3 begins with a lowercase 'requests' — operative verbs must be capitalized; "
            "(6) The header is missing signatories; (7) The topic line should use the full, formal "
            "topic title. Correcting these errors would produce a properly formatted, diplomatically "
            "realistic resolution."
        ),
        "key_concepts": "resolution error identification, PP punctuation, OP formatting, verb appropriateness, realism in drafting",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Drafting a Resolution Header and Sponsorship Block on Cyber Warfare",
        "prompt": (
            "You are the delegate of Japan in the First Committee (DISEC). The topic is 'Establishing "
            "Norms for State Behavior in Cyberspace.' Your working paper group is ready to convert "
            "your working paper into a draft resolution, and you have been assigned to write the "
            "header and sponsorship block.\n\n"
            "Japan has been a strong advocate for the application of existing international law to "
            "cyberspace and has supported the work of the UN Group of Governmental Experts (GGE) on "
            "information security. Japan's position emphasizes voluntary, non-binding norms of "
            "responsible state behavior, capacity-building for developing nations, and confidence-"
            "building measures. Your bloc includes Japan, Germany, Brazil, Kenya, and India as "
            "sponsors, with Mexico, Philippines, and Morocco as signatories.\n\n"
            "Write a complete and properly formatted resolution header including: the committee name, "
            "the document number format, the topic, the list of sponsors, the list of signatories, "
            "and any relevant procedural notes. Follow standard MUN resolution formatting conventions."
        ),
        "hints": (
            "The committee should be listed as 'General Assembly First Committee (DISEC)';"
            "Include a document number in the format typical for your conference (e.g., DR-1-1);"
            "List sponsors and signatories separately — sponsors are delegates who wrote the resolution, "
            "signatories merely want it discussed;"
            "Include the full formal topic title"
        ),
        "sample_answer": (
            "A properly formatted header should include: 'Committee: General Assembly First Committee "
            "(DISEC)' / 'Topic: Establishing Norms for State Behavior in Cyberspace' / "
            "'Document Number: DR-1-1' / 'Sponsors: Japan, Germany, Brazil, Kenya, India' / "
            "'Signatories: Mexico, Philippines, Morocco' — The header establishes the procedural "
            "foundation of the document and must be complete before any substantive clauses. Some "
            "conferences also require a date and a 'Submitted by' line indicating the primary author."
        ),
        "key_concepts": "resolution header, sponsors vs signatories, document numbering, committee identification, procedural formatting",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Writing a Final Operative Clause Requesting a Report on Biodiversity",
        "prompt": (
            "You are the delegate of Colombia in the United Nations Environment Programme (UNEP). "
            "The topic is 'Protecting Biodiversity in Megadiverse Countries.' Your resolution is nearly "
            "complete, and you need to write the final operative clause, which traditionally requests "
            "a follow-up mechanism or report.\n\n"
            "Colombia is one of the world's 17 megadiverse countries, home to approximately 10 percent "
            "of the planet's biodiversity. Colombia has championed the Kunming-Montreal Global "
            "Biodiversity Framework (GBF) and has called for the establishment of a dedicated fund for "
            "biodiversity conservation. The delegation wants the final clause to ensure accountability "
            "by requesting the Secretary-General to monitor and report on implementation.\n\n"
            "Write the final operative clause of the resolution. It should request the Secretary-General "
            "or another appropriate body to submit a report on the implementation of this resolution to "
            "the General Assembly or the relevant committee. The final operative clause should end with "
            "a period (not a semicolon) and include a timeline for the report."
        ),
        "hints": (
            "Use 'Requests' as the operative verb when directing the Secretary-General or Secretariat;"
            "Specify what body should receive the report (e.g., 'the General Assembly at its eighty-first session');"
            "Include a timeline: when should the report be submitted;"
            "End with a period, as this is the last operative clause"
        ),
        "sample_answer": (
            "A well-crafted final operative clause might read: '12. Requests the Secretary-General to "
            "submit a comprehensive report on the implementation of the present resolution to the "
            "General Assembly at its eighty-second session, including an assessment of progress toward "
            "the targets established in the Kunming-Montreal Global Biodiversity Framework and "
            "recommendations for further action by Member States and relevant international "
            "organizations.' — This clause uses the correct verb for directing the Secretariat, specifies "
            "the receiving body and session, describes the scope of the report, and ends with a period."
        ),
        "key_concepts": "final operative clause, requesting reports, Secretary-General, accountability mechanisms, proper ending punctuation",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "BEG",
        "title": "Converting a Policy Idea into Clause Language on Water Rights",
        "prompt": (
            "You are the delegate of Bangladesh in the Economic and Social Council (ECOFIN). The topic "
            "is 'Ensuring Universal Access to Clean Water and Sanitation.' A fellow delegate in your "
            "bloc has proposed the following policy idea in plain language: 'We should create a fund "
            "that helps poor countries build water treatment plants, and rich countries should pay for "
            "it, and the UN should check every year to make sure the money is being used correctly.'\n\n"
            "Bangladesh faces severe water challenges, including arsenic contamination of groundwater, "
            "seasonal flooding, and limited access to sanitation in rural areas. Despite these "
            "challenges, Bangladesh has made progress through community-based water management "
            "programs and NGO partnerships. The delegation supports international financial mechanisms "
            "for water infrastructure.\n\n"
            "Convert the plain-language policy idea above into two properly formatted operative clauses "
            "that use formal UN resolution language. The first clause should establish the fund, and the "
            "second should create the monitoring mechanism. Use appropriate operative verbs and maintain "
            "the substance of the original idea while elevating the language to diplomatic standards."
        ),
        "hints": (
            "Replace informal language with formal equivalents: 'poor countries' becomes 'least developed "
            "countries,' 'rich countries' becomes 'developed country parties,' 'check' becomes 'review';"
            "Use appropriate operative verbs: 'Establishes' or 'Recommends the creation of' for the fund, "
            "'Requests' for the monitoring mechanism;"
            "Include specifics where possible: name the fund, specify the review cycle;"
            "Maintain proper OP formatting with numbering and punctuation"
        ),
        "sample_answer": (
            "Two properly formatted operative clauses might read: '1. Recommends the establishment of a "
            "Clean Water Infrastructure Fund, administered under the auspices of the United Nations "
            "Development Programme, to provide grants and concessional loans to least developed countries "
            "for the construction and rehabilitation of water treatment facilities, financed through "
            "voluntary contributions from developed country parties; 2. Requests the Secretary-General "
            "to conduct an annual review of the Fund's disbursements and to report on the effectiveness "
            "of funded projects to the Economic and Social Council at each substantive session.' — "
            "These clauses transform the informal idea into formal UN language while preserving the "
            "policy substance."
        ),
        "key_concepts": "converting informal to formal language, operative clause drafting, UN terminology, fund establishment, monitoring mechanisms",
    },
    # ── INTERMEDIATE (10) ────────────────────────────────────────────────────
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Drafting a Multi-Clause Resolution Section on Nuclear Nonproliferation",
        "prompt": (
            "You are the delegate of Brazil in the First Committee (DISEC). The topic is 'Strengthening "
            "the Nuclear Nonproliferation Regime.' Your working paper group has been assigned to draft "
            "the operative section of a resolution that addresses three interconnected sub-issues: "
            "(1) universalization of the NPT, (2) establishment of Nuclear-Weapon-Free Zones (NWFZs), "
            "and (3) verification mechanisms through the IAEA.\n\n"
            "Brazil is a state party to the NPT and the Treaty of Tlatelolco, which established Latin "
            "America as a NWFZ. Brazil operates a uranium enrichment program for peaceful purposes and "
            "is sensitive to any measures that could restrict civilian nuclear technology. Brazil supports "
            "disarmament under Article VI of the NPT and has called for nuclear-weapon states to fulfill "
            "their disarmament obligations.\n\n"
            "Draft a set of six operative clauses (two per sub-issue) that form a coherent operative "
            "section. The clauses should be logically ordered, build upon each other, and use "
            "appropriately varied operative verbs. Include at least one clause with sub-clauses "
            "(lettered sub-points). Ensure the language reflects DISEC's authority as a recommending body."
        ),
        "hints": (
            "Group the clauses by sub-issue but ensure they flow logically from general to specific;"
            "Use a range of operative verbs: 'Reaffirms,' 'Calls upon,' 'Encourages,' 'Requests,' "
            "'Recommends,' 'Urges';"
            "At least one clause should have sub-clauses (a, b, c) for implementation details;"
            "Remember that DISEC recommends — it does not bind. Avoid language that implies enforcement authority"
        ),
        "sample_answer": (
            "A coherent six-clause operative section should: (1) Reaffirm the NPT as the cornerstone of "
            "the nonproliferation regime; (2) Call upon states not party to the NPT to accede to it without "
            "conditions; (3) Encourage the establishment of new NWFZs, particularly in the Middle East, with "
            "sub-clauses detailing: (a) convening a regional conference, (b) requesting IAEA technical "
            "assistance, (c) establishing a timeline for negotiations; (4) Request the IAEA to strengthen "
            "safeguards agreements; (5) Urge nuclear-weapon states to fulfill Article VI disarmament "
            "obligations; (6) Recommend the creation of a working group to assess verification technology "
            "needs. The clauses should demonstrate logical progression and avoid overstepping DISEC's mandate."
        ),
        "key_concepts": "multi-clause coherence, sub-issue organization, varied operative verbs, DISEC authority, NPT framework, sub-clauses",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Writing an Amendment to Strengthen a Clause on AI Governance",
        "prompt": (
            "You are the delegate of India in the General Assembly Plenary. The topic is 'Establishing "
            "an International Framework for Artificial Intelligence Governance.' A draft resolution has "
            "been submitted by the European bloc, and your delegation has concerns about Operative "
            "Clause 4, which currently reads:\n\n"
            "'4. Encourages Member States to develop national AI governance frameworks that align with "
            "international standards for transparency and accountability;'\n\n"
            "India, as a major technology hub with a rapidly growing AI sector, believes this clause "
            "is too vague and does not adequately address the needs of developing countries. India wants "
            "to (1) specify that capacity-building support should be provided to developing nations, "
            "(2) add a reference to the protection of data sovereignty, and (3) include a mechanism "
            "for technology transfer. India does not want to delete the original clause but wants to "
            "strengthen it through a friendly or unfriendly amendment.\n\n"
            "Draft the amendment to Operative Clause 4, using proper amendment formatting. Show both "
            "the original text and the proposed amended text, clearly indicating what is being added, "
            "deleted, or modified. Explain whether this would be a friendly or unfriendly amendment "
            "and the procedural implications."
        ),
        "hints": (
            "Use the standard amendment format: 'The delegate of India proposes to amend Operative "
            "Clause 4 by...' followed by the specific changes;"
            "Clearly mark additions (underline or bold) and deletions (strikethrough) if using text formatting;"
            "A friendly amendment requires the consent of all sponsors; an unfriendly amendment requires "
            "a vote of the committee;"
            "The amendment should add substance without completely rewriting the clause"
        ),
        "sample_answer": (
            "The amendment should read: 'The delegate of India proposes to amend Operative Clause 4 to "
            "read: 4. Encourages Member States to develop national AI governance frameworks that align "
            "with international standards for transparency and accountability, while respecting national "
            "data sovereignty, by: (a) Requesting developed countries to provide technical assistance and "
            "capacity-building support to developing nations in the establishment of AI regulatory "
            "institutions; (b) Facilitating the transfer of AI governance best practices and open-source "
            "tools through South-South and triangular cooperation mechanisms; (c) Ensuring that "
            "international AI standards account for the varying levels of technological development "
            "among Member States;' — This would likely be an unfriendly amendment since it substantially "
            "changes the scope of the clause, requiring a committee vote. The amendment adds specificity "
            "and addresses developing-country concerns."
        ),
        "key_concepts": "amendment drafting, friendly vs unfriendly amendments, clause modification, AI governance, data sovereignty, procedural implications",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Merging Two Working Papers on Terrorism Financing",
        "prompt": (
            "You are the delegate of Saudi Arabia in the Sixth Committee (Legal). The topic is "
            "'Strengthening International Legal Frameworks to Combat Terrorism Financing.' Two working "
            "papers have been submitted by rival blocs, and you have been tasked with merging them into "
            "a single draft resolution that both blocs can support.\n\n"
            "Working Paper 1 (Western bloc — led by Germany): Focuses on enhanced financial transparency, "
            "requiring all Member States to implement Financial Action Task Force (FATF) recommendations, "
            "strengthening Know Your Customer (KYC) regulations, and establishing a centralized UN "
            "database of designated terrorist financiers.\n\n"
            "Working Paper 2 (G77 bloc — led by Saudi Arabia): Emphasizes respect for national sovereignty "
            "in financial regulation, capacity-building for developing nations' financial intelligence "
            "units, addressing root causes of terrorism, and ensuring that counter-terrorism financing "
            "measures do not impede legitimate charitable giving (particularly Islamic zakat).\n\n"
            "Draft the operative section of a merged resolution (at least eight operative clauses) that "
            "incorporates key elements from both working papers. The merged text must find compromise "
            "language where the two papers conflict, particularly on the tension between transparency "
            "requirements and sovereignty concerns."
        ),
        "hints": (
            "Identify areas of overlap: both papers want to combat terrorism financing, so start there;"
            "For conflicting provisions, use compromise language: instead of 'requires' use 'encourages' "
            "with caveats like 'in accordance with national legal frameworks';"
            "Address the charitable giving concern explicitly to secure G77 support;"
            "Include capacity-building provisions to balance transparency requirements;"
            "Order clauses from consensus items to more contentious ones"
        ),
        "sample_answer": (
            "A merged resolution should include clauses that: (1) Reaffirm the importance of combating "
            "terrorism financing under existing UN conventions; (2) Encourage implementation of FATF "
            "recommendations 'in accordance with national legal frameworks and capacities'; (3) Call for "
            "capacity-building assistance to help developing nations strengthen financial intelligence "
            "units; (4) Recommend enhanced KYC regulations while 'ensuring that such measures do not "
            "impede legitimate charitable, religious, and humanitarian giving'; (5) Request the "
            "Secretary-General to explore the feasibility of a voluntary information-sharing mechanism "
            "(compromise on the centralized database); (6) Urge Member States to address root causes of "
            "terrorism through development and education; (7) Establish a review mechanism; (8) Request "
            "a progress report. This approach takes strong provisions from both papers and softens them "
            "with qualifiers that both blocs can accept."
        ),
        "key_concepts": "merger documents, compromise language, bloc reconciliation, FATF framework, sovereignty vs transparency, charitable giving protections",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Integrating Bloc Positions into a Draft on Economic Inequality",
        "prompt": (
            "You are the delegate of South Africa in the Second Committee (ECOFIN). The topic is "
            "'Reducing Global Economic Inequality through Inclusive Trade Policies.' Three blocs have "
            "submitted position statements, and as the lead author of the working paper, you must draft "
            "a preamble that reflects all three perspectives without alienating any bloc.\n\n"
            "Bloc A (African Group — led by South Africa): Emphasizes the legacy of colonialism and "
            "structural inequality in the global trading system, calls for special and differential "
            "treatment (SDT) for developing countries under WTO rules, and demands reform of Bretton "
            "Woods institutions to give developing nations greater voting power.\n\n"
            "Bloc B (EU bloc — led by Germany): Focuses on rules-based trade, intellectual property "
            "protection, good governance as a prerequisite for development, and sustainable development "
            "goals as the framework for reducing inequality.\n\n"
            "Bloc C (Latin American bloc — led by Argentina): Advocates for regional trade agreements, "
            "commodity price stabilization mechanisms, debt relief for heavily indebted countries, and "
            "South-South cooperation.\n\n"
            "Draft a preamble of eight preambulatory clauses that incorporates perspectives from all "
            "three blocs. Each clause should clearly draw from at least one bloc's position while "
            "being written in language acceptable to all."
        ),
        "hints": (
            "Start with universally agreed principles: the UN Charter, SDGs, previous ECOFIN resolutions;"
            "Address sensitive topics like colonialism with diplomatic language: 'historical factors that "
            "have contributed to structural inequality' rather than 'colonialism';"
            "Incorporate EU priorities by referencing good governance and rule of law alongside "
            "development goals;"
            "Include Latin American concerns through references to commodity-dependent economies and "
            "regional cooperation;"
            "Avoid language that explicitly blames any group of countries"
        ),
        "sample_answer": (
            "Eight PPs should cover: (1) Reaffirming the UN Charter's commitment to social progress "
            "and better standards of life (universal); (2) Recalling the 2030 Agenda and SDG 10 on "
            "reducing inequality (EU/universal); (3) Acknowledging historical factors that have "
            "contributed to structural imbalances in the international economic system (Africa); "
            "(4) Recognizing the importance of a rules-based multilateral trading system (EU); "
            "(5) Noting the particular vulnerability of commodity-dependent economies to price "
            "volatility (Latin America); (6) Emphasizing the role of good governance, transparency, "
            "and the rule of law in fostering sustainable economic development (EU); (7) Affirming the "
            "value of South-South and triangular cooperation as complements to North-South cooperation "
            "(Latin America/Africa); (8) Deeply concerned by the widening gap between developed and "
            "developing nations as evidenced by UNCTAD and World Bank data (Africa/universal). This "
            "preamble weaves together all three perspectives."
        ),
        "key_concepts": "bloc integration, multi-perspective drafting, diplomatic language, preamble construction, ECOFIN authority, consensus-building",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Drafting Operative Clauses with Implementation Timelines on Child Soldiers",
        "prompt": (
            "You are the delegate of Colombia in the United Nations Human Rights Council (UNHRC). "
            "The topic is 'Ending the Recruitment and Use of Child Soldiers.' Your bloc has agreed on "
            "several policy proposals, and you have been asked to draft five operative clauses that "
            "include specific implementation timelines and measurable benchmarks.\n\n"
            "Colombia has direct experience with the issue of child soldiers, as armed groups including "
            "the FARC and ELN historically recruited minors. Colombia's 2016 peace agreement included "
            "provisions for the demobilization and reintegration of child combatants, and the country "
            "has established specialized programs through the Colombian Institute for Family Welfare "
            "(ICBF). Colombia advocates for comprehensive reintegration programs and accountability "
            "for recruiters.\n\n"
            "Draft five operative clauses that each include: (1) a clear action, (2) a responsible "
            "actor or body, (3) a timeline or deadline, and (4) a measurable outcome or benchmark. "
            "The clauses should address different aspects of the issue: prevention, demobilization, "
            "reintegration, accountability, and monitoring. Use appropriately varied operative verbs."
        ),
        "hints": (
            "Each clause needs four elements: action, actor, timeline, and benchmark;"
            "Timelines should be realistic: use phrases like 'within 24 months,' 'by the end of the "
            "current biennium,' or 'no later than [specific session]';"
            "Benchmarks should be measurable: 'reduce the number of documented cases by 30 percent,' "
            "'establish programs in at least 15 affected countries';"
            "Vary the responsible actors: UNICEF, SRSG for Children and Armed Conflict, Member States, "
            "regional organizations, the ICC"
        ),
        "sample_answer": (
            "Five operative clauses with timelines might address: (1) Prevention — 'Urges Member States "
            "to enact or strengthen national legislation criminalizing the recruitment of children under "
            "18 by armed forces or groups, with the goal of universal legislative coverage by 2028;' "
            "(2) Demobilization — 'Requests UNICEF to expand community-based demobilization programs in "
            "at least 20 conflict-affected countries within 36 months;' (3) Reintegration — 'Calls upon "
            "donor states to increase funding for psychosocial support and educational reintegration "
            "programs by 40 percent over the next biennium;' (4) Accountability — 'Encourages the ICC "
            "and national courts to prioritize prosecution of individuals who recruit child soldiers, "
            "reporting on progress annually;' (5) Monitoring — 'Requests the SRSG for Children and "
            "Armed Conflict to submit a biennial report with measurable benchmarks.' Each clause is "
            "specific, actionable, and time-bound."
        ),
        "key_concepts": "implementation timelines, measurable benchmarks, multi-aspect resolution design, UNHRC authority, child soldier frameworks",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Writing a Compromise Clause on Sanctions Reform",
        "prompt": (
            "You are the delegate of Turkey in the Security Council simulation. The topic is 'Reforming "
            "UN Sanctions Regimes to Minimize Humanitarian Impact.' Two permanent members have opposing "
            "views, and you have been asked to draft a compromise operative clause that both sides might "
            "accept.\n\n"
            "The United States position: Sanctions are essential tools for maintaining international peace "
            "and security. Any reform must not weaken the deterrent effect of sanctions. The US opposes "
            "automatic sunset clauses and insists on maintaining the Sanctions Committee's discretion.\n\n"
            "Russia's position: Sanctions are often imposed for political purposes and disproportionately "
            "harm civilian populations. Russia demands mandatory humanitarian exemptions, automatic sunset "
            "clauses (requiring active renewal), and greater transparency in the listing and delisting "
            "process.\n\n"
            "Turkey, as a non-permanent member and a country affected by sanctions on neighboring states, "
            "seeks a middle ground. Draft two operative clauses that propose a compromise: one addressing "
            "humanitarian exemptions and one addressing the duration of sanctions regimes. Each clause "
            "must include language that both the US and Russia could potentially accept."
        ),
        "hints": (
            "For humanitarian exemptions: instead of 'mandatory,' use 'strengthened' or 'enhanced' — "
            "allow for exemptions without making them automatic;"
            "For duration: instead of 'automatic sunset clauses,' propose 'periodic mandatory review' "
            "that does not automatically terminate sanctions but requires active re-examination;"
            "Use Security Council-appropriate verbs: 'Decides,' 'Directs,' 'Requests' — the SC has "
            "binding authority;"
            "Include enough flexibility for both sides to claim partial victory"
        ),
        "sample_answer": (
            "Two compromise clauses might read: (1) 'Decides to strengthen humanitarian exemption "
            "procedures within all current and future sanctions regimes by directing the relevant "
            "Sanctions Committees to establish expedited review processes for humanitarian aid "
            "applications, with a target response time of 30 days, while preserving the Committees' "
            "authority to assess each application on its merits;' — This gives Russia stronger "
            "humanitarian provisions without making them automatic, preserving US-desired discretion. "
            "(2) 'Decides that all sanctions regimes shall be subject to a comprehensive review every "
            "18 months by the relevant Sanctions Committee, which shall submit a report to the Security "
            "Council assessing the sanctions' effectiveness and humanitarian impact, and recommending "
            "modifications or continuation;' — This addresses Russia's concern about indefinite "
            "sanctions through mandatory reviews without creating automatic sunset clauses the US opposes."
        ),
        "key_concepts": "compromise drafting, Security Council authority, sanctions reform, humanitarian exemptions, P5 dynamics, balancing positions",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Structuring a Resolution with Thematic Sections on Space Governance",
        "prompt": (
            "You are the delegate of Mexico in the Committee on the Peaceful Uses of Outer Space "
            "(COPUOS), simulated within the SPECPOL framework. The topic is 'Governing the "
            "Commercialization of Outer Space.' Your working paper group wants to organize the "
            "resolution into clearly labeled thematic sections — a technique used in longer, more "
            "complex resolutions.\n\n"
            "Mexico, while not a major space power, has a growing space program through the Mexican "
            "Space Agency (AEM) and is concerned about the commercialization of space creating a divide "
            "between space-faring and non-space-faring nations. Mexico supports the principle that "
            "outer space is the 'common heritage of mankind' and advocates for equitable access to "
            "orbital slots, space-based resources, and satellite technology.\n\n"
            "Draft the operative section of a resolution organized into three thematic sections: "
            "(I) Governance Framework, (II) Equitable Access, and (III) Environmental Protection of "
            "Outer Space. Each section should have a header and contain three to four operative clauses. "
            "Use proper formatting for thematic sections within a UN resolution, and ensure the clauses "
            "within each section are internally coherent."
        ),
        "hints": (
            "Thematic sections are indicated by Roman numeral headers within the operative section;"
            "Each section should address a distinct sub-topic but connect to the overall theme;"
            "Clauses within each section should progress logically: principle, action, implementation;"
            "The numbering of operative clauses is continuous across sections (1, 2, 3... not restarting);"
            "SPECPOL uses recommendatory language"
        ),
        "sample_answer": (
            "The resolution should have three clearly labeled sections: 'I. Governance Framework' with "
            "clauses that (1) reaffirm the Outer Space Treaty principles, (2) recommend establishment of "
            "a working group to develop binding norms for commercial activities, (3) call for registration "
            "requirements for all commercial space objects; 'II. Equitable Access' with clauses that "
            "(4) urge space-faring nations to share satellite data with developing countries, "
            "(5) encourage technology transfer through COPUOS, (6) recommend equitable allocation of "
            "orbital slots through the ITU; 'III. Environmental Protection' with clauses that "
            "(7) call for binding space debris mitigation guidelines, (8) encourage development of "
            "active debris removal technologies, (9) request the Secretary-General to convene an expert "
            "meeting on space sustainability. Numbering continues across sections."
        ),
        "key_concepts": "thematic sections, resolution organization, continuous numbering, COPUOS framework, space governance, common heritage principle",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Drafting Preambulatory Clauses That Build a Legal Argument on Indigenous Rights",
        "prompt": (
            "You are the delegate of Chile in the Permanent Forum on Indigenous Issues, simulated "
            "within the General Assembly Plenary. The topic is 'Protecting the Land Rights of Indigenous "
            "Peoples in the Context of Extractive Industries.' You must draft six preambulatory clauses "
            "that build a legal and normative argument — each clause should logically lead to the next, "
            "constructing the case for the operative section.\n\n"
            "Chile is home to several indigenous peoples, including the Mapuche, Aymara, and Rapa Nui. "
            "The Mapuche in particular have been involved in long-standing disputes over ancestral lands "
            "that overlap with mining and forestry concessions. Chile has ratified ILO Convention 169 on "
            "Indigenous and Tribal Peoples and has recognized indigenous rights in its 2022 constitutional "
            "reform process, though implementation remains contentious.\n\n"
            "Draft six preambulatory clauses that progressively build an argument from (1) established "
            "international law to (2) specific facts about the current situation to (3) the urgency of "
            "action. Each clause should reference a different source: international treaties, UN "
            "declarations, GA or ECOSOC resolutions, statistical reports, expert body findings, and "
            "regional instruments. The clauses must build upon each other logically."
        ),
        "hints": (
            "Start with the broadest legal basis and narrow to the most specific;"
            "Clause 1: universal rights (UDHR or ICCPR); Clause 2: specific indigenous rights framework "
            "(UNDRIP); Clause 3: a binding convention (ILO 169); Clause 4: a GA resolution; "
            "Clause 5: data or statistics; Clause 6: urgent concern;"
            "Use escalating language: 'Reaffirming,' 'Recalling,' 'Noting,' 'Recognizing,' "
            "'Deeply concerned,' 'Alarmed';"
            "Each clause should connect to the next through thematic progression"
        ),
        "sample_answer": (
            "Six progressive PPs should build from: (1) 'Reaffirming the right of all peoples to "
            "self-determination as enshrined in Article 1 of the ICCPR' — broadest legal basis; "
            "(2) 'Recalling the United Nations Declaration on the Rights of Indigenous Peoples (2007), "
            "in particular Articles 26-30 on land and resource rights' — specific indigenous framework; "
            "(3) 'Noting the obligations of States parties under ILO Convention 169 to consult with "
            "indigenous peoples regarding extractive activities on their territories' — binding treaty; "
            "(4) 'Guided by General Assembly resolution 69/2 on the World Conference on Indigenous "
            "Peoples outcome document' — GA commitment; (5) 'Recognizing that, according to the "
            "International Work Group for Indigenous Affairs, over 370 million indigenous people across "
            "90 countries face ongoing threats to their ancestral lands from extractive industries' — "
            "statistical basis; (6) 'Alarmed by reports of forced displacement, environmental "
            "degradation, and violations of free, prior, and informed consent in the granting of "
            "extractive concessions on indigenous territories' — urgency. This progression builds "
            "an irrefutable case for action."
        ),
        "key_concepts": "progressive argumentation, legal foundations, UNDRIP, ILO Convention 169, FPIC, escalating preambulatory language",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Writing Operative Clauses That Establish an International Body on Peacekeeping",
        "prompt": (
            "You are the delegate of Egypt in the Special Committee on Peacekeeping Operations "
            "(C-34), simulated within SPECPOL. The topic is 'Modernizing UN Peacekeeping Mandates for "
            "Contemporary Conflicts.' Your bloc proposes the creation of a new advisory body to improve "
            "peacekeeping mandate design, and you must draft the operative clauses that establish it.\n\n"
            "Egypt is one of the largest troop-contributing countries (TCCs) to UN peacekeeping "
            "operations and has long advocated for greater consultation between the Security Council "
            "and TCCs when designing mandates. Egypt has experienced firsthand the challenges of mandates "
            "that are overly ambitious, underfunded, or disconnected from ground realities. The "
            "delegation seeks a structured mechanism for TCC input into mandate formulation.\n\n"
            "Draft four operative clauses that establish a 'Peacekeeping Mandate Advisory Panel.' "
            "The clauses should address: (1) the creation of the panel, (2) its composition and "
            "membership, (3) its mandate and functions, and (4) its relationship to existing bodies "
            "(Security Council, C-34, DPO). Each clause should be detailed enough to serve as a "
            "functional blueprint. Include sub-clauses where appropriate."
        ),
        "hints": (
            "Clause 1 should formally establish the body: 'Recommends the establishment of...';"
            "Clause 2 should specify membership: number of members, selection criteria, regional "
            "representation, ex officio members;"
            "Clause 3 should define functions using sub-clauses: advisory role, review mandate drafts, "
            "assess feasibility, consult TCCs;"
            "Clause 4 should clarify the relationship: advisory only, reports to C-34, does not "
            "supersede Security Council authority;"
            "Remember SPECPOL recommends — it cannot create bodies with binding authority"
        ),
        "sample_answer": (
            "Four clauses establishing the Panel: (1) 'Recommends the establishment of a Peacekeeping "
            "Mandate Advisory Panel to enhance consultation between mandate-authorizing bodies and "
            "troop- and police-contributing countries;' (2) 'Further recommends that the Panel comprise "
            "15 members, including: (a) Five representatives of top troop-contributing countries, "
            "(b) Three representatives from the Security Council, (c) Two representatives from the "
            "Secretariat's Department of Peace Operations, (d) Five independent experts in conflict "
            "resolution, with due regard for equitable geographic representation and gender balance;' "
            "(3) 'Recommends that the Panel be mandated to: (a) Review draft peacekeeping mandates "
            "and provide advisory opinions on operational feasibility, (b) Consult with TCCs and PCCs "
            "prior to mandate renewal, (c) Assess the alignment of mandates with available resources, "
            "(d) Submit annual recommendations to the C-34;' (4) 'Affirms that the Panel shall serve "
            "in a strictly advisory capacity and shall not supersede the authority of the Security "
            "Council in matters of international peace and security.' These clauses create a complete "
            "institutional framework."
        ),
        "key_concepts": "establishing international bodies, institutional design, membership composition, mandate definition, advisory vs binding authority, TCC consultation",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "INT",
        "title": "Redrafting a Rejected Clause on Humanitarian Corridors",
        "prompt": (
            "You are the delegate of Vietnam in the Security Council simulation. The topic is "
            "'Establishing Humanitarian Corridors in Active Conflict Zones.' You previously submitted "
            "an operative clause that was rejected by several council members. The original clause read:\n\n"
            "'3. Demands that all parties to armed conflicts immediately cease hostilities and allow "
            "unrestricted humanitarian access throughout the entirety of their territories, with "
            "violations to be referred to the International Criminal Court;'\n\n"
            "The objections were: (a) China objected to the ICC referral language as overstepping the "
            "resolution's scope; (b) Russia objected to 'unrestricted' access as potentially being used "
            "for intelligence gathering; (c) the United States found 'cease hostilities' too broad and "
            "preferred language limited to humanitarian pauses; (d) France supported the clause's intent "
            "but wanted more specificity on corridor mechanisms.\n\n"
            "Redraft the clause to address all four objections while preserving the core humanitarian "
            "purpose. You may expand it into two clauses if needed. Explain your choices and how each "
            "objection is addressed."
        ),
        "hints": (
            "Replace 'cease hostilities' with 'humanitarian pauses' or 'temporary cessations of "
            "hostilities for humanitarian purposes' to address the US concern;"
            "Replace 'unrestricted' with 'safe, unimpeded, and monitored' to address Russia's concern;"
            "Remove the ICC referral and replace with a softer accountability mechanism, such as "
            "requesting the Secretary-General to report on compliance, to address China's concern;"
            "Add specificity on corridor mechanisms: notification procedures, designated routes, "
            "monitoring by OCHA, to address France's concern"
        ),
        "sample_answer": (
            "Redrafted clauses might read: '3. Decides that parties to armed conflicts shall facilitate "
            "temporary humanitarian pauses of no less than 72 hours' duration to allow safe, unimpeded, "
            "and monitored humanitarian access along designated corridors, with the following provisions: "
            "(a) Corridor routes shall be established through negotiation between parties to the conflict "
            "and the United Nations Office for the Coordination of Humanitarian Affairs (OCHA); "
            "(b) Humanitarian organizations operating within corridors shall provide advance notification "
            "to all parties and shall be subject to security screening procedures agreed upon by OCHA; "
            "(c) All parties shall guarantee the safety of humanitarian personnel and convoys operating "
            "within designated corridors; 4. Requests the Secretary-General to report to the Security "
            "Council on a quarterly basis regarding the implementation of and compliance with the "
            "humanitarian corridor provisions established in the present resolution;' — This addresses "
            "all four objections: pauses instead of ceasefire (US), monitored instead of unrestricted "
            "(Russia), reporting instead of ICC referral (China), and specific mechanisms (France)."
        ),
        "key_concepts": "clause redrafting, addressing P5 objections, compromise language, humanitarian corridors, Security Council dynamics, iterative drafting",
    },
    # ── ADVANCED (10) ────────────────────────────────────────────────────────
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Full Draft Resolution on Pandemic Preparedness and Vaccine Equity",
        "prompt": (
            "You are the delegate of Brazil in the World Health Organization (WHO) committee. The "
            "topic is 'Strengthening Global Pandemic Preparedness and Ensuring Equitable Vaccine "
            "Access.' After two days of debate, your bloc has emerged as the leading voice and you "
            "have been asked to draft a complete resolution that can attract majority support. Your "
            "bloc includes Brazil, India, South Africa, Indonesia, and Nigeria. Key opponents include "
            "delegations that prioritize intellectual property protections for pharmaceutical companies.\n\n"
            "The resolution must address five sub-issues: (1) early warning and surveillance systems, "
            "(2) technology transfer and TRIPS flexibilities, (3) manufacturing capacity in developing "
            "nations, (4) equitable distribution mechanisms, and (5) financing pandemic preparedness. "
            "Your bloc's position favors a TRIPS waiver for pandemic-related health technologies, "
            "establishment of regional manufacturing hubs, and a new pandemic preparedness fund. "
            "However, you must include enough compromise language to attract swing votes from delegations "
            "concerned about innovation incentives.\n\n"
            "Draft a complete resolution with: a full header, at least eight preambulatory clauses that "
            "build the legal and factual case, and at least twelve operative clauses organized into "
            "thematic sections addressing all five sub-issues. Include sub-clauses where appropriate. "
            "The resolution should be realistic enough to pass committee with a simple majority."
        ),
        "hints": (
            "Build the preamble from universal health rights to specific pandemic facts to urgency;"
            "Address IP concerns with compromise: 'voluntary licensing where possible, compulsory "
            "licensing in pandemic emergencies' rather than an outright TRIPS waiver;"
            "Include a 'sunset clause' approach — emergency measures that expire when the WHO declares "
            "the pandemic over;"
            "Balance developing-country priorities with incentives for pharmaceutical innovation;"
            "Include a robust implementation and review mechanism"
        ),
        "sample_answer": (
            "A complete resolution should include: Header with WHO committee, topic, sponsors (Brazil, "
            "India, South Africa, Indonesia, Nigeria), and signatories. Preamble (8+ PPs) building from "
            "WHO Constitution preamble, to WHA 73.1, to TRIPS Agreement Article 31bis, to COVID-19 "
            "mortality statistics, to WHO pandemic preparedness reviews. Operative section organized as: "
            "I. Early Warning (OPs 1-2: strengthen IHR compliance, establish genomic surveillance "
            "network); II. Technology Transfer (OPs 3-4: encourage voluntary licensing, authorize "
            "compulsory licensing during declared pandemics with adequate remuneration); III. Manufacturing "
            "(OPs 5-6: establish regional manufacturing hubs in Africa, Asia, Latin America with WHO "
            "technical support); IV. Distribution (OPs 7-9: strengthen allocation frameworks, establish "
            "equitable tiering based on vulnerability, create strategic stockpile); V. Financing "
            "(OPs 10-11: establish Pandemic Preparedness Fund with assessed and voluntary contributions, "
            "target of $10 billion annually); Review (OP 12: biennial review by WHA). The resolution "
            "must demonstrate sophisticated drafting with compromise language on contentious issues."
        ),
        "key_concepts": "full resolution drafting, thematic organization, TRIPS flexibilities, compromise language, pandemic preparedness, multi-bloc consensus",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Crisis Directive on Nuclear Proliferation Emergency",
        "prompt": (
            "You are the delegate of Germany in a Security Council crisis simulation. A crisis update "
            "has been delivered: intelligence reports indicate that a non-state actor operating in a "
            "failed state has acquired fissile material sufficient for a crude nuclear device. The "
            "IAEA has confirmed the material is missing from a poorly secured facility. The Security "
            "Council must act urgently.\n\n"
            "The crisis committee requires a directive — a short, action-oriented document that "
            "authorizes immediate steps. Unlike a standard resolution, a crisis directive is drafted "
            "under extreme time pressure and must balance speed with precision. Germany, as a "
            "non-permanent member, is drafting the directive in consultation with France and the UK.\n\n"
            "The P5 dynamics are as follows: the US and UK want military authorization to secure the "
            "material. France supports a combined military-diplomatic approach. Russia is cautious about "
            "authorizing force without host state consent. China opposes any action that could set a "
            "precedent for intervention.\n\n"
            "Draft a complete crisis directive (at least three preambulatory clauses and eight operative "
            "clauses) that: (1) characterizes the situation as a threat to international peace and "
            "security under Chapter VII, (2) authorizes a range of responses from diplomatic to "
            "military, (3) includes safeguards that address Russian and Chinese concerns, (4) establishes "
            "a timeline for action, and (5) creates a reporting mechanism. The directive must be "
            "drafted with enough precision to be actionable but enough flexibility to secure P5 unanimity."
        ),
        "hints": (
            "Invoke Chapter VII explicitly — this gives the SC binding authority and the legal basis "
            "for enforcement measures;"
            "Structure responses in escalating tiers: diplomatic engagement first, then targeted "
            "sanctions, then authorized use of 'all necessary means' as a last resort;"
            "Address Russia's concern by requiring host state consultation 'where possible' but "
            "authorizing action regardless if an 'imminent threat' exists;"
            "Address China's concern by including language that the directive is 'situation-specific "
            "and does not establish a precedent';"
            "Include strict timelines: 48-hour diplomatic window, 72-hour military authorization"
        ),
        "sample_answer": (
            "A crisis directive should include: Preamble invoking Chapter VII, referencing SC "
            "Resolution 1540 on non-state actors and WMDs, and characterizing the situation as a "
            "threat to international peace and security. Operative section: (1) Demands the non-state "
            "actor immediately surrender the fissile material to the IAEA; (2) Calls upon the host "
            "state to cooperate fully with international efforts; (3) Directs the Secretary-General to "
            "dispatch a special envoy within 24 hours; (4) Decides to impose targeted sanctions on "
            "individuals and entities associated with the acquisition; (5) Authorizes Member States, "
            "acting nationally or through regional arrangements, to take all necessary measures to "
            "secure the material if diplomatic efforts fail within 72 hours, with explicit language "
            "that this authorization is situation-specific and does not establish a precedent for "
            "future interventions; (6) Requires any military operation to coordinate with the IAEA "
            "for material verification and secure chain of custody; (7) Decides to establish a "
            "monitoring mechanism reporting to the Council every 48 hours; (8) Decides to remain "
            "actively seized of the matter. Each clause must balance urgency with the political "
            "constraints of securing P5 unanimity."
        ),
        "key_concepts": "crisis directives, Chapter VII authorization, escalating response tiers, P5 dynamics, non-state actors, nuclear security, precedent limitations",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Complex Multi-Party Resolution on Climate Finance and Loss and Damage",
        "prompt": (
            "You are the delegate of India in ECOFIN. The topic is 'Operationalizing the Loss and "
            "Damage Fund and Scaling Climate Finance for Vulnerable Nations.' This is a highly "
            "contentious topic with at least four distinct blocs holding different positions, and you "
            "must draft a resolution that can secure a two-thirds majority.\n\n"
            "Bloc positions: (1) AOSIS (Small Island Developing States — led by the Philippines): "
            "Demands dedicated, grant-based loss and damage funding separate from adaptation finance, "
            "with automatic disbursement triggers linked to climate thresholds. (2) African Group "
            "(led by Kenya): Wants the Fund to be housed at the UN with direct access modalities, "
            "not filtered through existing institutions like the World Bank. (3) EU bloc (led by "
            "Germany): Willing to contribute but insists on the World Bank as interim trustee, "
            "phased implementation, and contributor-base expansion to include high-emitting developing "
            "countries like China. (4) BASIC group (Brazil, South Africa, India, China): Opposes "
            "expansion of the contributor base to developing countries, insists on historical "
            "responsibility as the basis for contributions, and supports direct access.\n\n"
            "Draft a complete resolution (10+ PPs, 15+ OPs) that navigates these competing interests. "
            "The resolution must include creative compromise formulations on the most contentious "
            "issues: (a) the institutional home of the Fund, (b) the contributor base, (c) the "
            "disbursement mechanism, and (d) the scale of financing. Every compromise must be "
            "explained in the context of which blocs it aims to satisfy."
        ),
        "hints": (
            "On institutional home: propose a 'transitional arrangement' with the World Bank for an "
            "initial period, with a review to consider establishing an independent secretariat — "
            "this satisfies the EU initially while giving the African Group a pathway to independence;"
            "On contributor base: use 'developed country Parties and other Parties in a position to "
            "do so' — this avoids explicitly naming developing countries while opening the door;"
            "On disbursement: create a dual-track system with automatic triggers for extreme events "
            "(AOSIS) and application-based funding for slow-onset events (broader);"
            "On scale: avoid a single number but include a 'floor' and reference the needs assessment"
        ),
        "sample_answer": (
            "The resolution must demonstrate sophisticated multi-party negotiation skills. Key compromise "
            "formulations: (a) Institutional home: 'Decides that the Fund shall be serviced by the World "
            "Bank as interim trustee for an initial period of four years, after which the COP shall "
            "review the hosting arrangement with a view to establishing an independent secretariat' — "
            "satisfies EU (World Bank) and African Group (independence pathway); (b) Contributor base: "
            "'Urges developed country Parties, and invites other Parties and non-state actors in a "
            "position to do so, to contribute' — technically voluntary for developing countries "
            "(BASIC), but opens the door (EU); (c) Disbursement: dual-track with 'rapid response "
            "window' triggered by WMO-certified extreme weather events (AOSIS) and 'programmatic "
            "window' for slow-onset loss and damage (broader); (d) Scale: 'Acknowledges that the "
            "Fund's resources should reflect the scale of loss and damage needs as assessed by the "
            "Warsaw International Mechanism, with an initial target of no less than $100 billion "
            "annually by 2030.' The full resolution must weave these compromises into a coherent "
            "15+ operative clause document."
        ),
        "key_concepts": "multi-party negotiation, loss and damage, creative compromise, institutional design, contributor base diplomacy, dual-track mechanisms",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Amendment Strategy for a Contentious AI Governance Resolution",
        "prompt": (
            "You are the delegate of Japan in the General Assembly Plenary. The topic is 'International "
            "Governance of Artificial Intelligence.' A draft resolution has been submitted by a Western-"
            "led bloc that your delegation finds problematic in several respects. Rather than submitting "
            "a competing resolution, Japan's strategy is to reshape the existing draft through a "
            "carefully sequenced series of amendments.\n\n"
            "The draft resolution contains 10 operative clauses. Japan's specific concerns are:\n"
            "- OP 3 calls for a binding international AI treaty — Japan prefers non-binding norms\n"
            "- OP 5 proposes an International AI Agency with regulatory authority — Japan prefers an "
            "advisory body housed within UNESCO\n"
            "- OP 7 requires mandatory AI impact assessments for all AI systems — Japan wants to limit "
            "this to 'high-risk AI systems' only\n"
            "- OP 9 does not mention the role of the private sector — Japan wants to add multi-"
            "stakeholder participation\n\n"
            "Draft four amendments (one for each clause), and for each amendment explain: (1) whether "
            "it should be submitted as friendly or unfriendly, (2) the strategic order in which they "
            "should be introduced, (3) how each amendment affects the chances of the others passing, "
            "and (4) potential counter-amendments that opponents might propose. Present a complete "
            "amendment strategy document."
        ),
        "hints": (
            "Consider strategic sequencing: which amendment, if passed first, makes others easier to pass;"
            "The OP 7 amendment (narrowing scope to high-risk AI) is probably the easiest to pass — "
            "start there to build momentum;"
            "The OP 3 amendment (binding to non-binding) is the most contentious — save it for last "
            "or pair it with a concession;"
            "For each amendment, identify likely voting coalitions and potential swing votes;"
            "Consider which amendments might be offered as friendly amendments (requiring sponsor "
            "consent) versus unfriendly (requiring committee vote)"
        ),
        "sample_answer": (
            "A complete amendment strategy should present: Strategic Order: (1) First, amend OP 9 to "
            "add multi-stakeholder language — this is the least controversial and can be offered as a "
            "friendly amendment, building goodwill. (2) Second, amend OP 7 to narrow from 'all AI "
            "systems' to 'high-risk AI systems as defined by national authorities' — this has broad "
            "support from industry-friendly delegations and can pass on a vote. (3) Third, amend OP 5 "
            "to change from a regulatory authority to an 'advisory body established within UNESCO to "
            "provide technical guidance' — this reduces the institutional threat and may attract "
            "developing countries concerned about regulatory costs. (4) Finally, amend OP 3 to change "
            "from a 'binding treaty' to a 'set of internationally agreed voluntary norms and principles "
            "that may serve as the basis for future legally binding instruments' — this preserves the "
            "aspiration while removing the immediate binding commitment. Counter-amendment analysis for "
            "each should identify which delegations might oppose and what alternative formulations they "
            "might propose. The strategy document should also include fallback positions if key "
            "amendments fail."
        ),
        "key_concepts": "amendment strategy, strategic sequencing, friendly vs unfriendly amendments, voting coalition analysis, counter-amendments, AI governance",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Drafting a Security Council Resolution on Humanitarian Corridors in Active Conflict",
        "prompt": (
            "You are the delegate of Turkey in a Security Council simulation. The topic is "
            "'Establishing and Protecting Humanitarian Corridors in the Context of Urban Warfare.' "
            "The crisis situation involves a besieged city with 400,000 civilians trapped, where "
            "government forces and armed opposition groups are engaged in intense urban combat. "
            "Humanitarian agencies have been unable to deliver food, water, and medical supplies for "
            "three weeks.\n\n"
            "You are drafting a resolution that Turkey has been championing as a neutral mediator. "
            "The P5 dynamics are complex: the US and France support strong humanitarian access "
            "provisions; the UK supports the resolution but wants clear rules of engagement for "
            "corridor protection forces; Russia has ties to the government forces and will veto any "
            "resolution that appears to favor the opposition; China opposes any language that could "
            "be interpreted as regime change or precedent for intervention.\n\n"
            "Draft a complete Security Council resolution (at least six preambulatory clauses and "
            "twelve operative clauses) that: (1) establishes humanitarian corridors under Chapter VII, "
            "(2) creates a monitoring mechanism, (3) authorizes a protection force with clearly limited "
            "rules of engagement, (4) imposes consequences for violations, and (5) includes enough "
            "safeguards to avoid a Russian or Chinese veto. The resolution must be operationally "
            "detailed — specify corridor routes, timing, force composition, reporting requirements, "
            "and sunset provisions."
        ),
        "hints": (
            "Frame the resolution around humanitarian access, NOT the broader conflict — this avoids "
            "regime change concerns (China) and reduces perception of taking sides (Russia);"
            "Include language requiring ALL parties (government and opposition) to comply equally — "
            "this addresses Russia's concern about bias;"
            "Protection force should be limited to corridor defense, NOT offensive operations — "
            "specify 'defensive rules of engagement limited to protection of humanitarian convoys "
            "and personnel';"
            "Include a sunset clause: authorization expires in 90-180 days and must be actively "
            "renewed by the Council;"
            "Consequences should be graduated: reporting, then sanctions, then review — avoid "
            "automatic military escalation"
        ),
        "sample_answer": (
            "The resolution should demonstrate mastery of Security Council drafting. Preamble: invoke "
            "Chapter VII, reference IHL and Geneva Conventions, cite OCHA reports on humanitarian "
            "situation, demand access under UNSC Resolution 2417 (starvation as a method of warfare). "
            "Operative section: (1-2) Demand all parties — explicitly naming 'government forces, armed "
            "opposition groups, and any associated militias' — to allow humanitarian access; (3-4) "
            "Establish specific corridors with operational details: 'three designated corridors from "
            "[compass directions] operating for minimum 12-hour windows daily'; (5-6) Authorize a "
            "UN Protection Force of up to 5,000 troops under defensive rules of engagement 'limited "
            "to the protection of humanitarian convoys, distribution points, and medical facilities "
            "within designated corridor zones'; (7) Establish OCHA as corridor coordinator with "
            "authority to negotiate daily operational details; (8-9) Create a monitoring mechanism "
            "reporting to the Council weekly, with violations documented by name; (10) Impose targeted "
            "sanctions framework for individuals found to obstruct humanitarian access; (11) Set a "
            "180-day authorization period requiring Council renewal; (12) Remain seized of the matter. "
            "Every clause must balance operational effectiveness with P5 political constraints."
        ),
        "key_concepts": "Security Council resolution drafting, Chapter VII, humanitarian corridors, rules of engagement, P5 veto dynamics, sunset clauses, operational detail",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Drafting a Comprehensive Resolution with Financial Mechanisms on Ocean Pollution",
        "prompt": (
            "You are the delegate of Indonesia in the United Nations Environment Assembly (UNEA), "
            "simulated within UNEP. The topic is 'Ending Plastic Pollution: Towards an International "
            "Legally Binding Instrument.' You are the lead drafter of what is intended to be the "
            "foundational resolution calling for negotiations on a binding global plastics treaty.\n\n"
            "The negotiation landscape includes: (1) The High Ambition Coalition (EU, small island "
            "states, African Group) wants a binding treaty with production caps, mandatory EPR schemes, "
            "and a dedicated financial mechanism. (2) The Like-Minded Group (Saudi Arabia, US, Russia, "
            "China, India) opposes production caps and prefers a focus on downstream waste management "
            "and voluntary national action plans. (3) The Plastics Industry Alliance (not a formal UN "
            "group but influential through several delegations) wants to emphasize chemical recycling "
            "and innovation over regulatory approaches.\n\n"
            "Indonesia, as a major ocean-bordering nation severely affected by marine plastic pollution "
            "and also a developing nation with significant plastics industry employment, must draft a "
            "resolution (8+ PPs, 14+ OPs) that: (1) establishes an Intergovernmental Negotiating "
            "Committee (INC) with a mandate and timeline, (2) outlines the scope of the future treaty, "
            "(3) creates an interim financial mechanism, (4) addresses both upstream (production) and "
            "downstream (waste management) approaches without alienating either camp, and (5) includes "
            "a just transition framework for developing nations. The resolution must be realistic enough "
            "to achieve consensus in UNEA."
        ),
        "hints": (
            "Use constructive ambiguity on production caps: 'address the full lifecycle of plastics, "
            "including sustainable production and consumption patterns' — this implies production "
            "without saying 'caps';"
            "Frame the INC mandate broadly: 'develop an international legally binding instrument on "
            "plastic pollution, including in the marine environment' — this allows scope discussions "
            "during negotiations rather than resolving them now;"
            "Financial mechanism should be interim and voluntary initially, with a pathway to assessed "
            "contributions under the future treaty;"
            "Include just transition provisions: capacity-building, technology transfer, longer "
            "implementation timelines for developing nations;"
            "Reference UNEA Resolution 5/14 as the foundation"
        ),
        "sample_answer": (
            "The resolution should establish: Preamble referencing UNEA Res. 5/14, UNCLOS, CBD, "
            "scientific evidence on microplastics, and the disproportionate impact on developing coastal "
            "states. Operative section: I. Negotiating Process (OPs 1-4): Establish INC with mandate to "
            "'develop an international legally binding instrument on plastic pollution, including in the "
            "marine environment, which could include both binding and voluntary approaches, addressing "
            "the full lifecycle of plastics'; set timeline of five sessions over two years; request UNEP "
            "to serve as secretariat; ensure inclusive participation. II. Scope (OPs 5-7): Define scope "
            "to include 'sustainable production and consumption, product design, waste management, and "
            "remediation of existing pollution' — covers both upstream and downstream; include provisions "
            "for national action plans 'that reflect national circumstances'; address microplastics, "
            "single-use plastics, and legacy pollution. III. Financial Mechanism (OPs 8-10): Establish "
            "interim voluntary trust fund; invite contributions from all sources; request feasibility "
            "study on long-term financial mechanism under the treaty. IV. Just Transition (OPs 11-12): "
            "Capacity-building and technology transfer for developing nations; 'differentiated timelines "
            "reflecting national economic circumstances.' V. Review (OPs 13-14): Annual progress reports; "
            "midterm review of INC process. This resolution demonstrates advanced drafting by navigating "
            "highly contentious terrain with creative formulations."
        ),
        "key_concepts": "INC establishment, constructive ambiguity, lifecycle approach, financial mechanisms, just transition, consensus drafting, UNEA process",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Drafting Competing Resolutions and Merger Negotiations on Food Security",
        "prompt": (
            "You are the delegate of Argentina in the FAO committee. The topic is 'Ensuring Global "
            "Food Security Amid Climate Change and Conflict.' Two competing draft resolutions have "
            "been submitted, and the chair has asked your delegation to mediate a merger. You must "
            "produce the merged text.\n\n"
            "Draft Resolution A (Western/developed — sponsors: Germany, Japan, US): 15 operative "
            "clauses focusing on market-based solutions, agricultural trade liberalization, reduction "
            "of trade-distorting subsidies, intellectual property protection for seed technologies, "
            "private sector investment in agricultural R&D, and digital agriculture. Contains a clause "
            "calling for the elimination of export restrictions during food crises.\n\n"
            "Draft Resolution B (G77/developing — sponsors: Nigeria, Bangladesh, Ethiopia): 15 operative "
            "clauses focusing on food sovereignty, right to food as a human right, protection of "
            "smallholder farmers, seed-saving rights, climate adaptation funding, agroecology, "
            "strategic food reserves, and special safeguard mechanisms to protect developing country "
            "agriculture. Contains a clause calling for permanent exemptions from WTO agricultural "
            "liberalization commitments.\n\n"
            "Both resolutions have enough support to pass individually, but the chair strongly prefers "
            "a single merged text. Draft the merged resolution (10+ PPs, 18+ OPs) that combines the "
            "strongest elements of both while resolving contradictions. For each contentious point, "
            "explain your compromise formulation. The merged text must be acceptable to at least 80 "
            "percent of the sponsors from both original resolutions."
        ),
        "hints": (
            "Identify areas of genuine overlap: both want food security, both support R&D, both want "
            "climate adaptation;"
            "On trade: 'Encourages the progressive liberalization of agricultural trade while "
            "recognizing the right of developing countries to maintain special safeguard mechanisms "
            "during transitional periods' — combines both positions;"
            "On seeds: 'Supports both intellectual property protections for new seed technologies and "
            "the right of smallholder farmers to save, exchange, and sell farm-saved seeds' — parallel "
            "recognition;"
            "On export restrictions: 'Calls upon Member States to refrain from imposing export "
            "restrictions that exacerbate food crises, while recognizing the sovereign right of states "
            "to ensure domestic food security' — qualified both ways;"
            "Structure the merged text with thematic sections to give each bloc visible wins"
        ),
        "sample_answer": (
            "The merged resolution must demonstrate mastery of diplomatic compromise. Key merged "
            "formulations: (1) Trade: 'Encourages the progressive reduction of trade-distorting "
            "agricultural subsidies while affirming the right of developing countries to implement "
            "special safeguard mechanisms and public stockholding programs for food security purposes, "
            "in accordance with WTO rules;' (2) Seeds: 'Recognizes the importance of both plant variety "
            "protection systems that incentivize agricultural innovation and the rights of smallholder "
            "farmers, in accordance with the International Treaty on Plant Genetic Resources for Food "
            "and Agriculture, to save, use, exchange, and sell farm-saved seeds;' (3) Export restrictions: "
            "'Calls upon Member States to exercise restraint in imposing export restrictions on "
            "foodstuffs, and to notify the FAO and WTO before implementing any such measures, while "
            "acknowledging the sovereign right of states to take temporary measures to ensure domestic "
            "food supply;' (4) Investment: 'Encourages increased public and private investment in "
            "agricultural research, with particular emphasis on climate-resilient crop varieties, "
            "agroecological practices, and digital agriculture solutions appropriate to smallholder "
            "farming systems;' (5) Right to food: included in the preamble as a PP referencing the "
            "ICESCR, which developed nations can accept as aspirational context rather than operative "
            "obligation. The full 18+ OP resolution should be organized into sections: Trade and "
            "Markets, Production and Technology, Climate Adaptation, Emergency Response, and "
            "Implementation. Each section should contain visible wins for both blocs."
        ),
        "key_concepts": "resolution merger, compromise formulation, trade vs sovereignty, food security frameworks, WTO agriculture, parallel recognition, mediator drafting",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Drafting a Resolution Under Pressure with Hostile Amendments on Cyber Warfare",
        "prompt": (
            "You are the delegate of South Africa in DISEC. The topic is 'Developing International "
            "Norms for State Conduct in Cyberspace.' You have successfully introduced a draft resolution "
            "with 12 operative clauses. However, during the amendment phase, three hostile amendments "
            "have been introduced that threaten to fundamentally alter your resolution. You must draft "
            "counter-amendments or defensive revisions.\n\n"
            "Your original OP 4: 'Recommends that Member States refrain from conducting offensive "
            "cyber operations against critical civilian infrastructure, including healthcare systems, "
            "water treatment facilities, and electoral infrastructure;'\n\n"
            "Hostile Amendment 1 (by Russia): Add to OP 4: 'and further recommends that Member States "
            "refrain from developing, stockpiling, or deploying cyber weapons in any form;' — This "
            "would effectively ban all offensive cyber capabilities, which many delegations oppose.\n\n"
            "Hostile Amendment 2 (by US): Replace OP 8 (which calls for a binding cyber treaty) with: "
            "'Encourages Member States to continue participating in voluntary confidence-building "
            "measures through the UN Group of Governmental Experts;' — This guts the treaty aspiration.\n\n"
            "Hostile Amendment 3 (by China): Delete OP 10 (which calls for independent attribution "
            "mechanisms for cyber attacks) entirely, replacing it with: 'Affirms the sovereign right "
            "of each State to manage its own cybersecurity affairs without external interference;' — "
            "This eliminates accountability.\n\n"
            "For each hostile amendment, draft either: (a) a counter-amendment that addresses the "
            "legitimate concern behind the hostile amendment while preserving your resolution's core "
            "objectives, or (b) revised language for your original clause that preemptively incorporates "
            "enough of the hostile amendment to make it unnecessary. Explain your strategic rationale "
            "for each choice."
        ),
        "hints": (
            "For Amendment 1: the legitimate concern is restraint in cyber warfare. Counter by adding "
            "language about 'proportionality and necessity in accordance with international humanitarian "
            "law' without banning all capabilities;"
            "For Amendment 2: the concern is that a binding treaty is premature. Find middle ground: "
            "'Requests the Secretary-General to convene an open-ended working group to explore the "
            "development of a normative framework, which may include legally binding elements';"
            "For Amendment 3: the concern is external interference in sovereignty. Propose an attribution "
            "mechanism that is 'voluntary, transparent, and state-consented' rather than independent;"
            "Consider which amendments you might accept in modified form to build goodwill for "
            "defeating the most dangerous one"
        ),
        "sample_answer": (
            "Strategic response to each amendment: (1) Against Russia's amendment: Accept the spirit "
            "but narrow the scope — counter-amend to: 'Recommends that Member States refrain from "
            "conducting offensive cyber operations against critical civilian infrastructure, and further "
            "encourages all States to exercise restraint in the development and deployment of cyber "
            "capabilities in accordance with the principles of necessity, proportionality, and "
            "distinction under international humanitarian law;' — This acknowledges restraint without "
            "banning all capabilities. Strategy: offer this as a compromise to Russia before the vote. "
            "(2) Against US amendment: Revise OP 8 preemptively to: 'Requests the Secretary-General to "
            "convene an open-ended working group to develop a comprehensive normative framework for "
            "responsible State behavior in cyberspace, including consideration of the appropriate legal "
            "character of such norms, building upon the work of the GGE and the Open-Ended Working "
            "Group;' — This preserves the pathway to binding norms without explicitly saying 'treaty.' "
            "Strategy: accept US language about GGE while keeping the door open. (3) Against China's "
            "amendment: This is the most dangerous — fight it directly. Revise OP 10 to: 'Encourages "
            "the development of voluntary, transparent, and technically rigorous mechanisms for the "
            "attribution of cyber operations, with full respect for State sovereignty and with the "
            "consent of affected States before any public attribution;' — This adds sovereignty "
            "protections and consent requirements while preserving some attribution capacity. Overall "
            "strategy: accept modified versions of Amendments 1 and 2 (showing flexibility) to build "
            "coalition support for defeating Amendment 3, which is the existential threat to the "
            "resolution's purpose."
        ),
        "key_concepts": "counter-amendment drafting, defensive strategy, hostile amendments, cyber norms, IHL in cyberspace, strategic concessions, coalition management",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Full Resolution with Annexes on Women's Empowerment and Economic Participation",
        "prompt": (
            "You are the delegate of Mexico in the Commission on the Status of Women (CSW), simulated "
            "within SOCHUM. The topic is 'Advancing Women's Full and Equal Participation in the "
            "Economy.' Your bloc has asked you to draft a comprehensive resolution that includes not "
            "only the standard PP/OP format but also an annex — a supplementary document attached to "
            "the resolution that provides detailed implementation guidelines.\n\n"
            "Mexico has been a leader on gender equality in Latin America, having adopted constitutional "
            "reforms on gender parity, implemented the National Program for Equality between Women and "
            "Men (PROIGUALDAD), and established gender budgeting requirements. Mexico's position "
            "emphasizes the intersection of gender equality with economic development, indigenous "
            "women's rights, and the care economy.\n\n"
            "Draft a complete resolution (8+ PPs, 12+ OPs) with an appended annex titled 'Guidelines "
            "for National Action Plans on Women's Economic Empowerment.' The resolution's operative "
            "clauses should reference the annex where appropriate (e.g., 'in accordance with the "
            "guidelines annexed to the present resolution'). The annex should contain at least eight "
            "numbered guideline points organized into three sections: (I) Legal and Policy Framework, "
            "(II) Economic Measures, and (III) Monitoring and Accountability. The annex must be "
            "substantive enough to serve as a genuine implementation guide."
        ),
        "hints": (
            "The resolution and annex should be complementary: the resolution sets the mandate, the "
            "annex provides implementation detail;"
            "Reference the annex in at least two operative clauses: one that 'adopts' or 'endorses' "
            "the guidelines, and one that 'invites Member States to implement' them;"
            "The annex should use guideline language: 'States should,' 'It is recommended that,' "
            "'Best practices include';"
            "Cover the care economy (unpaid domestic work), gender pay gap, access to credit, "
            "women's entrepreneurship, workplace protections, and data collection;"
            "Include indigenous women and intersectional perspectives to reflect Mexico's priorities"
        ),
        "sample_answer": (
            "The resolution should include: Preamble referencing CEDAW, Beijing Platform for Action, "
            "SDG 5, CSW agreed conclusions, ILO Convention 190, and data on the gender pay gap and "
            "women's labor force participation. Operative section: (1) Reaffirm commitment to women's "
            "economic empowerment; (2) Endorse the guidelines in the annex; (3-5) Address legal reforms "
            "including equal pay legislation, anti-discrimination laws, and parental leave; (6-7) Call "
            "for gender-responsive budgeting and access to financial services; (8-9) Address the care "
            "economy through investment in care infrastructure and recognition of unpaid work in national "
            "accounts; (10) Invite Member States to develop national action plans in accordance with "
            "the annexed guidelines; (11-12) Request reporting and review mechanisms. The Annex should "
            "contain: Section I (Legal) — guidelines on legislative audits, equal pay laws, property "
            "rights, anti-harassment frameworks; Section II (Economic) — guidelines on gender-lens "
            "investing, women's entrepreneurship programs, digital financial inclusion, care "
            "infrastructure investment, agricultural support for rural women; Section III (Monitoring) — "
            "guidelines on gender-disaggregated data collection, national review mechanisms, "
            "international reporting, and civil society participation. The annex should total at "
            "least eight substantive guideline points."
        ),
        "key_concepts": "resolution with annexes, implementation guidelines, referencing supplementary documents, CSW framework, care economy, gender-responsive budgeting, intersectionality",
    },
    {
        "category_type": "DRAFT",
        "difficulty": "ADV",
        "title": "Drafting a Resolution Package on Digital Privacy with Companion Decision",
        "prompt": (
            "You are the delegate of the Philippines in the UNHRC. The topic is 'Protecting the Right "
            "to Privacy in the Digital Age.' Your bloc wants to submit not just a resolution but a "
            "resolution package: a main resolution plus a companion procedural decision that establishes "
            "a new Special Rapporteur mandate. This is an advanced drafting technique where the "
            "substantive resolution and the procedural decision work together.\n\n"
            "The Philippines has experienced significant tensions between digital privacy and national "
            "security, particularly in the context of anti-terrorism legislation and social media "
            "regulation. The delegation supports strong privacy protections balanced with legitimate "
            "law enforcement needs, and champions the rights of digital workers in the gig economy "
            "whose data is extensively harvested by platform companies.\n\n"
            "Draft both documents: (1) A main resolution (8+ PPs, 10+ OPs) on the right to privacy "
            "in the digital age, addressing government surveillance, corporate data collection, cross-"
            "border data flows, and the rights of gig economy workers. (2) A companion decision (3 PPs, "
            "5 OPs) that establishes a 'Special Rapporteur on Digital Privacy and Data Protection' with "
            "a defined mandate, appointment process, reporting requirements, and three-year term. The "
            "main resolution should reference the companion decision, and vice versa. Explain the "
            "strategic advantage of using a resolution package rather than a single document."
        ),
        "hints": (
            "The strategic advantage of a package: the resolution can focus on substantive standards "
            "while the decision handles the institutional mandate — this makes each document cleaner "
            "and allows delegations to support the substance even if they have reservations about "
            "the new mandate (they can vote separately);"
            "The main resolution should reference the decision: 'Welcomes the decision of the Human "
            "Rights Council to appoint a Special Rapporteur on Digital Privacy and Data Protection';"
            "The decision should reference the resolution: 'Pursuant to resolution [X] on the right "
            "to privacy in the digital age';"
            "The Special Rapporteur mandate should be specific: investigate, report, make recommendations, "
            "conduct country visits, receive communications;"
            "Include gig economy worker data rights as a distinctive contribution"
        ),
        "sample_answer": (
            "The resolution package demonstrates advanced institutional drafting. Main Resolution: "
            "Preamble referencing UDHR Art. 12, ICCPR Art. 17, GA Res. 68/167, Guiding Principles on "
            "Business and Human Rights, and data on surveillance and data breaches. Operative section: "
            "(1-2) Reaffirm privacy rights online and call for legislative reforms; (3-4) Address "
            "government surveillance: necessity, proportionality, independent oversight; (5-6) Address "
            "corporate data collection: consent frameworks, data minimization, right to erasure; "
            "(7) Address cross-border data flows: mutual legal assistance, adequacy frameworks; "
            "(8) Address gig economy workers: right to access personal data held by platforms, limits "
            "on algorithmic profiling, portability; (9) Welcome the establishment of the Special "
            "Rapporteur under the companion decision; (10) Request annual reporting. Companion Decision: "
            "PPs referencing the main resolution and existing privacy mandates. OPs: (1) Decide to "
            "appoint a Special Rapporteur on Digital Privacy and Data Protection for three years; "
            "(2) Define mandate: investigate privacy violations, conduct country visits with state "
            "consent, receive individual communications, engage with private sector entities, report "
            "annually to the HRC and GA; (3) Request cooperation of all stakeholders; (4) Request "
            "OHCHR to provide resources; (5) Decide to review the mandate at the appropriate session. "
            "Strategic advantage: separate voting allows broader support for each document."
        ),
        "key_concepts": "resolution packages, companion decisions, Special Rapporteur mandates, UNHRC procedures, institutional design, strategic document architecture, gig economy data rights",
    },
]

# ── NEGOTIATION QUESTIONS ─────────────────────────────────────────────────────
QUESTIONS += [
    # ── BEG (1/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Finding Allies in an Unmoderated Caucus on Climate Financing",
        "prompt": (
            "You are the delegate of Indonesia in the UNFCCC Standing Committee on Finance. "
            "An unmoderated caucus has just begun on the topic of climate financing mechanisms "
            "for small island developing states (SIDS). You have limited experience in MUN and "
            "need to find allies who share your position that developed nations should contribute "
            "a larger share to the Green Climate Fund.\n\n"
            "Several blocs are already forming around the room. The G-77 delegates are clustered "
            "near the front, while the EU bloc is conferring by the windows. A few unaligned "
            "delegates from Southeast Asia and the Pacific Islands are standing near the middle "
            "of the room looking uncertain about whom to approach.\n\n"
            "Describe your strategy for the first five minutes of this unmoderated caucus. Who "
            "do you approach first, what talking points do you open with, and how do you begin "
            "building a coalition without alienating potential partners from other blocs?"
        ),
        "hints": (
            "Think about natural allies based on geography and shared vulnerability to climate "
            "change. Consider approaching the unaligned Southeast Asian and Pacific Island "
            "delegates first since they may share your interests. Prepare two or three concise "
            "talking points about climate financing equity before approaching anyone."
        ),
        "sample_answer": (
            "Begin by approaching the unaligned Southeast Asian and Pacific Island delegates "
            "standing in the middle of the room, as they share geographic and economic "
            "vulnerability to climate change impacts. Open with a brief, friendly introduction "
            "and immediately establish common ground: 'As fellow nations facing rising sea "
            "levels and extreme weather, we share an interest in ensuring the Green Climate "
            "Fund receives adequate contributions from historically high-emitting nations.' "
            "Propose a simple shared principle -- that financing should be proportional to "
            "historical emissions -- and ask for their input to make them feel ownership of "
            "the emerging position. After securing tentative agreement from two or three "
            "delegates, approach the G-77 cluster as a small group rather than alone, which "
            "signals that momentum is already building. Avoid directly criticizing the EU "
            "position at this stage; instead, frame your coalition's stance as constructive "
            "and evidence-based. The goal in the first five minutes is to listen more than "
            "you speak, identify which delegates are most engaged, and establish yourself as "
            "a collaborative rather than confrontational partner."
        ),
        "key_concepts": "ally identification, unmoderated caucus strategy, coalition building basics, climate financing, G-77, SIDS vulnerability, Green Climate Fund",
    },
    # ── BEG (2/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Listening Strategies During Bloc Formation on Refugee Burden-Sharing",
        "prompt": (
            "You are the delegate of Brazil in the Third Committee of the UN General Assembly "
            "(SOCHUM). The topic under discussion is equitable burden-sharing for refugee "
            "resettlement, and you have been assigned to a working group tasked with drafting "
            "operative clauses on financial support for host nations.\n\n"
            "Your working group includes delegates from Turkey, Kenya, Germany, Japan, and "
            "Colombia. Several of these delegates have strong opinions and are speaking over "
            "one another. Turkey and Kenya, as major refugee-hosting nations, are pushing for "
            "binding financial commitments, while Germany and Japan are cautious about any "
            "language that implies mandatory contributions.\n\n"
            "As a newer delegate who wants to build trust and find compromise, describe the "
            "listening techniques you would use in this working group. How do you ensure every "
            "voice is heard, and how do you use active listening to identify areas of overlap "
            "that could form the basis of consensus language?"
        ),
        "hints": (
            "Active listening means paraphrasing what others say before responding. Try "
            "summarizing each delegate's core concern back to them to show understanding. "
            "Look for shared language -- words like 'voluntary,' 'capacity-based,' or "
            "'solidarity' that multiple delegates use -- as potential bridges."
        ),
        "sample_answer": (
            "First, position yourself as a neutral facilitator rather than an advocate for a "
            "fixed position. When Turkey speaks about the financial strain of hosting millions "
            "of refugees, paraphrase: 'If I understand correctly, Turkey is emphasizing that "
            "host nations bear disproportionate costs and need predictable financial support.' "
            "This validates their point and slows the conversation to a productive pace. When "
            "Germany expresses concern about binding commitments, summarize: 'Germany wants to "
            "ensure that any financial mechanism respects national budget sovereignty.' Take "
            "notes on a shared document visible to the group, organizing points into 'areas of "
            "agreement' and 'areas needing further discussion.' Notice that both sides may "
            "accept language around 'capacity-based contributions' -- Turkey wants contributions "
            "to be substantial, and Germany wants them to be voluntary, but both accept the idea "
            "of capacity as a metric. Ask clarifying questions rather than making statements: "
            "'Kenya, when you say predictable funding, are you referring to multi-year pledges "
            "or annual assessments?' This draws out specifics that enable compromise. By the end "
            "of the session, you should be able to propose a bridging phrase such as 'encourages "
            "Member States to make capacity-based, multi-year voluntary contributions' that "
            "incorporates language from multiple delegates."
        ),
        "key_concepts": "active listening, paraphrasing, working group dynamics, refugee burden-sharing, consensus building, facilitation, compromise language",
    },
    # ── BEG (3/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Simple Compromise on Arms Trade Treaty Provisions",
        "prompt": (
            "You are the delegate of Nigeria in the First Committee of the UN General Assembly "
            "(DISEC). The committee is debating strengthening the Arms Trade Treaty (ATT), and "
            "two opposing positions have emerged in your working group.\n\n"
            "Bloc A (led by the EU delegates) wants mandatory end-user certificates for all "
            "conventional arms transfers, with an international verification body. Bloc B (led "
            "by several African and Middle Eastern delegates) argues that mandatory verification "
            "would be costly, impractical for developing nations, and could be used as a "
            "pretext to restrict legitimate self-defense acquisitions.\n\n"
            "Nigeria has interests in both directions: you want to reduce illicit arms flows "
            "that fuel conflict in the Sahel, but you also want affordable access to defense "
            "equipment. Propose a simple compromise that addresses core concerns from both blocs."
        ),
        "hints": (
            "Look for a middle ground between mandatory and voluntary. Consider tiered "
            "approaches where obligations differ based on the value or type of arms transfer. "
            "Think about capacity-building provisions that address developing nations' "
            "implementation concerns."
        ),
        "sample_answer": (
            "Propose a tiered verification system that distinguishes between major conventional "
            "weapons systems (tanks, aircraft, warships) and small arms/light weapons. For "
            "major systems, accept mandatory end-user certificates as these transactions are "
            "fewer in number and already involve significant documentation. For small arms "
            "transfers, implement a voluntary certification program with incentives: nations "
            "that participate receive technical assistance and capacity-building support from "
            "the ATT Secretariat, funded by assessed contributions from major arms-exporting "
            "states. Include a five-year review mechanism to evaluate whether the voluntary "
            "tier should transition to mandatory once capacity has been built. This addresses "
            "Bloc A's desire for accountability by covering the most dangerous weapons "
            "categories immediately, while addressing Bloc B's concerns about cost and "
            "sovereignty by making small arms verification voluntary and supported. Nigeria "
            "benefits from both: reduced illicit flows of major weapons into the Sahel "
            "region and continued affordable access to small arms for legitimate security "
            "needs during the capacity-building period."
        ),
        "key_concepts": "compromise crafting, Arms Trade Treaty, tiered obligations, end-user certificates, capacity building, DISEC procedures, illicit arms flows",
    },
    # ── BEG (4/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Introduction to Caucus Dynamics in Pandemic Equity Debates",
        "prompt": (
            "You are the delegate of the Philippines in the World Health Assembly (WHA). The "
            "committee is discussing equitable access to pandemic preparedness resources, "
            "including vaccine distribution, medical supply chains, and technology transfer. "
            "The chair has called for a 15-minute unmoderated caucus.\n\n"
            "You notice three groups forming: (1) a large bloc of developing nations discussing "
            "compulsory licensing of vaccine patents, (2) a smaller group of pharmaceutical-"
            "producing nations defending intellectual property protections, and (3) a handful of "
            "middle-income countries like yours who are unsure which group to join.\n\n"
            "Explain the basic dynamics of this caucus situation. What are the advantages and "
            "risks of joining each group, and how should you decide where to position yourself "
            "as a delegate of the Philippines?"
        ),
        "hints": (
            "Consider the Philippines' actual interests: it is a developing nation that imports "
            "most vaccines but also has a growing pharmaceutical manufacturing sector. Think "
            "about which group's goals align most with your national interests and where you "
            "can have the most influence."
        ),
        "sample_answer": (
            "The three-group dynamic represents a classic MUN caucus pattern: two opposing poles "
            "and an undecided middle. Joining the large developing-nation bloc (Group 1) offers "
            "safety in numbers and alignment with the Philippines' immediate need for affordable "
            "vaccine access, but risks being one voice among many with little individual "
            "influence. Joining the pharmaceutical-producing bloc (Group 2) would be "
            "strategically unusual for the Philippines, but could position you as a bridge if "
            "you later carry their concerns back to the developing bloc. The middle-income "
            "group (Group 3) is where the Philippines can have the most influence: these "
            "undecided delegates will likely determine which bloc's draft resolution gains "
            "majority support. The best strategy is to spend the first five minutes with "
            "Group 3, establishing yourself as an informal coordinator of the middle-income "
            "caucus. Identify shared interests -- perhaps voluntary licensing with "
            "capacity-building support, rather than compulsory licensing. Then approach Group 1 "
            "with a modified position that could attract broader support: 'We support equitable "
            "access but propose voluntary licensing with incentive structures rather than "
            "compulsory measures, which will attract more co-sponsors.' This positions the "
            "Philippines as a pragmatic bridge-builder rather than a follower."
        ),
        "key_concepts": "caucus dynamics, bloc formation, middle-income positioning, pandemic equity, vaccine access, compulsory licensing, WHA procedures",
    },
    # ── BEG (5/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Basic Lobbying for Co-Sponsors on an AI Ethics Resolution",
        "prompt": (
            "You are the delegate of India in the Second Committee of the UN General Assembly "
            "(ECOFIN). You have drafted a working paper on establishing international guidelines "
            "for ethical AI development, with a focus on preventing algorithmic bias in financial "
            "services and employment screening.\n\n"
            "To move your working paper to a draft resolution, you need at least eight "
            "co-sponsors. Currently, you have three: India, South Africa, and Chile. You need "
            "five more. The committee has 50 delegates, and you have one more unmoderated caucus "
            "before the draft resolution deadline.\n\n"
            "Describe your lobbying strategy for securing the remaining five co-sponsors. Who "
            "do you target, what arguments do you tailor to each potential co-sponsor, and how "
            "do you handle a delegate who is interested but has reservations about specific "
            "operative clauses?"
        ),
        "hints": (
            "Prioritize delegates whose countries have expressed real-world interest in AI "
            "governance. Tailor your pitch to each country's specific interests. Be willing to "
            "add or modify operative clauses to accommodate co-sponsors -- flexibility is key "
            "to building support."
        ),
        "sample_answer": (
            "Target five categories of potential co-sponsors with tailored pitches. First, "
            "approach the EU delegates (Germany, France) who already have AI regulation "
            "frameworks (the EU AI Act) -- argue that international guidelines would extend "
            "their regulatory standards globally, benefiting European companies. Second, "
            "approach tech-sector developing nations (Vietnam, Kenya) who want to attract AI "
            "investment while protecting citizens -- emphasize that guidelines create a stable "
            "regulatory environment that encourages foreign investment. Third, approach "
            "delegates who have spoken on related topics like digital rights or data privacy, "
            "as they are philosophically aligned. For a delegate with reservations -- say "
            "Japan worries that strict guidelines could hamper innovation -- offer a specific "
            "amendment: change 'mandatory algorithmic audits' to 'encouraged algorithmic "
            "transparency reporting' in the relevant operative clause. Document this change "
            "in writing so Japan feels their input is reflected. Keep a simple spreadsheet "
            "tracking each delegate's status: 'confirmed,' 'interested,' 'opposed,' or "
            "'unknown.' Focus your remaining time on the 'interested' category, as converting "
            "them requires less effort than persuading opposed delegates."
        ),
        "key_concepts": "lobbying strategy, co-sponsor recruitment, working paper promotion, AI ethics, algorithmic bias, tailored argumentation, ECOFIN procedures",
    },
    # ── BEG (6/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Approaching a Hostile Delegate on Nuclear-Weapon-Free Zones",
        "prompt": (
            "You are the delegate of Mexico in DISEC. Your working paper proposes expanding "
            "nuclear-weapon-free zones (NWFZs) to cover the Middle East. During a moderated "
            "caucus, the delegate of a nuclear-armed state spoke strongly against your proposal, "
            "calling it 'naive and strategically destabilizing.'\n\n"
            "The chair has now called a 10-minute unmoderated caucus. You believe this delegate's "
            "opposition could prevent your resolution from passing, but you also know that "
            "engaging respectfully could either soften their stance or reveal compromise "
            "opportunities.\n\n"
            "How do you approach this hostile delegate during the unmoderated caucus? What "
            "opening line do you use, and what ground rules do you set for the conversation "
            "to keep it productive?"
        ),
        "hints": (
            "Never open with a defensive or argumentative statement. Acknowledge their concern "
            "as legitimate before presenting your perspective. Your goal is not to win an "
            "argument but to find out what specific language or provisions might reduce their "
            "opposition."
        ),
        "sample_answer": (
            "Approach the delegate calmly and with open body language. Open with: 'I heard "
            "your concerns during the moderated caucus and I think they raise important points "
            "about regional stability. Could we spend a few minutes discussing what specific "
            "provisions might address your security concerns?' This framing accomplishes "
            "several things: it validates their position, reframes the conversation from "
            "opposition to problem-solving, and asks for their input rather than defending "
            "your paper. If they engage, ask targeted questions: 'Is your concern about the "
            "verification mechanism, the timeline, or the scope of the zone?' Understanding "
            "their specific objection -- rather than their general opposition -- allows you "
            "to propose targeted amendments. For example, if they worry about verification, "
            "offer to include IAEA safeguards language. If they object to the scope, propose "
            "a phased approach starting with a confidence-building declaration of intent. Set "
            "a ground rule implicitly by modeling respectful dialogue: speak softly, ask "
            "questions, and take notes. Even if the delegate remains opposed, the conversation "
            "demonstrates to nearby delegates that you are reasonable and collaborative, which "
            "can attract additional support for your resolution."
        ),
        "key_concepts": "diplomatic engagement, conflict de-escalation, nuclear-weapon-free zones, hostile delegate management, DISEC procedures, IAEA safeguards, respectful dialogue",
    },
    # ── BEG (7/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Building a Small Bloc on Water Dispute Resolution",
        "prompt": (
            "You are the delegate of Egypt in the Sixth Committee of the UN General Assembly "
            "(Legal). The committee is discussing the law of transboundary aquifers and shared "
            "water resources. You want to build a small bloc of downstream nations that share "
            "your concern about upstream dam construction reducing water flow.\n\n"
            "You have identified five potential allies: Iraq (concerned about Turkish dams on "
            "the Tigris-Euphrates), Vietnam (concerned about Mekong River dams), Bangladesh "
            "(concerned about Ganges-Brahmaputra flow), Cambodia (also affected by Mekong "
            "projects), and Sudan (sharing Nile concerns with Egypt).\n\n"
            "Draft a brief position statement (3-4 sentences) that could unite these diverse "
            "downstream nations into a coherent bloc, and describe how you would present it "
            "during an unmoderated caucus."
        ),
        "hints": (
            "Focus on the shared principle -- the right to equitable and reasonable utilization "
            "of shared watercourses -- rather than any single river dispute. Reference the 1997 "
            "UN Watercourses Convention as a legal foundation. Keep the statement general enough "
            "that all five nations can endorse it without feeling it prioritizes one river basin "
            "over another."
        ),
        "sample_answer": (
            "Position statement: 'We, the undersigned downstream riparian states, affirm that "
            "the principle of equitable and reasonable utilization, as enshrined in the 1997 UN "
            "Convention on the Law of Non-Navigational Uses of International Watercourses, must "
            "be the foundation of all transboundary water governance. We call upon the "
            "international community to establish binding notification and consultation "
            "requirements for any upstream infrastructure project that significantly alters "
            "water flow to downstream states. We further urge the creation of an independent "
            "technical assessment mechanism under UN auspices to evaluate the transboundary "
            "impacts of proposed dam and diversion projects.' Present this during the "
            "unmoderated caucus by approaching each delegate individually, starting with "
            "Sudan (the closest ally on Nile issues) to secure an immediate endorsement that "
            "demonstrates momentum. Show each subsequent delegate that others have already "
            "signed on. Emphasize that the statement is deliberately general -- it does not "
            "name specific rivers or countries -- so endorsing it does not commit any delegate "
            "to a position on their specific bilateral dispute. This lowers the barrier to "
            "joining the bloc while creating a unified front for the committee's broader "
            "negotiations."
        ),
        "key_concepts": "bloc building, downstream riparian states, transboundary water law, 1997 Watercourses Convention, position statements, coalition recruitment, Sixth Committee",
    },
    # ── BEG (8/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "First-Time Delegate Caucus Navigation on Trade Wars",
        "prompt": (
            "You are the delegate of Vietnam in ECOFIN, attending your first MUN conference. "
            "The topic is the impact of trade wars on developing economies. A 20-minute "
            "unmoderated caucus has just been called, and you feel overwhelmed by the room's "
            "energy as experienced delegates immediately begin forming groups and negotiating.\n\n"
            "You have a prepared position paper that advocates for multilateral trade dispute "
            "resolution through the WTO rather than bilateral tariff escalation. However, you "
            "are unsure how to translate your paper into effective caucus participation.\n\n"
            "Provide a step-by-step guide for navigating this unmoderated caucus as a first-time "
            "delegate. Include what to do in the first, middle, and final portions of the "
            "20-minute period."
        ),
        "hints": (
            "Break the caucus into three phases: observe and orient (first 3-5 minutes), "
            "engage and contribute (middle 10 minutes), and consolidate (final 5 minutes). "
            "Having your position paper's key points written on a notecard can boost your "
            "confidence when speaking."
        ),
        "sample_answer": (
            "Phase 1 -- Observe and Orient (minutes 1-5): Stand at the edge of the room and "
            "observe which groups are forming and who is leading them. Listen to nearby "
            "conversations to identify which blocs align with your WTO-centered position. "
            "Prepare a notecard with three key talking points from your position paper: "
            "(1) Vietnam's export-dependent economy is harmed by bilateral tariff escalation, "
            "(2) the WTO dispute settlement mechanism provides a rules-based alternative, "
            "(3) developing nations need special and differential treatment provisions. "
            "Phase 2 -- Engage and Contribute (minutes 5-15): Approach the group whose "
            "discussion most closely aligns with your position. Introduce yourself briefly "
            "and ask what the group is working on. When there is a natural pause, share one "
            "of your talking points: 'Vietnam's perspective is that strengthening WTO dispute "
            "resolution is more effective than bilateral retaliation, which disproportionately "
            "harms smaller economies.' Ask others for their views to build rapport. If someone "
            "proposes a working paper, offer to contribute specific operative clauses on WTO "
            "reform. Phase 3 -- Consolidate (minutes 15-20): Exchange contact information "
            "(placards or delegate names) with allies you have identified. Clarify any "
            "commitments: 'So we agreed that I will draft the operative clause on special "
            "and differential treatment?' Confirm who is leading the working paper and offer "
            "to assist with specific sections."
        ),
        "key_concepts": "first-time delegate strategies, unmoderated caucus navigation, position paper application, WTO dispute resolution, trade wars, time management in caucus",
    },
    # ── BEG (9/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Identifying Common Ground on Peacekeeping Contributions",
        "prompt": (
            "You are the delegate of South Africa in the Special Political and Decolonization "
            "Committee (SPECPOL). The committee is debating reform of UN peacekeeping "
            "operations, specifically how to ensure more equitable troop and financial "
            "contributions from Member States.\n\n"
            "During a moderated caucus, you notice that while delegates disagree on specifics, "
            "nearly everyone has mentioned at least one of the following themes: (1) the need "
            "for better training standards, (2) concerns about troop-contributing countries "
            "bearing disproportionate risk, and (3) the desire for more regional peacekeeping "
            "capacity.\n\n"
            "Explain how you would use these three areas of overlap to draft unifying operative "
            "language that could attract support from both major financial contributors (like the "
            "US, EU members) and major troop contributors (like Bangladesh, Ethiopia, Rwanda)."
        ),
        "hints": (
            "The key insight is that both financial and troop contributors benefit from better "
            "training (reducing casualties and improving mission effectiveness). Frame your "
            "operative clauses so that each group sees their interests reflected. Avoid "
            "assigning blame for the current imbalance."
        ),
        "sample_answer": (
            "Draft three operative clauses, each built on one area of overlap. First, on "
            "training standards: 'Requests the Secretary-General to establish a unified "
            "pre-deployment training curriculum developed in consultation with both troop-"
            "contributing and financial-contributing Member States.' This appeals to financial "
            "contributors who want accountability and to troop contributors who want their "
            "soldiers better prepared. Second, on equitable risk-sharing: 'Encourages the "
            "development of a risk-compensation framework that provides enhanced reimbursement "
            "rates for personnel deployed in high-threat environments.' This validates troop "
            "contributors' sacrifices without demanding mandatory deployments from financial "
            "contributors. Third, on regional capacity: 'Calls upon the UN to strengthen "
            "partnerships with regional organizations, including the African Union and ASEAN, "
            "to develop standby peacekeeping capabilities with dedicated funding streams.' This "
            "appeals to African and Asian troop contributors who want recognition of regional "
            "expertise, and to Western financial contributors who see regional capacity as a "
            "cost-effective force multiplier. Present these three clauses as a package during "
            "the next unmoderated caucus, emphasizing that they address concerns raised by "
            "delegates across all blocs."
        ),
        "key_concepts": "common ground identification, peacekeeping reform, troop-contributing countries, financial contributors, SPECPOL, operative clause drafting, equitable burden-sharing",
    },
    # ── BEG (10/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "BEG",
        "title": "Introducing Your Position on Counter-Terrorism Financing",
        "prompt": (
            "You are the delegate of Turkey in the Security Council. The committee is discussing "
            "measures to combat terrorist financing, and the chair has called a moderated caucus "
            "with 90-second speaking times. You will be among the first speakers.\n\n"
            "Your position supports stronger international cooperation to freeze terrorist "
            "assets, but you are wary of measures that could be used to target legitimate "
            "charitable organizations or restrict remittance flows that many Turkish citizens "
            "rely on for family support abroad.\n\n"
            "Draft your 90-second opening statement that clearly introduces your position, "
            "signals your negotiation priorities, and invites other delegates to work with "
            "you. Your statement should position Turkey as a bridge between Western security "
            "priorities and developing-world economic concerns."
        ),
        "hints": (
            "In 90 seconds you can deliver roughly 200-250 words. Structure your statement: "
            "opening hook (1 sentence), position statement (2-3 sentences), key concern "
            "(2 sentences), invitation to collaborate (1-2 sentences). Practice concision."
        ),
        "sample_answer": (
            "Statement: 'Honorable Chair, distinguished delegates -- Turkey stands at the "
            "crossroads of continents and at the frontline of combating terrorist financing. "
            "We unequivocally support strengthening international mechanisms to identify, "
            "freeze, and seize assets linked to designated terrorist organizations under "
            "Security Council resolutions 1267 and 1373. However, Turkey urges this body to "
            "recognize that blunt financial instruments can cause devastating collateral harm. "
            "Overly broad asset-freezing provisions have shut down legitimate humanitarian "
            "organizations and disrupted remittance corridors that millions of families depend "
            "upon for survival. We therefore propose that any new framework include clear "
            "exemptions for licensed humanitarian operations and regulated remittance services, "
            "with due-process safeguards for delisting entities wrongly designated. Turkey is "
            "prepared to work with all delegations -- those prioritizing security enforcement "
            "and those prioritizing economic protection -- to craft balanced operative language. "
            "We invite interested delegates to join us in the upcoming unmoderated caucus to "
            "develop a comprehensive approach that is both effective against terrorist networks "
            "and protective of innocent livelihoods. Thank you.' This statement accomplishes "
            "four goals: it establishes credibility through geographic relevance, states a "
            "clear position, raises a specific concern that invites compromise, and explicitly "
            "invites collaboration."
        ),
        "key_concepts": "opening statements, position introduction, counter-terrorism financing, Security Council, bridge-building, remittance protections, moderated caucus speaking",
    },
    # ── INT (1/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Managing Bloc Disagreements on Sanctions Policy",
        "prompt": (
            "You are the delegate of Germany in the Security Council. Your bloc -- consisting of "
            "Germany, France, the United Kingdom, and two elected members from Eastern Europe -- "
            "has been negotiating a draft resolution on targeted sanctions against a fictional "
            "regime accused of systematic human rights violations.\n\n"
            "A serious disagreement has erupted within your bloc. France wants comprehensive "
            "economic sanctions including an oil embargo, arguing that targeted measures have "
            "been insufficient. The UK prefers targeted travel bans and asset freezes on "
            "individual regime officials, citing concerns about humanitarian impact on the "
            "civilian population. The two Eastern European members are split, with one "
            "supporting France and one supporting the UK.\n\n"
            "As Germany, you hold the swing position. Describe how you mediate this intra-bloc "
            "disagreement while maintaining bloc cohesion and producing a unified draft "
            "resolution before the next formal session."
        ),
        "hints": (
            "Consider proposing a sequenced approach: start with targeted sanctions and include "
            "a trigger mechanism that escalates to broader sanctions if benchmarks are not met. "
            "This gives France the escalation pathway while giving the UK the initial targeted "
            "approach. Focus on process -- how you run the intra-bloc discussion -- not just "
            "substance."
        ),
        "sample_answer": (
            "Begin by reframing the disagreement from 'comprehensive vs. targeted' to 'what "
            "sequence of measures maximizes pressure while maintaining humanitarian "
            "protections.' Call a private meeting of the five bloc members and set ground "
            "rules: each delegate has three minutes to present their red lines (non-negotiable "
            "elements), and everyone listens without interrupting. Document each delegate's "
            "red lines on a shared notepad. France's red line is likely that the resolution "
            "must include a pathway to an oil embargo; the UK's red line is that civilians "
            "must not bear the primary burden. These are not inherently contradictory. Propose "
            "a two-phase approach: Phase 1 imposes targeted travel bans, asset freezes, and "
            "an arms embargo on regime officials and entities, with a 90-day review period. "
            "Phase 2, triggered automatically if the regime fails to meet specific benchmarks "
            "(releasing political prisoners, allowing humanitarian access, engaging in "
            "dialogue), escalates to sectoral sanctions including oil. Include humanitarian "
            "exemptions for food, medicine, and essential services in both phases. This "
            "structure satisfies France because escalation is built in, satisfies the UK "
            "because the initial approach is targeted, and gives both Eastern European "
            "members a defensible position. Present the compromise as a jointly authored "
            "package and agree that all five delegates will speak in support during the next "
            "moderated caucus, projecting bloc unity to the rest of the committee."
        ),
        "key_concepts": "intra-bloc mediation, sanctions policy, sequenced escalation, red lines identification, bloc cohesion, Security Council procedures, humanitarian exemptions",
    },
    # ── INT (2/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Multi-Party Negotiation on Ocean Rights and Deep-Sea Mining",
        "prompt": (
            "You are the delegate of Chile in the UN Convention on the Law of the Sea (UNCLOS) "
            "review conference, simulated as a specialized GA committee. Four distinct interest "
            "groups have formed around the issue of deep-sea mining regulations in areas beyond "
            "national jurisdiction.\n\n"
            "Group 1 (Pacific Island states) wants a complete moratorium on deep-sea mining "
            "until environmental impact assessments prove it is safe. Group 2 (China, Russia, "
            "South Korea) wants to proceed with mining under the International Seabed Authority "
            "(ISA) framework with minimal environmental restrictions. Group 3 (EU members) "
            "supports mining with strong environmental safeguards and benefit-sharing with "
            "developing nations. Group 4 (landlocked developing countries) wants guaranteed "
            "revenue-sharing from any mining proceeds under the 'common heritage of mankind' "
            "principle.\n\n"
            "Chile, as a major copper-producing nation that could be economically impacted by "
            "deep-sea mineral extraction, has unique interests. Develop a multi-party "
            "negotiation strategy that engages all four groups and positions Chile as a central "
            "broker."
        ),
        "hints": (
            "Chile's position is nuanced: it benefits from higher commodity prices if deep-sea "
            "mining is restricted, but it also has a long Pacific coastline and interest in "
            "marine environmental protection. Use this complexity as an asset -- you can "
            "credibly speak to each group's concerns."
        ),
        "sample_answer": (
            "Chile's strategy should exploit its unique position as both an interested economic "
            "party and a Pacific coastal state. Begin with Group 1 (Pacific Islands): express "
            "solidarity on environmental protection, referencing Chile's own marine protected "
            "areas around Rapa Nui (Easter Island). Propose that rather than a permanent "
            "moratorium, the resolution call for a precautionary pause of five years during "
            "which comprehensive environmental baselines are established. This is more "
            "achievable than a blanket moratorium and may attract Group 3 support. Next, "
            "approach Group 3 (EU) with the modified proposal, adding their preferred language "
            "on environmental safeguards: mandatory environmental impact assessments, "
            "independent monitoring, and restoration bonds posted by mining companies. Add "
            "Group 4's benefit-sharing demand as a natural complement: 'Any future mining "
            "royalties collected by the ISA shall be distributed with priority allocation to "
            "landlocked and geographically disadvantaged developing states, consistent with "
            "UNCLOS Article 82.' This creates a three-group coalition (Pacific Islands + EU + "
            "landlocked states) that constitutes a strong majority. For Group 2 (mining "
            "proponents), offer a concession: instead of a moratorium, call it a "
            "'precautionary research phase' during which exploration (but not commercial "
            "extraction) may continue. This allows their state-sponsored enterprises to "
            "continue seabed research while delaying the commercial extraction that would "
            "compete with Chilean copper. Present the final package as a four-element deal: "
            "precautionary pause on extraction, continued exploration, mandatory environmental "
            "safeguards, and equitable benefit-sharing."
        ),
        "key_concepts": "multi-party negotiation, deep-sea mining, UNCLOS, International Seabed Authority, common heritage of mankind, benefit-sharing, precautionary principle, broker positioning",
    },
    # ── INT (3/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Bridging Competing Interests on AI Governance in the GA",
        "prompt": (
            "You are the delegate of Japan in the First Committee (DISEC), where the topic has "
            "expanded to include governance of autonomous weapons systems and military AI. Two "
            "competing draft resolutions are on the floor.\n\n"
            "Draft Resolution A (sponsored by Austria, Mexico, and Costa Rica) calls for a "
            "legally binding prohibition on fully autonomous weapons systems, requiring "
            "meaningful human control over all targeting and engagement decisions. Draft "
            "Resolution B (sponsored by the US, Israel, and Australia) proposes voluntary "
            "guidelines and best practices for the development and deployment of autonomous "
            "weapons, emphasizing state sovereignty over defense technology decisions.\n\n"
            "Japan has advanced AI capabilities and a significant defense industry, but also a "
            "constitutional commitment to peace and a public that is wary of autonomous "
            "weapons. Neither draft fully reflects Japan's interests. Develop a strategy to "
            "bridge these two drafts into a single compromise resolution, or explain why "
            "merging them is impossible and propose an alternative path."
        ),
        "hints": (
            "Consider the concept of 'meaningful human control' as a spectrum rather than a "
            "binary. Japan could propose different levels of human oversight depending on the "
            "lethality and context of the AI system. Think about what each side's true "
            "bottom line is versus their opening position."
        ),
        "sample_answer": (
            "Japan should pursue a merge strategy because the two drafts, while opposed in "
            "approach, share an underlying premise: both acknowledge that autonomous weapons "
            "raise governance challenges. The merge requires identifying each side's true "
            "bottom line. Draft A's sponsors will not accept a resolution without any binding "
            "element -- they need at least one enforceable provision. Draft B's sponsors will "
            "not accept a blanket prohibition -- they need flexibility for defensive AI "
            "systems. Japan's bridging proposal: a tiered regulatory framework. Tier 1 "
            "(binding prohibition): fully autonomous weapons systems that select and engage "
            "human targets without any human involvement -- an outright ban, satisfying Draft "
            "A's core demand. Tier 2 (binding regulation): semi-autonomous systems that assist "
            "human operators in targeting decisions -- require meaningful human control defined "
            "as human authorization before lethal force, with periodic review by a new "
            "international body. Tier 3 (voluntary guidelines): AI systems used for logistics, "
            "intelligence analysis, and defensive operations (missile defense, mine detection) "
            "-- governed by voluntary best practices and transparency reporting, satisfying "
            "Draft B's sovereignty concerns. Present this framework privately to the lead "
            "sponsors of both drafts before circulating publicly. Offer Japan as a lead "
            "co-sponsor of the merged resolution, lending credibility as a technologically "
            "advanced nation with a peace constitution. If either side refuses to negotiate, "
            "Japan should introduce the tiered framework as Draft Resolution C, attracting "
            "the moderate majority that finds both existing drafts too extreme."
        ),
        "key_concepts": "draft resolution merging, autonomous weapons governance, meaningful human control, tiered regulation, DISEC procedures, bridge-building, Japan peace constitution, compromise architecture",
    },
    # ── INT (4/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Amendment Negotiations on Economic Development Clauses",
        "prompt": (
            "You are the delegate of Kenya in ECOFIN. A draft resolution on sustainable "
            "economic development in Sub-Saharan Africa is nearing a vote, but three amendments "
            "have been proposed that threaten to fragment support.\n\n"
            "Amendment 1 (proposed by the US): Strike operative clause 7, which calls for a "
            "'0.7%% of GNI' official development assistance target, replacing it with language "
            "about 'encouraging voluntary contributions commensurate with national capacity.' "
            "Amendment 2 (proposed by China): Add an operative clause recognizing the Belt and "
            "Road Initiative as a model for South-South development cooperation. Amendment 3 "
            "(proposed by Nigeria): Strengthen operative clause 12 on debt relief by changing "
            "'encourages creditor nations to consider' to 'demands that creditor nations "
            "implement comprehensive debt restructuring.'\n\n"
            "As Kenya, you support the overall resolution but must navigate these amendments. "
            "Which do you accept, reject, or counter-amend, and how do you build voting "
            "coalitions for each amendment vote?"
        ),
        "hints": (
            "Consider each amendment's impact on the resolution's overall chances of passing. "
            "An amendment that strengthens one clause but causes ten delegates to vote against "
            "the entire resolution is counterproductive. Think strategically about which "
            "amendments to accept as the price of broader support."
        ),
        "sample_answer": (
            "Analyze each amendment's strategic impact. Amendment 1 (US, striking the 0.7%% "
            "target): This is dangerous because the 0.7%% target is a core African Group "
            "demand, but rejecting it outright could lose US support for the entire resolution. "
            "Counter-amend: retain the 0.7%% target as an aspirational benchmark but add "
            "language acknowledging 'varied national circumstances and timelines for achieving "
            "this target.' This preserves the principle while giving the US linguistic "
            "flexibility. Build a coalition of EU members (who have accepted the 0.7%% target "
            "in other contexts) and African states to support the counter-amendment. "
            "Amendment 2 (China, Belt and Road): Accept the spirit but modify the language. "
            "Naming a specific bilateral initiative in a multilateral resolution is unusual "
            "and could provoke opposition. Counter-amend to replace the BRI reference with "
            "'welcomes South-South and triangular cooperation initiatives that contribute to "
            "sustainable infrastructure development.' Privately tell China that this language "
            "implicitly covers BRI without creating a precedent of naming bilateral programs. "
            "Amendment 3 (Nigeria, demanding debt restructuring): While Kenya sympathizes, "
            "'demands' language will cause Western creditor nations to vote against the entire "
            "resolution. Approach Nigeria privately and propose: 'strongly urges creditor "
            "nations to engage constructively in comprehensive debt restructuring negotiations.' "
            "This is stronger than the original 'encourages' while avoiding the confrontational "
            "'demands.' Offer to co-sponsor Nigeria's separate resolution on debt relief in a "
            "future session as compensation for moderating this amendment."
        ),
        "key_concepts": "amendment strategy, counter-amendments, voting coalition building, ODA targets, debt restructuring, South-South cooperation, ECOFIN procedures, strategic compromise",
    },
    # ── INT (5/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Coalition Management During Climate Negotiation Deadlock",
        "prompt": (
            "You are the delegate of Colombia in the UNFCCC COP, simulated as a GA committee. "
            "You lead a coalition of eight Latin American and Caribbean nations advocating for "
            "a loss-and-damage financing mechanism funded by historically high-emitting nations. "
            "Negotiations have reached a deadlock: your coalition and the African Group (your "
            "allies) are refusing to accept a draft that lacks binding financial commitments, "
            "while the US and EU are refusing to accept language that implies legal liability "
            "for historical emissions.\n\n"
            "Within your own coalition, cracks are forming. Costa Rica is considering breaking "
            "away to support a weaker EU compromise because it needs EU trade concessions on a "
            "separate issue. Trinidad and Tobago is frustrated that negotiations are taking too "
            "long and wants to accept any deal on the table. Meanwhile, Bolivia is pushing your "
            "coalition toward even more radical demands.\n\n"
            "How do you manage these internal coalition dynamics while maintaining negotiating "
            "leverage with the opposing bloc?"
        ),
        "hints": (
            "Address internal threats in order of urgency. Costa Rica's potential defection is "
            "the most dangerous because it signals to the opposition that your coalition is "
            "fracturing. Consider what you can offer Costa Rica within the coalition to keep "
            "them from seeking outside deals. Balance Bolivia's radicalism by channeling it "
            "into a useful role."
        ),
        "sample_answer": (
            "Triage the internal threats. Priority one: Costa Rica. Call a private bilateral "
            "meeting and acknowledge their trade concerns directly: 'I understand the EU "
            "trade concessions are important to Costa Rica. Let us ensure our coalition's "
            "final position includes language on climate-trade linkages that benefits your "
            "agenda.' Add an operative clause to your coalition's draft that 'calls upon "
            "developed nations to eliminate tariffs on climate-vulnerable nations' agricultural "
            "exports,' giving Costa Rica a win they cannot get from the EU compromise alone. "
            "Priority two: Trinidad and Tobago. Their frustration is about process, not "
            "substance. Appoint their delegate as the coalition's official liaison to the "
            "committee chair, giving them a visible role and a sense of progress. Share "
            "your negotiation timeline: 'We plan to table our final offer within two sessions. "
            "Your patience will result in a stronger outcome than accepting the current deal.' "
            "Priority three: Bolivia. Rather than silencing radical demands, channel them "
            "strategically. Ask Bolivia to draft a maximalist working paper as the coalition's "
            "opening position for the next round. This serves two purposes: it keeps Bolivia "
            "engaged and productive, and it shifts the perceived center of negotiation, making "
            "your actual position seem more moderate by comparison. Externally, project unity "
            "by having all eight delegates sign a joint coalition statement before the next "
            "session. Coordinate speaking slots so each delegate reinforces the same three "
            "talking points. If the opposition learns about internal disagreements, they will "
            "exploit them by offering side deals to individual members."
        ),
        "key_concepts": "coalition management, internal dissent, loss and damage financing, UNFCCC negotiations, defection prevention, strategic role assignment, coalition unity, negotiation leverage",
    },
    # ── INT (6/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Negotiating Compromise Language on Human Rights Monitoring",
        "prompt": (
            "You are the delegate of South Africa in the UN Human Rights Council (HRC). A "
            "draft resolution proposes establishing a new independent monitoring mechanism "
            "for human rights conditions in a specific region. The draft has strong support "
            "from Western nations but faces opposition from the regional bloc and several "
            "Global South nations who view it as selective and politically motivated.\n\n"
            "You have been asked to serve as a neutral mediator between the two sides. The "
            "Western bloc's bottom line is that there must be some form of international "
            "oversight with reporting requirements. The opposing bloc's bottom line is that "
            "any mechanism must respect state sovereignty and not single out specific countries "
            "for differential treatment.\n\n"
            "Draft compromise language for the key operative clause that could satisfy both "
            "bottom lines. Explain your negotiation approach and why each element of your "
            "proposed language was chosen."
        ),
        "hints": (
            "Look at existing HRC mechanisms that have successfully balanced these tensions, "
            "such as the Universal Periodic Review (UPR), which applies equally to all nations. "
            "Consider a mechanism that technically covers all states in the region (or globally) "
            "but has enhanced reporting for situations of particular concern."
        ),
        "sample_answer": (
            "Proposed operative clause: 'Decides to establish a regional human rights "
            "situation assessment office, operating under the auspices of the Office of the "
            "High Commissioner for Human Rights, with a mandate to (a) provide technical "
            "assistance and capacity-building to all states in the region upon request, "
            "(b) produce an annual thematic report on human rights trends across the region, "
            "and (c) offer confidential recommendations to individual states based on "
            "information received from multiple sources, with findings shared with the "
            "state concerned before any public reporting.' Each element is designed to "
            "address specific bottom lines. Calling it an 'assessment office' rather than "
            "a 'monitoring mechanism' reduces the punitive connotation, addressing sovereignty "
            "concerns. Making it regional rather than country-specific means no single nation "
            "is singled out, satisfying the opposing bloc. However, the mandate to produce "
            "reports based on 'information received from multiple sources' gives the office "
            "real investigative capacity, satisfying the Western demand for international "
            "oversight. The provision for 'confidential recommendations' with prior state "
            "consultation respects sovereignty while ensuring accountability. The technical "
            "assistance component frames the mechanism as supportive rather than adversarial, "
            "which helps Global South allies vote yes. Present this language to both sides "
            "simultaneously in a joint meeting, preventing either side from perceiving it as "
            "the other's draft. Emphasize that South Africa's own experience with human rights "
            "transition gives it credibility to propose balanced solutions."
        ),
        "key_concepts": "compromise language drafting, human rights monitoring, HRC procedures, sovereignty concerns, neutral mediation, OHCHR mandate, confidential reporting, technical assistance framing",
    },
    # ── INT (7/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Lobbying P5 Members on Space Treaty Provisions",
        "prompt": (
            "You are the delegate of Mexico in the Committee on the Peaceful Uses of Outer "
            "Space (COPUOS), simulated as a GA committee. Your coalition of Latin American "
            "and African nations has drafted a resolution calling for a binding treaty "
            "prohibiting the weaponization of space, extending the 1967 Outer Space Treaty.\n\n"
            "To pass, your resolution needs at least passive acceptance from the P5 members, "
            "two of whom (the US and Russia) have active space military programs. China has "
            "historically supported space disarmament in rhetoric but has conducted anti-"
            "satellite weapons tests. France and the UK generally follow a middle path.\n\n"
            "Develop a lobbying strategy for each P5 member, identifying what concessions or "
            "modifications you might offer to secure their support or at least their "
            "abstention rather than a no vote."
        ),
        "hints": (
            "Remember that in COPUOS (and GA committees generally), there is no veto, but P5 "
            "opposition can still undermine a resolution's legitimacy and implementation. "
            "Consider what each P5 member values beyond the specific issue -- linkage to other "
            "negotiations, prestige, consistency with their stated positions."
        ),
        "sample_answer": (
            "Tailor the approach to each P5 member's interests and constraints. United States: "
            "The US will not accept a binding prohibition on space weapons given its Space "
            "Force investment. Offer a key concession: replace 'binding treaty' language with "
            "'framework for negotiation of legally binding instruments' and add a clause "
            "affirming 'the right of self-defense in space consistent with Article 51 of the "
            "UN Charter.' Ask the US to abstain rather than vote no, framing it as leadership "
            "on space governance rather than concession. Russia: Russia has proposed its own "
            "Prevention of an Arms Race in Outer Space (PAROS) resolution. Offer to incorporate "
            "PAROS language into your draft, crediting Russia's contribution. This appeals to "
            "Russian prestige and makes opposition to 'their own language' awkward. China: "
            "Engage China by including language on 'transparency and confidence-building "
            "measures for space activities' that aligns with their stated FMCT positions, "
            "while the anti-weaponization provisions align with their public rhetoric even if "
            "not their practice. France: Appeal to France's interest in EU strategic autonomy "
            "in space. Include language supporting multilateral space situational awareness "
            "sharing, which benefits European space programs. The UK: Link to the UK's post-"
            "Brexit desire for multilateral relevance. Offer UK co-sponsorship and credit for "
            "the verification provisions. Meet with France and the UK first to build momentum, "
            "then approach Russia with the PAROS incorporation, and finally the US with the "
            "modified language and the reality that four of five P5 members are on board."
        ),
        "key_concepts": "P5 lobbying strategy, space treaty negotiation, COPUOS, Outer Space Treaty, PAROS, tailored concessions, abstention strategy, prestige-based argumentation",
    },
    # ── INT (8/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Managing Multi-Party Amendment Process on Refugee Protection",
        "prompt": (
            "You are the delegate of Germany in the Third Committee (SOCHUM). A draft "
            "resolution on strengthening the international refugee protection framework is "
            "entering the amendment phase. Seven amendments have been submitted by different "
            "delegations, and you need to navigate the voting sequence strategically.\n\n"
            "The amendments include: (A) adding language on safe third country agreements, "
            "(B) strengthening non-refoulement provisions, (C) establishing a global refugee "
            "resettlement quota system, (D) creating a refugee skills recognition framework, "
            "(E) adding climate refugees to the definition of protected persons, (F) requiring "
            "biometric registration of all asylum seekers, and (G) establishing a rapid "
            "response fund for sudden displacement crises.\n\n"
            "Germany supports amendments B, D, E, and G, opposes A and F, and is neutral on C. "
            "Some amendments are contradictory. Develop a voting strategy that maximizes the "
            "chances of your preferred amendments passing while blocking those you oppose."
        ),
        "hints": (
            "Amendments are typically voted on in the order they were submitted, but the "
            "furthest from the original text is voted first. Consider how the passage or "
            "failure of early amendments affects later ones. If Amendment A passes, it may "
            "make Amendment B less impactful. Build vote-trading coalitions: 'I will support "
            "your amendment if you support mine.'"
        ),
        "sample_answer": (
            "First, map the amendment interdependencies. Amendments A (safe third country) and "
            "B (non-refoulement) are partially contradictory: strong non-refoulement provisions "
            "limit the use of safe third country agreements. If B passes first, A becomes "
            "harder to implement. Amendment E (climate refugees) is the most expansive change "
            "to the original text and will likely be voted on first under standard procedure. "
            "Voting strategy: Build a coalition to pass Amendment E first. Approach SIDS "
            "delegates and African states who are natural supporters of climate refugee "
            "recognition. A strong early vote sets a progressive tone for subsequent amendments. "
            "For Amendment B, coordinate with UNHCR-aligned delegations (Nordic countries, "
            "Canada, New Zealand) who consistently support non-refoulement strengthening. "
            "Offer a vote trade: support their Amendment D (skills recognition) in exchange "
            "for their active whipping on Amendment B. To block Amendment A, coordinate with "
            "the African Group and Latin American nations who oppose safe third country "
            "concepts as externalization of asylum responsibilities. To block Amendment F "
            "(biometric registration), align with privacy-conscious EU members and civil "
            "liberties advocates by raising concerns about data protection in conflict zones. "
            "For Amendment G (rapid response fund), this is likely uncontroversial -- save "
            "it for last and use it as a vote-trading chip: offer support for another "
            "delegate's amendment in exchange for their vote on G. On Amendment C (quota "
            "system), remain neutral publicly but vote in favor if it appears it will pass "
            "anyway, positioning Germany as a constructive partner. The key is sequencing: "
            "ensure your preferred amendments are voted on before contradictory ones, and "
            "spend your negotiating capital on blocking A and F while letting the coalition "
            "carry B, D, E, and G."
        ),
        "key_concepts": "amendment voting strategy, vote trading, amendment interdependencies, refugee protection framework, non-refoulement, climate refugees, SOCHUM procedures, coalition whipping",
    },
    # ── INT (9/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Bridging North-South Divide on Pandemic Treaty Negotiations",
        "prompt": (
            "You are the delegate of Indonesia in the World Health Assembly. Negotiations on "
            "a new pandemic preparedness treaty have stalled along a familiar North-South "
            "divide. Developed nations want strong provisions on pathogen surveillance data "
            "sharing, early warning transparency, and international inspection rights. "
            "Developing nations want guaranteed access to vaccines and therapeutics, technology "
            "transfer, and manufacturing capacity support.\n\n"
            "Both sides view the other's demands as one-sided. Developed nations argue that "
            "data sharing saves lives; developing nations argue that data sharing without "
            "benefit sharing repeats the inequities of COVID-19 vaccine distribution.\n\n"
            "Indonesia, as the world's fourth most populous nation and a country that "
            "experienced both pathogen surveillance controversies (the 2007 H5N1 virus-sharing "
            "dispute) and vaccine access inequities during COVID-19, is uniquely positioned to "
            "bridge this divide. Propose a comprehensive negotiation framework."
        ),
        "hints": (
            "Indonesia's 2007 decision to withhold H5N1 virus samples until benefit-sharing "
            "was guaranteed is a landmark case in global health governance. Use this precedent "
            "to argue for a quid pro quo framework: data sharing in exchange for benefit "
            "sharing, with both obligations legally linked."
        ),
        "sample_answer": (
            "Invoke Indonesia's 2007 H5N1 precedent explicitly: 'Indonesia's experience "
            "demonstrated that pathogen sharing without benefit sharing is unsustainable. The "
            "Pandemic Influenza Preparedness (PIP) Framework that resulted from that dispute "
            "provides a proven model for linking obligations.' Propose a 'Mutual Obligations "
            "Framework' with four interconnected pillars that cannot be separated. Pillar 1 -- "
            "Pathogen and Data Sharing: All Member States commit to sharing pathogen samples "
            "and genomic sequence data within 24 hours of identification, through WHO-"
            "designated laboratories. This satisfies developed-nation demands for transparency. "
            "Pillar 2 -- Benefit Sharing: Pharmaceutical companies accessing shared pathogen "
            "data must commit 10%% of resulting vaccine and therapeutic production at cost to "
            "a WHO allocation pool, with developing nations receiving priority. Pillar 3 -- "
            "Technology Transfer: A dedicated technology transfer mechanism, modeled on the "
            "Medicines Patent Pool, facilitates voluntary licensing of pandemic-related "
            "intellectual property to qualified manufacturers in developing nations. Pillar 4 "
            "-- Capacity Building: A pandemic preparedness fund, financed by assessed "
            "contributions proportional to GDP, supports regional manufacturing hubs in "
            "Africa, Southeast Asia, and Latin America. The critical negotiation point: these "
            "four pillars are legally linked. No state can enjoy benefits of Pillar 1 data "
            "without fulfilling Pillar 2 obligations, and vice versa. This reciprocity makes "
            "both sides' commitments credible. Present the framework as a 'single undertaking' "
            "-- nothing is agreed until everything is agreed -- which prevents cherry-picking "
            "and ensures both sides negotiate in good faith across all pillars simultaneously."
        ),
        "key_concepts": "North-South divide bridging, pandemic treaty, pathogen sharing, benefit sharing, PIP Framework, single undertaking, mutual obligations, WHA negotiation, technology transfer",
    },
    # ── INT (10/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "INT",
        "title": "Caucus Strategy for Counter-Terrorism Resolution in the Security Council",
        "prompt": (
            "You are the delegate of Egypt in the Security Council. A draft resolution on "
            "counter-terrorism cooperation in the Sahel region is being negotiated. You have "
            "called for an unmoderated caucus and need to accomplish three objectives in 15 "
            "minutes: (1) secure support from at least two African elected members for your "
            "proposed amendment on regional counter-terrorism forces, (2) address France's "
            "concerns about the resolution's impact on its military withdrawal timeline, and "
            "(3) prevent Russia from introducing language that could expand the resolution's "
            "scope to legitimize its own military activities in the region.\n\n"
            "These three objectives create tension: the time you spend on one reduces time "
            "for the others, and some conversations could undermine your position in other "
            "negotiations if overheard.\n\n"
            "Plan your 15-minute caucus minute by minute, including who you approach, in what "
            "order, and what you say to each."
        ),
        "hints": (
            "Prioritize based on urgency and difficulty. The most time-sensitive conversation "
            "is usually the one where you risk losing something (Russia introducing unwanted "
            "language) rather than gaining something (African member support). Consider whether "
            "you can delegate any conversations to allied delegates."
        ),
        "sample_answer": (
            "Minute-by-minute plan: Minutes 1-2: Immediately approach your closest ally on the "
            "Council (e.g., the delegate of a Gulf state or another African member already "
            "supporting your position) and brief them on the Russia concern. Ask them to "
            "engage Russia in a parallel conversation about the resolution's scope, presenting "
            "arguments for keeping it narrowly focused on the Sahel. This delegates the "
            "blocking task while you focus on coalition building. Minutes 2-6: Approach the "
            "first African elected member (e.g., Mozambique or Ghana). Present your amendment "
            "on regional counter-terrorism forces: 'Egypt proposes operative language "
            "authorizing the AU-UN Hybrid Force concept for Sahel counter-terrorism operations, "
            "with logistics and funding support from assessed UN contributions.' Emphasize that "
            "this elevates African agency in Sahel security rather than relying on external "
            "powers. Secure their tentative support or identify specific concerns to address "
            "later. Minutes 6-10: Approach France. Acknowledge their withdrawal timeline "
            "concerns directly: 'Egypt's amendment on regional forces is designed precisely to "
            "fill the security gap your withdrawal creates. We are not asking France to extend "
            "its presence -- we are proposing an alternative that allows orderly transition.' "
            "Offer to include language that 'welcomes France's constructive transition planning' "
            "to give them positive recognition. Minutes 10-13: Approach the second African "
            "elected member with the same pitch, noting that the first African member and "
            "France are already on board (or close to it). Momentum matters. Minutes 13-15: "
            "Check in with your ally who was engaging Russia. If Russia has been contained, "
            "good. If Russia is still pushing expansive language, approach Russia directly "
            "with a firm but diplomatic message: 'Egypt cannot support language that broadens "
            "the resolution beyond the Sahel context. We would need to see any such proposals "
            "in writing and would require additional consultation time before the vote.'"
        ),
        "key_concepts": "caucus time management, Security Council dynamics, counter-terrorism cooperation, Sahel security, delegation of tasks, France-Africa relations, Russia containment, amendment advocacy",
    },
    # ── ADV (1/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Crisis Negotiation: Emergency Security Council Session on Nuclear Escalation",
        "prompt": (
            "You are the delegate of the United Kingdom in the Security Council. An emergency "
            "session has been called after a fictional nuclear-armed state conducted a nuclear "
            "weapons test in violation of its IAEA safeguards agreement, and satellite imagery "
            "suggests it is preparing a second test. Three neighboring states have mobilized "
            "military forces along their borders, and two of them are requesting Security "
            "Council authorization for a naval blockade.\n\n"
            "The P5 is deeply divided: the US supports the blockade, China opposes any "
            "coercive measures and threatens a veto, Russia is ambivalent but leaning toward "
            "abstention, and France is proposing a diplomatic middle ground involving enhanced "
            "IAEA inspections with a 48-hour ultimatum. You must navigate this crisis in real "
            "time.\n\n"
            "As the UK, develop a comprehensive crisis negotiation strategy that prevents "
            "both a veto (which would paralyze the Council) and a premature military "
            "authorization (which could escalate to nuclear conflict). You have 30 minutes "
            "before the vote."
        ),
        "hints": (
            "In crisis negotiations, the first priority is preventing the worst outcome "
            "(nuclear conflict), not achieving the best outcome (comprehensive disarmament). "
            "Consider procedural tools: requesting a delay, proposing a presidential statement "
            "instead of a resolution, or splitting the resolution into separate votes on "
            "different elements."
        ),
        "sample_answer": (
            "The UK's strategy must address three simultaneous crises: the nuclear test, the "
            "military mobilization, and the P5 split. Step 1 (Minutes 1-5): Propose a "
            "procedural motion to suspend the vote for one hour to allow 'intensive "
            "consultations.' If the US objects, argue that a vetoed resolution is worse than "
            "a delayed one because it signals Council dysfunction to the proliferating state. "
            "Step 2 (Minutes 5-10): Meet privately with France to refine their 48-hour "
            "ultimatum proposal. Strengthen it by adding: (a) immediate dispatch of an IAEA "
            "emergency inspection team, (b) a freeze on the proliferating state's foreign "
            "assets in Council member states, and (c) a provision that if the 48-hour deadline "
            "passes without compliance, the Council will reconvene to consider 'further "
            "measures under Chapter VII' -- without specifying blockade, leaving options open. "
            "Step 3 (Minutes 10-18): Approach China with the modified French proposal. "
            "Emphasize that this buys time and avoids the blockade authorization China opposes. "
            "Offer a critical concession: include language affirming that 'all parties should "
            "exercise maximum restraint and pursue dialogue' -- code language China uses to "
            "oppose military action. Ask China to vote yes rather than merely abstain, arguing "
            "that a unanimous Council sends a stronger deterrent signal than a divided one. "
            "Step 4 (Minutes 18-23): Approach the US. This is the hardest conversation. Argue "
            "that the 48-hour ultimatum framework achieves the same objective as immediate "
            "blockade authorization but with greater legitimacy and without risking a Chinese "
            "veto. Emphasize that 'further measures under Chapter VII' preserves the blockade "
            "option after the deadline. If the US insists on immediate blockade language, "
            "propose splitting the resolution: Resolution A (IAEA inspection + asset freeze + "
            "ultimatum) passes unanimously; Resolution B (blockade authorization) is tabled "
            "for vote after the 48-hour period if needed. Step 5 (Minutes 23-27): Approach "
            "Russia. By now, frame the emerging consensus as a done deal that Russia should "
            "join to maintain its relevance. Offer to include language on 'negotiated security "
            "guarantees' for the proliferating state, which aligns with Russia's stated "
            "preference for diplomatic solutions. Step 6 (Minutes 27-30): Circulate the final "
            "text as a UK-France joint draft, positioning both as responsible mediators. Call "
            "for an immediate vote before any delegation can reopen negotiations."
        ),
        "key_concepts": "crisis negotiation, Security Council emergency session, veto prevention, nuclear proliferation, Chapter VII, IAEA inspections, resolution splitting, 48-hour ultimatum, P5 management",
    },
    # ── ADV (2/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Hostile Bloc Dynamics and Backroom Deals on Climate Financing",
        "prompt": (
            "You are the delegate of India in the UNFCCC COP, simulated as a GA committee. "
            "Negotiations on the New Collective Quantified Goal (NCQG) for climate financing "
            "have entered their final 48 hours. India leads the Like-Minded Developing "
            "Countries (LMDC) bloc demanding $1.3 trillion annually from developed nations. "
            "The EU is offering $300 billion with conditions on transparency and governance "
            "reforms in recipient countries.\n\n"
            "The situation has become hostile. The LMDC publicly accused the EU of 'climate "
            "colonialism' in a press statement, and the EU negotiator privately told you that "
            "your bloc's rhetoric is making it politically impossible for European governments "
            "to increase their offer. The US has disengaged from formal negotiations and is "
            "conducting backroom discussions with China on a bilateral climate deal that would "
            "bypass the multilateral process.\n\n"
            "You are also receiving intelligence that Saudi Arabia, a member of your LMDC bloc, "
            "is privately negotiating with the US to secure exemptions for fossil fuel "
            "exporters in any final deal. If true, this would fundamentally undermine your "
            "bloc's negotiating position.\n\n"
            "Develop a comprehensive strategy for the final 48 hours that addresses the EU "
            "hostility, the US-China backroom threat, and the potential Saudi betrayal."
        ),
        "hints": (
            "In endgame negotiations, the biggest risk is being bypassed by a deal struck "
            "between other parties. The US-China bilateral track is the most dangerous threat "
            "because it could present a fait accompli. Address this first by making yourself "
            "indispensable to any deal. Consider whether the 'climate colonialism' rhetoric "
            "has become counterproductive and how to walk it back without appearing weak."
        ),
        "sample_answer": (
            "This is a three-front war requiring simultaneous action on hostility management, "
            "backroom neutralization, and internal cohesion. Front 1 -- EU Hostility: Issue a "
            "carefully calibrated statement that walks back the 'climate colonialism' rhetoric "
            "without appearing to concede: 'India and the LMDC reaffirm their commitment to "
            "constructive dialogue. Our frustration reflects the urgency of the climate crisis, "
            "not disrespect for our European partners. We are ready to discuss creative "
            "financing structures.' Privately approach the EU chief negotiator with a specific "
            "counter-offer: accept $300 billion in direct grants plus $500 billion in "
            "concessional finance and leveraged private investment, totaling $800 billion "
            "with a roadmap to reach $1.3 trillion by 2035. Include a governance reform "
            "provision but frame it as 'mutual accountability' applying to both donors and "
            "recipients. This gives the EU a face-saving win on governance while nearly "
            "tripling their headline number through creative accounting. Front 2 -- US-China "
            "Backroom: This is the existential threat. A bilateral US-China deal would "
            "marginalize the LMDC and the entire multilateral process. Approach China directly "
            "and immediately. Remind China that a bilateral deal with the US will set a "
            "precedent for bypassing multilateral frameworks -- a precedent that could be used "
            "against China on trade, technology, and other issues. Propose that China bring "
            "India into the backroom discussions, converting a bilateral track into a "
            "trilateral one: 'US-China-India represents 40%% of global emissions and 40%% of "
            "global population. A trilateral framework would be more legitimate and more "
            "durable.' If China refuses, signal to the US that India will publicly oppose any "
            "bilateral deal as illegitimate, reducing its political value. Front 3 -- Saudi "
            "Arabia: Do not confront Saudi Arabia publicly, as this would expose bloc "
            "divisions. Instead, create a structural incentive for loyalty. Propose within the "
            "LMDC that the bloc's final position include 'just transition support for "
            "fossil-fuel-dependent economies,' which directly serves Saudi interests better "
            "than any backroom US deal. Simultaneously, share the LMDC's revised counter-offer "
            "with all bloc members simultaneously, including Saudi Arabia, so they learn about "
            "the new position at the same time as everyone else -- this prevents them from "
            "pre-negotiating concessions with the US. Endgame: orchestrate a dramatic 'final "
            "offer' moment where India presents the $800 billion counter-proposal in formal "
            "session, putting the EU in a position where rejecting a halved demand appears "
            "unreasonable to the global audience."
        ),
        "key_concepts": "endgame negotiation, hostile bloc dynamics, backroom deal neutralization, LMDC coalition, UNFCCC COP, climate financing NCQG, internal betrayal management, multilateral vs bilateral tracks, creative financing structures",
    },
    # ── ADV (3/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "P5 Engagement Strategy on Peacekeeping Reform",
        "prompt": (
            "You are the delegate of Ethiopia in the Special Committee on Peacekeeping "
            "Operations (C-34). As one of the largest troop-contributing countries to UN "
            "peacekeeping, Ethiopia is leading a coalition demanding fundamental reforms: "
            "greater voice for TCCs in mission planning, improved equipment and logistics "
            "support, faster reimbursement for troop costs, and enhanced safety protocols "
            "after multiple casualties in recent missions.\n\n"
            "Your reform package faces a structural obstacle: the P5 members control "
            "peacekeeping mandates through the Security Council, and they are reluctant to "
            "share decision-making authority with TCCs. However, the P5 also depends on TCCs "
            "like Ethiopia to provide troops, creating mutual leverage.\n\n"
            "The US (the largest financial contributor) opposes cost increases. China (an "
            "increasingly significant TCC) might support TCC empowerment but has its own "
            "agenda for expanding Chinese influence in peacekeeping. Russia wants to reduce "
            "peacekeeping budgets overall. France wants to maintain its influence over "
            "Francophone African missions. The UK is generally supportive of reform but will "
            "not break P5 consensus.\n\n"
            "Design a P5 engagement strategy that creates enough pressure or incentive for "
            "at least three P5 members to support your reform package."
        ),
        "hints": (
            "Your strongest leverage is the implicit threat that TCCs could reduce their "
            "contributions if reforms are not implemented -- though making this threat "
            "explicit is risky. Think about how to signal this possibility without stating "
            "it directly. Consider which P5 members you need to win over (at least three) "
            "and which you can afford to lose."
        ),
        "sample_answer": (
            "The strategy requires securing three P5 members while accepting that two may "
            "remain opposed. Target the UK, France, and China as the most achievable three, "
            "accepting US and Russian opposition. UK Engagement: The UK is the easiest target. "
            "Approach them first and offer a joint sponsorship of the reform package, giving "
            "the UK leadership credit. Modify your reform language to include 'evidence-based "
            "performance assessment' for peacekeeping operations, which aligns with UK "
            "priorities for accountability. Ask the UK to present the reform as their "
            "initiative within P5 consultations, which is more effective than an external "
            "demand. France Engagement: France's interest is maintaining influence over "
            "Francophone missions. Offer a strategic concession: your reform package will "
            "include a provision for 'regional expertise consultation' that formally "
            "recognizes the role of states with historical knowledge of mission areas. This "
            "effectively preserves France's privileged advisory role in Mali, DRC, and CAR "
            "while wrapping it in neutral language. Additionally, note that Ethiopia provides "
            "troops to MINUSMA and other Francophone missions -- if TCC conditions worsen, "
            "these deployments could be reconsidered. Do not frame this as a threat; instead, "
            "explain that 'domestic political pressure on casualties without adequate support "
            "may constrain future deployment decisions.' China Engagement: China's growing "
            "TCC role gives it genuine interest in TCC empowerment, but China also uses "
            "peacekeeping to expand global influence. Offer to support China's proposal for "
            "a peacekeeping training center under Chinese leadership, in exchange for China's "
            "support of the broader TCC reform package. Frame TCC empowerment as a precedent "
            "that benefits China's long-term peacekeeping strategy. Managing the US: Accept "
            "that the US will oppose cost increases. Mitigate by reframing financial reforms "
            "as 'cost efficiency through better planning' rather than budget increases. Include "
            "data showing that inadequate equipment leads to mission failures that cost more "
            "than preventive investment. Managing Russia: Russia's opposition to peacekeeping "
            "expansion is ideological. Do not invest significant negotiation capital here. "
            "Instead, include a clause on 'mission mandate review and streamlining' that gives "
            "Russia a face-saving element to point to. Implicit Leverage: Throughout all "
            "engagements, have the TCC coalition issue a joint statement expressing 'concern "
            "about the sustainability of current deployment models without systemic reform.' "
            "This signals the possibility of reduced contributions without making an explicit "
            "threat that could damage diplomatic relationships."
        ),
        "key_concepts": "P5 engagement, peacekeeping reform, TCC empowerment, C-34, implicit leverage, troop reimbursement, mission planning authority, P5 consensus dynamics, strategic concessions",
    },
    # ── ADV (4/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Coalition Fracture Management During Sanctions Negotiations",
        "prompt": (
            "You are the delegate of Nigeria in the Security Council. Your African coalition "
            "of three elected Council members (Nigeria, South Africa, and Kenya) has been "
            "negotiating jointly on a sanctions resolution targeting an African state accused "
            "of harboring terrorist groups. The coalition's unified position -- supporting "
            "targeted sanctions with humanitarian exemptions and a sunset clause -- gave you "
            "significant influence as a voting bloc.\n\n"
            "The coalition has now fractured. South Africa has been approached by China with "
            "an offer: if South Africa opposes the sanctions resolution, China will support "
            "South Africa's candidacy for a permanent Security Council seat in upcoming reform "
            "discussions. Kenya has been pressured by the US to support a stronger sanctions "
            "package without humanitarian exemptions, with the implicit threat that US "
            "development aid could be reconsidered.\n\n"
            "You are left holding the original coalition position alone. The vote is in six "
            "hours. How do you manage this coalition fracture, attempt to reunify your bloc, "
            "and protect Nigeria's interests regardless of whether reunification succeeds?"
        ),
        "hints": (
            "When a coalition fractures due to external incentives (Chinese seat promises, US "
            "aid threats), you cannot simply appeal to solidarity -- you must offer concrete "
            "counter-incentives or change the calculation. Consider whether the P5 promises "
            "are credible and help your allies see through them. Also prepare for the "
            "possibility that reunification fails and you must act independently."
        ),
        "sample_answer": (
            "Six-hour timeline requires parallel action tracks. Hour 1-2 -- Intelligence and "
            "Assessment: Verify the reported deals. Meet separately with South Africa and "
            "Kenya in one-on-one private conversations, not together (a group meeting would "
            "force public positions). With South Africa, probe: 'I have heard concerns that "
            "external factors may be influencing our coalition's position. Can we discuss "
            "your current thinking candidly?' If the China deal is confirmed, challenge its "
            "credibility: 'China's promise of Security Council reform support is contingent "
            "on reform actually happening, which requires Charter amendment and two-thirds GA "
            "majority. This is a promise China cannot unilaterally deliver. Our coalition's "
            "influence on this sanctions vote is real and immediate.' With Kenya, address the "
            "US pressure: 'If the US is conditioning development aid on Security Council "
            "votes, this is a form of coercion that undermines the sovereign independence of "
            "elected Council members. We should raise this concern with the Non-Aligned "
            "Movement.' Offer to publicly support Kenya against any retaliatory aid "
            "reductions. Hour 2-4 -- Coalition Repair: If South Africa and Kenya show "
            "willingness to re-engage, propose a modified coalition position that gives each "
            "partner something to take back to their external interlocutors. For South Africa: "
            "include language in the resolution that 'calls for comprehensive Security Council "
            "reform including expanded African representation,' which South Africa can present "
            "to China as a partial win. For Kenya: accept slightly stronger sanctions language "
            "(removing one humanitarian exemption for non-essential goods) that Kenya can "
            "present to the US as a harder stance. The modified position is weaker than the "
            "original but preserves coalition unity. Hour 4-5 -- Contingency Planning: If "
            "reunification fails, Nigeria must act independently. Approach France and the UK "
            "as alternative partners. Nigeria's vote is valuable -- offer to support the "
            "resolution with Nigeria's preferred humanitarian exemptions in exchange for UK/"
            "France backing a Nigerian amendment. Draft the amendment text in advance so it is "
            "ready to circulate. Hour 5-6 -- Final Positioning: Regardless of coalition "
            "status, deliver a strong statement in the final consultations before the vote "
            "that frames Nigeria's position as principled and forward-looking: 'Nigeria "
            "supports accountability for terrorist harboring while insisting that sanctions "
            "must not become collective punishment of innocent civilians. This is not a "
            "position of weakness but of moral clarity.' This positions Nigeria for post-vote "
            "diplomatic capital regardless of the outcome."
        ),
        "key_concepts": "coalition fracture management, external incentives, P5 deal-making, Security Council elected members, African Group dynamics, counter-incentives, contingency planning, sanctions with humanitarian exemptions, coalition repair",
    },
    # ── ADV (5/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Backroom Deal Architecture on Trade War De-Escalation",
        "prompt": (
            "You are the delegate of Japan in ECOFIN. The committee is debating a resolution "
            "on de-escalating trade wars and reforming the WTO dispute settlement mechanism. "
            "Formal negotiations have stalled because the US and China are using the committee "
            "as a proxy for their bilateral trade conflict, with each side introducing "
            "amendments designed to embarrass the other.\n\n"
            "You have identified an opportunity for a backroom deal. Both the US and China "
            "privately want the WTO Appellate Body restored (it has been non-functional since "
            "2019), but neither will make the first public move because it would be perceived "
            "as a concession. Several middle-power delegates (Japan, Australia, Brazil, India, "
            "EU members) share the interest in Appellate Body restoration.\n\n"
            "Design a backroom negotiation strategy that: (1) creates a face-saving mechanism "
            "for both the US and China to support Appellate Body restoration, (2) prevents "
            "either side from claiming victory, (3) keeps the deal invisible to the formal "
            "committee until it is ready to be unveiled, and (4) positions Japan as the "
            "architect of the breakthrough."
        ),
        "hints": (
            "Backroom deals require plausible deniability for all parties until the deal is "
            "announced. Consider using a 'friends of the chair' mechanism or an informal "
            "working group as cover for the backroom discussions. The key to face-saving is "
            "creating a narrative where both sides can claim the final outcome reflects their "
            "position."
        ),
        "sample_answer": (
            "Phase 1 -- Creating the Cover Structure (Day 1): Ask the committee chair to "
            "establish an informal 'Friends of the Chair' working group on WTO reform, "
            "consisting of eight middle-power delegates: Japan, Australia, Brazil, India, "
            "Germany, Mexico, South Korea, and Nigeria. This group provides legitimate cover "
            "for intensive negotiations outside the formal committee. Critically, neither the "
            "US nor China is a member, which gives them deniability ('we did not negotiate "
            "this -- the working group proposed it'). Phase 2 -- Parallel Backchannels (Days "
            "1-2): While the working group meets formally on general WTO reform, conduct "
            "private bilateral meetings with the US and China separately. Never bring them "
            "into the same room until the deal is ready. With the US: 'Japan's working group "
            "is drafting Appellate Body reform language that addresses your concerns about "
            "judicial overreach. We propose term limits for Appellate Body members, a "
            "clarified standard of review that limits the Body to legal interpretation rather "
            "than factual findings, and a sunset provision requiring reauthorization every "
            "five years.' These are genuine US concerns wrapped in Japan's initiative. With "
            "China: 'Japan's working group is drafting language that restores the rules-based "
            "trading system and prevents unilateral tariff actions outside WTO frameworks. "
            "The restored Appellate Body would have jurisdiction to review the legality of "
            "unilateral tariffs.' This frames restoration as a check on US protectionism, "
            "which China wants. Phase 3 -- Convergence (Day 2-3): After receiving feedback "
            "from both sides, draft a single text that incorporates both sets of modifications. "
            "The genius of the deal: the US-demanded reforms (term limits, limited scope) "
            "actually make the Appellate Body more acceptable to developing nations who have "
            "their own concerns about judicial overreach. Share the draft with working group "
            "members for refinement and broad co-sponsorship. Phase 4 -- The Reveal (Day 3): "
            "Have the working group present the draft as a 'consensus proposal from the "
            "Friends of the Chair' in formal session. Japan introduces it, surrounded by "
            "seven co-sponsors representing every region. The US and China, having already "
            "approved the language privately, express 'willingness to consider this "
            "constructive proposal' -- both can claim they are responding to middle-power "
            "initiative rather than making concessions to each other. Neither claims victory "
            "because the deal is attributed to Japan's working group, not to US-China "
            "bilateral compromise."
        ),
        "key_concepts": "backroom deal architecture, face-saving mechanisms, WTO Appellate Body, Friends of the Chair, plausible deniability, parallel backchannel negotiation, middle-power brokerage, trade war de-escalation",
    },
    # ── ADV (6/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Crisis Coalition Building During a Humanitarian Emergency Debate",
        "prompt": (
            "You are the delegate of Brazil in an emergency special session of the UN General "
            "Assembly. A humanitarian catastrophe is unfolding in a fictional state: massive "
            "internal displacement, allegations of ethnic cleansing, and a government blocking "
            "humanitarian access. The Security Council is deadlocked by a P5 veto, and the "
            "General Assembly has been convened under the 'Uniting for Peace' resolution.\n\n"
            "You need to build a coalition of 97 votes (two-thirds majority) to pass a "
            "resolution that: (1) demands immediate humanitarian access, (2) establishes an "
            "independent investigation commission, (3) recommends targeted sanctions against "
            "regime officials, and (4) refers the situation to the International Criminal "
            "Court. Each of these elements has different levels of support, and some delegates "
            "will only vote yes if certain elements are removed.\n\n"
            "Current vote count estimates: Element 1 (humanitarian access) has ~140 votes. "
            "Element 2 (investigation commission) has ~120 votes. Element 3 (targeted "
            "sanctions) has ~95 votes. Element 4 (ICC referral) has ~70 votes.\n\n"
            "How do you structure the resolution and negotiation to maximize the strength of "
            "the final outcome?"
        ),
        "hints": (
            "Consider whether a single resolution with all four elements is the best strategy, "
            "or whether splitting into multiple resolutions allows you to pass the strongest "
            "possible combination. Think about amendment-proofing your resolution and the risk "
            "that hostile amendments could strip elements before the final vote."
        ),
        "sample_answer": (
            "The vote-count analysis reveals a critical problem: a single resolution with all "
            "four elements would likely fail because Element 4 (ICC referral at ~70 votes) "
            "drags the package below the two-thirds threshold. Delegates who support "
            "humanitarian access but oppose ICC referral would vote against the entire package. "
            "Strategic Architecture: Split the content into two resolutions plus a presidential "
            "statement. Resolution A ('Humanitarian Protection'): Combines Elements 1 and 2 -- "
            "humanitarian access demand and investigation commission. These have 140 and 120 "
            "votes respectively; together, the package should clear 115+ votes comfortably. "
            "Draft this as the lead resolution with Brazil as primary sponsor. Include strong "
            "operative language on humanitarian corridors, a 72-hour compliance deadline, and "
            "a mandate for the investigation commission to report within 90 days. Resolution "
            "B ('Accountability Framework'): Contains Element 3 -- targeted sanctions "
            "recommendations. With ~95 estimated votes, this is close to the 97 threshold but "
            "not certain. Focus all negotiation energy on securing the marginal 5-10 votes. "
            "Target African Group and Caribbean Community (CARICOM) delegates who may be "
            "undecided. Modify the sanctions to focus narrowly on individuals (travel bans, "
            "asset freezes) rather than sector-wide measures, which may attract cautious "
            "delegates. Include a sunset clause that automatically lifts sanctions after 12 "
            "months unless renewed. Element 4 (ICC Referral): Do not include in either "
            "resolution. Instead, have a friendly delegation introduce the ICC referral "
            "language as a separate resolution to be considered at a subsequent session, after "
            "the investigation commission has reported. This is strategically superior because: "
            "(a) it does not drag down the other elements; (b) the investigation commission's "
            "findings will strengthen the case for ICC referral when it is eventually proposed; "
            "(c) it creates sustained pressure on the regime across multiple sessions rather "
            "than a single vote. Amendment Defense: Anticipate that allies of the target state "
            "will propose hostile amendments to weaken the resolutions. Prepare friendly "
            "amendments that pre-empt hostile ones -- for example, add 'urges all parties to "
            "cooperate with international humanitarian law' before opponents can introduce "
            "'calls upon all parties to respect sovereignty' language. Coordinate a voting "
            "bloc of 100+ delegates committed to voting against any hostile amendment, making "
            "their introduction futile. Coalition Management: Assign regional coordinators -- "
            "Brazil handles Latin America, a co-sponsor handles Africa, another handles Asia "
            "-- to whip votes in parallel. Hold a pre-vote coalition meeting to share the "
            "final text, address last-minute concerns, and ensure all 97+ delegates are "
            "physically present for the vote (absenteeism is a real risk in large GA sessions)."
        ),
        "key_concepts": "crisis coalition building, Uniting for Peace resolution, vote-count strategy, resolution splitting, amendment defense, ICC referral strategy, humanitarian access, two-thirds majority, emergency special session, sequential escalation",
    },
    # ── ADV (7/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Managing a Three-Way Deadlock on Economic Sanctions Reform",
        "prompt": (
            "You are the delegate of Mexico in the Sixth Committee (Legal). A contentious "
            "debate on the legal framework for unilateral economic sanctions has produced a "
            "three-way deadlock with no clear path to resolution.\n\n"
            "Position A (US, EU, Japan, Australia): Unilateral sanctions are a legitimate tool "
            "of foreign policy, protected by state sovereignty, and should not be subject to "
            "international legal constraints beyond existing jus cogens norms. Position B "
            "(Russia, China, Iran, Venezuela): Unilateral sanctions are illegal under "
            "international law, constitute economic coercion, and should be prohibited except "
            "when authorized by the Security Council. Position C (Mexico, Brazil, India, South "
            "Africa, Indonesia): Some unilateral sanctions may be legitimate but require "
            "guardrails -- humanitarian exemptions must be mandatory, secondary sanctions "
            "(targeting third-party states) should be prohibited, and affected states should "
            "have access to an adjudication mechanism.\n\n"
            "You lead Position C, which occupies the middle ground. Both sides are trying to "
            "pull you toward their position, and your coalition risks splitting if you lean "
            "too far in either direction. Design a strategy that leverages your middle "
            "position to achieve a meaningful outcome."
        ),
        "hints": (
            "The middle position in a three-way deadlock has structural power: neither extreme "
            "can win without your votes. But this power is fragile -- if your coalition splits, "
            "you become irrelevant. Focus on keeping your coalition united by identifying the "
            "one or two provisions that all five members agree on and making those the "
            "non-negotiable core of your position."
        ),
        "sample_answer": (
            "The strategic challenge is converting positional power (being in the middle) into "
            "substantive outcomes (actual legal guardrails on sanctions). Step 1 -- Coalition "
            "Hardening: Before engaging either extreme, convene Position C members for an "
            "intensive internal negotiation to identify true red lines. All five members "
            "likely agree on two points: (a) secondary sanctions are illegitimate because "
            "they coerce sovereign third parties, and (b) humanitarian exemptions for food, "
            "medicine, and essential services are non-negotiable. Declare these two points "
            "as the coalition's 'floor' -- any final outcome must include both. Publish a "
            "joint Position C statement formally, creating a public commitment that makes "
            "defection costly for individual members. Step 2 -- Structured Engagement with "
            "Position A: Position A is more likely to accept limited concessions than Position "
            "B, which is ideologically committed to prohibiting all unilateral sanctions. "
            "Approach the US privately: 'Mexico's coalition can support language preserving "
            "the right to unilateral sanctions, but only with mandatory humanitarian "
            "exemptions and a prohibition on secondary sanctions. Without these guardrails, "
            "we will align with Position B on a prohibition resolution.' This is a credible "
            "threat because Position B + Position C constitutes a majority in the GA. The "
            "US has more to lose from a prohibition resolution (even a non-binding one) than "
            "from accepting humanitarian exemptions. Approach the EU separately, noting that "
            "several EU members have already implemented humanitarian exemptions in their "
            "national sanctions regimes, making international standards consistent with "
            "existing practice. Step 3 -- Managed Engagement with Position B: Position B "
            "will not accept any outcome that legitimizes unilateral sanctions. However, you "
            "can secure their abstention rather than opposition by including their preferred "
            "language in preambular clauses: 'Reaffirming that sanctions authorized by the "
            "Security Council under Chapter VII remain the primary multilateral sanctions "
            "mechanism.' This does not prohibit unilateral sanctions but elevates the Security "
            "Council pathway, which Position B wants. Russia and China may abstain if the "
            "preambular language serves their narrative. Step 4 -- Draft the Compromise: "
            "Table a resolution with three operative sections. Section 1: Affirms the "
            "obligation of all states imposing unilateral economic measures to ensure "
            "humanitarian exemptions for food, medicine, essential services, and humanitarian "
            "organizations. Section 2: Declares that secondary sanctions -- extraterritorial "
            "application of one state's sanctions to third-party states and their nationals "
            "-- are inconsistent with state sovereignty and international trade law. Section "
            "3: Requests the International Law Commission to study the legality and "
            "appropriate guardrails for unilateral economic measures and report to the GA "
            "within two years. This gives Position A a win (unilateral sanctions are not "
            "prohibited), gives Position C their two guardrails (humanitarian exemptions and "
            "secondary sanctions prohibition), and gives Position B the ILC study (which may "
            "eventually support their prohibition argument). The ILC referral also defers the "
            "hardest question, buying time for all sides."
        ),
        "key_concepts": "three-way deadlock, middle-power leverage, unilateral sanctions, secondary sanctions, humanitarian exemptions, coalition hardening, credible threats, ILC referral, Sixth Committee, structured engagement",
    },
    # ── ADV (8/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Navigating P5 Rivalries in a Security Council Draft on Cyber Warfare Norms",
        "prompt": (
            "You are the delegate of the Philippines, serving as an elected member of the "
            "Security Council. A draft resolution on establishing norms for state behavior in "
            "cyberspace has been proposed, and it has become entangled in P5 rivalries.\n\n"
            "The US wants the resolution to condemn state-sponsored cyberattacks on critical "
            "infrastructure and establish an attribution mechanism. Russia and China want the "
            "resolution to affirm state sovereignty over domestic internet governance and "
            "reject external interference in national cyber policy. France wants to include "
            "provisions on protecting civilian infrastructure during armed conflict. The UK "
            "wants to link cyber norms to existing international humanitarian law.\n\n"
            "Each P5 member has privately told you that they will veto the resolution if it "
            "includes the other side's preferred language. The committee president has asked "
            "the Philippines to serve as the pen-holder for a revised draft.\n\n"
            "As pen-holder, design a draft resolution that navigates these contradictions and "
            "has a realistic chance of avoiding all five potential vetoes."
        ),
        "hints": (
            "The pen-holder role gives you significant structural power -- you control the "
            "text. Use ambiguous language strategically: phrases that each side can interpret "
            "as supporting their position. Consider whether some issues should be deliberately "
            "omitted from the resolution (addressed in a future session) to avoid triggering "
            "vetoes. Remember that a weak resolution that passes unanimously may be more "
            "valuable than a strong resolution that is vetoed."
        ),
        "sample_answer": (
            "As pen-holder, the Philippines controls the text and the narrative. The key "
            "insight is that each P5 member's veto threat is conditional on specific language "
            "being included -- therefore, the draft must include no language that any P5 "
            "member explicitly rejects while still creating a meaningful normative framework. "
            "Drafting Strategy -- Constructive Ambiguity: Preambular Clauses: Include "
            "language from both sides without operationalizing either. PP1: 'Reaffirming "
            "that international law, including the Charter of the United Nations, is "
            "applicable to state conduct in cyberspace' -- the UK/France position, but "
            "stated as a reaffirmation rather than a new obligation. PP2: 'Recognizing the "
            "sovereign right of states to govern information and communications technology "
            "within their territory in accordance with international law' -- the Russia/China "
            "position, but qualified by 'in accordance with international law,' which the "
            "US/UK will read as a limitation. Operative Section 1 -- Norms of Behavior: "
            "'Calls upon all states to refrain from knowingly conducting or knowingly "
            "supporting ICT activities that intentionally damage critical infrastructure "
            "providing essential services to the civilian population.' This addresses US "
            "concerns about cyberattacks on infrastructure without using the word "
            "'condemn' (which Russia would veto) or establishing attribution mechanisms "
            "(which China opposes). The word 'knowingly' provides plausible deniability "
            "that all P5 members require. Operative Section 2 -- IHL Application: "
            "'Affirms that the principles of distinction, proportionality, and precaution "
            "apply to state conduct in cyberspace during armed conflict.' This satisfies "
            "France and the UK by linking cyber norms to existing IHL. Russia may accept "
            "this because it only applies 'during armed conflict' -- not to peacetime "
            "cyber operations, which is where most state-sponsored activity occurs. "
            "Operative Section 3 -- Cooperation Framework: 'Establishes an Open-Ended "
            "Working Group to develop consensus recommendations on responsible state "
            "behavior in cyberspace, confidence-building measures, and capacity-building "
            "for developing states.' This defers the hardest decisions (attribution, "
            "sovereignty boundaries) to a future process while creating an institutional "
            "framework. Both sides can claim the OEWG will eventually validate their "
            "position. What is Deliberately Omitted: No attribution mechanism (US wants "
            "it, China/Russia will veto it). No affirmation of internet sovereignty as "
            "overriding international obligations (Russia/China want it, US/UK will veto "
            "it). No specific condemnation of any state or category of state behavior. "
            "No enforcement mechanism. Selling the Draft: Present it to each P5 member "
            "separately, emphasizing different elements. To the US: 'This is the first "
            "Security Council resolution affirming that IHL applies in cyberspace -- a "
            "principle the US has championed.' To Russia/China: 'This resolution explicitly "
            "recognizes cyber sovereignty -- the first Security Council text to do so.' "
            "To France/UK: 'This establishes that distinction and proportionality apply to "
            "cyber operations -- a landmark for humanitarian law.' Each characterization is "
            "accurate but emphasizes different aspects, allowing each P5 member to claim "
            "the resolution as their win."
        ),
        "key_concepts": "pen-holder strategy, constructive ambiguity, P5 veto navigation, cyber warfare norms, IHL in cyberspace, OEWG, sovereignty vs international law, critical infrastructure protection, Security Council drafting",
    },
    # ── ADV (9/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Endgame Negotiation on a Comprehensive Nuclear Test Ban Verification Protocol",
        "prompt": (
            "You are the delegate of Germany in the Conference on Disarmament (CD), simulated "
            "as a DISEC session. After years of deadlock, a comprehensive nuclear test ban "
            "treaty verification protocol is finally being negotiated. You are in the final "
            "48 hours before the treaty text must be finalized.\n\n"
            "Five critical issues remain unresolved: (1) On-site inspection rights -- how much "
            "notice is required and can inspections be refused? (2) National technical means -- "
            "can satellite intelligence be used as evidence of violations? (3) Dispute "
            "resolution -- ICJ jurisdiction or a treaty-specific arbitration body? (4) "
            "Withdrawal clause -- conditions and notice period for treaty withdrawal. (5) "
            "Entry into force -- which states must ratify before the treaty takes effect?\n\n"
            "You know that the US insists on short-notice inspections and NTM evidence use. "
            "Russia insists on the right to refuse inspections and opposes NTM evidence. China "
            "wants a long withdrawal notice period (24 months) and opposes ICJ jurisdiction. "
            "India (a non-signatory to the NPT) wants the entry-into-force provision to not "
            "require its ratification. Pakistan mirrors India's position.\n\n"
            "Design an endgame negotiation strategy for resolving all five issues in 48 hours."
        ),
        "hints": (
            "In endgame negotiations, linkage is your most powerful tool. Issues that are "
            "impossible to resolve in isolation can be resolved as part of a package deal "
            "where each party wins on their priority issue and concedes on others. Identify "
            "each party's priority issue (the one they care about most) and their tradeable "
            "issue (the one they would concede if they win their priority)."
        ),
        "sample_answer": (
            "The five issues cannot be resolved sequentially -- they must be linked in a "
            "grand bargain where each major party wins on their priority issue. Map the "
            "priorities: US priority: NTM evidence and inspection access. US tradeable: "
            "withdrawal clause and entry into force. Russia priority: Inspection refusal "
            "rights. Russia tradeable: NTM evidence (if limited). China priority: No ICJ "
            "jurisdiction. China tradeable: Withdrawal notice period (if sovereignty is "
            "protected). India/Pakistan priority: Entry into force without their required "
            "ratification. Tradeable: Most other issues (they want to stay outside the "
            "treaty). Grand Bargain Architecture: Issue 1 -- Inspections: Propose a "
            "'managed access' compromise used successfully in the Chemical Weapons "
            "Convention. On-site inspections are permitted with 48-hour notice (shorter than "
            "Russia wants, longer than the US wants). The inspected state can propose "
            "alternative arrangements to protect sensitive national security information "
            "unrelated to the treaty, but cannot outright refuse the inspection. An "
            "independent Technical Secretariat evaluates whether alternative arrangements "
            "satisfy inspection objectives. This gives Russia a mechanism to manage access "
            "without a blanket refusal right, and gives the US functional inspection access. "
            "Issue 2 -- NTM Evidence: Allow NTM data as 'supplementary information' that "
            "can trigger a consultation process and potentially an on-site inspection, but "
            "not as standalone evidence of violation for purposes of sanctions or enforcement. "
            "This gives the US a pathway from satellite data to inspections while preventing "
            "Russia's fear that NTM data alone could be used for political accusations. "
            "Issue 3 -- Dispute Resolution: Reject ICJ jurisdiction (China's priority win) "
            "and establish a treaty-specific Verification and Compliance Body with technical "
            "experts appointed by consensus of treaty parties. Disputes unresolved by this "
            "body can be escalated to the Security Council. This satisfies China while giving "
            "Western states an enforcement pathway. Issue 4 -- Withdrawal: Set a 12-month "
            "notice period (compromising between China's 24 months and the US preference for "
            "shorter periods), with mandatory consultation with all treaty parties and the "
            "Security Council during the notice period. Include a clause that withdrawal "
            "does not relieve obligations for activities conducted while the state was party "
            "to the treaty. Issue 5 -- Entry into Force: Do not require specific named states "
            "to ratify (India/Pakistan's win). Instead, require ratification by 44 states "
            "possessing nuclear power or research reactors, using a formula that technically "
            "includes India and Pakistan but does not name them, and that allows the treaty "
            "to enter into force without universal participation if a critical mass (e.g., "
            "40 of 44) ratifies. Presentation: Present the five-issue package as a 'single "
            "text' -- all issues rise or fall together. Do not allow cherry-picking. Schedule "
            "bilateral consultations with each major party in four-hour blocks over the 48 "
            "hours: US (hours 0-4), Russia (4-8), China (8-12), India/Pakistan (12-16), "
            "with hours 16-48 reserved for three rounds of plenary refinement and final "
            "adoption."
        ),
        "key_concepts": "endgame negotiation, grand bargain linkage, CTBT verification, managed access inspections, NTM evidence, treaty withdrawal clauses, entry into force, Conference on Disarmament, single-text negotiation, CWC precedent",
    },
    # ── ADV (10/10) ──
    {
        "category_type": "NEGOTIATION",
        "difficulty": "ADV",
        "title": "Orchestrating a Multi-Committee Negotiation on AI and Autonomous Weapons",
        "prompt": (
            "You are the delegate of Colombia at a large MUN conference where three committees "
            "are simultaneously addressing overlapping aspects of artificial intelligence "
            "governance. DISEC is negotiating autonomous weapons regulation. ECOFIN is "
            "negotiating AI and economic development. The HRC is negotiating AI and human "
            "rights. The conference rules allow joint sessions and cross-committee resolutions "
            "by mutual agreement of chairs.\n\n"
            "You have identified a strategic opportunity: the three committees are working at "
            "cross purposes. DISEC is moving toward strict AI regulation that could stifle the "
            "economic development ECOFIN wants to promote. The HRC is developing human rights "
            "standards that conflict with both DISEC's security-focused approach and ECOFIN's "
            "development-focused approach. If left uncoordinated, the three committees will "
            "produce contradictory resolutions.\n\n"
            "Colombia has delegations in all three committees. Design a cross-committee "
            "negotiation strategy that unifies the three workstreams into a coherent framework, "
            "positions Colombia as the architect of a landmark multi-committee resolution, and "
            "manages the political dynamics of chairs, blocs, and competing national interests "
            "across all three committees simultaneously."
        ),
        "hints": (
            "Cross-committee negotiation is the most complex form of MUN diplomacy. You need "
            "to coordinate your own delegation across three rooms, align with different "
            "allies in each committee, and convince three committee chairs to agree to a "
            "joint session. Start by mapping the contradictions between the three committees' "
            "draft texts and show each chair why coordination serves their committee's goals."
        ),
        "sample_answer": (
            "This requires a four-phase strategy executed simultaneously across three "
            "committees. Phase 1 -- Internal Coordination (Hours 1-3): Convene Colombia's "
            "three committee delegations for an emergency strategy session. Map the current "
            "draft texts from all three committees and identify specific contradictions: "
            "DISEC's draft may ban AI systems that ECOFIN's draft promotes for economic "
            "development; HRC's human rights standards may conflict with DISEC's exception "
            "for military AI; ECOFIN's deregulation language may undermine HRC's algorithmic "
            "accountability provisions. Create a unified Colombian position paper proposing a "
            "'Comprehensive AI Governance Framework' with three tiers: Tier 1 (universal "
            "principles applicable to all AI systems -- transparency, accountability, "
            "non-discrimination), Tier 2 (sector-specific regulations for military, economic, "
            "and social AI applications), and Tier 3 (implementation mechanisms differentiated "
            "by development level). Phase 2 -- Chair Engagement (Hours 3-6): Approach each "
            "committee chair separately with a tailored pitch. DISEC chair: 'Your committee's "
            "autonomous weapons resolution will be undermined if ECOFIN passes a competing "
            "resolution promoting unrestricted AI development. A joint resolution would give "
            "DISEC's security provisions broader legitimacy.' ECOFIN chair: 'DISEC is about "
            "to pass restrictions that could cripple AI-driven economic development in your "
            "committee's target countries. A coordinated approach lets ECOFIN protect "
            "development interests within a shared framework.' HRC chair: 'Neither DISEC "
            "nor ECOFIN is adequately addressing human rights -- a joint session ensures "
            "your committee's work is not sidelined.' Each chair's incentive is that a "
            "multi-committee resolution is a legacy achievement for their leadership. "
            "Phase 3 -- Cross-Committee Coalition Building (Hours 6-18): This is the most "
            "labor-intensive phase. In each committee, identify the key blocs and map their "
            "cross-committee positions. The EU likely supports regulation in all three "
            "committees -- recruit them as the co-sponsor for the joint resolution. China "
            "likely opposes strict regulation in DISEC but supports development in ECOFIN "
            "and sovereignty in HRC -- offer to include 'respect for national AI development "
            "strategies' language that satisfies their concerns across all three workstreams. "
            "The US likely supports military AI flexibility in DISEC, economic deregulation "
            "in ECOFIN, and selective human rights provisions in HRC -- offer Tier 2 sector-"
            "specific regulations that are less restrictive for military and economic "
            "applications than Tier 1 universal principles, giving the US differentiated "
            "treatment where it matters most to them. Key: use different allies as lead "
            "negotiators in each committee. In DISEC, partner with Japan (military tech "
            "balance). In ECOFIN, partner with India (development focus). In HRC, partner "
            "with South Africa (human rights credibility). Phase 4 -- Joint Session and "
            "Final Text (Hours 18-24): Once chairs agree to a joint session, present the "
            "Comprehensive Framework as a Colombia-led draft with co-sponsors from all "
            "three committees. The joint session should be structured with three segments: "
            "(1) presentation of the framework, (2) committee-specific breakout sessions to "
            "refine Tier 2 provisions, and (3) a reconvened plenary for final adoption. "
            "Colombia chairs the plenary segments as the proposing delegation, controlling "
            "the pace and preventing any single bloc from derailing the process. The final "
            "text should be a framework convention -- setting principles and mechanisms "
            "without resolving every detail -- allowing each committee to continue developing "
            "sector-specific provisions within the agreed architecture."
        ),
        "key_concepts": "cross-committee negotiation, multi-committee resolution, AI governance framework, tiered regulation, chair engagement, conference-level strategy, joint sessions, framework convention, Colombia bridge-building, simultaneous multi-front diplomacy",
    },
]

# ── RESEARCH QUESTIONS ────────────────────────────────────────────────────────
QUESTIONS += [
    # ── BEGINNER (10) ────────────────────────────────────────────────────────
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Researching Your Assigned Country",
        "prompt": (
            "You have been assigned to represent India in the United Nations General Assembly "
            "Third Committee (SOCHUM). The topic is 'Combating Human Trafficking and Modern Slavery.'\n\n"
            "As a first step in your preparation, you need to conduct basic country research. "
            "Create a one-page country profile for India that covers the following areas:\n\n"
            "1. Basic facts: population, GDP, government type, and major religions\n"
            "2. India's relationship with human trafficking — is it a source, transit, or destination country?\n"
            "3. Key domestic laws India has passed to address trafficking\n"
            "4. India's position on international treaties related to trafficking (e.g., the Palermo Protocol)\n"
            "5. India's key allies and regional partners on this issue\n\n"
            "Your profile should be approximately 300-400 words and written in a neutral, factual tone. "
            "This is not an opinion piece — it is a research document that will inform your position paper."
        ),
        "hints": (
            "Start with the CIA World Factbook or UN Data for basic country statistics;"
            "Check the US State Department's Trafficking in Persons (TIP) Report for India's tier ranking;"
            "Look at India's ratification status of the UN Convention against Transnational Organized Crime;"
            "Note any reservations India has made to relevant treaties"
        ),
        "sample_answer": (
            "A strong country profile would include India's population (~1.4 billion), federal parliamentary "
            "republic structure, and status as a source, destination, and transit country for trafficking. "
            "It would reference the Immoral Traffic Prevention Act (ITPA), India's ratification of SAARC "
            "conventions, and partnerships with Bangladesh and Nepal on cross-border trafficking."
        ),
        "key_concepts": "country research, country profile, human trafficking, Palermo Protocol, factual tone",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Finding UN Voting Records",
        "prompt": (
            "You are preparing to represent South Africa in the General Assembly First Committee (DISEC). "
            "The topic is 'Nuclear Disarmament and Non-Proliferation.'\n\n"
            "Your MUN advisor has asked you to research how South Africa has voted on key nuclear "
            "disarmament resolutions over the past decade. This will help you understand your country's "
            "consistent positions and any shifts in policy.\n\n"
            "Write a short research brief (250-350 words) that:\n"
            "1. Explains where to find official UN voting records (name the specific database)\n"
            "2. Summarizes South Africa's general voting pattern on nuclear disarmament resolutions\n"
            "3. Notes South Africa's unique history as a country that voluntarily dismantled its nuclear "
            "weapons program\n"
            "4. Identifies at least two specific resolutions or treaties relevant to this topic\n\n"
            "This exercise teaches you how to use primary UN sources to back up your country's positions."
        ),
        "hints": (
            "The UN Digital Library (digitallibrary.un.org) contains voting records;"
            "South Africa dismantled six nuclear warheads in 1989 — this is central to its credibility;"
            "Look at the Treaty on the Prohibition of Nuclear Weapons (TPNW) and the NPT;"
            "South Africa is part of the African Nuclear-Weapon-Free Zone (Treaty of Pelindaba)"
        ),
        "sample_answer": (
            "A good brief would identify the UN Digital Library and UN Bibliographic Information System as "
            "primary sources, note South Africa's consistent yes votes on disarmament resolutions, highlight "
            "its unique moral authority from voluntary denuclearization, and reference both the NPT and TPNW."
        ),
        "key_concepts": "UN voting records, UN Digital Library, nuclear disarmament, NPT, TPNW, South Africa",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Understanding Position Paper Structure",
        "prompt": (
            "You are representing Mexico in the Economic and Social Council (ECOSOC). The topic is "
            "'Reducing Income Inequality in Developing Nations.'\n\n"
            "Your conference requires a position paper submission. You have never written one before. "
            "Using the standard three-section position paper format, write a brief outline (not the full "
            "paper) that includes:\n\n"
            "1. SECTION 1 — Background: List 3-4 bullet points of facts you would include about income "
            "inequality globally and in Mexico specifically\n"
            "2. SECTION 2 — Country Position: List 2-3 bullet points describing Mexico's stance on income "
            "inequality, including relevant domestic programs\n"
            "3. SECTION 3 — Proposed Solutions: List 2-3 bullet points of solutions Mexico would support "
            "in committee\n\n"
            "For each bullet point, write 1-2 sentences. The entire outline should be 250-350 words. "
            "This exercise focuses on understanding the structure, not writing perfect prose."
        ),
        "hints": (
            "Position papers always follow: Background → Country Position → Solutions;"
            "Mexico's PROGRESA/Oportunidades/Prospera program is a well-known anti-poverty initiative;"
            "Use the Gini coefficient to discuss inequality levels;"
            "Solutions should be realistic and align with what Mexico has already supported internationally"
        ),
        "sample_answer": (
            "A solid outline would include global Gini data in the background, reference Mexico's conditional "
            "cash transfer programs (Prospera) in the country position, and propose South-South cooperation "
            "and progressive taxation frameworks in the solutions section."
        ),
        "key_concepts": "position paper, three-section format, background, country position, proposed solutions",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Identifying National Interests on Water Scarcity",
        "prompt": (
            "You are the delegate of Egypt in the UN Environment Programme (UNEP). The topic is "
            "'Addressing Global Water Scarcity and Transboundary Water Disputes.'\n\n"
            "Before you can write speeches or negotiate, you need to understand Egypt's core national "
            "interests on this topic. Write a brief analysis (250-300 words) that identifies:\n\n"
            "1. Why water is an existential issue for Egypt (think about the Nile River)\n"
            "2. Egypt's position on the Grand Ethiopian Renaissance Dam (GERD) dispute\n"
            "3. What Egypt wants from the international community on transboundary water issues\n"
            "4. Which countries are Egypt's allies and which are its rivals on this specific topic\n\n"
            "Focus on identifying interests, not writing a speech. Think like a policy analyst."
        ),
        "hints": (
            "Egypt depends on the Nile for over 90% of its freshwater — this is non-negotiable;"
            "The 1959 Nile Waters Agreement between Egypt and Sudan is a key document;"
            "Ethiopia's GERD threatens Egypt's water supply downstream;"
            "Egypt wants binding international agreements on water sharing, not voluntary frameworks"
        ),
        "sample_answer": (
            "A strong analysis would identify water security as Egypt's top national interest, explain the "
            "GERD dispute with Ethiopia, note Egypt's alliance with Sudan on Nile issues, and articulate "
            "Egypt's desire for binding transboundary water agreements under international law."
        ),
        "key_concepts": "national interests, water scarcity, Nile River, GERD, transboundary disputes, Egypt",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Reading a UN Background Guide",
        "prompt": (
            "You have received the background guide for your committee: the Human Rights Council (HRC). "
            "The topic is 'Protecting Freedom of Expression in the Digital Age.' You are representing "
            "Singapore.\n\n"
            "Many first-time delegates struggle to extract useful information from background guides. "
            "After reading a typical background guide, answer the following questions in 250-350 words:\n\n"
            "1. What is the purpose of a background guide? Who writes it and why?\n"
            "2. What are the three most important things to look for in a background guide?\n"
            "3. How would you use the background guide to identify Singapore's likely position on digital "
            "free speech? (Hint: Singapore has strict media regulation laws)\n"
            "4. What additional research should you do beyond the background guide?\n\n"
            "This exercise teaches you how to read strategically, not just passively."
        ),
        "hints": (
            "Background guides are written by committee chairs/directors to frame the topic;"
            "Look for: key terms/definitions, relevant UN resolutions, and questions to consider;"
            "Singapore's Protection from Online Falsehoods and Manipulation Act (POFMA) is relevant;"
            "Always supplement the background guide with independent country-specific research"
        ),
        "sample_answer": (
            "A good answer would explain that background guides are written by the dais to set the scope "
            "of debate, identify key terms, prior UN action, and guiding questions as the most important "
            "elements, connect Singapore's POFMA law to its likely cautious stance on unrestricted digital "
            "speech, and recommend researching Singapore's voting record at the HRC."
        ),
        "key_concepts": "background guide, strategic reading, committee preparation, Singapore, digital rights",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Using WHO Data for Health Policy Research",
        "prompt": (
            "You are representing Nigeria in the World Health Organization (WHO) committee. The topic is "
            "'Strengthening Global Pandemic Preparedness and Response.'\n\n"
            "Your research requires using data from international organizations like the WHO, World Bank, "
            "and UNICEF. Write a research summary (250-350 words) that:\n\n"
            "1. Lists 3 specific WHO databases or reports you would consult and what data each provides\n"
            "2. Includes 2-3 key health statistics about Nigeria (e.g., healthcare spending as % of GDP, "
            "doctor-to-patient ratio, vaccination rates)\n"
            "3. Explains how Nigeria was affected by the Ebola outbreak in 2014 and what lessons it learned\n"
            "4. Identifies Nigeria's key healthcare challenges relevant to pandemic preparedness\n\n"
            "This exercise teaches you to find and cite authoritative data sources."
        ),
        "hints": (
            "The WHO Global Health Observatory (GHO) has country-specific health data;"
            "Nigeria successfully contained Ebola in 2014 — this is a strength to reference;"
            "Look at the Global Health Security Index for pandemic preparedness rankings;"
            "Nigeria's healthcare spending is among the lowest in Africa as a percentage of GDP"
        ),
        "sample_answer": (
            "A strong summary would reference the WHO GHO, World Health Statistics report, and the Global "
            "Health Security Index. It would cite Nigeria's ~4% GDP health spending, its 1:2500 doctor-to-patient "
            "ratio, and its successful 2014 Ebola containment as evidence of both challenges and capacity."
        ),
        "key_concepts": "WHO data, health statistics, pandemic preparedness, Nigeria, data sources, Ebola",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Understanding Bloc Positions on Climate Finance",
        "prompt": (
            "You are representing the Philippines in the UN Framework Convention on Climate Change (UNFCCC) "
            "committee. The topic is 'Climate Finance and the Green Climate Fund.'\n\n"
            "In MUN, understanding bloc positions is essential for building alliances. Write a brief "
            "overview (250-350 words) that explains:\n\n"
            "1. What is a 'bloc' in the context of UN negotiations?\n"
            "2. Which bloc does the Philippines belong to on climate issues? (Hint: G-77 and China, AOSIS)\n"
            "3. What is the G-77's general position on climate finance — who should pay?\n"
            "4. How does the G-77 position differ from the position of developed countries (e.g., the EU, US)?\n"
            "5. Name two other countries that would be natural allies for the Philippines on this topic\n\n"
            "This exercise helps you understand the bloc dynamics that drive UN negotiations."
        ),
        "hints": (
            "The G-77 and China is the largest bloc of developing nations in the UN;"
            "The Philippines is especially vulnerable to typhoons and sea-level rise — climate vulnerability matters;"
            "The principle of 'Common But Differentiated Responsibilities' (CBDR) is central to G-77's position;"
            "Developed countries often prefer voluntary pledges; developing countries want binding commitments"
        ),
        "sample_answer": (
            "A strong overview would define blocs as negotiating groups with shared interests, identify the "
            "Philippines as part of G-77/China and the Climate Vulnerable Forum, explain CBDR as the basis "
            "for G-77's demand that developed countries fund climate action, and identify Bangladesh and "
            "Pacific island states as natural allies."
        ),
        "key_concepts": "bloc positions, G-77, climate finance, CBDR, UNFCCC, Philippines, alliances",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Basic Citation in MUN Research",
        "prompt": (
            "You are preparing a position paper for your role as the delegate of Canada in the "
            "General Assembly Second Committee (ECOFIN). The topic is 'Promoting Sustainable "
            "Development in Small Island Developing States (SIDS).'\n\n"
            "Your MUN advisor has told you that strong position papers cite their sources properly. "
            "Complete the following exercise (250-300 words):\n\n"
            "1. Explain why citing sources matters in a MUN position paper (2-3 sentences)\n"
            "2. List 4 types of sources that are considered credible in MUN research (e.g., UN documents, "
            "government reports)\n"
            "3. List 2 types of sources that should NOT be cited (e.g., Wikipedia, personal blogs)\n"
            "4. Write 3 sample citations relevant to Canada and SIDS — one from a UN source, one from a "
            "government source, and one from a reputable think tank or NGO\n\n"
            "This exercise builds good research habits from the start."
        ),
        "hints": (
            "Credible sources include: UN documents, World Bank, government .gov sites, peer-reviewed journals;"
            "Avoid: Wikipedia, social media posts, opinion editorials, anonymous blogs;"
            "Canada has contributed to the Green Climate Fund — this could be a government source;"
            "The SAMOA Pathway is a key UN document on SIDS"
        ),
        "sample_answer": (
            "A strong answer would explain that citations build credibility and help verify claims, list "
            "UN resolutions, government white papers, World Bank data, and academic journals as credible "
            "sources, warn against Wikipedia and social media, and provide properly formatted citations "
            "from UNGA resolutions, Canada's DFATD publications, and an OECD or IISD report."
        ),
        "key_concepts": "citation, credible sources, position paper, SIDS, research methodology",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Identifying Stakeholders on Cybersecurity",
        "prompt": (
            "You are representing Estonia in the General Assembly First Committee (DISEC). The topic is "
            "'Establishing Norms for State Behavior in Cyberspace.'\n\n"
            "Before you can develop your country's strategy, you need to identify all the key stakeholders "
            "involved in the cybersecurity debate. Write a stakeholder analysis (250-350 words) that:\n\n"
            "1. Lists at least 5 different types of stakeholders (e.g., nation-states, tech companies, "
            "civil society groups)\n"
            "2. For each stakeholder type, gives one specific example and their interest in the topic\n"
            "3. Explains why Estonia is a relevant voice in this debate (Hint: 2007 cyberattacks)\n"
            "4. Identifies which stakeholders Estonia would likely align with and why\n\n"
            "This exercise teaches you to think beyond just country positions."
        ),
        "hints": (
            "Estonia suffered massive cyberattacks in 2007, allegedly from Russia — this shapes its entire position;"
            "NATO's Cooperative Cyber Defence Centre of Excellence (CCDCOE) is based in Tallinn, Estonia;"
            "Stakeholders include: states, IGOs, private tech companies, civil society, hackers/criminal groups;"
            "Estonia would align with NATO allies and the EU on cyber norms"
        ),
        "sample_answer": (
            "A strong analysis would list nation-states (US, Russia, China), IGOs (UN GGE, ITU), private "
            "sector (Microsoft, Google), civil society (EFF, Access Now), and criminal actors as stakeholders. "
            "It would highlight Estonia's 2007 experience, the Tallinn Manual, and Estonia's alignment with "
            "NATO and EU positions on applying international law to cyberspace."
        ),
        "key_concepts": "stakeholder analysis, cybersecurity, Estonia, cyber norms, multi-stakeholder approach",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "BEG",
        "title": "Researching Bilateral Relations for Alliance Building",
        "prompt": (
            "You are representing Saudi Arabia in the Security Council. The topic is 'The Situation in "
            "Yemen and Regional Stability in the Middle East.'\n\n"
            "Understanding bilateral relationships is crucial for knowing who your allies and adversaries "
            "are in committee. Write a brief relationship map (250-350 words) that covers:\n\n"
            "1. Saudi Arabia's relationship with the United States — allies or rivals? Why?\n"
            "2. Saudi Arabia's relationship with Iran — what is the core tension?\n"
            "3. Saudi Arabia's role in the Yemen conflict — what is the Saudi-led coalition?\n"
            "4. Which Security Council members (P5 + elected) would likely support Saudi Arabia's position, "
            "and which would oppose it?\n"
            "5. One surprising or complex relationship (e.g., Saudi Arabia and Russia on oil/OPEC+)\n\n"
            "This exercise helps you predict committee dynamics before the conference starts."
        ),
        "hints": (
            "Saudi Arabia and the US have a strategic alliance based on oil and security;"
            "Saudi Arabia and Iran are rivals across sectarian (Sunni vs Shia) and geopolitical lines;"
            "Russia and China typically oppose Western intervention — but may have their own interests;"
            "The UAE is Saudi Arabia's closest coalition partner in Yemen"
        ),
        "sample_answer": (
            "A strong relationship map would describe the US-Saudi strategic partnership, the Saudi-Iran "
            "rivalry as both sectarian and geopolitical, Saudi Arabia's leadership of the coalition in Yemen, "
            "predict US/UK/France as likely supporters and Russia/China as skeptics, and note the complex "
            "Saudi-Russia relationship through OPEC+ cooperation despite competing interests in Syria."
        ),
        "key_concepts": "bilateral relations, alliance building, Security Council, Yemen, Saudi Arabia, Iran",
    },
    # ── INTERMEDIATE (10) ────────────────────────────────────────────────────
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Multi-Source Research Synthesis on Migration",
        "prompt": (
            "You are representing Turkey in the General Assembly Third Committee (SOCHUM). The topic is "
            "'Addressing the Root Causes of Forced Migration and Displacement.'\n\n"
            "Turkey hosts the world's largest refugee population, primarily from Syria. Your task is to "
            "synthesize information from multiple sources into a coherent research brief (400-500 words) "
            "that:\n\n"
            "1. Combines data from at least THREE different types of sources: a UN agency report (UNHCR), "
            "a government source (Turkish Directorate General of Migration Management), and an NGO or "
            "think tank report\n"
            "2. Identifies where these sources agree and where they present different perspectives\n"
            "3. Extracts Turkey's key talking points: burden-sharing, the EU-Turkey deal, and the concept "
            "of 'temporary protection'\n"
            "4. Notes any data discrepancies between sources (e.g., different refugee count estimates)\n\n"
            "The skill being tested here is your ability to triangulate information and identify the most "
            "reliable data points for your arguments."
        ),
        "hints": (
            "UNHCR's data portal has real-time refugee statistics by host country;"
            "Turkey often emphasizes that it has spent over $40 billion hosting refugees — verify this across sources;"
            "The 2016 EU-Turkey Statement is controversial — the EU and Turkey frame it differently;"
            "Look for discrepancies between government figures and independent monitoring organizations"
        ),
        "sample_answer": (
            "A strong synthesis would compare UNHCR's 3.6 million figure with Turkish government claims, "
            "note how the EU-Turkey deal is framed as a success by the EU but as insufficient by Turkey, "
            "identify burden-sharing as Turkey's core demand, and flag that NGOs like Amnesty International "
            "raise concerns about refugee rights that Turkey may not emphasize."
        ),
        "key_concepts": "multi-source synthesis, triangulation, forced migration, Turkey, EU-Turkey deal, UNHCR",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Writing a Position Paper Introduction",
        "prompt": (
            "You are representing France in the Security Council. The topic is 'Addressing the Threat of "
            "Foreign Terrorist Fighters and Returning Combatants.'\n\n"
            "Write the introduction section (first section) of a position paper (350-450 words) that:\n\n"
            "1. Opens with a compelling framing of the foreign terrorist fighter (FTF) issue — why is it "
            "urgent and global in scope?\n"
            "2. Provides key statistics on FTFs (estimated numbers, countries of origin, destination conflicts)\n"
            "3. References at least two relevant Security Council resolutions by number (e.g., S/RES/2178)\n"
            "4. Establishes France's credibility on this topic — France has experienced major terrorist "
            "attacks and has been active in counter-terrorism operations in the Sahel\n"
            "5. Ends with a transition sentence that previews France's position\n\n"
            "The introduction should be authoritative, well-cited, and set the stage for the policy "
            "arguments that would follow."
        ),
        "hints": (
            "S/RES/2178 (2014) specifically addresses foreign terrorist fighters;"
            "S/RES/2396 (2017) addresses returning and relocating FTFs;"
            "The November 2015 Paris attacks and the 2016 Nice attack are directly relevant;"
            "France's Operation Barkhane in the Sahel demonstrates its operational commitment;"
            "An estimated 40,000+ individuals traveled to join ISIS from over 80 countries"
        ),
        "sample_answer": (
            "A strong introduction would open with the scale of the FTF phenomenon, cite S/RES/2178 and "
            "S/RES/2396, reference the 40,000+ FTFs estimate, establish France's experience through the "
            "Paris/Nice attacks and Sahel operations, and transition smoothly into France's policy position "
            "emphasizing multilateral counter-terrorism frameworks."
        ),
        "key_concepts": "position paper introduction, foreign terrorist fighters, Security Council resolutions, France, counter-terrorism",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Analyzing Voting Patterns at the General Assembly",
        "prompt": (
            "You are representing Brazil in the General Assembly plenary. The topic is 'Reform of the "
            "United Nations Security Council.'\n\n"
            "Brazil is part of the G4 (along with Germany, India, and Japan), a group that advocates for "
            "permanent Security Council seats. Conduct a voting pattern analysis (400-500 words) that:\n\n"
            "1. Explains Brazil's position on UNSC reform and why it seeks a permanent seat\n"
            "2. Identifies voting blocs that support expansion (African Union, G4 supporters) vs. those "
            "that oppose it (Uniting for Consensus/Coffee Club — Italy, Pakistan, South Korea, Argentina)\n"
            "3. Analyzes why the P5 have mixed views on reform — which P5 members are more sympathetic "
            "to expansion and which resist it?\n"
            "4. Examines General Assembly resolution voting patterns on UNSC reform proposals\n"
            "5. Predicts which reform model has the best chance of success and why\n\n"
            "This exercise develops your ability to read political dynamics through voting data."
        ),
        "hints": (
            "The African Union's Ezulwini Consensus demands two permanent African seats with veto power;"
            "The Uniting for Consensus group opposes new permanent seats, preferring longer-term elected seats;"
            "The US and UK have expressed some support for limited expansion; China is more cautious;"
            "Russia has been ambiguous, sometimes supporting India's candidacy;"
            "GA Decision 62/557 is the framework for intergovernmental negotiations on reform"
        ),
        "sample_answer": (
            "A thorough analysis would map the G4 vs. UFC positions, note the African Union's distinct "
            "demands, explain P5 reluctance to dilute their own power, reference key GA decisions, and "
            "conclude that incremental expansion without new vetoes is the most politically viable model."
        ),
        "key_concepts": "voting patterns, UNSC reform, G4, Uniting for Consensus, P5, General Assembly",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Regional Group Dynamics in ECOFIN",
        "prompt": (
            "You are representing Indonesia in the General Assembly Second Committee (ECOFIN). The topic "
            "is 'Bridging the Digital Divide in Developing Countries.'\n\n"
            "Understanding regional group dynamics is critical for effective diplomacy. Write an analysis "
            "(350-450 words) that:\n\n"
            "1. Identifies the five UN regional groups and explains which group Indonesia belongs to\n"
            "2. Describes ASEAN's collective position on digital development and technology transfer\n"
            "3. Analyzes where the Asia-Pacific group's interests align with and diverge from the African "
            "Group and GRULAC (Latin America and Caribbean) on the digital divide\n"
            "4. Identifies potential cross-regional coalitions Indonesia could join or lead\n"
            "5. Explains the role of China and India as major players within the Asia-Pacific group and "
            "how Indonesia navigates between them\n\n"
            "This exercise builds understanding of how regional politics shape committee outcomes."
        ),
        "hints": (
            "The five regional groups are: African, Asia-Pacific, Eastern European, GRULAC, and WEOG;"
            "Indonesia is in the Asia-Pacific Group and is a leading member of ASEAN;"
            "ASEAN has a Master Plan on Digital Connectivity that could be a reference point;"
            "Developing country groups share concerns about technology transfer but may differ on IP protections;"
            "Indonesia has positioned itself as a digital economy leader in Southeast Asia"
        ),
        "sample_answer": (
            "A strong analysis would map the five regional groups, place Indonesia within the Asia-Pacific "
            "group and ASEAN, identify shared developing-country interests in technology transfer with "
            "Africa and GRULAC, note tensions around Chinese tech dominance vs. data sovereignty, and "
            "propose a cross-regional digital development coalition led by middle-power digital economies."
        ),
        "key_concepts": "regional groups, ASEAN, Asia-Pacific, digital divide, cross-regional coalitions, Indonesia",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Economic Data for Policy Arguments on Debt Relief",
        "prompt": (
            "You are representing Zambia in the General Assembly Second Committee (ECOFIN). The topic is "
            "'Sovereign Debt Restructuring and Economic Recovery in the Global South.'\n\n"
            "Zambia became one of the first countries to default on its sovereign debt during the COVID-19 "
            "pandemic. Build an evidence-based policy argument (400-500 words) using economic data:\n\n"
            "1. Research and present key economic indicators for Zambia: GDP, debt-to-GDP ratio, major "
            "creditors (bilateral, multilateral, private), and credit rating\n"
            "2. Explain the G20 Common Framework for Debt Treatments and why it has been slow to deliver results\n"
            "3. Compare Zambia's debt situation with at least one other country (e.g., Sri Lanka, Ghana)\n"
            "4. Use the economic data to argue for a specific policy position (e.g., mandatory debt "
            "restructuring mechanisms, IMF SDR reallocation, or creditor haircuts)\n\n"
            "Your argument should be grounded in numbers, not just rhetoric."
        ),
        "hints": (
            "Zambia's debt-to-GDP ratio exceeded 100% before restructuring talks began;"
            "China is Zambia's largest bilateral creditor — this complicates G20 Common Framework negotiations;"
            "The IMF approved a $1.3 billion Extended Credit Facility for Zambia in 2022;"
            "Compare with Ghana's debt restructuring under the Common Framework for parallel analysis;"
            "Private creditors (bondholders) have been reluctant to accept comparable treatment"
        ),
        "sample_answer": (
            "A data-driven argument would present Zambia's ~$17 billion external debt, its 120%+ debt-to-GDP "
            "ratio, the dominance of Chinese bilateral lending, compare with Ghana's parallel restructuring "
            "challenges, and argue for a binding sovereign debt workout mechanism that ensures comparable "
            "treatment across all creditor classes."
        ),
        "key_concepts": "sovereign debt, economic data, Zambia, G20 Common Framework, debt restructuring, evidence-based argument",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Comparing National and International Law on Refugees",
        "prompt": (
            "You are representing Australia in the UN High Commissioner for Refugees (UNHCR) Executive "
            "Committee. The topic is 'Strengthening the International Refugee Protection Framework.'\n\n"
            "Australia has a controversial asylum policy involving offshore processing in Nauru and Papua "
            "New Guinea. Write a comparative legal analysis (400-500 words) that:\n\n"
            "1. Summarizes the key provisions of the 1951 Refugee Convention and its 1967 Protocol, "
            "particularly the principle of non-refoulement\n"
            "2. Describes Australia's domestic asylum legislation (Migration Act 1958, Operation Sovereign Borders)\n"
            "3. Identifies where Australian domestic law diverges from or is in tension with international "
            "refugee law\n"
            "4. Explains how Australia defends its policies in international forums\n"
            "5. Notes any rulings by international bodies (e.g., UN Human Rights Committee) regarding "
            "Australia's asylum policies\n\n"
            "This exercise develops your ability to navigate the tension between national sovereignty "
            "and international legal obligations."
        ),
        "hints": (
            "Non-refoulement (Article 33 of the 1951 Convention) prohibits returning refugees to danger;"
            "Australia argues offshore processing does not violate non-refoulement because refugees are processed, not returned;"
            "The UN Human Rights Committee has found Australia in violation of the ICCPR regarding offshore detention;"
            "Australia's 'Pacific Solution' and 'Operation Sovereign Borders' are distinct but related policies"
        ),
        "sample_answer": (
            "A strong analysis would outline the Convention's core protections, detail Australia's offshore "
            "processing framework, identify the non-refoulement tension, note Australia's sovereignty-based "
            "defense, and reference specific UNHRC findings criticizing Australia's mandatory detention "
            "and third-country processing arrangements."
        ),
        "key_concepts": "refugee law, 1951 Convention, non-refoulement, Australia, offshore processing, national vs international law",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Analyzing NGO Reports for Committee Debate",
        "prompt": (
            "You are representing the Democratic Republic of Congo (DRC) in the Human Rights Council. "
            "The topic is 'Accountability for Human Rights Violations in Conflict Zones.'\n\n"
            "NGO reports from organizations like Human Rights Watch, Amnesty International, and the "
            "International Crisis Group are commonly cited in MUN debate. Write an analysis (350-450 words) "
            "that:\n\n"
            "1. Selects TWO major NGO reports about human rights in the DRC (you may reference real reports "
            "by organization name and approximate date)\n"
            "2. Summarizes the key findings of each report (2-3 sentences per report)\n"
            "3. Critically evaluates the strengths and limitations of using NGO reports as evidence in UN "
            "debates — are they objective? What biases might they have?\n"
            "4. Explains how the DRC as a country would likely respond to critical NGO reports about its "
            "own human rights record\n\n"
            "This exercise develops critical source evaluation skills."
        ),
        "hints": (
            "Human Rights Watch and Amnesty International have both published extensively on eastern DRC;"
            "The DRC government has sometimes accused NGOs of political bias or serving Western interests;"
            "NGO reports are valuable but may lack government-side perspectives;"
            "The UN's own OHCHR reports can serve as a counterbalance to NGO reports;"
            "Consider who funds the NGOs and how that might shape their focus"
        ),
        "sample_answer": (
            "A strong analysis would reference specific HRW and Amnesty reports on DRC conflicts, summarize "
            "findings on extrajudicial killings and sexual violence, critically note that NGOs may have "
            "Western-donor-influenced priorities, and explain that the DRC would challenge negative reports "
            "by citing sovereignty, ongoing reforms, and cooperation with UN peacekeeping (MONUSCO)."
        ),
        "key_concepts": "NGO reports, source evaluation, Human Rights Watch, Amnesty International, DRC, critical analysis",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Security Council Dynamics on Syrian Conflict",
        "prompt": (
            "You are representing the United Kingdom in the Security Council. The topic is 'The Political "
            "and Humanitarian Situation in Syria.'\n\n"
            "The Security Council has been largely gridlocked on Syria due to P5 divisions. Write a "
            "strategic analysis (400-500 words) that:\n\n"
            "1. Maps the P5 positions on Syria — who supports the Assad government and who has called for "
            "regime change or accountability?\n"
            "2. Counts and explains the Russian and Chinese vetoes on Syria-related resolutions (there "
            "have been over 16 combined)\n"
            "3. Analyzes how the veto dynamic has affected humanitarian access (e.g., cross-border aid "
            "through Bab al-Hawa)\n"
            "4. Identifies what the UK can realistically achieve given these constraints\n"
            "5. Proposes a UK strategy for advancing humanitarian objectives without triggering a veto\n\n"
            "This exercise develops understanding of P5 power dynamics and strategic realism."
        ),
        "hints": (
            "Russia has vetoed Syria resolutions more than any other P5 member — at least 16 times;"
            "China has often joined Russia in dual vetoes on Syria;"
            "The cross-border aid mechanism (through Bab al-Hawa, Bab al-Salam) has required regular renewal;"
            "The UK has advocated for accountability mechanisms like the IIIM (International, Impartial and Independent Mechanism);"
            "Humanitarian framing is harder to veto than political framing"
        ),
        "sample_answer": (
            "A strong analysis would detail Russia's military and political support for Assad, map the "
            "veto pattern chronologically, explain how vetoes blocked both accountability and humanitarian "
            "access, and propose a UK strategy focused on narrow humanitarian resolutions and General "
            "Assembly workarounds (e.g., Uniting for Peace) to circumvent Security Council deadlock."
        ),
        "key_concepts": "Security Council dynamics, P5, veto, Syria, humanitarian access, UK strategy, gridlock",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Building Evidence-Based Arguments on Gender Equality",
        "prompt": (
            "You are representing Rwanda in the Commission on the Status of Women (CSW). The topic is "
            "'Women's Political Participation and Leadership.'\n\n"
            "Rwanda has the highest percentage of women in parliament globally (over 61% in the lower "
            "house). Build an evidence-based argument (400-500 words) that:\n\n"
            "1. Presents Rwanda's statistics on women's political representation with specific numbers\n"
            "2. Explains the historical context — how did Rwanda achieve this? (Hint: post-genocide "
            "constitutional reforms)\n"
            "3. Addresses potential counterarguments — critics say Rwanda's women parliamentarians lack "
            "real power under an authoritarian system. How would Rwanda respond?\n"
            "4. Uses comparative data from at least 2 other countries (one with high and one with low "
            "women's representation) to strengthen your argument\n"
            "5. Proposes evidence-based policy recommendations that other countries could adopt\n\n"
            "This exercise teaches you to build arguments that anticipate and address opposition."
        ),
        "hints": (
            "Rwanda's 2003 constitution mandates a 30% quota for women in decision-making bodies;"
            "The post-genocide demographic imbalance (70% female population) drove initial inclusion;"
            "Compare with Nordic countries (Sweden ~47%) as high performers and countries with <15% representation;"
            "The IPU Parline database has global parliamentary gender data;"
            "Address the democracy critique carefully — acknowledge it without undermining your main argument"
        ),
        "sample_answer": (
            "A strong argument would cite Rwanda's 61%+ figure, explain the post-1994 constitutional quota "
            "system, compare with Sweden's voluntary party quotas and Saudi Arabia's recent municipal elections, "
            "address the authoritarianism critique by pointing to tangible policy outcomes in health and education "
            "driven by women legislators, and recommend constitutional quotas combined with capacity-building."
        ),
        "key_concepts": "evidence-based arguments, gender equality, Rwanda, women's representation, quotas, counterarguments",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "INT",
        "title": "Cross-Referencing Country Positions on AI Governance",
        "prompt": (
            "You are representing the European Union (observer) in the General Assembly Sixth Committee "
            "(Legal). The topic is 'Legal Frameworks for Artificial Intelligence Governance.'\n\n"
            "To build effective coalitions, you need to know where key countries stand. Create a position "
            "matrix (400-500 words) that cross-references the AI governance positions of:\n\n"
            "1. The European Union — what is the EU AI Act's approach? (risk-based regulation)\n"
            "2. The United States — what is the US approach? (innovation-first, sector-specific)\n"
            "3. China — what is China's approach? (state-guided, focused on algorithmic governance)\n"
            "4. India — what is India's approach? (developing-country perspective, data sovereignty)\n"
            "5. Brazil — what is Brazil's approach? (rights-based, inspired by its data protection law LGPD)\n\n"
            "For each, identify: (a) their regulatory philosophy, (b) key legislation or frameworks, "
            "(c) areas of potential agreement with the EU, and (d) areas of disagreement.\n\n"
            "This exercise builds coalition-mapping skills essential for negotiation."
        ),
        "hints": (
            "The EU AI Act classifies AI systems by risk level — unacceptable, high, limited, minimal;"
            "The US has relied on executive orders and sector-specific guidance rather than comprehensive legislation;"
            "China has enacted regulations on algorithmic recommendations, deepfakes, and generative AI;"
            "India has pushed for AI governance that accounts for developing country needs and data localization;"
            "Look for overlap: most countries agree on banning certain AI applications (e.g., social scoring)"
        ),
        "sample_answer": (
            "A strong matrix would compare the five approaches across regulatory philosophy, legislation, "
            "and compatibility dimensions. It would identify common ground on prohibiting harmful AI uses, "
            "note the US-EU tension on regulation's impact on innovation, and recognize India/Brazil's demand "
            "that AI governance address developing-country capacity gaps. The EU's coalition strategy would "
            "prioritize alignment with Brazil on rights-based approaches while finding issue-specific common "
            "ground with each actor."
        ),
        "key_concepts": "position matrix, AI governance, EU AI Act, cross-referencing, coalition mapping, regulatory approaches",
    },
    # ── ADVANCED (10) ────────────────────────────────────────────────────────
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Comprehensive Policy Analysis on the Sahel Crisis",
        "prompt": (
            "You are representing France in the Security Council. The topic is 'Addressing Insecurity "
            "and State Fragility in the Sahel Region.'\n\n"
            "The Sahel crisis involves interconnected challenges: jihadist insurgencies, military coups, "
            "climate change, food insecurity, and the withdrawal of French and UN peacekeeping forces. "
            "Write a comprehensive policy analysis (600-800 words) that:\n\n"
            "1. Maps the key actors: state actors (Mali, Burkina Faso, Niger, Chad), non-state actors "
            "(JNIM, ISGS, Wagner Group/Africa Corps), and international actors (France, UN, AU, ECOWAS, Russia)\n"
            "2. Analyzes the root causes of instability — not just symptoms. Why have multiple Sahelian "
            "states experienced coups since 2020?\n"
            "3. Evaluates France's military intervention (Operation Serval → Barkhane → withdrawal) — "
            "what went wrong and what lessons were learned?\n"
            "4. Assesses the role of Wagner Group/Russia in filling the security vacuum and what this means "
            "for Western interests\n"
            "5. Proposes a realistic French strategy going forward that accounts for anti-French sentiment "
            "in the region\n"
            "6. References at least 3 specific Security Council resolutions or UN reports\n\n"
            "This exercise demands deep research, honest self-assessment, and strategic thinking."
        ),
        "hints": (
            "S/RES/2640 (2022) extended MINUSMA's mandate — but Mali requested MINUSMA's withdrawal in 2023;"
            "France withdrew from Mali in 2022 after the military junta invited Wagner Group;"
            "Anti-French sentiment has deep colonial roots — France must acknowledge this;"
            "The Sahel Alliance (Mali, Burkina Faso, Niger) withdrew from ECOWAS in 2024;"
            "Climate change exacerbates conflict through resource competition — include this dimension"
        ),
        "sample_answer": (
            "A comprehensive analysis would map the complex actor landscape, trace instability to colonial "
            "governance legacies, failed state-building, and climate-driven resource competition. It would "
            "honestly assess France's Barkhane mission as militarily effective but politically unsustainable, "
            "analyze Wagner's exploitation of the security vacuum, and propose a recalibrated French strategy "
            "focused on economic development, multilateral partnerships (EU, AU), and grassroots engagement "
            "rather than direct military presence."
        ),
        "key_concepts": "comprehensive policy analysis, Sahel, France, Wagner Group, MINUSMA, root cause analysis, Security Council",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Writing an Award-Winning Position Paper",
        "prompt": (
            "You are representing China in the Security Council. The topic is 'Non-Proliferation and the "
            "Iranian Nuclear Program (JCPOA).'\n\n"
            "Write a complete, award-quality position paper (600-800 words) following the three-section "
            "format. Your paper must demonstrate:\n\n"
            "SECTION 1 — Background (200-250 words):\n"
            "- Comprehensive overview of the JCPOA, its key provisions, and its collapse after US withdrawal in 2018\n"
            "- Reference at least 2 specific Security Council resolutions (e.g., S/RES/2231)\n"
            "- Cite IAEA reports on Iran's enrichment levels\n\n"
            "SECTION 2 — China's Position (200-250 words):\n"
            "- Articulate China's nuanced position: opposition to nuclear proliferation BUT also opposition "
            "to unilateral sanctions and US 'maximum pressure'\n"
            "- Reference China's economic ties with Iran (oil imports, BRI)\n"
            "- Explain China's voting record on Iran-related resolutions\n\n"
            "SECTION 3 — Proposed Solutions (200-250 words):\n"
            "- Propose realistic solutions that align with China's interests: reviving the JCPOA framework, "
            "lifting unilateral (not UN) sanctions, regional security dialogue\n"
            "- Each solution should reference a precedent or existing mechanism\n\n"
            "This paper should be indistinguishable from what a top delegate would submit at a competitive "
            "collegiate conference."
        ),
        "hints": (
            "S/RES/2231 (2015) endorsed the JCPOA and established the framework for sanctions relief;"
            "The US withdrew from the JCPOA in May 2018 and reimposed unilateral sanctions;"
            "Iran has since enriched uranium to 60% — far beyond JCPOA limits;"
            "China is one of Iran's largest oil buyers and views Iran through the BRI lens;"
            "China consistently opposes unilateral sanctions as a matter of principle, not just on Iran"
        ),
        "sample_answer": (
            "An award-quality paper would demonstrate mastery of the JCPOA's technical provisions, cite "
            "S/RES/2231 and relevant IAEA Board of Governors reports, articulate China's dual opposition "
            "to proliferation and unilateral coercion, reference the China-Iran 25-year cooperation agreement, "
            "and propose a phased return to compliance with reciprocal sanctions relief — all in precise, "
            "diplomatic language with zero editorializing."
        ),
        "key_concepts": "position paper, JCPOA, China, Iran, S/RES/2231, IAEA, non-proliferation, award-winning",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Predictive Analysis of India's Behavior on Kashmir",
        "prompt": (
            "You are representing Pakistan in the Security Council. The topic is 'Self-Determination and "
            "Disputed Territories.' You know that India will be in the room.\n\n"
            "Conduct a predictive analysis (500-650 words) of India's likely behavior in committee:\n\n"
            "1. Based on India's historical positions, what arguments will India make regarding Kashmir?\n"
            "2. Which Security Council resolutions will India try to avoid discussing, and which will it "
            "reference? (Hint: S/RES/47 from 1948 called for a plebiscite)\n"
            "3. How has India's position evolved since the revocation of Article 370 in 2019?\n"
            "4. Which P5 members will India seek support from, and why?\n"
            "5. What procedural moves might India make to keep Kashmir off the agenda?\n"
            "6. How should Pakistan counter each of India's likely arguments?\n\n"
            "This exercise develops strategic anticipation — predicting opponent behavior based on "
            "research, not assumptions."
        ),
        "hints": (
            "India frames Kashmir as a bilateral issue and resists internationalization;"
            "S/RES/47 (1948) recommended a plebiscite — India now argues conditions have changed;"
            "India revoked Article 370 in August 2019, integrating Kashmir more fully into the Indian Union;"
            "India has strong diplomatic ties with the US, France, and Russia on the Security Council;"
            "India may invoke 'cross-border terrorism' to shift focus from self-determination to counter-terrorism"
        ),
        "sample_answer": (
            "A strong predictive analysis would anticipate India's bilateral-issue framing, its avoidance "
            "of S/RES/47, its post-Article 370 sovereignty arguments, its likely alignment with the US "
            "and France, and its procedural strategy to block Kashmir discussions. Pakistan's counter-strategy "
            "would focus on human rights documentation, OHCHR reports on Kashmir, and framing the issue as "
            "self-determination under the UN Charter."
        ),
        "key_concepts": "predictive analysis, Kashmir, India, Pakistan, S/RES/47, Article 370, opponent strategy",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Synthesizing Primary UN Documents on Oceans",
        "prompt": (
            "You are representing Fiji in the General Assembly plenary. The topic is 'Implementing the "
            "UN High Seas Treaty (BBNJ Agreement) and Protecting Marine Biodiversity.'\n\n"
            "The 2023 High Seas Treaty (Biodiversity Beyond National Jurisdiction) is a landmark agreement. "
            "Write a primary-source synthesis (500-700 words) that draws from official UN documents:\n\n"
            "1. Analyze the key provisions of the BBNJ Agreement, referencing specific articles on area-based "
            "management tools (ABMTs), environmental impact assessments (EIAs), marine genetic resources "
            "(MGRs), and capacity building\n"
            "2. Compare the BBNJ Agreement with UNCLOS (1982), explaining how the new treaty fills gaps "
            "left by the original convention\n"
            "3. Reference at least one General Assembly resolution that advanced the BBNJ process (e.g., "
            "A/RES/72/249)\n"
            "4. Explain Fiji's specific interests: why does this treaty matter existentially for Pacific "
            "Island nations?\n"
            "5. Identify outstanding challenges: which provisions are strong and which are weak or ambiguous?\n\n"
            "Use document citations (A/CONF.232/2023/4 for the treaty text) throughout."
        ),
        "hints": (
            "The BBNJ Agreement was adopted in June 2023 after nearly 20 years of negotiations;"
            "UNCLOS does not adequately govern biodiversity in areas beyond national jurisdiction (the high seas);"
            "Marine genetic resources and benefit-sharing were the most contentious negotiating issues;"
            "Fiji and Pacific Islands see rising sea levels threatening their EEZs and traditional fishing grounds;"
            "A/RES/72/249 established the intergovernmental conference to negotiate the treaty"
        ),
        "sample_answer": (
            "A rigorous synthesis would cite specific BBNJ articles on ABMTs and EIAs, compare with UNCLOS "
            "Part VII's limited high seas protections, reference A/RES/72/249 and the treaty text document, "
            "explain that Fiji's survival depends on ocean health and that Pacific Islands contributed most to "
            "the BBNJ process despite being smallest states, and identify the MGR benefit-sharing mechanism "
            "as potentially weak due to voluntary elements."
        ),
        "key_concepts": "primary UN documents, BBNJ Agreement, UNCLOS, Fiji, marine biodiversity, document synthesis",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Analyzing the Arms Trade Treaty Framework",
        "prompt": (
            "You are representing Germany in the Conference on the Arms Trade Treaty (ATT). The topic is "
            "'Preventing Diversion of Conventional Arms to Conflict Zones.'\n\n"
            "Write a treaty framework analysis (500-700 words) that:\n\n"
            "1. Outlines the key provisions of the Arms Trade Treaty (2013), including Articles 6 and 7 "
            "on prohibitions and export assessments\n"
            "2. Analyzes the treaty's enforcement mechanisms — or lack thereof. Why is compliance voluntary?\n"
            "3. Maps which major arms exporters have ratified the ATT and which have not (notably the US "
            "signed but did not ratify; Russia and China have neither signed nor ratified)\n"
            "4. Examines case studies of alleged ATT violations — e.g., arms transfers to Saudi Arabia "
            "for use in Yemen (relevant to Germany, which temporarily banned arms sales to Saudi Arabia)\n"
            "5. Proposes strengthening mechanisms that Germany would champion\n\n"
            "This analysis requires understanding both the legal text and its real-world application."
        ),
        "hints": (
            "Article 6 prohibits transfers that would violate UN arms embargoes or facilitate genocide/war crimes;"
            "Article 7 requires risk assessment before export authorization;"
            "The ATT has no enforcement mechanism — it relies on national implementation and annual reporting;"
            "Germany suspended arms exports to Saudi Arabia after the Khashoggi murder in 2018;"
            "The US, the world's largest arms exporter, unsigned the ATT under the Trump administration in 2019"
        ),
        "sample_answer": (
            "A thorough analysis would detail Articles 6 and 7, critique the voluntary compliance model, "
            "present the ratification gap (major exporters absent), use the Germany-Saudi Arabia case to "
            "show both the treaty's potential and its weakness, and propose enhanced reporting requirements, "
            "an independent monitoring body, and universalization campaigns as German priorities."
        ),
        "key_concepts": "Arms Trade Treaty, treaty analysis, arms diversion, Germany, enforcement mechanisms, Saudi Arabia",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Great Power Competition and Climate Governance",
        "prompt": (
            "You are representing Singapore in the General Assembly Second Committee (ECOFIN). The topic "
            "is 'The Impact of Great Power Competition on Multilateral Climate Action.'\n\n"
            "Write a strategic research paper (600-800 words) analyzing how US-China competition affects "
            "global climate governance:\n\n"
            "1. Trace the history of US-China climate cooperation: from the 2014 bilateral agreement that "
            "enabled the Paris Agreement, through Trump-era withdrawal, Biden-era re-engagement, and the "
            "Sunnylands Statement\n"
            "2. Analyze how great power rivalry undermines specific climate mechanisms: Green Climate Fund "
            "contributions, technology transfer commitments, and Loss and Damage fund negotiations\n"
            "3. Examine the role of the EU as a potential mediating force\n"
            "4. Assess the impact on small states like Singapore that depend on multilateral cooperation "
            "but cannot influence great power dynamics directly\n"
            "5. Propose a Singapore-led 'third way' strategy that advances climate action despite great "
            "power competition\n"
            "6. Reference at least 2 COP decisions or UNFCCC documents\n\n"
            "This exercise requires understanding both geopolitics and climate governance simultaneously."
        ),
        "hints": (
            "The 2014 US-China Joint Announcement on Climate Change was a diplomatic breakthrough;"
            "The US withdrew from the Paris Agreement in 2020 and rejoined in 2021;"
            "The Sunnylands Statement (2023) resumed bilateral climate cooperation;"
            "Singapore is vulnerable to sea-level rise despite being a financial hub;"
            "COP27 established the Loss and Damage fund; COP28 called for transitioning away from fossil fuels;"
            "Small states can lead through moral authority and technical expertise"
        ),
        "sample_answer": (
            "A sophisticated analysis would trace the cooperation-competition cycle in US-China climate "
            "relations, demonstrate how rivalry reduces ambition on finance and technology transfer, credit "
            "the EU's mediation role, and articulate Singapore's vulnerability despite its wealth. The "
            "'third way' strategy would leverage Singapore's role as an ASEAN hub and financial center to "
            "propose climate finance mechanisms that operate independently of great power patronage."
        ),
        "key_concepts": "great power competition, US-China, climate governance, Paris Agreement, Singapore, multilateralism",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Mapping Interconnected Crises in the Horn of Africa",
        "prompt": (
            "You are representing Ethiopia in the General Assembly plenary. The topic is 'Addressing "
            "Interconnected Crises: Conflict, Climate, and Food Insecurity in the Horn of Africa.'\n\n"
            "The Horn of Africa (Ethiopia, Somalia, Eritrea, Djibouti, Sudan, South Sudan, Kenya, Uganda) "
            "faces overlapping crises. Write a crisis mapping analysis (600-750 words) that:\n\n"
            "1. Identifies at least 5 distinct but interconnected crises in the region (e.g., Tigray conflict, "
            "Somalia's Al-Shabaab insurgency, Sudan civil war, drought, refugee flows)\n"
            "2. Maps the causal connections between these crises — how does conflict in one country create "
            "refugee flows that destabilize another? How does drought exacerbate ethnic tensions?\n"
            "3. Analyzes Ethiopia's complex role: it is both a crisis-affected country and a regional power "
            "with peacekeeping contributions\n"
            "4. Evaluates the effectiveness of existing international responses (IGAD, AU, UN OCHA)\n"
            "5. Proposes an integrated regional framework that addresses root causes rather than symptoms\n\n"
            "This exercise tests your ability to see systemic patterns across borders."
        ),
        "hints": (
            "The Tigray conflict (2020-2022) displaced millions and created a humanitarian catastrophe;"
            "The Horn of Africa experienced its worst drought in 40 years in 2022-2023;"
            "Ethiopia hosts over 900,000 refugees, mostly from South Sudan, Somalia, and Eritrea;"
            "The Sudan civil war (2023-present) has created a new mass displacement crisis;"
            "IGAD (Intergovernmental Authority on Development) is the regional body but has limited enforcement power"
        ),
        "sample_answer": (
            "A strong crisis map would visually/textually connect Tigray's displacement to Sudanese border "
            "tensions, link drought to pastoralist conflicts in Kenya-Ethiopia-Somalia border areas, show "
            "how Al-Shabaab exploits state fragility, position Ethiopia as both affected and influential, "
            "critique IGAD's mandate limitations, and propose an integrated AU-UN framework with climate "
            "adaptation, conflict mediation, and development pillars."
        ),
        "key_concepts": "crisis mapping, interconnected crises, Horn of Africa, Ethiopia, systems thinking, IGAD",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Advanced Source Evaluation on Xinjiang",
        "prompt": (
            "You are representing a member of the Organisation of Islamic Cooperation (OIC) — choose "
            "Turkey — in the Human Rights Council. The topic is 'Human Rights Situations Requiring the "
            "Council's Attention.'\n\n"
            "The situation of Uyghurs in Xinjiang, China is one of the most contested human rights issues "
            "at the UN. Conduct an advanced source evaluation (500-700 words) that:\n\n"
            "1. Categorizes sources into tiers: primary UN sources (OHCHR assessment), government sources "
            "(China's white papers, US State Department reports), academic research, investigative journalism "
            "(ASPI, BuzzFeed News investigations), and survivor testimony\n"
            "2. Evaluates the reliability and potential biases of each source category\n"
            "3. Identifies where sources converge (suggesting higher reliability) and where they diverge\n"
            "4. Explains Turkey's difficult position: as an OIC member and Turkic state, it has cultural ties "
            "to Uyghurs, but it also has deep economic ties with China (BRI, trade)\n"
            "5. Recommends what sources Turkey should cite and which to avoid, and why\n\n"
            "This exercise develops sophisticated critical thinking about evidence in politically charged topics."
        ),
        "hints": (
            "The OHCHR published its Xinjiang assessment in August 2022, finding 'serious human rights violations';"
            "China's white papers frame Xinjiang policies as counter-terrorism and vocational training;"
            "ASPI (Australian Strategic Policy Institute) has mapped detention facilities using satellite imagery;"
            "Turkey initially criticized China in 2019 but later softened its stance after Chinese economic pressure;"
            "The OIC as a bloc has been divided — many members have economic ties with China"
        ),
        "sample_answer": (
            "A sophisticated evaluation would tier the OHCHR assessment as the most authoritative primary source, "
            "note that US reports carry geopolitical bias, acknowledge China's counter-narrative while identifying "
            "its limitations, credit investigative journalism for satellite evidence, note convergence between "
            "OHCHR and independent investigations, and advise Turkey to cite the OHCHR report as politically "
            "safer than US State Department reports while navigating its China economic dependency."
        ),
        "key_concepts": "source evaluation, Xinjiang, Uyghurs, OHCHR, bias analysis, Turkey, evidence hierarchy",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Country Matrix for Bloc Building on Tech Regulation",
        "prompt": (
            "You are representing the European Union (observer) in the General Assembly First Committee "
            "(DISEC). The topic is 'Responsible State Behavior in the Use of ICTs in the Context of "
            "International Security.'\n\n"
            "Construct a detailed country matrix (500-700 words) for bloc-building purposes that:\n\n"
            "1. Creates a matrix of at least 12 countries across the following dimensions:\n"
            "   - Support for binding vs. voluntary cyber norms\n"
            "   - Position on state sovereignty vs. multi-stakeholder governance of the internet\n"
            "   - Membership in relevant groups (GGE, OEWG, Freedom Online Coalition, SCO)\n"
            "   - Key national interests (surveillance, commerce, human rights, military)\n"
            "2. Identifies three potential blocs: (a) Western democratic (EU, US, Japan, Australia, Canada), "
            "(b) sovereignty-focused (Russia, China, Iran, Cuba), (c) swing states (India, Brazil, "
            "South Africa, Indonesia, Nigeria)\n"
            "3. For each swing state, analyzes which direction they lean on specific sub-issues and why\n"
            "4. Proposes an EU strategy for winning over at least 2 swing states with specific concessions\n\n"
            "This exercise is what real diplomats do when preparing for multilateral negotiations."
        ),
        "hints": (
            "The UN GGE (Group of Governmental Experts) produced consensus norms in 2015 and 2021;"
            "The OEWG (Open-Ended Working Group) is the parallel, more inclusive process;"
            "Russia and China favor a new treaty under UN auspices; Western states prefer voluntary norms;"
            "India is a swing state: it values sovereignty but also has a massive tech sector;"
            "Brazil's Marco Civil da Internet is a rights-based framework that aligns somewhat with EU values;"
            "The Freedom Online Coalition includes 38 states committed to internet freedom"
        ),
        "sample_answer": (
            "A sophisticated matrix would plot 12+ countries across the four dimensions, clearly delineate "
            "the three blocs, show that India leans sovereignty on surveillance but freedom on commerce, "
            "that Brazil aligns with the EU on rights but the Global South on development, and propose EU "
            "concessions on technology transfer and capacity building to win over India and Brazil."
        ),
        "key_concepts": "country matrix, bloc building, cyber norms, GGE, OEWG, swing states, EU strategy",
    },
    {
        "category_type": "RESEARCH",
        "difficulty": "ADV",
        "title": "Strategic Use of Precedent on Responsibility to Protect",
        "prompt": (
            "You are representing Brazil in the Security Council. The topic is 'The Responsibility to "
            "Protect (R2P) and Humanitarian Intervention.'\n\n"
            "Brazil authored the concept of 'Responsibility While Protecting' (RWP) as a response to NATO's "
            "intervention in Libya (2011). Write a strategic precedent analysis (600-800 words) that:\n\n"
            "1. Traces the evolution of R2P from the 2001 ICISS report through the 2005 World Summit Outcome "
            "Document (A/RES/60/1, paragraphs 138-139) to its application in Libya (S/RES/1973)\n"
            "2. Analyzes why the Libya intervention generated backlash — what went wrong with R2P's "
            "implementation? How did regime change exceed the mandate?\n"
            "3. Explains Brazil's RWP concept: accountability for those who intervene, not just those who "
            "are targeted for intervention\n"
            "4. Examines subsequent cases where R2P was invoked or could have been invoked (Syria, Myanmar, "
            "Yemen) and why the Security Council failed to act\n"
            "5. Uses these precedents strategically to argue for a reformed R2P framework that includes "
            "accountability mechanisms for intervening states\n"
            "6. References at least 4 specific UN documents throughout\n\n"
            "This exercise demonstrates how precedent can be wielded as a diplomatic tool."
        ),
        "hints": (
            "A/RES/60/1 paragraphs 138-139 are the foundational R2P text adopted by world leaders in 2005;"
            "S/RES/1973 (2011) authorized the no-fly zone over Libya but was interpreted to support regime change;"
            "Brazil circulated the RWP concept note as A/66/551-S/2011/701;"
            "Russia and China vetoed Syria resolutions partly due to Libya precedent concerns;"
            "The Secretary-General issues annual reports on R2P implementation"
        ),
        "sample_answer": (
            "A masterful precedent analysis would trace R2P's trajectory from concept to contested practice, "
            "demonstrate how Libya's misapplication poisoned the well for Syria and beyond, present Brazil's "
            "RWP as a constructive reform rather than rejection of R2P, cite A/RES/60/1, S/RES/1973, and "
            "Brazil's concept note to build an airtight argumentative chain, and propose specific accountability "
            "mechanisms (e.g., post-intervention review by the ICJ or an independent panel) that would restore "
            "R2P's legitimacy while preventing mandate overreach."
        ),
        "key_concepts": "R2P, Responsibility While Protecting, Libya, precedent analysis, Brazil, humanitarian intervention, Security Council",
    },
]

# ── PROCEDURE QUESTIONS ───────────────────────────────────────────────────────
QUESTIONS += [
    # ── BEGINNER (10) ────────────────────────────────────────────────────────
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "Understanding the Speakers List",
        "prompt": (
            "You are a first-time delegate at a Model UN conference. The committee session has just begun, "
            "and the Chair announces: 'The floor is now open for the Speakers List on the topic of "
            "International Cooperation on Climate Change. Delegates wishing to be added to the Speakers "
            "List, please raise your placards.'\n\n"
            "You are not sure what to do. Answer the following questions in 200-250 words:\n\n"
            "1. What is the Speakers List, and what is its purpose in a MUN committee?\n"
            "2. How do you get added to the Speakers List?\n"
            "3. What happens when it is your turn to speak? How long do you typically get?\n"
            "4. What does it mean when the Speakers List is 'exhausted' or 'closed'?\n"
            "5. Can you be on the Speakers List more than once?"
        ),
        "hints": (
            "The Speakers List is the primary formal mode of debate in committee;"
            "Raise your placard when the Chair asks — the Chair adds your country name to the list;"
            "Speaking time is usually 60-90 seconds, set at the beginning of committee;"
            "When no one is left on the list, debate on the topic closes and the committee moves to voting"
        ),
        "sample_answer": (
            "A good answer would explain that the Speakers List is the formal queue for speeches on the "
            "topic, that delegates raise placards to be added, that they receive the set speaking time when "
            "called, that an exhausted list closes debate, and that delegates can be added multiple times "
            "but may not appear consecutively."
        ),
        "key_concepts": "speakers list, formal debate, placard, speaking time, exhausted list",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "How to Raise Your Placard",
        "prompt": (
            "You are representing Kenya in the General Assembly and it is your first committee session. "
            "The Chair keeps saying 'Raise your placards' at different moments during the session — to "
            "join the Speakers List, to vote on motions, and to show support for proposals.\n\n"
            "Write a brief guide (200-250 words) for a fellow first-time delegate explaining:\n\n"
            "1. What is a placard in MUN? What does it look like?\n"
            "2. When should you raise your placard? (List at least 3 different situations)\n"
            "3. What is the difference between raising your placard to speak and raising it to vote?\n"
            "4. What happens if you raise your placard at the wrong time?\n"
            "5. Can you ever lower your placard after raising it during a vote?"
        ),
        "hints": (
            "A placard is a nameplate with your country name — it sits in front of you on the desk;"
            "Raise it when: the Chair opens the Speakers List, when voting on motions, when called for a roll call;"
            "During a procedural vote, you must vote yes or no (no abstentions usually);"
            "Raising your placard at the wrong time is not penalized but may confuse the Chair"
        ),
        "sample_answer": (
            "A helpful guide would describe the placard as a country nameplate, list situations where it "
            "is raised (Speakers List, voting, requesting to be recognized), distinguish between speaking "
            "and voting uses, note that mistimed raises are awkward but not penalized, and explain that "
            "votes are generally final once counted."
        ),
        "key_concepts": "placard, voting, recognition, formal procedure, committee etiquette",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "Motions vs. Points: What's the Difference?",
        "prompt": (
            "You are a delegate in the Economic and Social Council (ECOSOC). During committee, you hear "
            "other delegates say things like 'Motion for a moderated caucus' and 'Point of inquiry.' "
            "You are confused about the difference between motions and points.\n\n"
            "Write a clear explanation (200-300 words) that covers:\n\n"
            "1. What is a motion in MUN? Give 3 examples of common motions.\n"
            "2. What is a point in MUN? Give 3 examples of common points.\n"
            "3. What is the key difference between a motion and a point?\n"
            "4. Do motions require a vote? Do points?\n"
            "5. Which takes precedence — a motion or a point? Why?"
        ),
        "hints": (
            "Motions propose an action for the committee (e.g., move to caucus, close debate);"
            "Points are requests directed at the Chair (e.g., point of order, point of inquiry);"
            "Motions require a vote (simple majority); points do not;"
            "Points of order take precedence because they address procedural violations"
        ),
        "sample_answer": (
            "A clear explanation would define motions as proposals that change what the committee does "
            "(caucus, close debate, table a topic), define points as requests to the Chair (order, inquiry, "
            "personal privilege), explain that motions require votes while points don't, and note that "
            "points of order interrupt and take precedence because they address rule violations."
        ),
        "key_concepts": "motions, points, point of order, point of inquiry, procedural basics, voting",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "Yielding Your Speaking Time",
        "prompt": (
            "You are the delegate of Mexico and you have just finished your speech on the Speakers List "
            "with 20 seconds remaining. The Chair says: 'The delegate of Mexico, you have 20 seconds "
            "remaining. Do you wish to yield your time?'\n\n"
            "Explain the three types of yields available to you in 200-250 words:\n\n"
            "1. Yield to the Chair — what happens to the remaining time?\n"
            "2. Yield to another delegate — how does this work? Can they yield again?\n"
            "3. Yield to questions — what does this mean? Who asks the questions?\n\n"
            "For each type, explain when it would be strategically smart to use it."
        ),
        "hints": (
            "Yield to Chair = remaining time is forfeited and the Chair moves on;"
            "Yield to another delegate = your ally gets to speak using your remaining time;"
            "Yield to questions = other delegates can ask you follow-up questions;"
            "Yielding to an ally is great for coalition building; yielding to questions shows confidence"
        ),
        "sample_answer": (
            "A strong answer would describe all three yields, explain that yielding to the Chair forfeits "
            "time, yielding to a delegate gives an ally speaking opportunity (no re-yield allowed), and "
            "yielding to questions invites scrutiny but demonstrates mastery. Strategically, yield to an "
            "ally to amplify your bloc's message, or yield to questions if you are confident."
        ),
        "key_concepts": "yielding time, yield to Chair, yield to delegate, yield to questions, speaking strategy",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "Setting the Agenda",
        "prompt": (
            "Your committee — the General Assembly Second Committee (ECOFIN) — has two topics on the "
            "agenda:\n"
            "  Topic A: 'Financing Sustainable Development in Least Developed Countries'\n"
            "  Topic B: 'Regulating Cryptocurrency and Digital Financial Systems'\n\n"
            "The Chair opens the floor for motions to set the agenda. Two delegates raise their placards. "
            "Delegate A moves to set Topic A first; Delegate B moves to set Topic B first.\n\n"
            "Explain the agenda-setting process in 200-250 words:\n\n"
            "1. Why does the committee need to set an agenda? Can it debate both topics simultaneously?\n"
            "2. How do delegates make a motion to set the agenda?\n"
            "3. What happens after two competing motions are proposed? How does the committee decide?\n"
            "4. Does the committee always get to both topics? What determines this?\n"
            "5. Can you speak for or against a motion to set the agenda?"
        ),
        "hints": (
            "Committees debate one topic at a time — the agenda determines the order;"
            "Each delegate making the motion gets a brief speech (usually 30 seconds) to argue for their preferred topic;"
            "The committee votes — simple majority wins;"
            "Whether the second topic is reached depends on how quickly the first topic concludes;"
            "One speaker for and one against each motion is standard"
        ),
        "sample_answer": (
            "A good answer would explain that committees debate sequentially, describe the motion-and-vote "
            "process, note that speakers for and against are heard before voting, explain that the second "
            "topic is reached only if time permits, and note that strategic delegates consider which topic "
            "benefits their country more when deciding how to vote."
        ),
        "key_concepts": "agenda setting, motion, committee procedure, topic selection, simple majority",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "Moderated vs. Unmoderated Caucus",
        "prompt": (
            "Your Chair has just asked: 'Are there any motions on the floor?' Two delegates raise their "
            "placards:\n"
            "  - Delegate A: 'Motion for a moderated caucus, 10 minutes, speaking time 1 minute, on the "
            "    topic of renewable energy solutions.'\n"
            "  - Delegate B: 'Motion for an unmoderated caucus, 15 minutes.'\n\n"
            "The Chair asks the committee to vote on these motions. Explain in 250-300 words:\n\n"
            "1. What is a moderated caucus? How does it work? Who controls the flow?\n"
            "2. What is an unmoderated caucus? How does it work? What do delegates do during one?\n"
            "3. What are the key differences between the two?\n"
            "4. When would you propose a moderated caucus vs. an unmoderated caucus?\n"
            "5. In this scenario, which motion is voted on first? Why?"
        ),
        "hints": (
            "Moderated: delegates raise placards, Chair calls on speakers, structured and formal;"
            "Unmoderated: delegates leave their seats and talk freely, informal;"
            "Moderated caucuses have a specific sub-topic; unmoderated caucuses are for negotiation and drafting;"
            "The most disruptive motion (unmoderated, as delegates leave seats) is typically voted on last"
        ),
        "sample_answer": (
            "A clear answer would describe moderated caucuses as structured debates with a sub-topic and "
            "timed speeches, unmoderated caucuses as free-form negotiation periods, highlight that moderated "
            "caucuses are Chair-controlled while unmoderated are delegate-driven, explain that moderated "
            "caucuses focus debate while unmoderated enables alliance-building, and note that less disruptive "
            "motions are voted on first."
        ),
        "key_concepts": "moderated caucus, unmoderated caucus, informal debate, negotiation, motions",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "Understanding Right of Reply",
        "prompt": (
            "You are representing Iran in the General Assembly First Committee (DISEC). During a speech, "
            "the delegate of Israel directly criticizes Iran's nuclear program, saying: 'Iran's reckless "
            "pursuit of nuclear weapons threatens the entire Middle East.'\n\n"
            "You feel your country has been misrepresented. Your advisor mentions you can request a "
            "'Right of Reply.' Answer these questions in 200-250 words:\n\n"
            "1. What is a Right of Reply?\n"
            "2. When can you request one? What triggers the right?\n"
            "3. How do you formally request it? Do you raise your placard or send a note to the Chair?\n"
            "4. How long is a Right of Reply speech typically?\n"
            "5. Is the Right of Reply guaranteed, or is it at the Chair's discretion?\n"
            "6. What should you say — and not say — in a Right of Reply?"
        ),
        "hints": (
            "Right of Reply is granted when a delegate feels their country has been directly and inaccurately referenced;"
            "It is usually requested in writing (a note to the Chair);"
            "Speaking time is shorter than regular speeches — usually 30-60 seconds;"
            "It is at the Chair's discretion — the Chair may deny it;"
            "Stay diplomatic — do not escalate or make personal attacks"
        ),
        "sample_answer": (
            "A good answer would define Right of Reply as a procedural tool to address direct "
            "misrepresentation, explain the written request process, note the shortened speaking time, "
            "emphasize that the Chair decides whether to grant it, and advise the delegate to correct "
            "factual errors diplomatically rather than attacking the other delegate."
        ),
        "key_concepts": "right of reply, procedural rights, diplomatic response, Chair's discretion",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "Basic Voting Procedures",
        "prompt": (
            "The committee has completed debate on a draft resolution. The Chair announces: 'We will now "
            "move into voting procedure. The doors are sealed. No delegate may enter or leave the committee "
            "room. There will be no communication with outside parties.'\n\n"
            "As a first-time delegate, explain the basic voting procedure in 200-300 words:\n\n"
            "1. What does it mean when the doors are 'sealed' and why does this happen?\n"
            "2. What is a simple majority? What is a two-thirds majority? When is each required?\n"
            "3. What are the voting options: Yes, No, Abstain? Can you always abstain?\n"
            "4. What is a roll call vote? How is it different from a placard vote?\n"
            "5. What does 'Yes with rights' or 'No with rights' mean in a roll call vote?"
        ),
        "hints": (
            "Sealing the doors ensures no outside influence during voting — it is a rule in most conferences;"
            "Simple majority = more than half of those voting; two-thirds is needed for some procedural motions;"
            "In General Assembly substantive votes, you can abstain; in procedural votes, you usually cannot;"
            "Roll call: each country is called alphabetically and states its vote aloud;"
            "'With rights' means you will explain your vote after the result is announced"
        ),
        "sample_answer": (
            "A clear answer would explain that sealed doors prevent outside influence, define simple and "
            "two-thirds majorities, distinguish between procedural (no abstention) and substantive (abstention "
            "allowed) votes, describe roll call as alphabetical oral voting, and explain that 'with rights' "
            "allows a brief explanation of vote after the result."
        ),
        "key_concepts": "voting procedure, simple majority, two-thirds majority, roll call, abstention, sealed doors",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "The Role of the Chair",
        "prompt": (
            "You are at your first MUN conference. The person at the front of the room keeps saying things "
            "like 'The motion is in order,' 'The delegate is out of order,' and 'The Chair recognizes the "
            "delegate of Brazil.' You want to understand the Chair's role.\n\n"
            "Write a brief explanation (200-250 words) covering:\n\n"
            "1. Who is the Chair (or President/Director)? Are they a delegate?\n"
            "2. What are the Chair's main responsibilities? List at least 4.\n"
            "3. What does it mean when the Chair says something is 'in order' or 'out of order'?\n"
            "4. Can you disagree with the Chair? If so, how?\n"
            "5. How should you address the Chair when speaking?"
        ),
        "hints": (
            "The Chair is a student (or sometimes staff) who runs the committee — they are not a delegate;"
            "Responsibilities: manage speakers list, recognize delegates, rule on motions, maintain decorum;"
            "'In order' = procedurally correct; 'Out of order' = violates rules of procedure;"
            "You can appeal the Chair's decision — this requires a vote from the committee;"
            "Address the Chair as 'Honorable Chair' or 'Mr./Madam Chair'"
        ),
        "sample_answer": (
            "A good explanation would identify the Chair as a non-delegate committee leader, list managing "
            "the speakers list, ruling on motions, maintaining order, and recognizing speakers as key duties, "
            "define in/out of order in procedural terms, explain that the appeal process allows the committee "
            "to override the Chair by vote, and note proper forms of address."
        ),
        "key_concepts": "Chair, dais, in order, out of order, appeal, committee management, decorum",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "BEG",
        "title": "How to Submit a Working Paper",
        "prompt": (
            "You and several other delegates have been drafting ideas during unmoderated caucuses. Your "
            "bloc leader says it is time to 'submit a working paper' to the Chair. You are not sure what "
            "this means or how it works.\n\n"
            "Write a brief guide (200-250 words) explaining:\n\n"
            "1. What is a working paper? How is it different from a draft resolution?\n"
            "2. What should a working paper contain?\n"
            "3. How do you submit it? To whom? Does it need signatures?\n"
            "4. What happens after the working paper is submitted — does the Chair review it?\n"
            "5. Can the working paper be changed after submission?"
        ),
        "hints": (
            "A working paper is an informal document that outlines your bloc's ideas — it is not yet a formal draft resolution;"
            "It does not need to follow UN resolution format but should have clear proposals;"
            "Submit it to the Chair or dais — some conferences require a minimum number of signatories;"
            "The Chair reviews it and may suggest changes before it is introduced to the committee;"
            "Working papers can be revised — they are not binding until adopted as a draft resolution"
        ),
        "sample_answer": (
            "A helpful guide would distinguish working papers as informal idea documents (no formal format "
            "required) from draft resolutions (formal UN format), explain that they contain key proposals, "
            "describe submission to the dais with required signatories, note the Chair's review and "
            "introduction to committee, and emphasize that working papers are living documents that evolve."
        ),
        "key_concepts": "working paper, draft resolution, submission process, signatories, informal document",
    },
    # ── INTERMEDIATE (10) ────────────────────────────────────────────────────
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Strategic Use of Motion to Table",
        "prompt": (
            "You are representing Russia in the Security Council. A draft resolution on imposing sanctions "
            "against a country your government supports is gaining momentum. You believe it might pass if "
            "it comes to a vote now. However, you want to delay the vote to buy time for diplomatic "
            "negotiations outside committee.\n\n"
            "A motion to table the draft resolution could serve your purpose. Write an analysis "
            "(300-400 words) that:\n\n"
            "1. Explains what a motion to table means — what happens to the draft resolution?\n"
            "2. Describes how the motion is introduced and voted on\n"
            "3. Explains the difference between tabling (temporary delay) and withdrawing a resolution\n"
            "4. Analyzes when tabling is strategically useful — give 2-3 scenarios\n"
            "5. Discusses the risks: can your opponents use procedural moves to bring it back?\n"
            "6. Notes whether Russia should use this motion or save its veto for the actual vote\n\n"
            "Think about this as a strategic decision, not just a procedural question."
        ),
        "hints": (
            "Tabling postpones consideration indefinitely — but it can be brought back with a motion to reconsider;"
            "A motion to table requires a simple majority and is non-debatable in most rules;"
            "Tabling is useful when you might lose a straight vote but think the political situation may shift;"
            "Using a veto is a last resort — it carries political cost. Procedural maneuvers cost less;"
            "If the motion to table fails, you have revealed your opposition without actually blocking anything"
        ),
        "sample_answer": (
            "A strategic analysis would explain tabling as postponement without withdrawal, note it requires "
            "simple majority with no debate, contrast it with the political cost of a veto, identify scenarios "
            "like waiting for new information or building a blocking minority, and advise Russia to attempt "
            "tabling first to avoid the diplomatic fallout of a veto, while keeping the veto in reserve."
        ),
        "key_concepts": "motion to table, strategic delay, veto, Security Council, procedural strategy, tabling vs withdrawal",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Roll Call vs. Placard Voting",
        "prompt": (
            "Your committee is about to vote on a contentious draft resolution on nuclear disarmament. "
            "A delegate raises their placard and says: 'Motion for a roll call vote.' Another delegate "
            "seems confused and asks why a roll call vote is different from a regular vote.\n\n"
            "Write a detailed explanation (300-400 words) that:\n\n"
            "1. Describes how a placard (show-of-hands) vote works\n"
            "2. Describes how a roll call vote works step by step\n"
            "3. Explains why a delegate would request a roll call vote — what strategic advantage does it provide?\n"
            "4. Describes the options available in a roll call vote: Yes, No, Abstain, Pass, Yes with Rights, "
            "No with Rights\n"
            "5. Explains what 'Pass' means in a roll call vote and when it is strategic to pass\n"
            "6. Notes whether the motion for roll call vote is debatable and what majority it requires"
        ),
        "hints": (
            "Placard vote is quick: raise placard for yes, no, or abstain — votes are counted visually;"
            "Roll call: the Chair reads each country alphabetically; each delegate states their vote aloud;"
            "Roll call makes every country's vote public and on the record — this creates accountability;"
            "'Pass' means you defer your vote to the end of the roll call — useful for swing states;"
            "The motion for roll call vote requires a simple majority and is not debatable"
        ),
        "sample_answer": (
            "A thorough explanation would contrast the quick, anonymous nature of placard votes with the "
            "transparent, recorded nature of roll call votes, explain that roll call creates diplomatic "
            "accountability, detail all voting options including Pass (defer to second round), and note "
            "the strategic value of requesting roll call to pressure swing states into taking a public stance."
        ),
        "key_concepts": "roll call vote, placard vote, voting options, pass, accountability, voting strategy",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Points of Order vs. Points of Inquiry",
        "prompt": (
            "During a heated moderated caucus on humanitarian intervention, two delegates raise points:\n\n"
            "Delegate A: 'Point of order! The previous speaker exceeded their speaking time by 15 seconds "
            "and the Chair did not intervene.'\n\n"
            "Delegate B: 'Point of inquiry. Could the Chair please clarify whether working papers need to "
            "be submitted in duplicate?'\n\n"
            "Write an analysis (300-400 words) explaining:\n\n"
            "1. What is a Point of Order? When is it appropriate to raise one?\n"
            "2. What is a Point of Inquiry (or Point of Parliamentary Inquiry)? When is it appropriate?\n"
            "3. What is a Point of Personal Privilege? Give an example.\n"
            "4. Which of these points can interrupt a speaker? Which cannot?\n"
            "5. How should the Chair respond to each type of point?\n"
            "6. When do delegates misuse these points, and how does the Chair handle abuse?"
        ),
        "hints": (
            "Point of Order: raised when you believe the rules of procedure have been violated;"
            "Point of Inquiry: a question to the Chair about procedure — NOT about content;"
            "Point of Personal Privilege: raised when you cannot hear, the room is too cold, etc.;"
            "Only Point of Order and Point of Personal Privilege can interrupt a speaker;"
            "Chairs rule points 'well taken' or 'not well taken' — their ruling can be appealed"
        ),
        "sample_answer": (
            "A strong analysis would define each point type, explain that Points of Order address rule "
            "violations and can interrupt speakers, Points of Inquiry are procedural questions to the Chair "
            "that cannot interrupt, and Points of Personal Privilege address physical comfort and can "
            "interrupt. It would note that the Chair rules on validity and that misusing points to make "
            "political statements is ruled out of order."
        ),
        "key_concepts": "point of order, point of inquiry, point of personal privilege, interruption, Chair ruling",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Friendly vs. Unfriendly Amendments",
        "prompt": (
            "Your committee is considering a draft resolution on climate change. The draft has 12 operative "
            "clauses. The delegate of India wants to add a new clause about technology transfer. The delegate "
            "of Canada wants to remove a clause about mandatory emissions targets.\n\n"
            "Write an explanation (300-400 words) covering:\n\n"
            "1. What is an amendment to a draft resolution? What can it change?\n"
            "2. What is the difference between a friendly amendment and an unfriendly amendment?\n"
            "3. Who decides whether an amendment is friendly or unfriendly?\n"
            "4. What is the process for introducing an unfriendly amendment? Does it require a vote?\n"
            "5. Can you amend an amendment? Is there a limit?\n"
            "6. In the scenario above, analyze whether India's and Canada's changes would likely be "
            "friendly or unfriendly, and why."
        ),
        "hints": (
            "Amendments can add, remove, or modify operative clauses — NOT preambulatory clauses;"
            "Friendly amendment: all sponsors of the original draft agree to the change — no vote needed;"
            "Unfriendly amendment: sponsors do not agree — it must be voted on by the committee;"
            "You cannot amend an amendment (no second-degree amendments in most MUN rules);"
            "India's addition might be friendly if it aligns with sponsors' interests; Canada's removal of "
            "mandatory targets would likely be unfriendly if the sponsors favor binding commitments"
        ),
        "sample_answer": (
            "A clear explanation would define amendments as changes to operative clauses, distinguish friendly "
            "(sponsor-approved, no vote) from unfriendly (contested, requires committee vote), explain that "
            "sponsors decide whether to accept an amendment as friendly, note the ban on second-degree "
            "amendments, and analyze that India's technology transfer clause is likely friendly while Canada's "
            "removal of mandatory targets would be unfriendly."
        ),
        "key_concepts": "amendments, friendly amendment, unfriendly amendment, draft resolution, sponsors, operative clauses",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Division of the Question",
        "prompt": (
            "A draft resolution on 'Addressing the Humanitarian Crisis in Gaza' has 15 operative clauses. "
            "Most delegates support clauses 1-12, which address humanitarian aid delivery. However, clauses "
            "13-15 call for an arms embargo and referral to the ICC, which several delegations strongly oppose.\n\n"
            "The delegate of the United Kingdom raises: 'Motion for Division of the Question, to vote on "
            "operative clauses 13, 14, and 15 separately from the rest of the resolution.'\n\n"
            "Explain this procedure in 300-400 words:\n\n"
            "1. What is Division of the Question? When is it used?\n"
            "2. How does the voting work once the question is divided?\n"
            "3. What is the strategic purpose — why would the UK want this?\n"
            "4. Can the original sponsors object? How?\n"
            "5. What happens if the separated clauses fail but the rest passes?\n"
            "6. When might Division of the Question backfire on the country proposing it?"
        ),
        "hints": (
            "Division of the Question allows the committee to vote on specific clauses separately;"
            "The motion requires a simple majority to pass;"
            "The UK's strategy: save the humanitarian clauses while killing the accountability clauses;"
            "Sponsors can argue against the motion but cannot block it if the committee votes for it;"
            "If separated clauses fail, the resolution passes without them — it is effectively weakened"
        ),
        "sample_answer": (
            "A strong answer would explain division as separating a resolution into votable parts, describe "
            "the sequential voting process, identify the UK's strategy of isolating controversial clauses "
            "to preserve the humanitarian core, note that sponsors can only argue against the motion but not "
            "block it, and warn that division can backfire if it allows opponents to gut the most meaningful "
            "provisions while passing a watered-down text."
        ),
        "key_concepts": "division of the question, clause-by-clause voting, strategic procedure, draft resolution, UN voting",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Appealing the Chair's Decision",
        "prompt": (
            "During committee, the Chair rules a motion 'out of order.' The delegate who proposed the "
            "motion strongly disagrees and believes the Chair misinterpreted the rules. The delegate "
            "raises their placard and says: 'I would like to appeal the decision of the Chair.'\n\n"
            "Write a detailed explanation (300-400 words) covering:\n\n"
            "1. What does it mean to appeal the Chair's decision?\n"
            "2. What is the process? Is it debatable? What vote is required to overturn?\n"
            "3. What happens if the appeal succeeds? What if it fails?\n"
            "4. When is it appropriate to appeal vs. when is it disruptive or disrespectful?\n"
            "5. How do experienced delegates use the threat of an appeal without actually making one?\n"
            "6. Can the Chair retaliate against a delegate who appeals? (Hint: they shouldn't, but...)"
        ),
        "hints": (
            "An appeal challenges the Chair's ruling and puts it to a committee vote;"
            "Usually, one speaker for and one speaker against the appeal is allowed;"
            "Overturning requires a two-thirds majority in most rules (the Chair's ruling stands by default);"
            "Appeals should be reserved for genuine procedural errors — frivolous appeals waste committee time;"
            "The implicit threat of an appeal can cause the Chair to reconsider without a formal challenge"
        ),
        "sample_answer": (
            "A thorough explanation would describe the appeal as a democratic check on the Chair's power, "
            "outline the debate-and-vote process, note the high bar (two-thirds) for overturning, distinguish "
            "legitimate appeals from disruptive ones, explain that experienced delegates use the implied "
            "threat of appeal to get the Chair to reconsider, and note that while Chairs should not retaliate, "
            "repeatedly challenging the Chair can affect a delegate's relationship with the dais."
        ),
        "key_concepts": "appeal, Chair's decision, two-thirds majority, procedural challenge, committee dynamics",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Suspension vs. Adjournment of the Meeting",
        "prompt": (
            "It is the end of Day 1 of a two-day conference. The Chair says: 'The Chair will now entertain "
            "a motion for suspension of the meeting.' A confused delegate asks: 'Is that the same as "
            "adjournment?'\n\n"
            "Write a clear explanation (250-350 words) covering:\n\n"
            "1. What is suspension of the meeting? When does it happen?\n"
            "2. What is adjournment of the meeting? When does it happen?\n"
            "3. What is adjournment of debate? How is it different from the other two?\n"
            "4. Which of these is used at the end of a session day? Which at the end of the conference?\n"
            "5. Are these motions debatable? What majority do they require?\n"
            "6. Why does the distinction matter?"
        ),
        "hints": (
            "Suspension = pause the meeting with intent to resume later (e.g., lunch break, end of day);"
            "Adjournment of the meeting = end the meeting permanently (end of conference);"
            "Adjournment of debate = stop debate on the current topic (not the whole meeting);"
            "Suspension is used between sessions; adjournment is used at the very end;"
            "These motions are not debatable and require a simple majority"
        ),
        "sample_answer": (
            "A clear explanation would define suspension as a temporary pause (lunch, overnight), "
            "adjournment of the meeting as permanent closure (end of conference), and adjournment of "
            "debate as stopping discussion on the current topic while the meeting continues. It would "
            "note that confusion between these terms is common, that all are non-debatable with simple "
            "majority requirements, and that using the wrong term signals procedural inexperience."
        ),
        "key_concepts": "suspension, adjournment, adjournment of debate, meeting management, procedural terminology",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Managing Speaking Time Strategically",
        "prompt": (
            "You are an experienced delegate representing the United Kingdom in a General Assembly committee. "
            "The committee is debating 'Reform of International Financial Institutions.' You notice that "
            "the current moderated caucus has 1-minute speaking times, which feels too long for the "
            "narrow sub-topic being discussed. You also realize that shorter speaking times would allow "
            "more countries to speak, increasing your bloc's visibility.\n\n"
            "Write a strategic analysis (300-400 words) covering:\n\n"
            "1. How does a delegate propose a moderated caucus with specific speaking times?\n"
            "2. What factors should you consider when choosing the total caucus time and individual "
            "speaking time? (e.g., 10 minutes with 30-second speaking time vs. 10 minutes with 1-minute)\n"
            "3. How can you use speaking time strategically to advantage your bloc?\n"
            "4. When should you motion for a moderated caucus with longer speaking times?\n"
            "5. What is the Chair's role in setting or modifying speaking times?"
        ),
        "hints": (
            "The motion must specify: total time, individual speaking time, and sub-topic;"
            "Shorter speaking times (30 sec) = more speakers but less depth; longer (90 sec) = fewer but richer;"
            "If your bloc has many members, shorter times mean more of your allies get airtime;"
            "If you have a complex argument to make, propose longer times so you can develop your point;"
            "The Chair may suggest modifications to the motion before putting it to a vote"
        ),
        "sample_answer": (
            "A strategic analysis would explain the motion format, weigh the trade-offs between speaker "
            "count and speech depth, recommend shorter times when your bloc has numerical advantage, longer "
            "times when your position requires detailed argumentation, and note that the Chair can modify "
            "but the proposing delegate decides whether to accept the modification."
        ),
        "key_concepts": "speaking time, moderated caucus, bloc strategy, time management, motion format",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Consensus vs. Majority Voting",
        "prompt": (
            "Your committee has been debating for two days and has produced a draft resolution that most "
            "delegates support. The Chair asks: 'Is there any objection to adopting this resolution by "
            "consensus?' Three delegates look unsure about what this means.\n\n"
            "Write an explanation (300-400 words) covering:\n\n"
            "1. What is consensus in the UN/MUN context? Is it the same as unanimity?\n"
            "2. How does consensus adoption work procedurally?\n"
            "3. What happens if one delegate objects to consensus?\n"
            "4. Why do committees prefer consensus over voting? What are the political advantages?\n"
            "5. In what situations is consensus impossible and voting necessary?\n"
            "6. Name a real UN body that operates primarily by consensus (and why it does so)."
        ),
        "hints": (
            "Consensus means no delegation formally objects — it does not mean everyone agrees;"
            "A single objection breaks consensus and forces a vote;"
            "Consensus resolutions carry more political weight because they show broad agreement;"
            "The General Assembly often adopts resolutions by consensus — but can also vote;"
            "The Conference on Disarmament operates by consensus, which has led to decades of deadlock"
        ),
        "sample_answer": (
            "A thorough explanation would distinguish consensus (no objection) from unanimity (all vote yes), "
            "describe the 'any objection?' procedure, explain that a single objection triggers a vote, note "
            "that consensus gives resolutions stronger political legitimacy, identify that controversial "
            "topics like disarmament often cannot achieve consensus, and cite the Conference on Disarmament "
            "as an example where the consensus rule has caused paralysis."
        ),
        "key_concepts": "consensus, majority voting, unanimity, political legitimacy, Conference on Disarmament",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "INT",
        "title": "Procedural Flow of a Committee Session",
        "prompt": (
            "A new delegate asks you: 'I'm confused about the order of everything. Can you walk me through "
            "what happens from the moment committee starts to the moment we vote on a resolution?'\n\n"
            "Write a step-by-step guide (350-450 words) covering the typical flow of an MUN committee "
            "session from start to finish:\n\n"
            "1. Roll Call — what happens and what are the two attendance options?\n"
            "2. Setting the Agenda — how and why\n"
            "3. Opening the Speakers List — formal debate begins\n"
            "4. Moderated and Unmoderated Caucuses — when and why they interrupt formal debate\n"
            "5. Working Papers → Draft Resolutions — the document evolution\n"
            "6. Introducing Draft Resolutions — what the sponsors do\n"
            "7. Amendments — the last chance to change the text\n"
            "8. Closure of Debate — how debate ends\n"
            "9. Voting Procedure — how the resolution is adopted or rejected\n\n"
            "For each step, write 2-3 sentences explaining what happens."
        ),
        "hints": (
            "Roll Call: delegates answer 'Present' or 'Present and Voting' — the latter means no abstaining;"
            "The flow is not always linear — caucuses interrupt formal debate throughout;"
            "Working papers become draft resolutions once they have enough signatories and the Chair approves;"
            "Closure of debate requires a motion and two-thirds majority;"
            "Voting procedure seals the room — no entry, exit, or outside communication"
        ),
        "sample_answer": (
            "A comprehensive guide would walk through all nine steps sequentially, noting that 'Present "
            "and Voting' commits you to yes or no, that agenda setting determines topic order, that caucuses "
            "are proposed via motions throughout debate, that working papers evolve into drafts with sponsors "
            "and signatories, that closure requires two-thirds, and that voting seals the room for final "
            "adoption or rejection."
        ),
        "key_concepts": "committee flow, roll call, speakers list, caucus, draft resolution, voting procedure, closure of debate",
    },
    # ── ADVANCED (10) ────────────────────────────────────────────────────────
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Controlling Committee Flow Through Procedural Motions",
        "prompt": (
            "You are an experienced delegate representing the United States in the Security Council. The "
            "committee is debating 'The Situation in the South China Sea.' China is pushing a draft "
            "resolution that would affirm sovereignty over disputed features. You want to slow down "
            "China's momentum without using your veto yet.\n\n"
            "Write a strategic playbook (500-600 words) for using procedural motions to control committee "
            "flow:\n\n"
            "1. How can you use moderated caucus motions to shift the sub-topic away from China's "
            "preferred framing?\n"
            "2. When should you motion for an unmoderated caucus to break China's momentum in formal debate?\n"
            "3. How can you use the motion to table or adjourn debate to delay a vote?\n"
            "4. What is the strategic value of proposing amendments to water down China's draft?\n"
            "5. When should you motion for closure of debate — and when should you block it?\n"
            "6. At what point do you stop using procedural tools and resort to the veto?\n\n"
            "Include specific motion language you would use for at least 3 of these moves."
        ),
        "hints": (
            "Moderated caucuses on sub-topics you choose can redirect the conversation away from China's draft;"
            "Unmoderated caucuses break formal debate momentum and give you time to lobby;"
            "Motion to table requires simple majority; it postpones without killing the resolution;"
            "Amendments force the committee to debate your changes, consuming time and shifting focus;"
            "Closure of debate requires two-thirds — if you have more than one-third allies, you can block it"
        ),
        "sample_answer": (
            "A sophisticated playbook would detail specific motion language for redirecting caucuses, "
            "explain the timing of unmoderated breaks to disrupt momentum, outline amendment strategy to "
            "dilute the draft, describe blocking closure of debate with a one-third minority, and advise "
            "saving the veto as a last resort since it carries significant diplomatic costs."
        ),
        "key_concepts": "procedural control, Security Council, strategic motions, veto, committee flow, amendment strategy",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Strategic Motion Sequencing to Block a Resolution",
        "prompt": (
            "You are representing Saudi Arabia in the Human Rights Council. A draft resolution critical "
            "of your country's human rights record has been submitted with enough signatories to be "
            "introduced. You do not have the votes to defeat it outright in a straight yes/no vote.\n\n"
            "Design a step-by-step procedural strategy (500-600 words) to prevent this resolution from "
            "passing:\n\n"
            "1. Step 1: What procedural motion do you introduce first? (Consider: motion for no action)\n"
            "2. Step 2: If Step 1 fails, what is your next move? (Consider: unfriendly amendments)\n"
            "3. Step 3: How do you use Division of the Question to your advantage?\n"
            "4. Step 4: Can you motion to adjourn debate before the vote?\n"
            "5. Step 5: If all else fails, what is your final procedural option?\n\n"
            "For each step, explain the procedural basis, the vote required, and the likelihood of success. "
            "Also analyze: at what point does aggressive procedural maneuvering become counterproductive?"
        ),
        "hints": (
            "A motion for no action (or 'no decision') asks the committee to take no action on the resolution — it requires simple majority;"
            "Unfriendly amendments to add language that other opponents also dislike can build a blocking coalition;"
            "Division of the Question can isolate the most offensive clauses for separate defeat;"
            "Adjournment of debate on the topic requires simple majority and effectively kills the resolution;"
            "Too many procedural maneuvers can alienate neutral delegates and make you look obstructionist"
        ),
        "sample_answer": (
            "A masterful strategy would sequence no-action motion first (lowest political cost), then "
            "introduce weakening amendments to peel off moderate supporters, use division of the question "
            "to isolate the most critical clauses, attempt adjournment of debate as a near-final move, and "
            "acknowledge that excessive procedural maneuvering risks backlash. The analysis would note that "
            "each failed motion makes the next harder to win as delegates grow impatient."
        ),
        "key_concepts": "motion sequencing, blocking strategy, no action motion, amendments, division of question, HRC",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Security Council Veto Mechanics",
        "prompt": (
            "You are an advisor to the delegation of China in the Security Council. The topic is "
            "'Sanctions on North Korea's Nuclear Program.' A new draft resolution proposes expanding "
            "sanctions. China has historically been cautious about excessive sanctions on North Korea.\n\n"
            "Write a comprehensive analysis (500-650 words) of the veto power and its strategic use:\n\n"
            "1. How does the veto work procedurally? What constitutes a 'negative vote' by a permanent member?\n"
            "2. What is the difference between a veto and an abstention by a P5 member? Can a P5 member "
            "abstain without blocking the resolution?\n"
            "3. What is a 'double veto' — vetoing both the substance and the procedural question of "
            "whether a matter is substantive?\n"
            "4. How has the veto been used historically on North Korea sanctions? Which P5 members have "
            "blocked or weakened resolutions?\n"
            "5. What are the political costs of a veto? When is it better to abstain and let a resolution "
            "pass rather than veto it?\n"
            "6. Recommend: should China veto, abstain, or negotiate amendments to this draft?"
        ),
        "hints": (
            "A negative vote by any P5 member on a substantive matter = veto — the resolution fails;"
            "A P5 abstention does NOT constitute a veto — the resolution can still pass with 9 yes votes;"
            "The 'double veto' occurs when a P5 member vetoes the preliminary question of whether an issue is substantive;"
            "China and Russia vetoed strengthened North Korea sanctions in 2022 for the first time;"
            "China often prefers to water down resolutions through negotiation rather than vetoing outright"
        ),
        "sample_answer": (
            "A thorough analysis would detail the Article 27 veto mechanism, distinguish veto from abstention "
            "with historical examples, explain the double veto concept, note China's 2022 veto on North Korea "
            "as a shift from its usual approach, analyze the reputational costs of vetoing, and recommend "
            "that China negotiate amendments to reduce sanctions scope rather than veto, reserving the veto "
            "for truly unacceptable provisions."
        ),
        "key_concepts": "veto, Security Council, P5, abstention, double veto, North Korea, China, Article 27",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Crisis Committee Procedure Differences",
        "prompt": (
            "You have been assigned to a crisis committee for the first time: the Joint Cabinet Crisis "
            "simulating the Cuban Missile Crisis (1962). You are playing Robert McNamara, US Secretary of "
            "Defense. The committee structure is completely different from what you are used to in General "
            "Assembly committees.\n\n"
            "Write a comprehensive guide (500-650 words) comparing crisis committee procedure with "
            "standard GA procedure:\n\n"
            "1. How does debate work differently in crisis? Is there a Speakers List? Moderated caucuses?\n"
            "2. What are crisis notes (or directives)? How do they replace draft resolutions?\n"
            "3. What is the role of the crisis staff (backroom)? How do they respond to delegate actions?\n"
            "4. How does the crisis arc work? What are crisis updates and how do they change the situation?\n"
            "5. What are personal directives vs. communal directives? When would McNamara use each?\n"
            "6. How is voting different — or is there voting at all?\n"
            "7. What skills transfer from GA to crisis, and what new skills are needed?"
        ),
        "hints": (
            "Crisis committees are faster and more flexible — the Speakers List may be abandoned entirely;"
            "Crisis notes/directives are short action documents that change the simulation's reality;"
            "The backroom staff adjudicates actions: they decide if your directive succeeds or fails;"
            "Crisis arcs are pre-planned events that escalate tension (e.g., a Soviet submarine is detected);"
            "Personal directives use your character's resources (McNamara controls the military); communal "
            "directives are committee-wide actions (e.g., issuing a presidential statement)"
        ),
        "sample_answer": (
            "A comprehensive guide would contrast the fluid, fast-paced crisis format with structured GA "
            "debate, explain directives as action-oriented replacements for resolutions, describe the "
            "backroom's role as both storyteller and referee, detail crisis arcs and updates, distinguish "
            "personal (McNamara ordering military readiness) from communal (cabinet issuing policy) directives, "
            "note that voting may be replaced by consensus or Chair discretion, and identify creative "
            "thinking and adaptability as crisis-specific skills."
        ),
        "key_concepts": "crisis committee, directives, backroom, crisis arc, personal directive, communal directive, McNamara",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Handling Multiple Draft Resolutions",
        "prompt": (
            "Your committee — the General Assembly First Committee (DISEC) — has produced THREE competing "
            "draft resolutions on 'Conventional Arms Control':\n\n"
            "  Draft 1 (Western bloc): Focuses on transparency, arms trade treaty strengthening\n"
            "  Draft 2 (NAM/G-77): Focuses on disarmament, technology transfer, development linkage\n"
            "  Draft 3 (Compromise): Merges elements of both, sponsored by a coalition of middle powers\n\n"
            "Write a strategic procedural analysis (500-600 words) covering:\n\n"
            "1. In what order are multiple draft resolutions voted on? Who decides?\n"
            "2. If Draft 1 passes, can the committee still vote on Drafts 2 and 3? Why or why not?\n"
            "3. What is a motion to vote on drafts in a specific order, and why is this strategically important?\n"
            "4. Can a delegate motion to merge or consolidate draft resolutions? How?\n"
            "5. If you support Draft 3 (compromise), what is your optimal procedural strategy?\n"
            "6. What happens if no draft resolution passes? Is there a 'failed committee' outcome?"
        ),
        "hints": (
            "Draft resolutions are typically voted on in the order they were submitted — but this can be challenged;"
            "In most MUN rules, passing one draft does NOT prevent voting on others — multiple can pass;"
            "However, if drafts contain contradictory clauses, the Chair may rule that a later draft supersedes;"
            "Merging drafts requires cooperation between sponsor groups and Chair facilitation;"
            "If you support Draft 3, you want it voted on last (after the other two potentially fail) or first "
            "(if you think it has the broadest support and passing it first may preempt the others)"
        ),
        "sample_answer": (
            "A strategic analysis would explain the default submission-order voting, describe how to motion "
            "for a different order, note that multiple drafts can pass unless contradictory, explain the "
            "merge process through informal negotiation, recommend Draft 3 supporters motion to vote it "
            "first to preempt polarization, and note that a committee can technically fail to pass any "
            "resolution — which is rare but acceptable."
        ),
        "key_concepts": "multiple draft resolutions, voting order, merging drafts, procedural strategy, DISEC",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Procedural Strategies for Small Delegations",
        "prompt": (
            "You are representing Tuvalu — a small Pacific Island nation with a 4-person delegation — "
            "at a large conference with 200+ delegates. You are in a General Assembly committee with 100 "
            "delegates. You cannot match the speaking time or bloc size of large delegations like the "
            "US, China, or the EU member states.\n\n"
            "Write a strategic guide (450-600 words) on how small delegations can use procedure to "
            "maximize their influence:\n\n"
            "1. How can you use the motion system to get your sub-topics onto the agenda?\n"
            "2. How should you target your moderated caucus proposals — broad topics or narrow ones?\n"
            "3. How can yielding time and yielding to questions amplify your visibility?\n"
            "4. What role should you play in the amendment process — sponsor or strategic signatory?\n"
            "5. How can you leverage your moral authority as a climate-vulnerable SIDS?\n"
            "6. What procedural moves should you avoid as a small delegation?"
        ),
        "hints": (
            "Small delegations should propose narrow moderated caucuses on their niche — this forces the "
            "committee to discuss your issue on your terms;"
            "Yielding to questions shows confidence and keeps you in the spotlight longer;"
            "As a signatory (not sponsor), you support without bearing the burden of defending the entire draft;"
            "Tuvalu's moral authority on climate is enormous — use it in every speech;"
            "Avoid: proposing motions you cannot win, leading blocs you cannot manage, or spreading too thin"
        ),
        "sample_answer": (
            "A smart guide would recommend proposing narrow sub-topic caucuses (e.g., 'sea-level rise impacts "
            "on sovereignty'), yielding to questions to demonstrate expertise, serving as strategic signatory "
            "on multiple drafts rather than sole sponsor, leveraging existential climate vulnerability for "
            "moral authority, and avoiding overextension by focusing on quality contributions over quantity."
        ),
        "key_concepts": "small delegation strategy, Tuvalu, SIDS, procedural leverage, moral authority, strategic signatory",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Closing Debate Strategically",
        "prompt": (
            "You are representing Germany in a General Assembly committee. Your bloc's draft resolution "
            "has strong support — you estimate at least 60% of the committee favors it. However, the "
            "opposing bloc is introducing amendments and proposing new caucuses to weaken your draft "
            "and build their own support.\n\n"
            "You want to close debate and move to voting before the opposition gains momentum. Write "
            "a strategic analysis (450-600 words) covering:\n\n"
            "1. What is a motion to close debate? What majority does it require?\n"
            "2. Why is the two-thirds requirement significant — how does it affect your strategy?\n"
            "3. When is the optimal moment to close debate? Too early? Too late?\n"
            "4. How do you prevent the opposition from closing debate when it benefits them?\n"
            "5. What are the speeches 'for' and 'against' closure? How do you make a compelling argument "
            "for closure without appearing to shut down democratic debate?\n"
            "6. What happens after debate closes — can new amendments still be introduced?"
        ),
        "hints": (
            "Closure of debate requires a two-thirds majority — you need significantly more than simple majority;"
            "Two speakers against closure are usually permitted — they will argue the committee has not "
            "finished deliberating;"
            "The optimal moment is when your support is at its peak but before the opposition's amendments erode it;"
            "To block closure, you need more than one-third of the committee — organize your bloc to vote no;"
            "After closure, no new amendments or caucuses — only voting procedure remains;"
            "Frame closure as: 'The committee has thoroughly debated and is ready to take meaningful action'"
        ),
        "sample_answer": (
            "A strategic analysis would explain the two-thirds threshold, identify the optimal timing window "
            "between peak support and opposition momentum, recommend framing closure as readiness to act "
            "rather than silencing debate, advise organizing the two-thirds coalition in advance through "
            "whipping, explain how to block opposition closure attempts with a one-third minority, and "
            "note that after closure, only voting remains — no further amendments."
        ),
        "key_concepts": "closure of debate, two-thirds majority, strategic timing, blocking, voting procedure",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Precedence of Motions",
        "prompt": (
            "Three delegates raise their placards simultaneously at the end of a moderated caucus:\n\n"
            "  Delegate A: 'Motion for an unmoderated caucus, 15 minutes.'\n"
            "  Delegate B: 'Motion to close debate.'\n"
            "  Delegate C: 'Motion for a moderated caucus, 10 minutes, 1-minute speaking time, on the "
            "  topic of enforcement mechanisms.'\n\n"
            "The Chair needs to decide which motion to entertain first. Write a comprehensive analysis "
            "(450-600 words) covering:\n\n"
            "1. What is the precedence (priority order) of motions in standard MUN rules of procedure?\n"
            "2. In this scenario, which motion is entertained first, second, and third? Why?\n"
            "3. If the first motion passes, what happens to the remaining motions?\n"
            "4. What is the logic behind the precedence system — why are some motions prioritized?\n"
            "5. How can a savvy delegate exploit the precedence system? For example, if you want to "
            "prevent an unmoderated caucus, what motion could you introduce first?\n"
            "6. Do all conferences use the same precedence order? What variations exist?"
        ),
        "hints": (
            "General precedence (most to least disruptive): adjournment of meeting > adjournment of debate > "
            "closure of debate > suspension > unmoderated caucus > moderated caucus;"
            "More disruptive motions take precedence — closure of debate is more disruptive than a caucus;"
            "If closure of debate passes, the caucus motions are moot — the committee moves to voting;"
            "A delegate can preempt an unmoderated caucus by motioning for closure of debate first;"
            "Some conferences reverse the order (least disruptive first) — check the rules packet"
        ),
        "sample_answer": (
            "A thorough analysis would present the standard precedence hierarchy, determine that Delegate B's "
            "closure of debate is entertained first (most disruptive), followed by Delegate A's unmoderated "
            "caucus, then Delegate C's moderated caucus, explain the logic of prioritizing disruptive motions "
            "to prevent unnecessary debate, show how delegates can exploit this to preempt opponents' preferred "
            "formats, and note that conference-specific rules may vary the order."
        ),
        "key_concepts": "precedence of motions, motion hierarchy, closure of debate, disruptive motions, procedural strategy",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "Complex Amendment Strategies",
        "prompt": (
            "You are representing Japan in the General Assembly First Committee (DISEC). A draft resolution "
            "on 'Regulation of Autonomous Weapons Systems' has been introduced with 15 operative clauses. "
            "You support the overall resolution but believe three clauses are too vague and one clause "
            "sets a dangerous precedent. Other delegations have their own amendment proposals.\n\n"
            "Design a comprehensive amendment strategy (500-650 words):\n\n"
            "1. How do you decide which clauses to amend vs. which to accept as-is?\n"
            "2. You have 4 proposed changes — should you submit them as one amendment or four separate "
            "amendments? What are the pros and cons of each approach?\n"
            "3. How do you build support for your amendments before formally introducing them?\n"
            "4. If another delegation introduces an unfriendly amendment you oppose, how do you defeat it "
            "procedurally and politically?\n"
            "5. What happens if two competing amendments target the same clause? Which is voted on first?\n"
            "6. How do you handle a situation where an amendment you support passes but fundamentally "
            "changes the resolution's character — do you still support the final text?"
        ),
        "hints": (
            "Separate amendments give you flexibility — if one fails, others can still pass;"
            "But too many amendments slow the process and may irritate delegates who want to vote;"
            "Build support during unmoderated caucuses — show the language to potential supporters before introducing;"
            "To defeat an unwanted amendment: lobby against it privately, speak against it in the for/against speeches;"
            "Competing amendments to the same clause are voted on in reverse order of submission or furthest from original;"
            "If amendments change the resolution's character, you may need to vote no on the final text despite supporting the original"
        ),
        "sample_answer": (
            "A sophisticated strategy would prioritize amending the dangerous-precedent clause over vague "
            "language fixes, recommend separate amendments for flexibility, describe the pre-introduction "
            "lobbying process, outline political and procedural tactics to defeat unwanted amendments, "
            "explain competing amendment voting order, and analyze the difficult decision of withdrawing "
            "support if amendments distort the resolution's original intent."
        ),
        "key_concepts": "amendment strategy, unfriendly amendments, competing amendments, lobbying, resolution integrity",
    },
    {
        "category_type": "PROCEDURE",
        "difficulty": "ADV",
        "title": "GA vs. Security Council Procedural Differences",
        "prompt": (
            "You are a Head Delegate briefing your team before a conference. Your delegation has members "
            "in both the General Assembly Third Committee and the Security Council. Several of your "
            "delegates have only done GA before.\n\n"
            "Write a detailed briefing document (500-700 words) comparing GA and Security Council "
            "procedural differences:\n\n"
            "1. Membership and representation: How many members? Who are they?\n"
            "2. Voting: Simple majority vs. qualified majority. The veto power. What counts as a "
            "procedural vs. substantive vote?\n"
            "3. Document types: Resolutions vs. Presidential Statements vs. Press Statements — what is "
            "the hierarchy and when is each used?\n"
            "4. Debate format: How does the smaller size change debate dynamics?\n"
            "5. Power dynamics: How does P5 dominance affect negotiation strategies for elected members?\n"
            "6. Enforcement: GA resolutions are non-binding; SC resolutions under Chapter VII are binding. "
            "What does this mean for drafting language?\n"
            "7. Practical tips: What should your SC delegates do differently from your GA delegates?"
        ),
        "hints": (
            "SC has 15 members (5 permanent, 10 elected); GA has 193 members;"
            "SC requires 9 affirmative votes for substantive matters, with no P5 veto;"
            "SC produces: resolutions (binding under Ch. VII), presidential statements (consensus), press statements (informal);"
            "In a 15-member body, every delegate's position matters — there is no hiding in the crowd;"
            "Elected members (E10) must work harder to be heard over P5 dominance;"
            "Chapter VII language ('decides' vs. 'calls upon') determines enforceability"
        ),
        "sample_answer": (
            "A thorough briefing would contrast the 193-member GA with the 15-member SC, detail the veto "
            "and 9-vote threshold, explain the document hierarchy, note that SC's small size creates more "
            "intense interpersonal dynamics, advise E10 members to find niches and build coalitions with "
            "sympathetic P5 members, distinguish Chapter VII binding language from Chapter VI recommendations, "
            "and recommend SC delegates focus on precision of language since every word carries legal weight."
        ),
        "key_concepts": "GA vs Security Council, P5, E10, Chapter VII, binding resolutions, veto, procedural differences",
    },
]

# ── GENERAL QUESTIONS ─────────────────────────────────────────────────────────
QUESTIONS += [
    # ── BEGINNER (10) ────────────────────────────────────────────────────────
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Conference Preparation Checklist",
        "prompt": (
            "You are attending your very first Model UN conference next weekend. You have been assigned "
            "to represent Argentina in the General Assembly Third Committee (SOCHUM). The topic is "
            "'Protecting the Rights of Indigenous Peoples.'\n\n"
            "Your club advisor has asked you to create a conference preparation checklist. Write a "
            "comprehensive checklist (250-350 words) that covers:\n\n"
            "1. Research preparation (what to research and where to find information)\n"
            "2. Document preparation (position paper, notes, printed materials)\n"
            "3. Physical preparation (what to bring, what to wear, logistics)\n"
            "4. Mental preparation (managing nerves, setting goals)\n"
            "5. Day-of preparation (what to do when you arrive at the conference)\n\n"
            "For each category, list 3-4 specific actionable items. This checklist should be useful "
            "enough that a complete beginner could follow it and show up prepared."
        ),
        "hints": (
            "Research: background guide, country profile, UN voting records, relevant treaties like ILO Convention 169;"
            "Documents: print your position paper, bring a copy of the rules of procedure, bring a notepad;"
            "Physical: business attire, country placard, water bottle, snacks, phone charger;"
            "Mental: practice your opening speech, set a realistic goal (e.g., speak at least 3 times);"
            "Day-of: arrive early, find your seat, introduce yourself to neighbors"
        ),
        "sample_answer": (
            "A strong checklist would include specific research tasks (read background guide, research "
            "Argentina's indigenous population), document preparation (printed position paper, speech notes), "
            "physical items (Western business attire, notepad, pens), mental preparation strategies (practice "
            "speaking aloud, set achievable goals), and day-of actions (arrive 30 minutes early, review notes)."
        ),
        "key_concepts": "conference preparation, checklist, first-time delegate, logistics, research preparation",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Understanding Committee Types",
        "prompt": (
            "Your MUN club is registering for a conference and the registration form asks you to rank "
            "your committee preferences. The options include:\n\n"
            "  - General Assembly (GA) committees (First through Sixth)\n"
            "  - Economic and Social Council (ECOSOC)\n"
            "  - Security Council (SC)\n"
            "  - Human Rights Council (HRC)\n"
            "  - Specialized Agencies (WHO, UNHCR, etc.)\n"
            "  - Crisis Committees\n\n"
            "Write a guide (250-350 words) for your club members explaining:\n\n"
            "1. What does each type of committee do? (1-2 sentences each)\n"
            "2. How big is each committee? (approximate number of delegates)\n"
            "3. Which committees are best for beginners and why?\n"
            "4. Which committees are more advanced and why?\n"
            "5. What is the key difference between a GA committee and a crisis committee?"
        ),
        "hints": (
            "GA committees are the largest (up to 193 members) and follow standard MUN procedure — ideal for beginners;"
            "Security Council has 15 members — more intense, every delegate matters;"
            "Crisis committees have dynamic scenarios that change in real-time based on delegate actions;"
            "Specialized agencies focus on specific policy areas with expert-level discussion;"
            "Beginners should start with GA or ECOSOC; crisis and SC are for experienced delegates"
        ),
        "sample_answer": (
            "A helpful guide would describe each committee type's focus and size, recommend GA/ECOSOC for "
            "beginners due to standard procedure and large committees (less pressure), suggest SC and crisis "
            "for experienced delegates, and highlight that GA follows structured debate while crisis is "
            "fast-paced and requires improvisation."
        ),
        "key_concepts": "committee types, GA, Security Council, ECOSOC, crisis committee, beginner recommendations",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Note-Passing Etiquette",
        "prompt": (
            "During your first committee session, you notice delegates passing small folded notes to each "
            "other through the pages (student volunteers). Some notes are going to delegates across the "
            "room. You want to participate but are not sure about the rules.\n\n"
            "Write a guide on note-passing etiquette (200-300 words) covering:\n\n"
            "1. What is note-passing and why is it important in MUN?\n"
            "2. What should notes typically contain? Give 3 examples of good notes.\n"
            "3. What should notes NOT contain? Give 2 examples of inappropriate notes.\n"
            "4. How do you physically send a note? Who delivers it?\n"
            "5. Can the Chair read your notes? What happens if a note is inappropriate?\n"
            "6. How do you use notes strategically to build alliances?"
        ),
        "hints": (
            "Notes are the primary way to communicate during formal debate without disrupting proceedings;"
            "Good notes: 'Would you like to co-sponsor our working paper?', policy coordination, caucus invitations;"
            "Bad notes: personal messages, jokes, anything offensive — the Chair CAN read notes;"
            "Pages (student volunteers) deliver notes — fold them and write the recipient country on the outside;"
            "The Chair or dais may confiscate inappropriate notes and warn or penalize the sender"
        ),
        "sample_answer": (
            "A solid guide would describe note-passing as essential for alliance-building during formal debate, "
            "give examples like policy coordination and caucus invitations, warn against personal or offensive "
            "content, describe the page-delivery system, note that the dais can read any note, and recommend "
            "using notes to identify potential allies and invite them to join working groups."
        ),
        "key_concepts": "note-passing, committee communication, pages, etiquette, alliance building",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Dress Code and Professional Conduct",
        "prompt": (
            "Your MUN club advisor has sent an email saying: 'Remember, Western Business Attire is "
            "required at the conference. Delegates not meeting the dress code may not be admitted to "
            "committee.' Several club members are unsure what this means.\n\n"
            "Write a comprehensive guide (250-300 words) covering:\n\n"
            "1. What is 'Western Business Attire'? Provide specific examples for all genders.\n"
            "2. What is NOT acceptable? Give examples.\n"
            "3. Beyond clothing, what does professional conduct look like in a MUN committee?\n"
            "4. How should you address other delegates? (By country name, not personal name)\n"
            "5. What behaviors can get you warned or removed from committee?\n"
            "6. Why does MUN emphasize professional conduct — what is it simulating?"
        ),
        "hints": (
            "Business attire: suits, blazers, dress shirts, ties, dress shoes, professional dresses or skirts;"
            "Not acceptable: jeans, sneakers, T-shirts, casual wear, athletic wear;"
            "Address delegates as 'The delegate of [Country]' or 'The honorable delegate';"
            "Behaviors that get warnings: using phones, side conversations during speeches, disrespectful language;"
            "MUN simulates real diplomatic settings where professionalism matters"
        ),
        "sample_answer": (
            "A clear guide would define Western Business Attire with gender-inclusive examples, list "
            "unacceptable clothing, describe professional conduct as formal diplomatic simulation, explain "
            "the country-name addressing convention, list behaviors that violate decorum, and connect the "
            "dress code to the goal of authentically simulating international diplomacy."
        ),
        "key_concepts": "dress code, Western Business Attire, professional conduct, decorum, diplomatic simulation",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "How to Read a Background Guide Effectively",
        "prompt": (
            "You have received a 15-page background guide for your committee. The topic is 'Addressing "
            "Global Food Insecurity' and you are representing Ethiopia. You have limited time before the "
            "conference and want to read the guide efficiently.\n\n"
            "Write a step-by-step reading strategy (250-350 words) that covers:\n\n"
            "1. First pass (15 minutes): What do you look for on a quick skim?\n"
            "2. Second pass (30 minutes): What do you read carefully and take notes on?\n"
            "3. Research phase (30 minutes): What additional research do you do after reading?\n"
            "4. What should you highlight or bookmark in the background guide?\n"
            "5. What are the 'Questions a Resolution Should Address' section and why is it critical?\n"
            "6. How does the background guide help you identify potential allies and opponents?"
        ),
        "hints": (
            "First pass: read headings, introduction, conclusion, and any country-specific mentions;"
            "Second pass: read sections on past UN action, key definitions, and the questions to address;"
            "Research phase: look up Ethiopia's specific policies on food security, FAO data, AU positions;"
            "Highlight: key statistics, relevant resolutions, and any mention of your country or region;"
            "The 'questions to address' section is essentially the Chair's guide to what the resolution should cover"
        ),
        "sample_answer": (
            "An effective strategy would outline a three-phase reading approach (skim, deep-read, research), "
            "identify key sections to focus on (past UN action, definitions, guiding questions), recommend "
            "highlighting country-specific mentions and statistics, explain that the guiding questions reveal "
            "the Chair's expectations for the resolution, and note that the background guide reveals which "
            "countries have competing interests on the topic."
        ),
        "key_concepts": "background guide, strategic reading, research strategy, time management, preparation",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Understanding Awards Criteria",
        "prompt": (
            "After the conference, awards are given for Best Delegate, Outstanding Delegate, and Honorable "
            "Mention. You want to understand what the judges are looking for so you can improve.\n\n"
            "Write an explanation (250-350 words) covering:\n\n"
            "1. What are the typical award levels and what do they mean?\n"
            "2. What criteria do judges (the dais/chairs) use to evaluate delegates? List at least 5.\n"
            "3. Is winning an award only about giving great speeches? What else matters?\n"
            "4. How important is staying 'in character' (representing your country accurately)?\n"
            "5. Can a delegate from a small or unpopular country still win Best Delegate? How?\n"
            "6. What is the biggest mistake first-time delegates make when trying to win awards?"
        ),
        "hints": (
            "Award levels: Best Delegate (top), Outstanding Delegate, Honorable Mention, sometimes Verbal Commendation;"
            "Criteria include: quality of speeches, diplomacy and negotiation, resolution writing, research depth, "
            "staying in policy, professionalism;"
            "Behind-the-scenes work (bloc leading, drafting) matters as much as speeches;"
            "Staying in character is critical — a delegate of North Korea should not advocate for Western-style democracy;"
            "Small country delegates win by being the indispensable coalition builder or drafter"
        ),
        "sample_answer": (
            "A good explanation would list the award tiers, identify speech quality, negotiation, drafting, "
            "research, and professionalism as key criteria, emphasize that behind-the-scenes contributions "
            "matter as much as speeches, stress the importance of accurate country representation, explain "
            "that small country delegates win through coalition-building skill, and warn against focusing "
            "only on speeches while neglecting diplomacy."
        ),
        "key_concepts": "awards criteria, Best Delegate, evaluation, speeches, negotiation, country representation",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Managing Conference Anxiety",
        "prompt": (
            "You are about to attend your first MUN conference. You are nervous about speaking in front "
            "of the committee, worried about not knowing the rules, and anxious about representing your "
            "country incorrectly.\n\n"
            "Write a self-help guide (250-300 words) for managing MUN conference anxiety:\n\n"
            "1. What are the most common fears first-time delegates have? (List 3-4)\n"
            "2. What practical steps can you take to reduce anxiety before the conference?\n"
            "3. What can you do during committee if you feel overwhelmed?\n"
            "4. How do experienced delegates handle nervousness? (Hint: they still get nervous too)\n"
            "5. What is a realistic goal for a first conference? (Hint: it is not winning Best Delegate)\n"
            "6. What should you tell yourself if you make a mistake during committee?"
        ),
        "hints": (
            "Common fears: speaking publicly, not knowing the rules, saying something wrong, looking foolish;"
            "Before: practice your opening speech, review the rules, attend practice sessions;"
            "During: start by taking notes, pass notes to allies, speak in a smaller caucus first before the big room;"
            "Experienced delegates are nervous too — the difference is they have strategies for managing it;"
            "Realistic first-conference goal: speak at least once on the speakers list, participate in a caucus;"
            "Everyone makes mistakes — the Chair will not remember yours by the end of the day"
        ),
        "sample_answer": (
            "A supportive guide would normalize anxiety, list common fears, recommend practical preparation "
            "(practice, study rules), suggest starting with smaller contributions (notes, caucus participation) "
            "before attempting speeches, share that experienced delegates manage nerves rather than eliminate "
            "them, set the realistic goal of active participation rather than winning, and reframe mistakes "
            "as learning opportunities."
        ),
        "key_concepts": "conference anxiety, public speaking, first-time delegate, mental preparation, realistic goals",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Working With a Partner Delegate",
        "prompt": (
            "At some conferences, countries send two delegates — a 'double delegation.' You and your partner "
            "have been assigned to represent India in ECOFIN. You need to coordinate your efforts.\n\n"
            "Write a guide (250-300 words) on how to work effectively with a partner delegate:\n\n"
            "1. How should you divide responsibilities before the conference? (e.g., who writes the "
            "position paper, who researches specific sub-topics)\n"
            "2. During committee, how do you divide speaking and negotiating roles?\n"
            "3. What happens if you and your partner disagree on strategy?\n"
            "4. How do you communicate during formal debate without disrupting committee?\n"
            "5. What are the advantages of a double delegation over a single delegate?\n"
            "6. What is the biggest mistake double delegations make?"
        ),
        "hints": (
            "Divide sub-topics: one partner researches economic aspects, the other focuses on social/political;"
            "During committee: one speaks while the other takes notes and passes notes to allies;"
            "Disagreements should be resolved privately — never contradict your partner in front of the committee;"
            "Communicate via written notes between you or whispered conversation during caucuses;"
            "Advantages: more coverage, one can network while the other speaks;"
            "Biggest mistake: both partners doing the same thing and not covering more ground"
        ),
        "sample_answer": (
            "A practical guide would recommend dividing research by sub-topic, alternating speaking and "
            "support roles during committee, establishing a private conflict-resolution protocol, using "
            "written notes for in-committee coordination, leveraging the two-person advantage for "
            "simultaneous networking and speaking, and warning against redundancy and failing to divide labor."
        ),
        "key_concepts": "double delegation, partner coordination, role division, teamwork, communication",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Basic Time Management at Conferences",
        "prompt": (
            "Your conference runs from 9:00 AM to 6:00 PM over two days. The schedule includes:\n"
            "  - Committee Sessions (3 hours each, 2 per day)\n"
            "  - Lunch Break (1 hour)\n"
            "  - Social Events (evening of Day 1)\n\n"
            "You have limited time and want to maximize your impact. Write a time management guide "
            "(250-300 words) covering:\n\n"
            "1. How should you spend the first 30 minutes of the first committee session?\n"
            "2. What should you do during unmoderated caucuses? How do you avoid wasting time?\n"
            "3. How do you use lunch breaks productively (without burning out)?\n"
            "4. What should your priorities be on Day 1 vs. Day 2?\n"
            "5. When should you focus on speaking vs. when should you focus on drafting?\n"
            "6. How important are social events — should you attend or use the time to prepare?"
        ),
        "hints": (
            "First 30 minutes: listen, take notes, identify which delegates are your potential allies;"
            "Unmoderated caucuses: have a plan — approach specific delegates, join or form a working group;"
            "Lunch: eat quickly, review notes, identify 2-3 goals for the afternoon session;"
            "Day 1 priorities: build alliances, gather information; Day 2: draft resolution, push for sponsors;"
            "Speak early to establish presence; shift to drafting once working papers begin;"
            "Social events are great for networking — but do not stay up late before Day 2"
        ),
        "sample_answer": (
            "A smart guide would recommend listening and identifying allies in the first 30 minutes, having "
            "specific goals for each unmoderated caucus, using lunch for brief review rather than intense "
            "preparation, prioritizing alliance-building on Day 1 and drafting/speaking on Day 2, balancing "
            "speaking and behind-the-scenes work, and attending social events for networking while maintaining rest."
        ),
        "key_concepts": "time management, conference schedule, priorities, unmoderated caucus, Day 1 vs Day 2",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "BEG",
        "title": "Formal vs. Informal Debate",
        "prompt": (
            "During your first committee session, you notice two very different modes of debate. Sometimes "
            "the committee is quiet and one person speaks at a time (formal). Other times, everyone is "
            "standing, moving around, and talking in small groups (informal).\n\n"
            "Write an explanation (250-300 words) comparing formal and informal debate:\n\n"
            "1. What is formal debate? What activities happen during it?\n"
            "2. What is informal debate? What activities happen during it?\n"
            "3. When does the committee switch between the two? What triggers the switch?\n"
            "4. Which type of debate is more important for winning awards? Why?\n"
            "5. What should you be doing during each type?\n"
            "6. Can you participate meaningfully if you are too shy for formal debate? How?"
        ),
        "hints": (
            "Formal: Speakers List speeches, moderated caucuses — one person speaks at a time, structured;"
            "Informal: unmoderated caucuses — free movement, group discussions, working paper drafting;"
            "The switch happens via motions — a delegate motions for a caucus during formal debate;"
            "Awards: both matter! Speaking shows leadership; informal work shows diplomacy and drafting skill;"
            "During formal debate: speak, listen, take notes; during informal: negotiate, draft, build alliances;"
            "Shy delegates can shine in informal settings through drafting, note-passing, and small group negotiation"
        ),
        "sample_answer": (
            "A clear explanation would describe formal debate as structured single-speaker proceedings "
            "and informal debate as free-form group negotiation, explain that motions trigger the switch, "
            "emphasize that both matter equally for awards (speaking shows leadership, informal work shows "
            "diplomacy), outline activities for each mode, and encourage shy delegates to focus on informal "
            "contributions like drafting and small-group negotiation."
        ),
        "key_concepts": "formal debate, informal debate, Speakers List, unmoderated caucus, participation strategies",
    },
    # ── INTERMEDIATE (10) ────────────────────────────────────────────────────
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Strategic Note-Passing to Build Alliances",
        "prompt": (
            "You are representing Turkey in the Human Rights Council. The topic is 'Freedom of Religion "
            "and Belief.' During the first moderated caucus, you identify three potential allies based on "
            "their speeches: Malaysia, Senegal, and Indonesia.\n\n"
            "Write a strategic note-passing plan (350-400 words) that:\n\n"
            "1. Drafts the text of your first note to each country (be specific — write the actual note)\n"
            "2. Explains why you are targeting these three countries and not others\n"
            "3. Describes your follow-up strategy — what do you do when they respond?\n"
            "4. Explains how to use notes to propose and organize an unmoderated caucus group\n"
            "5. Describes how to use notes to build a working paper coalition\n"
            "6. Warns about common note-passing mistakes that undermine your credibility"
        ),
        "hints": (
            "First notes should be short and specific: 'Would Turkey and Malaysia coordinate on a working paper? We share concerns about Islamophobia reporting mechanisms';"
            "Target these three because they are OIC members with shared interests on religious freedom;"
            "Follow-up: propose a specific meeting spot during the next unmod caucus;"
            "Organize your caucus group via notes: 'Working group meeting at the back left during next unmod — bring policy ideas';"
            "Mistakes: sending too many notes (looks unfocused), sending notes to opponents (information leak), writing vague notes"
        ),
        "sample_answer": (
            "A strong plan would draft specific, concise notes tailored to each country's stated position, "
            "explain the OIC connection as the basis for targeting, describe a funnel strategy (note → caucus "
            "meeting → working paper collaboration), provide a sample organizing note for a working group, "
            "and warn against information leaks and unfocused mass note-sending."
        ),
        "key_concepts": "strategic note-passing, alliance building, OIC, working group formation, targeted outreach",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Understanding Awards Judging",
        "prompt": (
            "You have attended several conferences and received Honorable Mention once. You want to "
            "understand what separates Best Delegate from Outstanding Delegate from Honorable Mention "
            "so you can improve.\n\n"
            "Write an analysis (350-450 words) covering:\n\n"
            "1. What does the dais (Chairs/Directors) actually look for? List the evaluation criteria "
            "and explain which ones are weighted most heavily.\n"
            "2. What distinguishes a Best Delegate performance from an Outstanding Delegate performance?\n"
            "3. What common mistakes prevent good delegates from winning Best Delegate?\n"
            "4. How important is the position paper? Can a weak position paper disqualify you?\n"
            "5. Does the country assignment matter? Is it harder to win with a small/unpopular country?\n"
            "6. How do you make yourself memorable to the dais without being obnoxious?"
        ),
        "hints": (
            "Criteria (roughly weighted): diplomatic engagement (25%), speech quality (20%), resolution "
            "writing/drafting (20%), research depth (15%), professionalism/policy accuracy (10%), position paper (10%);"
            "Best Delegate = excellent across all criteria AND leads the committee (sets the agenda, builds the main coalition);"
            "Outstanding = strong in most areas but didn't drive the overall committee direction;"
            "Common mistakes: dominating without collaborating, great speeches but no drafting, ignoring weaker delegates;"
            "Small countries CAN win — it requires creative coalition building and indispensable contributions"
        ),
        "sample_answer": (
            "A detailed analysis would break down evaluation criteria with approximate weights, distinguish "
            "Best Delegate (committee leadership and consistency) from Outstanding (strong but not the driver), "
            "identify common pitfalls like over-domination and neglecting behind-the-scenes work, note that "
            "position papers rarely disqualify but strong ones add edge, explain that small countries can "
            "win through indispensable contributions, and advise consistent quality over flashy moments."
        ),
        "key_concepts": "awards judging, Best Delegate, evaluation criteria, committee leadership, self-improvement",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Managing a Bloc as Bloc Leader",
        "prompt": (
            "You are representing South Africa in the General Assembly, and your bloc of 12 African and "
            "developing nations has chosen you as bloc leader. You are responsible for coordinating "
            "positions, organizing unmoderated caucus discussions, and managing the working paper.\n\n"
            "Write a bloc leadership guide (350-450 words) covering:\n\n"
            "1. What are the responsibilities of a bloc leader? List at least 5.\n"
            "2. How do you manage delegates who want to go in different directions?\n"
            "3. How do you ensure every bloc member gets speaking time and feels included?\n"
            "4. What is your strategy for writing and editing the working paper collaboratively?\n"
            "5. How do you negotiate with other blocs on behalf of your group?\n"
            "6. What are the risks of being bloc leader? When does leadership become a liability?"
        ),
        "hints": (
            "Responsibilities: coordinate positions, assign speaking topics, manage the working paper, "
            "represent the bloc in inter-bloc negotiations, keep everyone informed;"
            "Handle disagreements by finding common ground and allowing dissent on non-critical points;"
            "Assign specific operative clauses to different members so everyone contributes to drafting;"
            "When negotiating with other blocs, know your red lines vs. negotiable points;"
            "Risk: if the bloc's resolution fails, the leader takes disproportionate blame; also, "
            "micromanaging pushes members away"
        ),
        "sample_answer": (
            "A comprehensive guide would list coordination, drafting, negotiation, and inclusion as key "
            "responsibilities, recommend finding common ground and allowing flexibility on secondary issues, "
            "suggest assigning clause ownership to ensure engagement, describe inter-bloc negotiation with "
            "clear mandates from the group, and warn against micromanagement and assuming personal credit "
            "for collective work."
        ),
        "key_concepts": "bloc leadership, coalition management, working paper, inter-bloc negotiation, inclusion",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Handling Hostile Delegates Diplomatically",
        "prompt": (
            "You are representing Israel in the Human Rights Council. During a moderated caucus, the "
            "delegate of Iran makes aggressive and personal attacks on your country, going beyond normal "
            "diplomatic critique. Some of their statements feel personally directed at you as a delegate, "
            "not just at Israel as a country.\n\n"
            "Write a strategic response guide (350-400 words) covering:\n\n"
            "1. How do you distinguish between legitimate policy criticism and personal hostility?\n"
            "2. What are your procedural options for responding? (Right of Reply, Point of Order, etc.)\n"
            "3. How do you craft a response that is firm but diplomatic — not emotional?\n"
            "4. When should you escalate to the Chair? What constitutes an inappropriate personal attack?\n"
            "5. How do you win the 'audience' (other delegates) when someone attacks you?\n"
            "6. Write the first two sentences of a diplomatic response to the scenario above."
        ),
        "hints": (
            "Policy criticism: 'Israel's settlement policy violates international law' — legitimate;"
            "Personal attack: 'The delegate of Israel is dishonest and should be ashamed' — inappropriate;"
            "Right of Reply addresses misrepresentation; Point of Order addresses rule violations;"
            "Craft responses that redirect to policy: 'Israel respects the views of all delegates and would "
            "like to redirect the discussion to solutions';"
            "Winning the audience: stay calm, factual, and solutions-oriented — the aggressive delegate loses credibility;"
            "Never respond with hostility — you lose credibility immediately"
        ),
        "sample_answer": (
            "A mature guide would distinguish policy critique from personal attacks, recommend Right of "
            "Reply for factual corrections and Point of Order for decorum violations, advise calm and "
            "policy-focused responses, suggest escalating to the Chair only for clear personal attacks, "
            "explain that composure wins audience sympathy, and draft a response like: 'The delegate of "
            "Israel thanks the honorable delegate for their perspective. We believe this committee is best "
            "served by focusing on constructive solutions.'"
        ),
        "key_concepts": "hostile delegates, diplomatic response, composure, Right of Reply, conflict management",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Crisis Committee Preparation",
        "prompt": (
            "You have been assigned to a crisis committee for the first time. The committee is a historical "
            "simulation of the 1994 Rwandan Genocide, and you are playing the role of a member of the UN "
            "Security Council during the crisis.\n\n"
            "Write a preparation guide (350-450 words) that covers:\n\n"
            "1. How does preparing for a crisis committee differ from preparing for a GA committee?\n"
            "2. What research should you do about your specific character/role?\n"
            "3. What is a 'crisis arc' and how should you anticipate it?\n"
            "4. What materials should you bring to a crisis committee that you wouldn't bring to GA?\n"
            "5. How does the pace of a crisis committee differ from GA? How do you keep up?\n"
            "6. What is the most common mistake first-time crisis delegates make?"
        ),
        "hints": (
            "Crisis prep: research your character's biography, powers, resources, and historical decisions;"
            "Understand the historical timeline — the crisis arc will follow it but may diverge based on delegate actions;"
            "Bring: a laptop or tablet for quick research, character bio sheet, timeline of events;"
            "Crisis is FAST — decisions happen in minutes, not hours. You must think quickly and act boldly;"
            "Common mistake: treating crisis like GA (being too passive, waiting for formal debate instead of writing directives)"
        ),
        "sample_answer": (
            "A thorough guide would contrast GA's policy focus with crisis's character and action focus, "
            "recommend researching the specific character's powers and historical actions, explain crisis "
            "arcs as pre-planned escalations, list crisis-specific materials (laptop, timeline, character sheet), "
            "emphasize the speed difference, and warn against passivity as the biggest first-time mistake."
        ),
        "key_concepts": "crisis committee, preparation, character research, crisis arc, directives, pace management",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Multi-Day Conference Strategy",
        "prompt": (
            "You are attending a three-day conference (Friday evening through Sunday afternoon). You are "
            "representing France in the Security Council with 15 delegates total.\n\n"
            "Write a strategic plan (350-450 words) for how to approach each day:\n\n"
            "1. Friday Evening (Session 1: 3 hours): What are your goals? What should you accomplish?\n"
            "2. Saturday (Sessions 2-3: 6 hours): How does your strategy shift from Day 1?\n"
            "3. Sunday Morning (Session 4: 3 hours): What is the endgame? How do you close?\n"
            "4. How do you pace yourself to avoid burnout over three days?\n"
            "5. What happens between sessions? How do you use the overnight gap?\n"
            "6. How should your speaking strategy evolve from Day 1 to Day 3?"
        ),
        "hints": (
            "Friday: establish presence, identify allies, learn the landscape — do NOT overcommit to positions;"
            "Saturday morning: begin working papers, formalize alliances; Saturday afternoon: draft resolution, sponsor negotiations;"
            "Sunday: close debate, manage amendments, voting — this is execution time;"
            "Overnight: review notes, refine strategy, rest — do not stay up all night;"
            "Day 1 speeches: broad positioning; Day 2: specific policy arguments; Day 3: calls to action and unity"
        ),
        "sample_answer": (
            "A smart plan would use Friday for reconnaissance and positioning, Saturday for alliance-building "
            "and drafting, Sunday for execution and voting, recommend adequate rest between sessions, suggest "
            "overnight strategy refinement, and describe speech evolution from broad framing (Day 1) to "
            "specific arguments (Day 2) to closing appeals (Day 3)."
        ),
        "key_concepts": "multi-day strategy, pacing, conference planning, speaking evolution, endgame",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Leveraging Unmoderated Caucuses Effectively",
        "prompt": (
            "An unmoderated caucus has been approved for 15 minutes. Most delegates stand up and form "
            "clusters. You notice that some delegates are highly effective during unmods while others "
            "wander aimlessly.\n\n"
            "Write a tactical guide (350-400 words) for maximizing unmoderated caucuses:\n\n"
            "1. What should you do in the first 60 seconds of an unmod?\n"
            "2. How do you choose which group to join? What if there are multiple groups?\n"
            "3. What role should you play within your group — leader, drafter, or connector?\n"
            "4. How do you 'poach' a delegate from a rival group diplomatically?\n"
            "5. When should you leave one group to join another? How do you do it gracefully?\n"
            "6. What should you have accomplished by the end of the unmod?\n"
            "7. What do the best delegates do that average delegates don't during unmods?"
        ),
        "hints": (
            "First 60 seconds: scan the room, identify where your allies are clustering, approach with purpose;"
            "Join the group most aligned with your position — or the one writing the working paper you want to influence;"
            "Play the role that is missing: if no one is writing, be the drafter; if no one is leading, step up;"
            "Poaching: approach a delegate from a rival group one-on-one with a specific value proposition;"
            "Leave gracefully: 'I want to touch base with a few other delegations — I will be back';"
            "By end: have concrete next steps, know who is in your coalition, and have text drafted"
        ),
        "sample_answer": (
            "A tactical guide would recommend purposeful movement in the first minute, strategic group "
            "selection based on alignment and influence opportunity, adaptable role-playing based on group "
            "needs, diplomatic poaching through one-on-one value propositions, graceful exits, and concrete "
            "deliverables by the end. The best delegates are the ones who leave unmods with written text, "
            "confirmed allies, and clear next steps."
        ),
        "key_concepts": "unmoderated caucus, group dynamics, drafting, coalition building, tactical networking",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Transitioning from Working Paper to Draft Resolution",
        "prompt": (
            "Your bloc has been developing a working paper during unmoderated caucuses. The Chair announces "
            "that working papers may be submitted for approval as draft resolutions. Your working paper "
            "needs significant work before it can become a draft.\n\n"
            "Write a guide (350-450 words) on the transition process:\n\n"
            "1. What format changes are needed? (Working paper format vs. UN resolution format)\n"
            "2. What are preambulatory clauses and operative clauses? How do you write each?\n"
            "3. How many signatories do you need? What is the difference between a sponsor and a signatory?\n"
            "4. What does the Chair look for when reviewing a draft? What might get rejected?\n"
            "5. How do you handle competing working papers from other blocs? Merge or compete?\n"
            "6. What are the most common formatting mistakes that first-time resolution writers make?"
        ),
        "hints": (
            "UN format: preambulatory clauses (noting, recalling, emphasizing) + operative clauses (urges, calls upon, decides);"
            "Sponsors wrote the resolution and will defend it; signatories just want it discussed (don't necessarily support);"
            "Usually 1/4 to 1/5 of committee must sign; the Chair checks format, scope, and policy relevance;"
            "Common mistakes: numbering errors, using operative language in preambulatory clauses, not referencing prior UN action;"
            "Merge when possible — fewer drafts means your ideas have a better chance of passing"
        ),
        "sample_answer": (
            "A comprehensive guide would describe the UN resolution format with preambulatory and operative "
            "clause conventions, distinguish sponsors from signatories, note signatory thresholds, describe "
            "Chair review criteria (format, relevance, scope), recommend merging competing papers when "
            "interests overlap, and list common formatting errors like misused clause language and missing "
            "references to prior UN action."
        ),
        "key_concepts": "working paper, draft resolution, preambulatory clauses, operative clauses, sponsors, signatories",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Understanding the Role of Pages and Admin Staff",
        "prompt": (
            "You notice student volunteers (pages) walking around the committee room delivering notes, "
            "collecting working papers, and helping the Chair. You also notice an 'Admin Staff' table "
            "where delegates submit documents.\n\n"
            "Write an explanation (300-350 words) covering:\n\n"
            "1. Who are pages and what do they do? Are they delegates?\n"
            "2. How should you interact with pages — what is the etiquette?\n"
            "3. What does the Admin Staff (or Rapporteur) do?\n"
            "4. How do you submit a working paper or draft resolution through the proper channels?\n"
            "5. Can you ask the Admin Staff for help with resolution formatting?\n"
            "6. What role do pages play in the Chair's evaluation of delegates? (Hint: they observe.)"
        ),
        "hints": (
            "Pages are volunteers who deliver notes and assist with logistics — they are NOT delegates;"
            "Be polite to pages — fold notes properly, write the recipient country clearly;"
            "Admin Staff handle document submission, printing, and distribution;"
            "Submit working papers to Admin Staff who forward to the Chair for approval;"
            "Some Admin Staff will help with formatting; others will only check for compliance;"
            "Pages may report to the Chair about delegate behavior — professionalism matters even in interactions with staff"
        ),
        "sample_answer": (
            "A clear explanation would identify pages as non-delegate volunteers handling note delivery and "
            "logistics, describe polite interaction norms, explain Admin Staff's role in document management, "
            "outline the submission pipeline (delegate → Admin → Chair), note that formatting help varies "
            "by conference, and importantly warn that pages observe delegate behavior and may inform the "
            "Chair's evaluation."
        ),
        "key_concepts": "pages, admin staff, document submission, committee logistics, professionalism",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "INT",
        "title": "Building a Conference Portfolio",
        "prompt": (
            "You have attended 5 conferences over the past year and want to track your growth as a MUN "
            "delegate. Your club advisor suggests building a 'conference portfolio.'\n\n"
            "Write a guide (350-400 words) on building and using a MUN portfolio:\n\n"
            "1. What should a conference portfolio contain? List at least 6 items to include.\n"
            "2. How do you track your speaking performance across conferences?\n"
            "3. How do you document lessons learned from each conference?\n"
            "4. How can a portfolio help you improve from conference to conference?\n"
            "5. How can a portfolio be used for college applications, resumes, or scholarship essays?\n"
            "6. What is the difference between a portfolio that helps you improve vs. one that just "
            "collects dust?"
        ),
        "hints": (
            "Include: position papers, awards, self-assessment notes, speech drafts, feedback from chairs, "
            "resolution texts you contributed to, a conference log;"
            "Track speaking: note how many times you spoke, in what format, and what feedback you received;"
            "After each conference, write a 1-page reflection: what went well, what to improve, specific goals for next time;"
            "A useful portfolio is one you actively review before each conference — not just a storage folder;"
            "For applications: highlight leadership, negotiation skills, global awareness, and public speaking growth"
        ),
        "sample_answer": (
            "A practical guide would list portfolio contents (papers, awards, reflections, speech drafts, "
            "feedback, resolution contributions), recommend structured self-assessment after each conference, "
            "suggest tracking speaking frequency and quality, explain that reviewing the portfolio before "
            "each new conference drives improvement, and describe how to frame MUN experience for college "
            "applications and resumes."
        ),
        "key_concepts": "conference portfolio, self-assessment, growth tracking, college applications, reflection",
    },
    # ── ADVANCED (10) ────────────────────────────────────────────────────────
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Head Delegate Responsibilities and Team Management",
        "prompt": (
            "You have been appointed Head Delegate for your school's MUN team. Your team has 20 members "
            "across 8 committees at a major conference. You have a mix of experienced delegates and "
            "first-timers.\n\n"
            "Write a comprehensive leadership plan (500-600 words) covering:\n\n"
            "1. Pre-conference: How do you assign countries and committees to team members?\n"
            "2. Pre-conference: How do you prepare the team — practice sessions, research review, etc.?\n"
            "3. During the conference: How do you check in with delegates across different committees?\n"
            "4. How do you support first-time delegates without hovering or micromanaging?\n"
            "5. How do you handle team conflicts — e.g., two delegates who want the same country?\n"
            "6. Post-conference: How do you conduct a team debrief?\n"
            "7. How do you balance your own committee performance with your leadership responsibilities?\n\n"
            "Include specific examples of how you would handle at least 2 realistic scenarios."
        ),
        "hints": (
            "Country assignment: consider experience (give newcomers easier countries), interests, and committee type;"
            "Prep sessions: run mock moderated caucuses, review position papers, practice speeches;"
            "During conference: designate a check-in schedule (during breaks), create a group chat for updates;"
            "Support first-timers: pair them with experienced delegates, set achievable goals, debrief after Day 1;"
            "Conflicts: use a preference form and resolve diplomatically — the team comes first;"
            "Debrief: structured reflection — what each delegate learned, team-wide patterns, goals for next conference"
        ),
        "sample_answer": (
            "A thorough plan would describe a structured country/committee assignment process, outline "
            "practice session format, create a check-in schedule during the conference, recommend a buddy "
            "system for newcomers, propose a fair preference-based country assignment system, plan a "
            "structured post-conference debrief, and acknowledge the tension between personal performance "
            "and team leadership — suggesting the Head Delegate prioritize team success over personal awards."
        ),
        "key_concepts": "Head Delegate, team management, leadership, delegation preparation, mentoring, debrief",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Running a Delegation Across Multiple Committees",
        "prompt": (
            "Your school is sending 30 delegates to a national conference. They are spread across 12 "
            "different committees, including GA, ECOSOC, Security Council, and two crisis committees. "
            "As Head Delegate, you need a system to coordinate across all committees.\n\n"
            "Write an operational plan (500-600 words) covering:\n\n"
            "1. Communication infrastructure: How do delegates report back to you? How often?\n"
            "2. Cross-committee strategy: When the same topic appears in multiple committees, how do "
            "you ensure your delegation's positions are consistent?\n"
            "3. Resource allocation: Some delegates need more help than others. How do you prioritize?\n"
            "4. Real-time problem solving: A delegate in the Security Council is overwhelmed and the "
            "crisis committee delegates are confused. How do you handle both simultaneously?\n"
            "5. Information sharing: How do you ensure insights from one committee benefit delegates in "
            "related committees?\n"
            "6. End-of-day sync: What does your nightly team meeting look like?"
        ),
        "hints": (
            "Create a shared group chat or channel organized by committee — not one big group;"
            "Cross-committee consistency: create a 1-page 'position brief' that all delegates reference for key topics;"
            "Prioritize based on need (new delegates) and strategic importance (competitive committees);"
            "Delegate your leadership: appoint 'committee captains' for groups of 2-3 related committees;"
            "Nightly sync: 30-minute meeting with brief reports from each committee, discuss strategy for the next day;"
            "Cross-pollination: if ECOSOC is discussing climate finance, share relevant points with the UNFCCC delegate"
        ),
        "sample_answer": (
            "An operational plan would establish committee-specific communication channels, create a unified "
            "position brief for cross-cutting topics, use a triage system for delegate support, appoint "
            "committee captains to distribute leadership, describe a structured nightly sync meeting, and "
            "set up a cross-committee intelligence-sharing protocol for related topics."
        ),
        "key_concepts": "multi-committee delegation, coordination, communication, position consistency, leadership delegation",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Conference Circuit Strategy",
        "prompt": (
            "Your school's MUN program has a limited budget and can attend only 6 conferences per academic "
            "year. There are over 20 conferences available, ranging from local practice conferences to "
            "national competitive conferences and international events.\n\n"
            "Write a conference selection strategy (450-600 words) covering:\n\n"
            "1. What factors should you consider when choosing conferences? (List at least 6)\n"
            "2. How do you balance between practice conferences (low stakes) and competitive conferences "
            "(high stakes) across the year?\n"
            "3. What is the ideal conference progression for a developing team?\n"
            "4. How do costs (registration, travel, hotel) factor into your decisions?\n"
            "5. How do you evaluate a conference's quality before attending? (What signals to look for)\n"
            "6. Should your team specialize in certain conferences or attend a wide variety? Why?\n"
            "7. How does the conference circuit affect college applications for your team members?"
        ),
        "hints": (
            "Factors: quality, cost, distance, committee offerings, competition level, reputation, timing;"
            "Ideal progression: 2 practice (fall), 2 competitive (winter), 1 major national (spring), 1 reach (spring);"
            "Quality signals: experienced secretariat, published background guides, clear rules, past delegate reviews;"
            "Budget: local conferences save on travel; consider carpooling, hosting visiting delegates, fundraising;"
            "Consistency matters for college apps — attending the same strong conferences annually builds a track record;"
            "Specializing builds reputation but variety develops adaptability"
        ),
        "sample_answer": (
            "A strategic plan would list selection criteria, propose a developmental arc from practice to "
            "competitive across the year, incorporate budget analysis with cost-saving measures, describe "
            "quality evaluation methods, recommend a mix of familiar and new conferences, and note that "
            "consistent participation in recognized conferences carries weight for college applications."
        ),
        "key_concepts": "conference circuit, conference selection, budget planning, program development, competition strategy",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Mentoring Novice Delegates",
        "prompt": (
            "You are a senior delegate with 3 years of MUN experience. Your club has 15 new members who "
            "have never attended a conference. The club advisor has asked you to design a mentoring program "
            "that prepares them for their first conference in 8 weeks.\n\n"
            "Write a detailed mentoring plan (500-600 words) covering:\n\n"
            "1. Week-by-week curriculum: What skills do you teach in what order over 8 weeks?\n"
            "2. How do you teach public speaking to students who are terrified of it?\n"
            "3. How do you teach research and position paper writing?\n"
            "4. How do you simulate committee experience? (Mock sessions, practice exercises)\n"
            "5. How do you match mentors with mentees? (What factors to consider)\n"
            "6. How do you measure whether mentees are ready for their first conference?\n"
            "7. What is the most important thing you can teach a new delegate that is NOT about MUN skills?"
        ),
        "hints": (
            "Week 1-2: MUN basics, committee types, rules overview; Week 3-4: research and position paper; "
            "Week 5-6: public speaking and speech writing; Week 7-8: mock committee sessions;"
            "Public speaking: start with small groups (3-4 people), build up to the full club;"
            "Mock sessions are the most valuable training tool — nothing replaces practice;"
            "Match mentors based on personality (pair shy mentees with patient mentors);"
            "Readiness: can they give a 60-second speech and participate in a caucus?;"
            "Most important non-MUN skill: confidence that failure is okay and growth is the goal"
        ),
        "sample_answer": (
            "A comprehensive plan would lay out an 8-week progressive curriculum, describe graduated "
            "public speaking exposure, include position paper workshops, plan at least 2 mock sessions, "
            "recommend personality-based mentor matching, define readiness as confident participation "
            "(not perfection), and emphasize that the most valuable lesson is that failure is a learning "
            "opportunity, not a disaster."
        ),
        "key_concepts": "mentoring, novice delegates, training curriculum, public speaking, mock sessions, confidence",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Understanding the Politics of Awards",
        "prompt": (
            "After attending many conferences, you begin to notice patterns in how awards are distributed. "
            "Some delegates who seem to dominate committee do not win, while quieter delegates sometimes "
            "receive Best Delegate. You want to understand the deeper dynamics at play.\n\n"
            "Write a critical analysis (500-600 words) covering:\n\n"
            "1. What are the official criteria for awards at most conferences?\n"
            "2. What are the unofficial factors that influence awards decisions? (Be honest.)\n"
            "3. How do different dais members evaluate delegates differently based on their own biases?\n"
            "4. Why do some dominant delegates lose? What is the difference between domination and leadership?\n"
            "5. How does the 'best delegate trap' work — where chasing awards actually hurts your performance?\n"
            "6. What is the most ethical approach to competing for awards?\n"
            "7. How should you handle disappointment if you believe you deserved an award but did not receive one?"
        ),
        "hints": (
            "Official criteria: speeches, diplomacy, drafting, research, policy accuracy;"
            "Unofficial factors: dais personal preferences, school reputation, how likeable you are, "
            "implicit biases about gender/race/accent;"
            "Domination vs. leadership: dominating silences others; leading empowers others to contribute;"
            "The 'best delegate trap': delegates who focus on winning become aggressive, ignore smaller "
            "delegations, and sacrifice collaboration for visibility — the dais notices;"
            "Ethical approach: focus on contribution, not competition; let the awards follow the performance;"
            "Disappointment: debrief objectively, learn from the experience, remember awards are not the only measure of growth"
        ),
        "sample_answer": (
            "A candid analysis would present official criteria alongside unofficial dynamics (bias, school "
            "reputation, likeability), distinguish leadership (empowering the committee) from domination "
            "(monopolizing it), explain how chasing awards leads to counterproductive behavior, recommend "
            "focusing on genuine contribution as the most ethical and effective strategy, and advise handling "
            "disappointment through objective self-reflection rather than resentment."
        ),
        "key_concepts": "awards politics, domination vs leadership, bias, best delegate trap, ethical competition",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Advanced Crisis Arc Strategy",
        "prompt": (
            "You are playing the role of National Security Advisor in a crisis committee simulating a "
            "fictional near-peer military confrontation between two major powers. The crisis arc has "
            "been escalating: a naval incident, cyberattacks, border troop movements, and now a "
            "hostage situation involving diplomats.\n\n"
            "Write a comprehensive crisis strategy (500-650 words) covering:\n\n"
            "1. How do you read the crisis arc? What patterns indicate where the backroom is taking the story?\n"
            "2. What are the three types of crisis actions: public directives, personal directives, and "
            "crisis notes? When do you use each?\n"
            "3. How do you balance escalation vs. de-escalation? When is each appropriate?\n"
            "4. How do you manage the backroom — understanding that your actions only succeed if the "
            "crisis staff approve them?\n"
            "5. How do you create a personal arc (character development) that impresses the dais?\n"
            "6. What is the 'portfolio power' concept and how do you expand your character's influence?\n"
            "7. How do you win Best Delegate in a crisis committee — is it different from GA?"
        ),
        "hints": (
            "Read the arc: if the backroom keeps escalating, they want you to respond — passivity is punished;"
            "Public directives change the committee's reality; personal directives change YOUR character's reality;"
            "Escalation is appropriate when the narrative demands it; de-escalation wins if you can broker peace convincingly;"
            "Manage the backroom: write detailed, plausible directives — vague actions get vague results;"
            "Personal arc: show character growth — start cautious, become decisive as the crisis demands;"
            "Portfolio power: use personal directives to gain resources, allies, or information beyond your official role;"
            "Crisis Best Delegate: creativity, initiative, and narrative contribution matter more than speeches"
        ),
        "sample_answer": (
            "A sophisticated strategy would describe arc-reading techniques, distinguish public from personal "
            "directives, argue for calibrated escalation matched to narrative needs, recommend detailed and "
            "plausible directives to satisfy the backroom, plan a character arc from cautious advisor to "
            "decisive leader, explain portfolio expansion through strategic personal directives, and note "
            "that crisis Best Delegate rewards narrative creativity over traditional speechmaking."
        ),
        "key_concepts": "crisis arc, directives, backroom management, portfolio power, escalation, character development",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Handling Conference Controversies Ethically",
        "prompt": (
            "During a conference, several ethical issues arise:\n"
            "  - Scenario A: You discover that a delegate from another school plagiarized their position paper.\n"
            "  - Scenario B: A delegate is making historically insensitive comments while role-playing an authoritarian regime.\n"
            "  - Scenario C: Your own teammate is fabricating statistics during speeches to sound more credible.\n\n"
            "Write an ethical analysis (500-600 words) addressing:\n\n"
            "1. For each scenario: What is the ethical issue? What should you do? Who should you tell?\n"
            "2. Where is the line between realistic role-playing and harmful speech in MUN?\n"
            "3. What responsibility does the dais have in monitoring ethical issues?\n"
            "4. How do conference codes of conduct typically handle these situations?\n"
            "5. What is the difference between competitive integrity and being a 'snitch'?\n"
            "6. How should the MUN community balance simulation realism with delegate safety and dignity?"
        ),
        "hints": (
            "Plagiarism: report to your advisor first, then the dais — this is a serious academic integrity issue;"
            "Insensitive role-play: the Chair should intervene if comments cross from policy into hate speech;"
            "Fabricated statistics: address with your teammate privately first — but if they continue, the dais should know;"
            "Role-playing authoritarian positions is acceptable; celebrating atrocities is not;"
            "Competitive integrity: reporting genuine violations is not 'snitching' — it protects the activity;"
            "Safety > realism — delegates should never feel personally attacked or unsafe"
        ),
        "sample_answer": (
            "A thoughtful analysis would address each scenario with specific ethical reasoning, distinguish "
            "between accurate role-playing and harmful speech, assign responsibility to both delegates and "
            "the dais, reference typical conference codes of conduct, reframe reporting violations as "
            "protecting the activity's integrity, and argue that delegate safety and dignity must always "
            "take precedence over simulation realism."
        ),
        "key_concepts": "ethics, plagiarism, role-playing boundaries, conference conduct, competitive integrity, safety",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Building a MUN Program from Scratch",
        "prompt": (
            "You are a student at a school that has never had a Model UN club. You want to start one from "
            "scratch and eventually take a team to conferences. You have support from one faculty advisor "
            "and zero budget.\n\n"
            "Write a founding plan (500-650 words) covering:\n\n"
            "1. Getting started: How do you recruit members? What do you tell students who have never "
            "heard of MUN?\n"
            "2. Faculty and administration: How do you get official club status and a budget?\n"
            "3. Training: How do you teach MUN when you are the most experienced person (and you only "
            "have moderate experience)?\n"
            "4. First conference: How do you choose the right conference for a brand-new team?\n"
            "5. Fundraising: How do you fund conference registrations, travel, and materials?\n"
            "6. Sustainability: How do you ensure the club survives after you graduate?\n"
            "7. Culture: What values and traditions should you establish from Day 1?"
        ),
        "hints": (
            "Recruitment: present at assemblies, social media, target debate/history/politics students;"
            "Administration: write a formal proposal with educational benefits — MUN builds public speaking, research, global awareness;"
            "Training: use YouTube resources (MUN tutorials), invite alumni from nearby schools, run mock sessions;"
            "First conference: choose a local, beginner-friendly conference with training workshops;"
            "Fundraising: bake sales, school grants, community sponsorships, GoFundMe;"
            "Sustainability: recruit underclassmen, create a leadership structure (president, VP, secretary);"
            "Culture: emphasize learning over winning, support over competition, inclusion over elitism"
        ),
        "sample_answer": (
            "A comprehensive plan would outline recruitment strategies, describe the formal proposal to "
            "administration, propose a training program using free resources, recommend a small local "
            "conference for the first outing, list practical fundraising ideas, create a succession plan "
            "with officer positions for underclassmen, and establish a team culture centered on learning, "
            "inclusion, and support rather than awards obsession."
        ),
        "key_concepts": "program building, club founding, recruitment, fundraising, sustainability, team culture",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Transitioning MUN Skills to Real-World Careers",
        "prompt": (
            "You are a graduating senior who has done MUN for 4 years. You want to articulate how your "
            "MUN experience has prepared you for real-world careers — whether in diplomacy, law, business, "
            "or other fields.\n\n"
            "Write an analysis (500-650 words) covering:\n\n"
            "1. What transferable skills does MUN develop? List at least 8 specific skills and map each "
            "to a real-world career application.\n"
            "2. How do you describe MUN experience on a resume or CV without it sounding like 'just a club'?\n"
            "3. For students interested in actual diplomacy: What is the pathway from MUN to a real UN "
            "career? How realistic is it?\n"
            "4. For students interested in law: How does MUN prepare you for law school and legal practice?\n"
            "5. For students interested in business: How do negotiation and coalition-building translate "
            "to corporate environments?\n"
            "6. What are the limitations of MUN — what does it NOT teach you about the real world?\n"
            "7. How should you frame your MUN experience in a college application essay?"
        ),
        "hints": (
            "Skills: public speaking, research, negotiation, writing, critical thinking, time management, "
            "teamwork, cultural awareness;"
            "Resume: use action verbs — 'Led a 15-member delegation,' 'Drafted and negotiated a 12-clause resolution';"
            "Diplomacy pathway: MUN → International Relations degree → competitive exams (FSO, UN YPP);"
            "Law: MUN's argumentation, research, and advocacy directly mirror legal practice;"
            "Business: coalition-building = stakeholder management, negotiation = deal-making;"
            "Limitations: MUN simplifies real politics, lacks accountability, and does not capture the years "
            "of relationship-building that real diplomacy requires;"
            "College essays: focus on personal growth and specific moments, not awards lists"
        ),
        "sample_answer": (
            "A nuanced analysis would map 8+ MUN skills to specific career applications, provide resume "
            "language examples, outline realistic pathways to diplomacy/law/business, honestly acknowledge "
            "MUN's limitations (simplified politics, no real consequences), and advise framing college "
            "essays around transformative experiences and growth rather than award counts."
        ),
        "key_concepts": "career skills, resume, diplomacy pathway, transferable skills, college applications, self-reflection",
    },
    {
        "category_type": "GENERAL",
        "difficulty": "ADV",
        "title": "Competing at Collegiate vs. High School Level",
        "prompt": (
            "You are transitioning from high school MUN to collegiate MUN. You have been a successful "
            "high school delegate (multiple Best Delegate awards) but you have heard that collegiate MUN "
            "is 'a completely different game.'\n\n"
            "Write a comparative analysis (500-600 words) covering:\n\n"
            "1. What are the key differences between high school and collegiate MUN? (List at least 6)\n"
            "2. How does the level of research and preparation differ?\n"
            "3. How does the quality of debate and speechmaking change?\n"
            "4. What new committee formats exist at the collegiate level? (e.g., ICJ, ad hoc, joint crisis)\n"
            "5. How does the social and networking aspect of MUN change in college?\n"
            "6. What mistakes do high school superstars make when they first compete at the collegiate level?\n"
            "7. What should you focus on in your first semester of collegiate MUN?\n"
            "8. How do major collegiate conferences (HNMUN, YMUN, ChoMUN, UPMUNC) differ from each other?"
        ),
        "hints": (
            "Key differences: longer conferences (4 days), deeper research expected, more diverse committee types, "
            "higher procedural standards, larger delegations, stronger competition;"
            "Collegiate delegates have studied the topics in university courses — the research bar is much higher;"
            "Speeches are more substantive and less performative — nuance beats volume;"
            "New formats: ICJ (adversarial), ad hoc (Chair-driven), joint crisis (multi-committee);"
            "Social aspect: MUN becomes a networking tool for careers in IR, law, and policy;"
            "Common mistake: relying on high school charisma without backing it up with substance;"
            "First semester: observe, learn the culture, build depth over breadth"
        ),
        "sample_answer": (
            "A thorough analysis would identify key differences in research depth, debate quality, committee "
            "variety, and conference culture, explain that substance replaces performance at the collegiate "
            "level, describe unique formats like ICJ and joint crisis, note the career networking dimension, "
            "warn against relying on high school style without substance, recommend a first-semester focus "
            "on observation and learning, and briefly profile major collegiate conferences."
        ),
        "key_concepts": "collegiate MUN, high school vs college, transition, committee formats, research depth, networking",
    },
]


class Command(BaseCommand):
    help = "Seed the database with high-quality MUN practice questions"

    def add_arguments(self, parser):
        parser.add_argument("--flush", action="store_true", help="Delete all seeded questions before re-seeding")

    def handle(self, *args, **options):
        if options["flush"]:
            deleted, _ = PracticeQuestion.objects.filter(is_seeded=True).delete()
            self.stdout.write(self.style.WARNING(f"Flushed {deleted} seeded questions."))

        # Create categories
        cat_map = {}
        for cat_data in CATEGORIES:
            cat, created = CurriculumCategory.objects.get_or_create(
                slug=cat_data["slug"],
                defaults=cat_data,
            )
            cat_map[cat_data["category_type"]] = cat
            if created:
                self.stdout.write(f"  Created category: {cat.name}")

        # Seed questions
        created_count = 0
        skipped_count = 0
        for q in QUESTIONS:
            cat = cat_map[q["category_type"]]
            _, created = PracticeQuestion.objects.get_or_create(
                title=q["title"],
                category=cat,
                defaults={
                    "question_type": CATEGORY_QUESTION_TYPE[q["category_type"]],
                    "prompt": q["prompt"],
                    "sample_answer": q.get("sample_answer", ""),
                    "difficulty": q["difficulty"],
                    "hints": q.get("hints", ""),
                    "key_concepts": q.get("key_concepts", ""),
                    "is_seeded": True,
                    "quality_score": 4.5,
                },
            )
            if created:
                created_count += 1
            else:
                skipped_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done! Created {created_count}, skipped {skipped_count} (already exist). "
                f"Total seeded: {PracticeQuestion.objects.filter(is_seeded=True).count()}"
            )
        )
