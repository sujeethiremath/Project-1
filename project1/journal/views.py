from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def journal(request):
	return HttpResponse("Journal Page")