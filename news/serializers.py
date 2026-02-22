# news/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # Make featured_image optional so the POST request doesn't fail without it
    featured_image = serializers.ImageField(required=False, allow_null=True)
    author_name = serializers.ReadOnlyField(source='author.username')
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'category', 'featured_image', 'image_url', 'author_name', 'status', 'created_at']
        read_only_fields = ['author_name', 'status', 'created_at']

class ArticleAdminSerializer(serializers.ModelSerializer):
    """
    Serializer for admin review - includes all fields including rejection_reason
    """
    featured_image = serializers.ImageField(required=False, allow_null=True)
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'category', 'featured_image', 'image_url', 'author_name', 'status', 'rejection_reason', 'created_at', 'updated_at']
        read_only_fields = ['author_name', 'status', 'rejection_reason', 'created_at', 'updated_at']
