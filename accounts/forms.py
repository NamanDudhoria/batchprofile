from django import forms
from django.contrib.auth.forms import UserCreationForm
from profiles.models import CustomUser, Project

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'bio', 'skills', 'domain')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'domain', 'project_url', 'file']