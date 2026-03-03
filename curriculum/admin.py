from django.contrib import admin
from .models import (
    CurriculumCategory, Lesson, PracticeQuestion,
    Submission, AIFeedback, UserProgress,
)


@admin.register(CurriculumCategory)
class CurriculumCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'icon', 'order']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'order', 'estimated_minutes']
    list_filter = ['category', 'difficulty']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['category', 'order']


@admin.register(PracticeQuestion)
class PracticeQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'question_type', 'difficulty']
    list_filter = ['category', 'question_type', 'difficulty']


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'submission_type', 'status', 'created_at']
    list_filter = ['status', 'submission_type', 'category']
    readonly_fields = ['created_at']


@admin.register(AIFeedback)
class AIFeedbackAdmin(admin.ModelAdmin):
    list_display = ['submission', 'overall_score', 'created_at']
    readonly_fields = ['created_at']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'completed', 'completed_at']
    list_filter = ['completed']
