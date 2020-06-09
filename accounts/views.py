from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout, authenticate

def register_user(request):
    user = get_user_model()

    if request.method == 'POST':
        new_user = user(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST ['first_name'],
            last_name = request.POST ['last_name'],
        )

        new_user.set_password(request.POST['password'])
        new_user.save()
        return redirect('login')
    return render (request, 'accounts/register.html')
    

def login_user(request):
    if request.method == "POST":
        user = authenticate (
            request,
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user is not None:
            login(request,user)
            return redirect('home')
    return render (request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')
