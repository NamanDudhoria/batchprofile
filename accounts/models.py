from django.db import models
from django.contrib.auth.models import AbstractUser

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ActivitySubmission(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    proof_url = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file_proof = models.FileField(upload_to='activity_proofs/', blank=True, null=True)
    activity_image = models.ImageField(upload_to='activity_images/', blank=True, null=True)

    def __str__(self):
        return f"Submission for {self.activity.name}"

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    domains = models.CharField(max_length=255)
    project_url = models.URLField(max_length=200, blank=True, null=True)
    project_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    file = models.FileField(upload_to='project_files/', blank=True, null=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import AbstractUser

class Domain(models.Model):
    DOMAIN_CHOICES = [
        ('FINANCE', 'Finance'),
        ('CONSULTING', 'Consulting'),
        ('RESEARCH', 'Research'),
        ('DATA_ANALYSIS', 'Data Analysis'),
        ('GENERAL', 'General')
    ]
    
    name = models.CharField(max_length=50, choices=DOMAIN_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.get_name_display()

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    domains = models.ManyToManyField(Domain, related_name='users', blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    hackerrank_url = models.URLField(max_length=200, blank=True, null=True)
    leetcode_url = models.URLField(max_length=200, blank=True, null=True)
    kaggle_url = models.URLField(max_length=200, blank=True, null=True)
    total_activity_points = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

