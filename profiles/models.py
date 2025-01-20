from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    DOMAIN_CHOICES = [
        ('analytics', 'Analytics'),
        ('consulting', 'Consulting'),
        ('research', 'Research'),
        ('general', 'General'),
    ]

    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    domain = models.CharField(
        max_length=20,
        choices=DOMAIN_CHOICES,
        default='general'
    )
    resume = models.FileField(upload_to='resumes/', blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    domain = models.CharField(max_length=20, choices=CustomUser.DOMAIN_CHOICES)
    project_url = models.URLField(blank=True)
    file = models.FileField(upload_to='projects/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PlacementActivity(models.Model):
    ACTIVITY_TYPES = [
        ('project', 'Project Submission'),
        ('certification', 'Certification'),
        ('competition', 'Competition'),
        ('research', 'Research Paper'),
        ('internship', 'Internship'),
        ('other', 'Other Activity')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity_type = models.CharField(
        max_length=100,
        choices=ACTIVITY_TYPES,
        default='other'
    )
    description = models.TextField(default='')
    points = models.IntegerField(default=0)
    completed_date = models.DateField(default=timezone.now)
    verification_status = models.BooleanField(default=False)

