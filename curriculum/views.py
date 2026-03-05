from django.utils import timezone
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import (
    CurriculumCategory, Lesson, PracticeQuestion,
    Submission, AIFeedback, UserProgress, ChatMessage,
)
from .serializers import (
    CurriculumCategorySerializer, CurriculumCategoryListSerializer,
    LessonSerializer, PracticeQuestionSerializer,
    SubmissionSerializer, SubmissionCreateSerializer,
    AIFeedbackSerializer, UserProgressSerializer,
    GenerateQuestionsSerializer, ChatMessageSerializer, ChatSendSerializer,
)
from . import ai_service


# ── Category Views ──────────────────────────────────────────

class CategoryListView(generics.ListAPIView):
    """List all curriculum categories (lightweight)."""
    queryset = CurriculumCategory.objects.all()
    serializer_class = CurriculumCategoryListSerializer
    permission_classes = [permissions.AllowAny]


class CategoryDetailView(generics.RetrieveAPIView):
    """Retrieve a single category with all lessons & questions."""
    queryset = CurriculumCategory.objects.all()
    serializer_class = CurriculumCategorySerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


# ── Lesson Views ────────────────────────────────────────────

class LessonListView(generics.ListAPIView):
    """List lessons, optionally filtered by category slug."""
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Lesson.objects.all()
        category_slug = self.request.query_params.get('category')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        difficulty = self.request.query_params.get('difficulty')
        if difficulty:
            qs = qs.filter(difficulty=difficulty)
        return qs


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


# ── Practice Question Views ─────────────────────────────────

class PracticeQuestionListView(generics.ListAPIView):
    """List practice questions, optionally filtered."""
    serializer_class = PracticeQuestionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = PracticeQuestion.objects.all()
        category_slug = self.request.query_params.get('category')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        question_type = self.request.query_params.get('type')
        if question_type:
            qs = qs.filter(question_type=question_type)
        difficulty = self.request.query_params.get('difficulty')
        if difficulty:
            qs = qs.filter(difficulty=difficulty)
        return qs


class PracticeQuestionDetailView(generics.RetrieveAPIView):
    queryset = PracticeQuestion.objects.all()
    serializer_class = PracticeQuestionSerializer
    permission_classes = [permissions.AllowAny]


# ── Submission Views ─────────────────────────────────────────

class SubmissionListView(generics.ListAPIView):
    """List current user's submissions."""
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)


class SubmissionCreateView(generics.CreateAPIView):
    """Create a new submission and trigger AI review."""
    serializer_class = SubmissionCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        self._submission = serializer.save(user=self.request.user)
        # Trigger AI review synchronously so feedback is in the response
        self._run_ai_review(self._submission)

    def create(self, request, *args, **kwargs):
        """Override create to return full submission data with feedback."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # Refresh from DB to pick up the newly-created feedback relation
        self._submission.refresh_from_db()
        output = SubmissionSerializer(self._submission).data
        return Response(output, status=status.HTTP_201_CREATED)

    def _run_ai_review(self, submission):
        """Run DiplomAI review on the submission."""
        try:
            question_prompt = submission.question.prompt if submission.question else ""
            category_type = submission.category.category_type

            # Get text content — extract from file if text_content is empty
            text_content = submission.text_content
            if not text_content and submission.file_upload:
                text_content = ai_service.extract_text_from_file(submission.file_upload)

            if category_type == 'DRAFT':
                result = ai_service.review_draft_resolution(
                    text_content, question_prompt
                )
            elif category_type == 'SPEECH':
                result = ai_service.review_speech(
                    text_content=text_content,
                    video_url=submission.video_url,
                    question_prompt=question_prompt,
                )
            elif category_type == 'NEGOTIATION':
                result = ai_service.review_negotiation(
                    text_content, question_prompt
                )
            else:
                result = ai_service.review_general(
                    text_content, question_prompt
                )

            AIFeedback.objects.create(
                submission=submission,
                overall_score=result.get('overall_score', 0),
                strengths=result.get('strengths', ''),
                improvements=result.get('improvements', ''),
                detailed_feedback=result.get('detailed_feedback', ''),
                suggestions=result.get('suggestions', ''),
            )
            submission.status = 'REVIEWED'
            submission.save()

        except Exception as e:
            # Log error but don't break the submission flow
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"AI review failed for submission {submission.id}: {e}")


class SubmissionDetailView(generics.RetrieveAPIView):
    """Get submission detail with feedback."""
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)


# ── AI Generate Questions ────────────────────────────────────

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def generate_questions(request):
    """Generate practice questions on the fly using DiplomAI."""
    serializer = GenerateQuestionsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    questions = ai_service.generate_practice_questions(
        category_type=serializer.validated_data['category_type'],
        difficulty=serializer.validated_data.get('difficulty', 'INT'),
        count=serializer.validated_data.get('count', 3),
    )

    return Response({"questions": questions}, status=status.HTTP_200_OK)


# ── User Progress Views ─────────────────────────────────────

class UserProgressListView(generics.ListAPIView):
    """List current user's lesson progress."""
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_lesson_complete(request, lesson_id):
    """Mark a lesson as complete for the current user."""
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except Lesson.DoesNotExist:
        return Response({"error": "Lesson not found."}, status=status.HTTP_404_NOT_FOUND)

    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson,
    )
    progress.completed = True
    progress.completed_at = timezone.now()
    progress.save()

    return Response(UserProgressSerializer(progress).data, status=status.HTTP_200_OK)


