from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_page, name='student_page'),
    path('info/', views.student_info, name='student_info'),
    path('courses/', views.student_courses, name='student_courses'),
    path('achievements/', views.student_achievements, name='student_achievements'),
]