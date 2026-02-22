from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    UserArticleListView,
    PendingArticleListView,
    ApproveArticleView,
    RejectArticleView
)

urlpatterns = [
    # Public endpoints
    path('', ArticleListView.as_view(), name='article-list'),

    # User endpoints
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('my-articles/', UserArticleListView.as_view(), name='user-articles'),

    # Admin review endpoints
    path('admin/pending/', PendingArticleListView.as_view(), name='admin-pending'),
    path('admin/<int:pk>/approve/', ApproveArticleView.as_view(), name='admin-approve'),
    path('admin/<int:pk>/reject/', RejectArticleView.as_view(), name='admin-reject'),

    # Detail endpoint (must be last - slug could match other paths)
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
