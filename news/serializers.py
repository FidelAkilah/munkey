# news/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'category', 'image_url', 'author_name', 'status', 'created_at']
        read_only_fields = ['author_name', 'status', 'created_at']

class ArticleAdminSerializer(serializers.ModelSerializer):
    """
    Serializer for admin review - includes all fields including rejection_reason
    """
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'category', 'image_url', 'author_name', 'status', 'rejection_reason', 'created_at', 'updated_at']
        read_only_fields = ['author_name', 'status', 'rejection_reason', 'created_at', 'updated_at']
