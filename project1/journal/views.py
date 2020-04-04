from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def journal(request):
	page_data = {"data" : [1,2,3,4,5]}
	return render(request, 'journal/journal.html', context=page_data)