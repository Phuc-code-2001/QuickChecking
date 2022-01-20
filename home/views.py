from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    context = {'title': 'Home', 'home_active': 'active'}
    return render(request, 'home/index.html', context)

def login(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    context = {'title': 'Login', 'login_active': 'active'}
    return render(request, 'home/login.html', context)

def about(request):
    context = {'title': 'About', 'about_active': 'active'}
    return render(request, 'home/about.html', context)