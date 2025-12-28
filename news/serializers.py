# news/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # Make featured_image optional so the POST request doesn't fail without it
    featured_image = serializers.ImageField(required=False, allow_null=True)
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'category', 'featured_image', 'author_name', 'created_at']
        read_only_fields = ['author_name', 'created_at']