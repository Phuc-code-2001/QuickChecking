from django.shortcuts import render, redirect, reverse
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

