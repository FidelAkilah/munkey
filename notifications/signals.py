from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Notification
from .helpers import notify, STREAK_MILESTONES


@receiver(post_save, sender='curriculum.AIFeedback')
def notify_ai_feedback_ready(sender, instance, created, **kwargs):
    """Notify user when AI feedback is generated for their submission."""
    if not created:
        return
    submission = instance.submission
    notify(
        recipient=submission.user,
        notification_type=Notification.Type.AI_FEEDBACK_READY,
        title='AI Feedback Ready',
        message=f"Your submission has been reviewed! Score: {instance.overall_score}/100",
        link=f"/curriculum/question/{submission.question_id}" if submission.question_id else "/dashboard",
    )


@receiver(post_save, sender='curriculum.AIFeedback')
def notify_streak_milestone(sender, instance, created, **kwargs):
    """Notify user when they hit a streak milestone (7, 14, 30, 60, 100 days)."""
    if not created:
        return
    from curriculum.models import UserStats
    user = instance.submission.user
    try:
        stats = UserStats.objects.get(user=user)
    except UserStats.DoesNotExist:
        return
    if stats.current_streak_days in STREAK_MILESTONES:
        notify(
            recipient=user,
            notification_type=Notification.Type.STREAK_MILESTONE,
            title='Streak Milestone!',
            message=f"Amazing! You've maintained a {stats.current_streak_days}-day practice streak!",
            link="/dashboard",
        )


@receiver(pre_save, sender='news.Article')
def capture_article_old_status(sender, instance, **kwargs):
    """Stash the old status so post_save can detect transitions."""
    if instance.pk:
        try:
            instance._old_status = sender.objects.values_list('status', flat=True).get(pk=instance.pk)
        except sender.DoesNotExist:
            instance._old_status = None
    else:
        instance._old_status = None


@receiver(post_save, sender='news.Article')
def notify_article_status_change(sender, instance, created, **kwargs):
    """Notify article author when their article is approved or rejected."""
    if created:
        return
    old_status = getattr(instance, '_old_status', None)
    if old_status != 'PENDING':
        return
    if instance.status == 'APPROVED':
        notify(
            recipient=instance.author,
            notification_type=Notification.Type.ARTICLE_APPROVED,
            title='Article Approved',
            message=f"Your article '{instance.title}' has been approved and is now live!",
            link=f"/news/{instance.slug}",
        )
    elif instance.status == 'REJECTED':
        reason = instance.rejection_reason or 'No reason provided'
        notify(
            recipient=instance.author,
            notification_type=Notification.Type.ARTICLE_REJECTED,
            title='Article Needs Revisions',
            message=f"Your article '{instance.title}' needs revisions. Reason: {reason}",
            link="/news/my-articles",
        )


@receiver(post_save, sender='community.Comment')
def notify_new_comment(sender, instance, created, **kwargs):
    """Notify article author when someone comments on their article."""
    if not created:
        return
    article = instance.article
    # Don't notify if the commenter is the article author
    if instance.user == article.author:
        return
    notify(
        recipient=article.author,
        notification_type=Notification.Type.NEW_COMMENT,
        title='New Comment',
        message=f"{instance.user.username} commented on '{article.title}'",
        link=f"/news/{article.slug}",
    )
