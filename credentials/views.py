from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('banksite_app:Home')
        else:
            messages.info(request,"Invalid User")
            return redirect('credentials:login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('credentials:register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email-ID is already taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)

                user.save();
                return redirect('credentials:login')
        else:
            messages.info(request, "password not matched")
            return redirect('credentials:register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('banksite_app:Home')
