from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Home(request):
    return render(request, 'home.html')

def Registration(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2= request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password doesnt Match")
        else:
            new_user = User.objects.create_user(username, email, password1)
            new_user.save()
            return redirect('login')
    return render(request, "registration.html")

def Login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = authenticate(request, username=username, password1=password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password Incorrect!")
    return render(request, "login.html")

def Logout(request):
    logout(request)
    return render(request, "logout.html")    
