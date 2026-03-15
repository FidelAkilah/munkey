from django.db import models
from django.conf import settings


class CurriculumCategory(models.Model):
    """Categories like Speech, Draft Resolution, Negotiation, etc."""
    CATEGORY_CHOICES = [
        ('SPEECH', 'Speech & Public Speaking'),
        ('DRAFT', 'Draft Resolution Writing'),
        ('NEGOTIATION', 'Negotiation & Diplomacy'),
        ('RESEARCH', 'Research & Position Papers'),
        ('PROCEDURE', 'Rules of Procedure'),
        ('GENERAL', 'General MUN Skills'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=10, default='📚', help_text="Emoji icon for the category")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Curriculum Categories'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Individual lessons within a category."""
    DIFFICULTY_CHOICES = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
    ]

    category = models.ForeignKey(CurriculumCategory, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField(help_text="Lesson content in markdown")
    difficulty = models.CharField(max_length=3, choices=DIFFICULTY_CHOICES, default='BEG')
    order = models.PositiveIntegerField(default=0)
    estimated_minutes = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class PracticeQuestion(models.Model):
    """Practice questions for each category."""
    QUESTION_TYPE_CHOICES = [
        ('SPEECH', 'Speech Prompt'),
        ('DRAFT', 'Draft Resolution Exercise'),
        ('NEGOTIATION', 'Negotiation Scenario'),
        ('QUIZ', 'Multiple Choice Quiz'),
        ('OPEN', 'Open-Ended Question'),
    ]

    category = models.ForeignKey(CurriculumCategory, related_name='questions', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default='OPEN')
    title = models.CharField(max_length=255)
    prompt = models.TextField(help_text="The question or scenario prompt")
    sample_answer = models.TextField(blank=True, help_text="Optional sample/ideal answer for AI reference")
    difficulty = models.CharField(max_length=3, choices=Lesson.DIFFICULTY_CHOICES, default='BEG')
    hints = models.TextField(blank=True, help_text="Optional hints for the student")
    key_concepts = models.TextField(blank=True, help_text="Comma-separated key MUN concepts this question tests")
    is_seeded = models.BooleanField(default=False, help_text="True for hand-curated/pre-seeded questions")
    quality_score = models.FloatField(null=True, blank=True, help_text="Quality rating 0-5 for future curation")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_seeded', '-created_at']

    def __str__(self):
        return self.title


class Submission(models.Model):
    """User submissions: text (draft resolutions) or file (speech videos)."""
    SUBMISSION_TYPE_CHOICES = [
        ('TEXT', 'Text Submission'),
        ('FILE', 'File Upload'),
        ('VIDEO_URL', 'Video URL'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('REVIEWED', 'AI Reviewed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='curriculum_submissions', on_delete=models.CASCADE)
    question = models.ForeignKey(PracticeQuestion, related_name='submissions', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(CurriculumCategory, related_name='submissions', on_delete=models.CASCADE)
    submission_type = models.CharField(max_length=10, choices=SUBMISSION_TYPE_CHOICES, default='TEXT')
    text_content = models.TextField(blank=True, help_text="For draft resolutions or text answers")
    file_upload = models.FileField(upload_to='curriculum/uploads/%Y/%m/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="URL to uploaded speech video")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.get_submission_type_display()} ({self.created_at.strftime('%Y-%m-%d')})"


class AIFeedback(models.Model):
    """AI-generated feedback for submissions."""
    submission = models.OneToOneField(Submission, related_name='feedback', on_delete=models.CASCADE)
    overall_score = models.PositiveIntegerField(default=0, help_text="Score out of 100")
    rubric_scores = models.JSONField(null=True, blank=True, help_text="Per-criterion rubric breakdown: {criterion: {score, max, comment}}")
    strengths = models.TextField(blank=True)
    improvements = models.TextField(blank=True)
    detailed_feedback = models.TextField(blank=True)
    suggestions = models.TextField(blank=True, help_text="Actionable next steps")
    example_revision = models.TextField(blank=True, null=True, help_text="AI-rewritten example of the student's weakest section")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AI Feedback'
        verbose_name_plural = 'AI Feedback'

    def __str__(self):
        return f"Feedback for {self.submission} — Score: {self.overall_score}/100"


class UserProgress(models.Model):
    """Track a user's progress through the curriculum."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='curriculum_progress', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='progress', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'lesson')
        verbose_name_plural = 'User Progress'

    def __str__(self):
        status = '✅' if self.completed else '⬜'
        return f"{status} {self.user.username} — {self.lesson.title}"


class ChatMessage(models.Model):
    """Chat messages between user and DiplomAI about a question or topic."""
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'DiplomAI'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chat_messages', on_delete=models.CASCADE)
    question = models.ForeignKey(PracticeQuestion, related_name='chat_messages', on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=64, db_index=True, help_text="Groups messages in a conversation")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"[{self.role}] {self.content[:60]}..."
