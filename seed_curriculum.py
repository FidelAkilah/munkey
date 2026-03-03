import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from curriculum.models import CurriculumCategory, PracticeQuestion

# Seed categories
categories = [
    ('Speech & Public Speaking', 'speech', 'SPEECH', 'Master opening speeches, rebuttals, and closing statements. Learn rhetoric, delivery, and persuasion.', '🎤', 1),
    ('Draft Resolution Writing', 'draft-resolution', 'DRAFT', 'Write compelling operative and preambulatory clauses. Learn UN formatting and diplomatic language.', '📜', 2),
    ('Negotiation & Diplomacy', 'negotiation', 'NEGOTIATION', 'Build blocs, broker compromises, and navigate complex diplomatic scenarios.', '🤝', 3),
    ('Research & Position Papers', 'research', 'RESEARCH', 'Deep-dive into topics, write position papers, and build evidence-based arguments.', '🔍', 4),
    ('Rules of Procedure', 'rules-of-procedure', 'PROCEDURE', 'Master motions, points, voting procedures, and parliamentary strategy.', '⚖️', 5),
    ('General MUN Skills', 'general', 'GENERAL', 'Cross-cutting skills every delegate needs: time management, note-passing, crisis response.', '📚', 6),
]

for name, slug, cat_type, desc, icon, order in categories:
    CurriculumCategory.objects.get_or_create(
        slug=slug,
        defaults={'name': name, 'category_type': cat_type, 'description': desc, 'icon': icon, 'order': order}
    )

print(f"Seeded {CurriculumCategory.objects.count()} categories")

# Seed sample practice questions
speech_cat = CurriculumCategory.objects.get(slug='speech')
draft_cat = CurriculumCategory.objects.get(slug='draft-resolution')
nego_cat = CurriculumCategory.objects.get(slug='negotiation')

questions = [
    (speech_cat, 'SPEECH', 'Opening Speech: Climate Crisis', 
     'You are the delegate of Brazil in the UNEP committee. The topic is "Addressing the Impacts of Climate Change on Developing Nations." Write a 90-second opening speech that establishes your country\'s position, highlights key concerns, and proposes initial solutions.', 'BEG',
     'Start with a powerful hook. State your country\'s stance clearly. Mention specific policies Brazil has implemented.'),
    
    (speech_cat, 'SPEECH', 'Rebuttal: Nuclear Disarmament',
     'The delegate of the United States has just argued that nuclear deterrence is essential for global peace. As the delegate of Iran, deliver a 60-second rebuttal that challenges this position while maintaining diplomatic composure.', 'INT',
     'Acknowledge the previous speaker\'s points before countering. Use specific examples and treaties.'),
    
    (draft_cat, 'DRAFT', 'Draft Resolution: Access to Clean Water',
     'Write a draft resolution for the WHO committee on "Ensuring Universal Access to Clean Water by 2035." Include at least 5 preambulatory clauses and 8 operative clauses. Ensure proper UN formatting and realistic policy proposals.', 'INT',
     'Reference existing UN frameworks (SDG 6). Use proper clause formatting: "Noting with concern...", "Encourages member states..."'),
    
    (draft_cat, 'DRAFT', 'Amend This Resolution',
     'The following operative clause has been proposed: "Requests all member states to immediately cease all industrial pollution into freshwater sources." As the delegate of China, propose a friendly amendment that makes this clause more realistic while preserving its intent.', 'ADV',
     'Consider economic implications. Propose phased timelines. Add language about technical assistance.'),
    
    (nego_cat, 'NEGOTIATION', 'Bloc Building Exercise',
     'You are the delegate of India in the DISEC committee discussing "Regulation of Autonomous Weapons Systems." You need to build a bloc of at least 5 countries. Describe your strategy: Which countries would you approach first? What compromises would you offer? How would you handle disagreements within the bloc?', 'INT',
     'Think about regional allies, shared interests, and common concerns. Consider what each country needs.'),
    
    (nego_cat, 'NEGOTIATION', 'Crisis Negotiation',
     'BREAKING: A humanitarian crisis has erupted in a fictional country. As the delegate of your assigned nation in the Security Council, you have 5 minutes to negotiate with 3 other delegates (P5 members). Write out your negotiation strategy, initial proposal, and red lines you won\'t cross.', 'ADV',
     'Define your BATNA (Best Alternative to Negotiated Agreement). Know your veto power dynamics.'),
]

for cat, q_type, title, prompt, diff, hints in questions:
    PracticeQuestion.objects.get_or_create(
        title=title,
        defaults={'category': cat, 'question_type': q_type, 'prompt': prompt, 'difficulty': diff, 'hints': hints}
    )

print(f"Seeded {PracticeQuestion.objects.count()} practice questions")
