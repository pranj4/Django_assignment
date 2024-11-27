from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            messages.error(request, 'Invalid username or password')  # Show error message
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'username': request.user.username})

@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})

