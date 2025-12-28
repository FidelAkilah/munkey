from django.shortcuts import render

from rest_framework import generics
from .models import Conference
from .serializers import ConferenceSerializer

class ConferenceList(generics.ListAPIView):
    queryset = Conference.objects.filter(is_active=True)
    serializer_class = ConferenceSerializer