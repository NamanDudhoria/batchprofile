from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Project, Activity, Domain

class CustomUserCreationForm(UserCreationForm):
    domains = forms.ModelMultipleChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'email', 
            'profile_picture', 
            'bio', 
            'skills', 
            'domains', 
            'resume', 
            'linkedin_url', 
            'github_url', 
            'hackerrank_url', 
            'leetcode_url', 
            'kaggle_url'
        )
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 3}),
        }

class CustomUserChangeForm(UserChangeForm):
    domains = forms.ModelMultipleChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'email', 
            'profile_picture', 
            'bio', 
            'skills', 
            'domains', 
            'resume', 
            'linkedin_url', 
            'github_url', 
            'hackerrank_url', 
            'leetcode_url', 
            'kaggle_url'
        )
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 3}),
        }

class ProjectForm(forms.ModelForm):
    domains = forms.ModelMultipleChoiceField(
        queryset=Domain.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'domains', 'project_url', 'file', 'completed_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'completed_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if file.size > 5*1024*1024:  # 5MB limit
                raise forms.ValidationError("File size must be under 5MB")
        return file

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'activity_type', 'completed_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'completed_date': forms.DateInput(attrs={'type': 'date'}),
            'activity_type': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == 'Untitled Activity':
            raise forms.ValidationError("Please provide a meaningful title")
        return title
