from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer, ArticleAdminSerializer

class ArticleListView(generics.ListAPIView):
    """
    Public endpoint - only shows APPROVED articles
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Only show APPROVED articles to the public
        queryset = Article.objects.filter(status='APPROVED')
        
        # Additional filtering: If user is not logged in or is a Junior, only show safe content
        if not self.request.user.is_authenticated or self.request.user.role == 'JR':
            return queryset.filter(is_junior_safe=True)
        return queryset

class ArticleCreateView(generics.CreateAPIView):
    """
    Allow any authenticated user to submit articles
    Status is automatically set to PENDING
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        # Force status to PENDING - don't trust frontend
        serializer.save(author=self.request.user, status=Article.Status.PENDING)

class UserArticleListView(generics.ListAPIView):
    """
    Allow users to see their own submitted articles
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

class PendingArticleListView(generics.ListAPIView):
    """
    Admin endpoint - list all pending articles for review
    """
    serializer_class = ArticleAdminSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Article.objects.filter(status='PENDING').order_by('created_at')

class ApproveArticleView(APIView):
    """
    Admin endpoint - approve a pending article
    """
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            if article.status != 'PENDING':
                return Response(
                    {'error': 'Only pending articles can be approved'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            article.status = Article.Status.APPROVED
            article.save()
            return Response({'status': 'approved', 'message': 'Article published successfully'})
        except Article.DoesNotExist:
            return Response(
                {'error': 'Article not found'},
                status=status.HTTP_404_NOT_FOUND
            )

class RejectArticleView(APIView):
    """
    Admin endpoint - reject a pending article
    """
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            if article.status != 'PENDING':
                return Response(
                    {'error': 'Only pending articles can be rejected'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            rejection_reason = request.data.get('reason', '')
            article.status = Article.Status.REJECTED
            article.rejection_reason = rejection_reason
            article.save()
            return Response({'status': 'rejected', 'message': 'Article rejected'})
        except Article.DoesNotExist:
            return Response(
                {'error': 'Article not found'},
                status=status.HTTP_404_NOT_FOUND
            )
