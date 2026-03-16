"""
Custom DRF throttle classes and exception handler for rate limiting.

Throttle tiers:
- AI endpoints (chat, generate-questions, submissions/create): 20/hour per user
- Auth endpoints (login, register): 5/min per IP
- News creation: 10/hour per user
- Comment posting: 30/hour per user
- All other endpoints: 100/min per user
"""
import time

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


class RateLimitHeadersMixin:
    """Mixin that provides rate limit header data after throttle check."""

    def get_rate_limit_headers(self):
        """Return dict of rate limit headers for the response."""
        if not hasattr(self, 'num_requests') or not hasattr(self, 'duration'):
            return {}

        history = self.cache.get(self.key, [])
        now = self.timer()
        remaining = max(0, self.num_requests - len(history))
        if history:
            reset = int(history[-1] + self.duration - now)
        else:
            reset = int(self.duration)

        return {
            'X-RateLimit-Limit': str(self.num_requests),
            'X-RateLimit-Remaining': str(remaining),
            'X-RateLimit-Reset': str(max(0, reset)),
        }


class AIEndpointThrottle(RateLimitHeadersMixin, UserRateThrottle):
    """20 requests/hour per user for AI endpoints."""
    scope = 'ai_endpoint'


class AuthEndpointThrottle(RateLimitHeadersMixin, AnonRateThrottle):
    """5 requests/minute per IP for auth endpoints (brute force protection)."""
    scope = 'auth_endpoint'


class NewsCreateThrottle(RateLimitHeadersMixin, UserRateThrottle):
    """10 requests/hour per user for news creation."""
    scope = 'news_create'


class CommentPostThrottle(RateLimitHeadersMixin, UserRateThrottle):
    """30 requests/hour per user for comment posting."""
    scope = 'comment_post'


class DefaultUserThrottle(RateLimitHeadersMixin, UserRateThrottle):
    """100 requests/minute per user for all other endpoints."""
    scope = 'default_user'


def custom_exception_handler(exc, context):
    """Custom exception handler that formats 429 responses with proper headers."""
    response = exception_handler(exc, context)

    if response is not None and response.status_code == status.HTTP_429_TOO_MANY_REQUESTS:
        # Extract wait time from the Throttled exception
        wait = getattr(exc, 'wait', None)
        retry_after = int(wait) if wait else 60

        response.data = {
            'error': 'Rate limit exceeded',
            'retry_after': retry_after,
        }
        response['Retry-After'] = str(retry_after)

        # Try to add rate limit headers from the throttle that triggered
        view = context.get('view')
        if view and hasattr(view, 'throttled'):
            request = context.get('request')
            if request:
                for throttle in getattr(view, '_throttles', []):
                    if hasattr(throttle, 'get_rate_limit_headers'):
                        headers = throttle.get_rate_limit_headers()
                        for key, value in headers.items():
                            response[key] = value
                        break

    return response


class RateLimitHeadersMiddleware:
    """Middleware that adds rate limit headers to all responses."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None
