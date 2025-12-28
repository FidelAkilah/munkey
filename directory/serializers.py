from rest_framework import serializers
from .models import Conference

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        # These fields must match exactly what you wrote in models.py
        fields = ['id', 'name', 'city', 'country', 'latitude', 'longitude', 'start_date', 'is_active']