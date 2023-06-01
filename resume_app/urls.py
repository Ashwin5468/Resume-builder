from django.urls import path
from . import views

urlpatterns = [
    path('create-resume/', views.create_resume, name='create_resume'),
    path('preview/<int:personal_info_id>/', views.resume_preview, name='resume_preview'),
    # Add more URL patterns as needed
]