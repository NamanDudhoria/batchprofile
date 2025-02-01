from django.shortcuts import render


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

# Search functionality
def search_students(request):
    query = request.GET.get('q', '')
    students = CustomUser.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(skills__icontains=query) |
        Q(domain__icontains=query)
    )
    return JsonResponse({'students': list(students.values())})

# Export profile as PDF
def export_profile_pdf(request, pk):
    student = get_object_or_404(CustomUser, pk=pk)
    template_path = 'profiles/pdf_template.html'
    context = {'student': student}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.username}_profile.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation error')
    return response

# Activity points calculation
def calculate_points(request):
    user = request.user
    activities = PlacementActivity.objects.filter(user=user)
    total_points = sum(activity.points for activity in activities)
    user.total_points = total_points
    user.save()
    return JsonResponse({'total_points': total_points})

from django.shortcuts import render
from profiles.models import CustomUser, Domain

def batch_profile(request):
    students = CustomUser.objects.all()
    domains = Domain.objects.all()
    current_domain = request.GET.get('domain', '')
    return render(request, 'profiles/batch_profile.html', {
        'students': students,
        'domains': domains,
        'current_domain': current_domain
    })