"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import (
    ThrottledTokenObtainPairView,
    ThrottledTokenRefreshView,
    global_search,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Throttled auth endpoints (must come before djoser includes to take priority)
    path('auth/jwt/create/', ThrottledTokenObtainPairView.as_view(), name='jwt-create'),
    path('auth/jwt/refresh/', ThrottledTokenRefreshView.as_view(), name='jwt-refresh'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # Global search
    path('api/search/', global_search, name='global-search'),
    # Modular Routing
    path('api/users/', include('accounts.urls')),
    path('api/news/', include('news.urls')),
    path('api/conferences/', include('directory.urls')),
    path('api/forum/', include('community.urls')),
    path('api/skills/', include('skills.urls')),
    path('api/curriculum/', include('curriculum.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
