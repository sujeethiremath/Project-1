from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	page_data = {"data" : [1,2,3,4,5]}
	return render(request, 'core/home.html', context=page_data)


def about(request):
	page_data = {"data" : [1,2,3,4,5]}
	return render(request, 'core/About.html', context=page_data)