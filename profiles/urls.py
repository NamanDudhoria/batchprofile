from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('user/<str:username>/', views.profile_view, name='user_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('add-project/', views.add_project, name='add_project'),
    path('add-activity/', views.add_activity, name='add_activity'),
    path('users/', views.user_list, name='user_list'),
]
