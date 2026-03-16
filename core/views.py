"""
Throttled wrappers for auth endpoints (djoser/simplejwt).
These override the default djoser JWT views to add brute-force rate limiting.
"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from djoser.views import UserViewSet
from core.throttling import AuthEndpointThrottle


class ThrottledTokenObtainPairView(TokenObtainPairView):
    """JWT login with 5/min IP-based rate limiting."""
    throttle_classes = [AuthEndpointThrottle]


class ThrottledTokenRefreshView(TokenRefreshView):
    """JWT refresh with 5/min IP-based rate limiting."""
    throttle_classes = [AuthEndpointThrottle]


class ThrottledUserCreateViewSet(UserViewSet):
    """User registration with 5/min IP-based rate limiting on create."""

    def get_throttles(self):
        if self.action == 'create':
            return [AuthEndpointThrottle()]
        return super().get_throttles()
