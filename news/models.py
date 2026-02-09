from django.db import models
from accounts.models import User

class Article(models.Model):
    class Category(models.TextChoices):
        NEWS = 'NW', 'Global News'
        GUIDE = 'GD', 'Preparation Guides'
        INTERVIEW = 'IN', 'Delegate Interviews'

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending Review'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=Category.choices, default=Category.NEWS)
    featured_image = models.ImageField(upload_to='news_images/')
    content = models.TextField()
    is_breaking = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )
    rejection_reason = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Logic: Only show articles safe for Juniors if flagged
    is_junior_safe = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at'] # Newest first

