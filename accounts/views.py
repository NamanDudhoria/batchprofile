from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

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