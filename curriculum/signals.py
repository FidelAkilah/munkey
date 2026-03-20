from datetime import date

from django.db.models import Avg, Max
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AIFeedback, Submission, UserStats


@receiver(post_save, sender=AIFeedback)
def update_user_stats_on_feedback(sender, instance, created, **kwargs):
    """Recalculate UserStats every time an AIFeedback record is created."""
    if not created:
        return

    user = instance.submission.user
    stats, _ = UserStats.objects.get_or_create(user=user)

    # Aggregate from all reviewed submissions
    reviewed = Submission.objects.filter(user=user, status='REVIEWED')
    feedbacks = AIFeedback.objects.filter(submission__user=user)

    agg = feedbacks.aggregate(avg=Avg('overall_score'), best=Max('overall_score'))
    stats.total_submissions = reviewed.count()
    stats.average_score = round(agg['avg'] or 0, 1)
    stats.best_score = agg['best'] or 0

    # Per-category averages
    cat_scores = {}
    cat_data = (
        feedbacks
        .values('submission__category__category_type')
        .annotate(avg=Avg('overall_score'), best=Max('overall_score'))
    )
    for row in cat_data:
        cat_type = row['submission__category__category_type']
        if cat_type:
            count = feedbacks.filter(submission__category__category_type=cat_type).count()
            cat_scores[cat_type] = {
                'avg': round(row['avg'] or 0, 1),
                'count': count,
                'best': row['best'] or 0,
            }
    stats.scores_by_category = cat_scores

    # Streak logic
    today = date.today()
    if stats.last_active_date is None:
        stats.current_streak_days = 1
    elif stats.last_active_date == today:
        pass  # Already active today, no change
    elif (today - stats.last_active_date).days == 1:
        stats.current_streak_days += 1
    else:
        stats.current_streak_days = 1

    stats.last_active_date = today
    if stats.current_streak_days > stats.longest_streak_days:
        stats.longest_streak_days = stats.current_streak_days

    stats.save()
