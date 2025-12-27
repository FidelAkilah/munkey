from django.db import models
from accounts.models import User

class Article(models.Model):
    class Category(models.TextChoices):
        NEWS = 'NW', 'Global News'
        GUIDE = 'GD', 'Preparation Guides'
        INTERVIEW = 'IN', 'Delegate Interviews'

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=Category.choices, default=Category.NEWS)
    featured_image = models.ImageField(upload_to='news_images/')
    content = models.TextField()
    is_breaking = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Logic: Only show articles safe for Juniors if flagged
    is_junior_safe = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at'] # Newest first

