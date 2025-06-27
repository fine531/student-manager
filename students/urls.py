"""
URL Configuration for Students App
This file defines the URL patterns for the student management system.
"""

from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # Home page - list all students
    path('', views.index, name='index'),
    
    # Add new student page
    path('add/', views.add_student, name='add_student'),
    
    # Success page after adding student
    path('success/', views.success, name='success'),
    
    # Delete student (POST request)
    path('delete/<str:student_id>/', views.delete_student, name='delete_student'),
    
    # Activity logs page
    path('logs/', views.logs, name='logs'),
] 