from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('view/', views.view_questions, name='view_questions'),
]
