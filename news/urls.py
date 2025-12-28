from django.urls import path
from .views import ArticleListView, ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
]