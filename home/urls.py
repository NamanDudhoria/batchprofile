from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hire-from-us/', views.hire_from_us, name='hire_from_us'),
]