from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Domain(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    hackerrank_url = models.URLField(max_length=200, blank=True, null=True)
    leetcode_url = models.URLField(max_length=200, blank=True, null=True)
    kaggle_url = models.URLField(max_length=200, blank=True, null=True)
    total_activity_points = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='profiles_customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='profiles_customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
    
class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    domains = models.ManyToManyField(Domain, related_name='projects')
    project_url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='projects/', blank=True, null=True)
    completed_date = models.DateField(default=timezone.now)
    verification_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class PlacementActivity(models.Model):
    ACTIVITY_TYPES = [
        ('project', 'Project Submission'),
        ('certification', 'Certification'),
        ('competition', 'Competition'),
        ('research', 'Research Paper'),
        ('internship', 'Internship'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='placement_activities')
    title = models.CharField(max_length=200,default='Untitled Activity')
    description = models.TextField()
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    points = models.IntegerField(default=0)
    completed_date = models.DateField(default=timezone.now)
    verification_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.get_activity_type_display()})"

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    skills = models.TextField()
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()