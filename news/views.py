from rest_framework import generics, permissions
from .models import Article
from .serializers import ArticleSerializer

class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Filtering for global reach: remove city silos
        queryset = Article.objects.all()
        # Logic: If user is not logged in or is a Junior, only show safe content
        if not self.request.user.is_authenticated or self.request.user.role == 'JR':
            return queryset.filter(is_junior_safe=True)
        return queryset