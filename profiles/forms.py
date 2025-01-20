# profiles/forms.py
from django import forms
from .models import Project, CustomUser

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'domain', 'project_url', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'bio', 'skills',
                 'domain', 'linkedin_url', 'github_url', 'resume']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.TextInput(attrs={'placeholder': 'Enter skills separated by commas'}),
        }

class ProfileSearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Search by name, skills, or domain...',
        'class': 'form-control'
    }))
    domain = forms.ChoiceField(required=False, choices=[('', 'All')] + CustomUser.DOMAIN_CHOICES,
                              widget=forms.Select(attrs={'class': 'form-select'}))