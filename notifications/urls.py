from django.urls import path
from .views import NotificationListView, mark_read, mark_all_read, unread_count

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/read/', mark_read, name='notification-mark-read'),
    path('read-all/', mark_all_read, name='notification-read-all'),
    path('unread-count/', unread_count, name='notification-unread-count'),
]
