# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('batch/', views.batch_profile, name='batch_profile'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload-project/', views.upload_project, name='upload_project'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]