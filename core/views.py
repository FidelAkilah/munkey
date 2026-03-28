"""
Throttled wrappers for auth endpoints (djoser/simplejwt),
plus the global search endpoint.
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


# ── Global Search ──────────────────────────────────────────

from rest_framework import permissions, status as http_status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def global_search(request):
    """Search across articles, lessons, practice questions, and conferences.

    Query params:
        q     — search query (required, min 2 chars)
        type  — all|articles|questions|conferences|lessons (default: all)
    """
    query = request.GET.get('q', '').strip()
    if len(query) < 2:
        return Response(
            {"error": "Query must be at least 2 characters."},
            status=http_status.HTTP_400_BAD_REQUEST,
        )

    search_type = request.GET.get('type', 'all').lower()
    search_query = SearchQuery(query, search_type='websearch')

    # Check if user is junior for safety filtering
    is_junior = (
        request.user.is_authenticated
        and hasattr(request.user, 'role')
        and request.user.role == 'JR'
    )

    results = {}

    if search_type in ('all', 'articles'):
        results['articles'] = _search_articles(search_query, query, is_junior)

    if search_type in ('all', 'lessons'):
        results['lessons'] = _search_lessons(search_query, query)

    if search_type in ('all', 'questions'):
        results['questions'] = _search_questions(search_query, query)

    if search_type in ('all', 'conferences'):
        results['conferences'] = _search_conferences(search_query, query)

    return Response(results)


def _search_articles(search_query, raw_query, is_junior):
    from news.models import Article

    qs = Article.objects.filter(status='APPROVED')
    if is_junior:
        qs = qs.filter(is_junior_safe=True)

    qs = (
        qs.annotate(
            search=SearchVector('title', 'content'),
            rank=SearchRank(SearchVector('title', 'content'), search_query),
        )
        .filter(search=search_query)
        .order_by('-rank')[:10]
    )

    return [
        {
            'id': a.id,
            'title': a.title,
            'slug': a.slug,
            'snippet': _snippet(a.content, raw_query),
            'category': a.get_category_display(),
            'created_at': a.created_at.isoformat(),
            'type': 'article',
        }
        for a in qs
    ]


def _search_lessons(search_query, raw_query):
    from curriculum.models import Lesson

    qs = (
        Lesson.objects.annotate(
            search=SearchVector('title', 'content'),
            rank=SearchRank(SearchVector('title', 'content'), search_query),
        )
        .filter(search=search_query)
        .select_related('category')
        .order_by('-rank')[:10]
    )

    return [
        {
            'id': l.id,
            'title': l.title,
            'slug': l.slug,
            'snippet': _snippet(l.content, raw_query),
            'category': l.category.name,
            'category_type': l.category.category_type,
            'difficulty': l.difficulty,
            'type': 'lesson',
        }
        for l in qs
    ]


def _search_questions(search_query, raw_query):
    from curriculum.models import PracticeQuestion

    qs = (
        PracticeQuestion.objects.annotate(
            search=SearchVector('title', 'prompt'),
            rank=SearchRank(SearchVector('title', 'prompt'), search_query),
        )
        .filter(search=search_query)
        .select_related('category')
        .order_by('-rank')[:10]
    )

    return [
        {
            'id': q.id,
            'title': q.title,
            'snippet': _snippet(q.prompt, raw_query),
            'category': q.category.name,
            'category_type': q.category.category_type,
            'difficulty': q.difficulty,
            'question_type': q.question_type,
            'type': 'question',
        }
        for q in qs
    ]


def _search_conferences(search_query, raw_query):
    from directory.models import Conference

    qs = (
        Conference.objects.filter(is_active=True)
        .annotate(
            search=SearchVector('name', 'city', 'country'),
            rank=SearchRank(SearchVector('name', 'city', 'country'), search_query),
        )
        .filter(search=search_query)
        .order_by('-rank')[:10]
    )

    return [
        {
            'id': c.id,
            'name': c.name,
            'city': c.city,
            'country': c.country,
            'start_date': c.start_date.isoformat() if c.start_date else None,
            'type': 'conference',
        }
        for c in qs
    ]


def _snippet(text, query, max_length=200):
    """Extract a snippet around the first occurrence of the query."""
    if not text:
        return ''
    lower_text = text.lower()
    lower_query = query.lower()
    idx = lower_text.find(lower_query)
    if idx == -1:
        return text[:max_length] + ('...' if len(text) > max_length else '')
    start = max(0, idx - 80)
    end = min(len(text), idx + len(query) + 120)
    snippet = ('...' if start > 0 else '') + text[start:end] + ('...' if end < len(text) else '')
    return snippet
