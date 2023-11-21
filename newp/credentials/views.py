from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import path, include

# ...

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)  # Use 'request' as the first argument

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")  # Use 'error' instead of 'info' for error messages
            return redirect('login')

    return render(request, 'login.templates')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')  # Use 'error' instead of 'info' for error messages
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')  # Use 'error' instead of 'info' for error messages
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)  # Provide 'password' argument here

                user.save()
                return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')  # Use 'error' instead of 'info' for error messages
            return redirect('register')

    return render(request, 'register.templates')

def logout(request):
    auth.logout(request)
    return redirect('/')

