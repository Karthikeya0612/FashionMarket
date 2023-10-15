from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth 
# Create your views here.

def login(request):
    if request.method == "POST":
        userName = request.POST['userName']
        password = request.POST['password']

        user = auth.authenticate(username=userName, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'customers/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        password = request.POST['password']
        if User.objects.filter(username=userName).exists():
            messages.info(request, "User Name Taken")
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email taken")
            return redirect('signup')
        else:
            user = User.objects.create_user(email=email, first_name=firstName, last_name=lastName ,username=userName, password=password)
            user.save()
            return redirect('login')
        

    else:
        return render(request, 'customers/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

