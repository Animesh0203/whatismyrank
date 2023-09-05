from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import fetch
from .models import links
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views import View
from mainapp.forms import LoginForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

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
            print(form.errors)
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'mainapp/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')

def get_id(request):

	if request.method == 'POST':

		request.POST._mutable=True
		request.POST['link'] = request.POST['link'].replace('https://www.youtube.com/watch?v=','')

		form = fetch(request.POST)

		if form.is_valid():

			form = form.cleaned_data

			obj = links()
			obj.link = form['link']
		
		obj.save()
		form = fetch()
	
	else:

		form = fetch()

	return render(request,'mainapp/submit.html',{'form':form})

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
    return render(request, 'mainapp/login.html', context)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'mainapp/recoverpassword.html'
    email_template_name = 'mainapp/password_reset_email.html'
    subject_template_name = 'mainapp/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy(homepage)
