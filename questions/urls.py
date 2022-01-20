from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('view/<int:question_id>', views.view_questions, name='view_questions'),
    path('add/', views.add_questions, name='add_questions'),
]
