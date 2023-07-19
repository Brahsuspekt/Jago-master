from django.shortcuts import render, redirect
from users.forms import LoginForm, EmailForm, CodeForm, UserRegisterFrom
from django.contrib.auth import authenticate, login, logout
from users.utils import get_verify_code_and_send, authenticate_code
from django.contrib import messages
from django.contrib.auth.models import User 

# Create your views here.


def register(request):
    form = UserRegisterFrom() 
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        return redirect('login')
    #     if form.is_valid():
    #         user = form.save()
    #         return redirect('login')
    #     else:
    #         messages.info(request, 'Registration Failed')
    else:
        form = UserRegisterFrom()
    return render(request, 'auths/register.html', {'form':form})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        return redirect('program:index_page')
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     user = authenticate(username=username, password=password)
        #     if user is not None:
        #         login(request, user)
        #         return redirect('courses')
        #     else:
        #         messages.info(request, 'Invalid Credentials, Login Faild!')
        # else:
        #     form = LoginForm()
    else:
        form = LoginForm()    
    return render(request, 'auths/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('courses')


def get_user_email(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            get_verify_code_and_send(email)
            return redirect('verify_code')
        else:
            messages.info(request, 'Email Dose Not Exist')
    else:
        form = EmailForm()
    return render(request, 'auths/verify.html', {'form':form})


def verify_email(request):
    form = CodeForm()
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            authenticate_code(code)
            if authenticate_code(code):
                return redirect('courses')
            else:
                messages.info(request, 'Invalid Code')
        else:
            form = CodeForm()
    return redirect(request, 'auths/verify_code.html', {'form':form})