from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector
from django.db import models


class Conference(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            GinIndex(SearchVector('name', 'city', 'country', config='english'), name='conference_search_idx'),
        ]

    def __str__(self):
        return self.name