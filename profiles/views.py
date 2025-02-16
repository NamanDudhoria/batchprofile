from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import CustomUser, Project, Activity
from accounts.forms import CustomUserChangeForm, ProjectForm, ActivityForm

def profile_view(request, username=None):
    user = get_object_or_404(CustomUser, username=username)
    is_own_profile = user == request.user
    
    projects = user.projects.all().order_by('-completed_date')
    activities = user.activities.all().order_by('-completed_date')
    
    context = {
        'profile_user': user,
        'projects': projects,
        'activities': activities,
        'is_own_profile': is_own_profile,
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profiles:profile_view', username=request.user.username)  # Pass username to profile view
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profiles/edit_profile.html', {'form': form})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            form.save_m2m()
            messages.success(request, 'Project added successfully!')
            return redirect('profiles:profile_view', username=request.user.username)  # Pass username to profile view
    else:
        form = ProjectForm()
    return render(request, 'profiles/add_project.html', {'form': form})


@login_required
def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            messages.success(request, 'Activity added successfully!')
            return redirect('profiles:profile_view', username=request.user.username)  # Pass username to profile view
    else:
        form = ActivityForm()
    return render(request, 'profiles/add_activity.html', {'form': form})

@login_required
def user_list(request):
    users = CustomUser.objects.all().order_by('date_joined')
    return render(request, 'profiles/user_list.html', {'users': users})