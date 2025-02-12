from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import FileExtensionValidator, URLValidator, MinValueValidator
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

def validate_file_size(value):
    filesize = value.size
    if filesize > 5*1024*1024:  # 5MB limit
        raise ValidationError("Maximum file size is 5MB")

def validate_image_size(value):
    filesize = value.size
    if filesize > 2*1024*1024:  # 2MB limit
        raise ValidationError("Maximum image size is 2MB")
    
class Domain(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = 'Domains'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    profile_picture = CloudinaryField('image', blank=True, null=True)
    bio = models.TextField(blank=True, null=True, max_length=500)
    skills = models.TextField(blank=True, null=True)
    domains = models.ManyToManyField(Domain, related_name='users', blank=True)
    resume = CloudinaryField('Resume', blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    github_url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    hackerrank_url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    leetcode_url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    kaggle_url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    total_activity_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = 'Custom Users'
        ordering = ['-total_activity_points', 'username']

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        if self.bio and len(self.bio) > 500:
            raise ValidationError({'bio': 'Bio must be less than 500 characters.'})

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    domains = models.ManyToManyField(Domain, related_name='projects')
    project_url = models.URLField(blank=True, null=True, validators=[URLValidator()])
    file = models.FileField(
        upload_to='projects/', 
        blank=True, 
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'zip', 'rar', 'doc', 'docx']),
            validate_file_size
        ]
    )
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateField(default=timezone.now)
    verification_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-completed_date', '-created_date']
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.completed_date and self.completed_date > timezone.now().date():
            raise ValidationError({'completed_date': 'Completion date cannot be in the future.'})

class Activity(models.Model):
    EXPERIENCE_TYPE_CHOICES = [
        ('internship', 'Internship'),
        ('volunteer', 'Volunteer Work'),
        ('research', 'Research'),
        ('course', 'Course'),
        ('project', 'Project'),
        ('work','Job'),
        ('freelance', 'Freelance Work'),
        ('other', 'Other'),
    ]
    
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    description = models.TextField()
    experience_type = models.CharField(max_length=50, choices=EXPERIENCE_TYPE_CHOICES, default='other')
    start_date = models.DateField(default=timezone.now)
    completed_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='activities')

    def __str__(self):
        return f"{self.experience_type} at {self.company}"