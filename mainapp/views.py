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