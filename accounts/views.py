from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profiles:profile_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, 'Logged in successfully!')
        return super().get_success_url()
