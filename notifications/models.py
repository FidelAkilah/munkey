from django.db import models
from django.conf import settings


class Notification(models.Model):
    """User notifications for article approvals, comments, AI feedback, and milestones."""

    class Type(models.TextChoices):
        ARTICLE_APPROVED = 'ARTICLE_APPROVED', 'Article Approved'
        ARTICLE_REJECTED = 'ARTICLE_REJECTED', 'Article Rejected'
        NEW_COMMENT = 'NEW_COMMENT', 'New Comment'
        AI_FEEDBACK_READY = 'AI_FEEDBACK_READY', 'AI Feedback Ready'
        STREAK_MILESTONE = 'STREAK_MILESTONE', 'Streak Milestone'
        SYSTEM = 'SYSTEM', 'System'

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='notifications',
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=20, choices=Type.choices)
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False, db_index=True)
    link = models.CharField(max_length=500, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', '-created_at']),
            models.Index(fields=['recipient', 'is_read']),
        ]

    def __str__(self):
        status = '🔵' if not self.is_read else '⚪'
        return f"{status} [{self.get_type_display()}] {self.recipient.username}: {self.title}"
