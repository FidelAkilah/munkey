from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        JUNIOR = 'JR', 'Junior (Elementary/JH)'
        SENIOR = 'SR', 'Senior (HS/College)'
        ADMIN = 'AD', 'Moderator/Admin'

    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.SENIOR
    )
    
    # Safety Check: Junior users might need "Parental Consent" or "Restricted DM" flags
    is_restricted = models.BooleanField(default=False) 

    def save(self, *args, **kwargs):
        # Auto-restrict if user is Junior (Logic for your safe space)
        if self.role == self.Role.JUNIOR:
            self.is_restricted = True
        super().save(*args, **kwargs)