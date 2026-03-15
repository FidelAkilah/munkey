from django.urls import path
from . import views

urlpatterns = [
    # Categories
    path('categories/', views.CategoryListView.as_view(), name='curriculum-categories'),
    path('categories/<slug:slug>/', views.CategoryDetailView.as_view(), name='curriculum-category-detail'),

    # Lessons
    path('lessons/', views.LessonListView.as_view(), name='curriculum-lessons'),
    path('lessons/<slug:slug>/', views.LessonDetailView.as_view(), name='curriculum-lesson-detail'),

    # Practice Questions
    path('questions/', views.PracticeQuestionListView.as_view(), name='curriculum-questions'),
    path('questions/<int:pk>/', views.PracticeQuestionDetailView.as_view(), name='curriculum-question-detail'),

    # Submissions
    path('submissions/', views.SubmissionListView.as_view(), name='curriculum-submissions'),
    path('submissions/create/', views.SubmissionCreateView.as_view(), name='curriculum-submit'),
    path('submissions/<int:pk>/', views.SubmissionDetailView.as_view(), name='curriculum-submission-detail'),

    # AI Generate
    path('generate-questions/', views.generate_questions, name='curriculum-generate-questions'),

    # Question of the Day
    path('question-of-the-day/', views.question_of_the_day, name='curriculum-qotd'),

    # DiplomAI Chat
    path('chat/', views.chat_send, name='curriculum-chat'),
    path('chat/history/', views.chat_history, name='curriculum-chat-history'),

    # Progress
    path('progress/', views.UserProgressListView.as_view(), name='curriculum-progress'),
    path('progress/complete/<int:lesson_id>/', views.mark_lesson_complete, name='curriculum-complete-lesson'),

    # Dashboard stats
    path('stats/', views.curriculum_stats, name='curriculum-stats'),
]
