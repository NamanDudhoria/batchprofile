from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Project, Activity, Domain
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    domains = forms.ModelMultipleChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        help_text="Select your areas of expertise"
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
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself'}),
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List your skills'}),
        }

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            if profile_picture.size > 2*1024*1024:  # 2MB
                raise ValidationError("Profile picture must be under 2MB")
            if not profile_picture.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Only PNG, JPG, or JPEG files are allowed")
        return profile_picture

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if resume.size > 5*1024*1024:  # 5MB
                raise ValidationError("Resume must be under 5MB")
            if not resume.name.lower().endswith(('.pdf', '.doc', '.docx')):
                raise ValidationError("Only PDF, DOC, or DOCX files are allowed")
        return resume

class CustomUserChangeForm(UserChangeForm):
    password = None  # Remove password field from form
    domains = forms.ModelMultipleChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        help_text="Select your areas of expertise"
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

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            if profile_picture.size > 2*1024*1024:
                raise ValidationError("Profile picture must be under 2MB")
            if not profile_picture.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Only PNG, JPG, or JPEG files are allowed")
        return profile_picture

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if resume.size > 5*1024*1024:
                raise ValidationError("Resume must be under 5MB")
            if not resume.name.lower().endswith(('.pdf', '.doc', '.docx')):
                raise ValidationError("Only PDF, DOC, or DOCX files are allowed")
        return resume

class ProjectForm(forms.ModelForm):
    domains = forms.ModelMultipleChoiceField(
        queryset=Domain.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Select relevant domains for your project"
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
            if file.size > 5*1024*1024:
                raise ValidationError("File must be under 5MB")
            if not file.name.lower().endswith(('.pdf', '.zip', '.rar', '.doc', '.docx')):
                raise ValidationError("Only PDF, ZIP, RAR, DOC, or DOCX files are allowed")
        return file

    def clean_completed_date(self):
        completed_date = self.cleaned_data.get('completed_date')
        if completed_date and completed_date > forms.fields.datetime.date.today():
            raise ValidationError("Completion date cannot be in the future")
        return completed_date

class ActivityForm(forms.ModelForm):
    ongoing = forms.BooleanField(required=False, label="Ongoing Activity")
    class Meta:
        model = Activity
        fields = ['title', 'description', 'experience_type', 'start_date', 'completed_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'completed_date': forms.DateInput(attrs={'type': 'date'}),
            'experience_type': forms.Select(choices=Activity.EXPERIENCE_TYPE_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()
        ongoing = cleaned_data.get('ongoing')
        completed_date = cleaned_data.get('completed_date')

        if not ongoing and not completed_date:
            raise ValidationError("Please provide a completed date or mark the activity as ongoing.")

        if completed_date and completed_date > forms.fields.datetime.date.today():
            raise ValidationError("Completion date cannot be in the future.")

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long")
        return title