# ── Dashboard Stats ──────────────────────────────────────────

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def curriculum_stats(request):
    """Get user's curriculum dashboard stats — comprehensive progress overview."""
    user = request.user
    total_lessons = Lesson.objects.count()
    completed_lessons = UserProgress.objects.filter(user=user, completed=True).count()
    total_submissions = Submission.objects.filter(user=user).count()
    reviewed_submissions = Submission.objects.filter(user=user, status='REVIEWED').count()

    avg_score = 0
    if reviewed_submissions > 0:
        from django.db.models import Avg, Max, Min, Count
        score_stats = (
            AIFeedback.objects
            .filter(submission__user=user)
            .aggregate(
                avg=Avg('overall_score'),
                best=Max('overall_score'),
                lowest=Min('overall_score'),
            )
        )
        avg_score = score_stats['avg'] or 0

        # Per-category breakdown
        category_stats = (
            Submission.objects
            .filter(user=user, status='REVIEWED')
            .values('category__name', 'category__category_type')
            .annotate(
                count=Count('id'),
                avg_score=Avg('feedback__overall_score'),
                best_score=Max('feedback__overall_score'),
            )
            .order_by('-avg_score')
        )

        # Recent scores for trend
        recent_scores = list(
            AIFeedback.objects
            .filter(submission__user=user)
            .order_by('-created_at')
            .values_list('overall_score', flat=True)[:10]
        )
    else:
        score_stats = {'avg': 0, 'best': 0, 'lowest': 0}
        category_stats = []
        recent_scores = []

    # Skill level estimation based on average score
    if avg_score >= 85:
        skill_level = "Advanced"
    elif avg_score >= 65:
        skill_level = "Intermediate"
    elif avg_score > 0:
        skill_level = "Beginner"
    else:
        skill_level = "New Delegate"

    return Response({
        "total_lessons": total_lessons,
        "completed_lessons": completed_lessons,
        "completion_percentage": round((completed_lessons / total_lessons * 100) if total_lessons > 0 else 0, 1),
        "total_submissions": total_submissions,
        "reviewed_submissions": reviewed_submissions,
        "average_score": round(avg_score, 1),
        "best_score": score_stats.get('best') or 0,
        "lowest_score": score_stats.get('lowest') or 0,
        "skill_level": skill_level,
        "category_breakdown": list(category_stats) if category_stats else [],
        "recent_scores": recent_scores,
    })


# ── DiplomAI Chat ────────────────────────────────────────────

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def chat_send(request):
    """Send a message to DiplomAI and get a response."""
    import uuid

    serializer = ChatSendSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user_message = serializer.validated_data['message']
    session_id = serializer.validated_data.get('session_id') or str(uuid.uuid4())[:16]
    question_id = serializer.validated_data.get('question_id')

    question = None
    question_context = ""
    if question_id:
        try:
            question = PracticeQuestion.objects.get(pk=question_id)
            question_context = f"Title: {question.title}\nType: {question.get_question_type_display()}\nPrompt: {question.prompt}"
            if question.hints:
                question_context += f"\nHints: {question.hints}"
        except PracticeQuestion.DoesNotExist:
            pass

    # Save user message
    ChatMessage.objects.create(
        user=request.user,
        question=question,
        session_id=session_id,
        role='user',
        content=user_message,
    )

    # Build conversation history
    history = ChatMessage.objects.filter(
        user=request.user,
        session_id=session_id,
    ).order_by('created_at').values('role', 'content')

    messages = list(history)

    # Get AI response
    ai_response = ai_service.chat_with_diplomai(messages, question_context)

    # Save AI response
    ai_msg = ChatMessage.objects.create(
        user=request.user,
        question=question,
        session_id=session_id,
        role='assistant',
        content=ai_response,
    )

    return Response({
        "session_id": session_id,
        "response": ChatMessageSerializer(ai_msg).data,
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def chat_history(request):
    """Get chat history for a session."""
    session_id = request.query_params.get('session_id')
    if not session_id:
        return Response({"error": "session_id is required."}, status=status.HTTP_400_BAD_REQUEST)

    messages = ChatMessage.objects.filter(
        user=request.user,
        session_id=session_id,
    ).order_by('created_at')

    return Response(ChatMessageSerializer(messages, many=True).data)
