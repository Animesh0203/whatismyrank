from django.shortcuts import render
from django.http import HttpResponse
from .forms import fetch
from .models import links

def homepage(request):
	
	return render(request,"mainapp/home.html")

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