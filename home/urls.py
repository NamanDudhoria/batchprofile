from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hire-from-us/', views.hire_from_us, name='hire_from_us'),
    path('batch-profile/', views.batch_profile, name='batch_profile'),  # Example additional URL pattern
]