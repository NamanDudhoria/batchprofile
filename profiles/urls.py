from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('user/<str:username>/', views.profile_view, name='user_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('add-project/', views.add_project, name='add_project'),
<<<<<<< HEAD
    path('edit-project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('add-activity/', views.add_activity, name='add_activity'),
    path('edit-activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('delete-activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
=======
    path('add-activity/', views.add_activity, name='add_activity'),
>>>>>>> 7b70513757c298ab07b65d8b7b63bc5c5ae65976
    path('users/', views.user_list, name='user_list'),
]
