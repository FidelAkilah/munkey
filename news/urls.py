from django.urls import path
from . import views  # Make sure you have at least one view defined

urlpatterns = [
    # If you don't have views yet, leave it empty like this [] 
    # but the variable MUST exist.
    # path('register/', views.RegisterView.as_view(), name='register'),
]