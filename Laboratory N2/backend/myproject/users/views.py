from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


def sign_in(request):
    if request.method == 'GET':
        if request.method == 'GET':
            if request.user.is_authenticated:
                return redirect('profile')

            form = LoginForm()
            return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')

        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    registered_users = User.objects.all()
    user = request.user
    return render(request, 'profile.html', {
        'user': user,
        'registered_users': registered_users
    })


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'users/register.html', {'form': form})
