from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('hire-from-us/', views.hire_from_us, name='hire_from_us'),
    path('search/', views.search_students, name='search_students'),
    path('batch-profile/', views.batch_profile, name='batch_profile'),
]
