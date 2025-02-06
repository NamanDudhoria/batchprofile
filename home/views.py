from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser, Domain
from django.db.models import Q
from django.http import JsonResponse

def home(request):
    core_courses = [
        'Basic Econometrics',
        'Macroeconomic Theory',
        'Mathematics for Economics',
        'Microeconomic Theory-I',
        'Advanced Topics in Macroeconomics',
        'Microeconomic Theory-II',
        'International Trade Theory',
        'Financial Economics',
    ]

    elective_courses = {
        'International Trade': [
            'Empirical Issues in Trade',
            'Trade and Development',
            'WTO and Contemporary Trade Issues',
            'Advanced Topics in Trade Theory'
        ],
        'Finance': [
            'Investment Theory',
            'Banking and Financial Intermediation',
            'Derivatives and Risk Management',
            'Financial Modeling'
        ],
        'Other Courses': [
            'Economics of Networks',
            'Applied Econometrics',
            'The Economics of the Environment',
            'Labour Economics'
        ]
    }

    context = {
        'core_courses': core_courses,
        'elective_courses': elective_courses,
    }
    return render(request, 'home/index.html', context)

def hire_from_us(request):
    return render(request, 'home/hire_from_us.html')

def search_students(request):
    query = request.GET.get('q', '')
    students = CustomUser.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(skills__icontains=query)
    )
    return JsonResponse({'students': list(students.values())})

def batch_profile(request):
    students = CustomUser.objects.all()
    domains = Domain.objects.all()
    current_domain = request.GET.get('domain', '')
    return render(request, 'profiles/batch_profile.html', {
        'students': students,
        'domains': domains,
        'current_domain': current_domain
    })
