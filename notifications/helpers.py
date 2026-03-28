from .models import Notification


def notify(recipient, notification_type, title, message, link=''):
    """Create a notification for a user."""
    return Notification.objects.create(
        recipient=recipient,
        type=notification_type,
        title=title,
        message=message,
        link=link,
    )


STREAK_MILESTONES = [7, 14, 30, 60, 100]
