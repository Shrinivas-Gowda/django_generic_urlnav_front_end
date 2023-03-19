from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def create_account(request):
    return render(request,'create_account.html')

def forgot_password(request):
    return render(request,'forgot_password.html')

def about(request):
    return render(request,'about.html')

