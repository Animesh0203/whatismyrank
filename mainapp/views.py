from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views import View
from mainapp.forms import LoginForm
from django.contrib import messages

def homepage(request):
    return render(request, "mainapp/home.html", {})


def base(response):
    return render(response, "mainapp/base.html", {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
            messages.success(request, 'Account created and logged in successfully.')
            return redirect('homepage')
        else:
            messages.error(request, 'Form is not valid. Please check the errors.')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'mainapp/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')

<<<<<<< Updated upstream
=======
def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("homepage")

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("homepage")
            else:
                context['error_message'] = "Invalid email or password."
        else:
            context['error_message'] = "Please correct the errors below."
    else:
        form = LoginForm()

    context['form'] = form
    return render(request, 'mainapp/register.html', context)



def get_id(request):
>>>>>>> Stashed changes

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("homepage")

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']  # Use 'password1' instead of 'password'
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("homepage")
            else:
                context['error_message'] = "Invalid email or password."
        else:
            context['error_message'] = "Please correct the errors below."
    else:
        form = LoginForm()

    context['form'] = form
    return render(request, 'mainapp/register.html', context)
