from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Domain, Project, Activity

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed_date', 'verification_status')
    list_filter = ('verification_status', 'domains', 'completed_date')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'completed_date'

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'activity_type', 'points', 'completed_date', 'verification_status')
    list_filter = ('activity_type', 'verification_status', 'completed_date')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'completed_date'

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'user', 'experience_type', 'start_date', 'completed_date')
    list_filter = ('experience_type', 'completed_date')
    search_fields = ('company', 'position', 'description', 'user__username')
    date_hierarchy = 'completed_date'

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Domain)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Activity, ActivityAdmin)