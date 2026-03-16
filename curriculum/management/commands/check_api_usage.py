"""
Management command to check today's OpenAI API usage stats.

Usage:
    python manage.py check_api_usage
    python manage.py check_api_usage --days 7
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Sum, Count
from django.conf import settings

from curriculum.models import APIUsageLog


class Command(BaseCommand):
    help = "Print today's OpenAI API usage stats (tokens, calls, by endpoint)"

    def add_arguments(self, parser):
        parser.add_argument(
            '--days', type=int, default=1,
            help='Number of days to look back (default: 1 = today only)',
        )

    def handle(self, *args, **options):
        days = options['days']
        since = timezone.now() - timezone.timedelta(days=days)
        daily_limit = getattr(settings, 'DAILY_TOKEN_LIMIT', 500000)

        logs = APIUsageLog.objects.filter(timestamp__gte=since)

        total_tokens = logs.aggregate(total=Sum('estimated_tokens'))['total'] or 0
        total_calls = logs.count()

        self.stdout.write(self.style.HTTP_INFO(
            f"\n{'=' * 50}"
            f"\n  OpenAI API Usage — Last {days} day(s)"
            f"\n{'=' * 50}"
        ))

        self.stdout.write(f"\n  Total API calls:    {total_calls}")
        self.stdout.write(f"  Total tokens used:  {total_tokens:,}")
        self.stdout.write(f"  Daily token limit:  {daily_limit:,}")

        # Today's usage specifically
        today_tokens = APIUsageLog.tokens_used_today()
        pct = (today_tokens / daily_limit * 100) if daily_limit > 0 else 0
        if pct >= 90:
            style = self.style.ERROR
        elif pct >= 70:
            style = self.style.WARNING
        else:
            style = self.style.SUCCESS
        self.stdout.write(style(
            f"  Today's usage:      {today_tokens:,} / {daily_limit:,} ({pct:.1f}%)"
        ))

        # Breakdown by endpoint
        endpoint_stats = (
            logs.values('endpoint')
            .annotate(calls=Count('id'), tokens=Sum('estimated_tokens'))
            .order_by('-tokens')
        )

        if endpoint_stats:
            self.stdout.write(f"\n  {'Endpoint':<25} {'Calls':>8} {'Tokens':>12}")
            self.stdout.write(f"  {'-' * 45}")
            for stat in endpoint_stats:
                self.stdout.write(
                    f"  {stat['endpoint']:<25} {stat['calls']:>8} {stat['tokens']:>12,}"
                )

        # Top users
        user_stats = (
            logs.values('user__username')
            .annotate(calls=Count('id'), tokens=Sum('estimated_tokens'))
            .order_by('-tokens')[:10]
        )

        if user_stats:
            self.stdout.write(f"\n  {'User':<25} {'Calls':>8} {'Tokens':>12}")
            self.stdout.write(f"  {'-' * 45}")
            for stat in user_stats:
                username = stat['user__username'] or 'anonymous'
                self.stdout.write(
                    f"  {username:<25} {stat['calls']:>8} {stat['tokens']:>12,}"
                )

        self.stdout.write(f"\n{'=' * 50}\n")
