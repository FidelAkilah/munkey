from django.db import models
from accounts.models import User
from news.models import Article
# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_approved = models.BooleanField(default=False) # Safety Gate
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # CS Tip: Trigger an AI Moderation API here
        # if ai_check(self.text) == "SAFE": self.is_approved = True
        super().save(*args, **kwargs)