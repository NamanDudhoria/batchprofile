from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Domain(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Added unique constraint
    
    class Meta:
        verbose_name_plural = 'Domains'
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)  # Changed to TextField for more flexibility
    domains = models.ManyToManyField(Domain, related_name='users', blank=True)  # Changed to ManyToManyField
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    hackerrank_url = models.URLField(max_length=200, blank=True, null=True)
    leetcode_url = models.URLField(max_length=200, blank=True, null=True)
    kaggle_url = models.URLField(max_length=200, blank=True, null=True)
    total_activity_points = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.username

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    domains = models.ManyToManyField(Domain, related_name='projects')
    project_url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='projects/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)  # Added creation date
    completed_date = models.DateField(default=timezone.now)
    verification_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-completed_date']  # Added default ordering

    def __str__(self):
        return self.title

class Activity(models.Model):  # Renamed from PlacementActivity for consistency
    ACTIVITY_TYPES = [
        ('project', 'Project Submission'),
        ('certification', 'Certification'),
        ('competition', 'Competition'),
        ('research', 'Research Paper'),
        ('internship', 'Internship'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=200, default='Untitled Activity')
    description = models.TextField()
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    points = models.PositiveIntegerField(default=0)  # Changed to PositiveIntegerField
    created_date = models.DateTimeField(auto_now_add=True)  # Added creation date
    completed_date = models.DateField(default=timezone.now)
    verification_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Activities'
        ordering = ['-completed_date']

    def __str__(self):
        return f"{self.title} ({self.get_activity_type_display()})"

# Removed Student model as it's redundant with CustomUser


