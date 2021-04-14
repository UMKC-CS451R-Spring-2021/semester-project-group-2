from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'homepage.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact.html')


def login_request(request):
    form = AuthenticationForm()
    messages.info(request, "Logged in successfully")
    return render(request, 'dashboard.html', {'form': form, 'present_logout': True})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('/banking/homepage')
