from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from journal.models import Journal
from journal.forms import add_journal, edit_journal
from rest_framework import viewsets
from rest_framework import permissions
from journal.serializers import UserSerializer, JournalSerializer

# Create your views here.


@login_required(login_url='/login/')
def journal(request):
	page_data = fillpagedata(request.user)
	return render(request, 'journal/journal.html', {"dat":page_data})




def fillpagedata(uname):
	page_data = {}
	records = Journal.objects.all().filter(Username = uname)
	y = 1
	for x in records:
		row = "record{}".format(str(y))
		y = y + 1
		page_data[row] = []
		page_data[row].append(x.Date)
		page_data[row].append(x.Description)
		page_data[row].append(x.id)
	return page_data


def addentry(request):
	page_data = {"add_journal_form" : add_journal}
	if request.method == 'POST':
		add_journal_form = add_journal(request.POST)
		if(add_journal_form.is_valid()):
			desc = add_journal_form.cleaned_data["Description"]
			ent = add_journal_form.cleaned_data["Entry"]
			journal = Journal()
			journal.Username = request.user
			journal.Description = desc
			journal.Entry = ent
			journal.save()
			page_data = fillpagedata(request.user)
			return render(request, 'journal/journal.html', {"dat": page_data})
	return render(request, 'journal/addentry.html', context=page_data)



def editentry(request):
	if request.method == 'POST':
		edit_journal_form = edit_journal(request.POST)
		if(edit_journal_form.is_valid()):
			desc = edit_journal_form.cleaned_data["Description"]
			ids = edit_journal_form.cleaned_data["ID"]
			ent = edit_journal_form.cleaned_data["Entry"]
			journal = Journal.objects.get(id=ids)
			journal.Description = desc
			journal.Entry = ent
			journal.save()
			page_data = fillpagedata(request.user)
			return render(request, 'journal/journal.html', {"dat": page_data})
	else:
		page_data = {}
		records = Journal.objects.get(id = request.GET['id'])
		data_dict = {'Description': records.Description, 'Entry': records.Entry, 'ID' : request.GET['id']}
		et = edit_journal(initial=data_dict)
		page_data["edit_journal_form"] = et
	return render(request, 'journal/editjournal.html', context=page_data)



def removeentry(request):
	remove_id = request.GET['id']
	record = Journal.objects.get(id=remove_id)
	record.delete()
	page_data = fillpagedata(request.user)
	return render(request, 'journal/journal.html', {"dat": page_data})



class JournalViewSet(viewsets.ModelViewSet):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer
	permission_classes = [permissions.IsAuthenticated]



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

