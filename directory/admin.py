
from django.contrib import admin
from .models import Conference

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    # This makes the table look professional in the dashboard
    list_display = ('name', 'city', 'country', 'start_date', 'is_active')
    list_filter = ('country', 'is_active')
    search_fields = ('name', 'city')
