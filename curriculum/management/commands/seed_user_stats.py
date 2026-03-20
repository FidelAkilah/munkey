"""
Management command to create/update UserStats for all existing users
who have at least one submission.

Usage:
    python manage.py seed_user_stats
"""

from datetime import date

from django.core.management.base import BaseCommand
from django.db.models import Avg, Max, Count

from accounts.models import User
from curriculum.models import Submission, AIFeedback, UserStats


class Command(BaseCommand):
    help = "Create or update UserStats records for all users with submissions."

    def handle(self, *args, **options):
        users_with_submissions = (
            User.objects.filter(curriculum_submissions__isnull=False).distinct()
        )
        created_count = 0
        updated_count = 0

        for user in users_with_submissions:
            stats, created = UserStats.objects.get_or_create(user=user)

            reviewed = Submission.objects.filter(user=user, status='REVIEWED')
            feedbacks = AIFeedback.objects.filter(submission__user=user)

            agg = feedbacks.aggregate(avg=Avg('overall_score'), best=Max('overall_score'))
            stats.total_submissions = reviewed.count()
            stats.average_score = round(agg['avg'] or 0, 1)
            stats.best_score = agg['best'] or 0

            # Per-category
            cat_scores = {}
            cat_data = (
                feedbacks
                .values('submission__category__category_type')
                .annotate(avg=Avg('overall_score'), best=Max('overall_score'), count=Count('id'))
            )
            for row in cat_data:
                cat_type = row['submission__category__category_type']
                if cat_type:
                    cat_scores[cat_type] = {
                        'avg': round(row['avg'] or 0, 1),
                        'count': row['count'],
                        'best': row['best'] or 0,
                    }
            stats.scores_by_category = cat_scores

            # Set last_active_date from most recent submission
            latest = Submission.objects.filter(user=user).order_by('-created_at').first()
            if latest:
                stats.last_active_date = latest.created_at.date()

            # Initial streak = 1 if they have any submissions
            if stats.current_streak_days == 0 and stats.total_submissions > 0:
                stats.current_streak_days = 1
                stats.longest_streak_days = max(stats.longest_streak_days, 1)

            stats.save()

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Done: {created_count} created, {updated_count} updated."
        ))
