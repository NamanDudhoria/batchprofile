from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Project, CustomUser, Domain, ActivitySubmission
from accounts.models import Activity

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'domain', 'project_url', 'file', 'project_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'domain': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'project_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
            'profile_picture', 'bio', 'skills', 'domain', 'resume', 'linkedin_url', 
            'github_url', 'hackerrank_url', 'leetcode_url', 'kaggle_url', 
            'total_activity_points'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'data-preview': 'profile-picture-preview'
            }),
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter skills separated by commas'}),
            'domain': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'hackerrank_url': forms.URLInput(attrs={'class': 'form-control'}),
            'leetcode_url': forms.URLInput(attrs={'class': 'form-control'}),
            'kaggle_url': forms.URLInput(attrs={'class': 'form-control'}),
            'total_activity_points': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            # Add validation for image size and format
            if profile_picture.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Image file too large ( > 5MB )")
            if not profile_picture.content_type.startswith('image'):
                raise forms.ValidationError("File type is not supported")
        return profile_picture

class ProfileUpdateForm(forms.ModelForm):
    """Form for updating existing user profiles"""
    class Meta:
        model = CustomUser
        fields = [
            'profile_picture', 'bio', 'skills', 'domain', 'resume', 
            'linkedin_url', 'github_url', 'hackerrank_url', 'leetcode_url', 
            'kaggle_url'
        ]
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'data-preview': 'profile-picture-preview'
            }),
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter skills separated by commas'}),
            'domain': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'hackerrank_url': forms.URLInput(attrs={'class': 'form-control'}),
            'leetcode_url': forms.URLInput(attrs={'class': 'form-control'}),
            'kaggle_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class ProfileSearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Search by name, skills, or domain...',
        'class': 'form-control'
    }))
    domain = forms.ModelChoiceField(
        queryset=Domain.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    min_activity_points = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Minimum Activity Points'
        })
    )

class ActivitySubmissionForm(forms.ModelForm):
    class Meta:
        model = ActivitySubmission
        fields = ['activity', 'proof_url', 'description', 'file_proof', 'activity_image']
        widgets = {
            'activity': forms.Select(attrs={'class': 'form-select'}),
            'proof_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL to verify completion (e.g., HackerRank certificate)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description of what you completed'
            }),
            'file_proof': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'activity_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'placeholder': 'Upload image proof (optional)'
            }),
        }

class ActivityFilterForm(forms.Form):
    TOPIC_CHOICES = [
        ('', 'All Topics'),
        ('DBMS', 'Database Management Systems'),
        ('PDSA', 'Programming, Data Structures and Algorithms'),
        ('R', 'Programming Concepts using R'),
        ('ML', 'Machine Learning'),
        ('DV', 'Data Visualization'),
        ('DL', 'Deep Learning'),
        ('CONSULTING', 'Business Proposal/Consultancy'),
        ('MACRO', 'Macroeconomic Theory'),
        ('MATH', 'Mathematics for Economics'),
        ('FINANCE', 'Finance'),
        ('RESEARCH', 'Independent Research'),
    ]

    topic = forms.ChoiceField(
        choices=TOPIC_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    difficulty = forms.ChoiceField(
        choices=[
            ('', 'All Levels'),
            ('EASY', 'Easy'),
            ('INTERMEDIATE', 'Intermediate'),
            ('ADVANCED', 'Advanced'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class ExampleForm(forms.Form):
    TOPIC_CHOICES = [
        ('ECONOMICS', 'Economics'),
        ('FINANCE', 'Finance'),
        ('TRADE', 'International Trade'),
        ('RESEARCH', 'Independent Research'),
    ]

    topic = forms.ChoiceField(
        choices=TOPIC_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    difficulty = forms.ChoiceField(
        choices=[
            ('', 'All Levels'),
            ('EASY', 'Easy'),
            ('INTERMEDIATE', 'Intermediate'),
            ('ADVANCED', 'Advanced'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )