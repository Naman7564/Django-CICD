from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to TaskFlow, {user.username}!')
            return redirect('todos:index')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})
