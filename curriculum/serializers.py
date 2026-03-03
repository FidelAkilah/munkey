from rest_framework import serializers
from .models import (
    CurriculumCategory, Lesson, PracticeQuestion,
    Submission, AIFeedback, UserProgress,
)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'slug', 'content', 'difficulty', 'order', 'estimated_minutes', 'created_at']


class PracticeQuestionSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = PracticeQuestion
        fields = ['id', 'title', 'prompt', 'question_type', 'difficulty', 'hints', 'category_name', 'created_at']


class CurriculumCategorySerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    questions = PracticeQuestionSerializer(many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = CurriculumCategory
        fields = [
            'id', 'name', 'slug', 'category_type', 'description', 'icon',
            'order', 'lessons', 'questions', 'lesson_count', 'question_count',
        ]

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_question_count(self, obj):
        return obj.questions.count()


class CurriculumCategoryListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing categories (no nested data)."""
    lesson_count = serializers.SerializerMethodField()
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = CurriculumCategory
        fields = ['id', 'name', 'slug', 'category_type', 'description', 'icon', 'order', 'lesson_count', 'question_count']

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_question_count(self, obj):
        return obj.questions.count()


class AIFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIFeedback
        fields = ['id', 'overall_score', 'strengths', 'improvements', 'detailed_feedback', 'suggestions', 'created_at']


class SubmissionSerializer(serializers.ModelSerializer):
    feedback = AIFeedbackSerializer(read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Submission
        fields = [
            'id', 'username', 'question', 'category', 'category_name',
            'submission_type', 'text_content', 'file_upload', 'video_url',
            'status', 'feedback', 'created_at',
        ]
        read_only_fields = ['user', 'status', 'feedback']


class SubmissionCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating submissions."""

    class Meta:
        model = Submission
        fields = ['id', 'question', 'category', 'submission_type', 'text_content', 'file_upload', 'video_url']
        read_only_fields = ['id']

    def validate(self, data):
        sub_type = data.get('submission_type', 'TEXT')
        if sub_type == 'TEXT' and not data.get('text_content'):
            raise serializers.ValidationError("Text content is required for text submissions.")
        if sub_type == 'FILE' and not data.get('file_upload'):
            raise serializers.ValidationError("File upload is required for file submissions.")
        if sub_type == 'VIDEO_URL' and not data.get('video_url'):
            raise serializers.ValidationError("Video URL is required for video submissions.")
        return data


class UserProgressSerializer(serializers.ModelSerializer):
    lesson_title = serializers.ReadOnlyField(source='lesson.title')
    category_name = serializers.ReadOnlyField(source='lesson.category.name')

    class Meta:
        model = UserProgress
        fields = ['id', 'lesson', 'lesson_title', 'category_name', 'completed', 'completed_at']
        read_only_fields = ['user']


class GenerateQuestionsSerializer(serializers.Serializer):
    """Serializer for AI question generation request."""
    category_type = serializers.ChoiceField(choices=[c[0] for c in CurriculumCategory.CATEGORY_CHOICES])
    difficulty = serializers.ChoiceField(choices=['BEG', 'INT', 'ADV'], default='INT')
    count = serializers.IntegerField(min_value=1, max_value=5, default=3)
