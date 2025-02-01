from django.contrib import admin
from profiles.models import CustomUser, Project

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Project)
