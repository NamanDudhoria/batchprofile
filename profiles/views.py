# profiles/views.py
# profiles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import CustomUser, Project, PlacementActivity, Domain
from .forms import ProjectForm, CustomUserCreationForm, ProfileSearchForm


def home(request):
    return render(request, 'index.html')

def student_detail(request, pk):
    student = get_object_or_404(CustomUser, pk=pk)
    skills = student.skills.split(',')
    context = {
        'student': student,
        'skills': [skill.strip() for skill in skills]
    }
    return render(request, 'profiles/student_detail.html', context)

@login_required
def dashboard(request):
    user_projects = Project.objects.filter(user=request.user)
    user_activities = PlacementActivity.objects.filter(user=request.user).order_by('-completed_date')

    context = {
        'projects': user_projects,
        'activities': user_activities,
    }


@login_required
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, 'Project uploaded successfully!')
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'profiles/upload_project.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = CustomUserForm(instance=request.user)
    return render(request, 'profiles/edit_profile.html', {'form': form})


def batch_profile(request):
    form = ProfileSearchForm(request.GET)
    students = CustomUser.objects.all()

    if form.is_valid():
        if form.cleaned_data['search']:
            search_query = form.cleaned_data['search']
            students = students.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(skills__icontains=search_query)
            )

        if form.cleaned_data['domain']:
            students = students.filter(domain=form.cleaned_data['domain'])

    return render(request, 'profiles/batch_profile.html', {
        'students': students,
        'form': form
    })


# Add any additional views you need here