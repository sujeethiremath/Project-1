from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tasks.models import Tasks
from tasks.models import TaskCategory
from tasks.models import HiddenStatus
from tasks.forms import AddTask
from tasks.forms import edit_task
from rest_framework import viewsets
from rest_framework import permissions
from tasks.serializers import TaskSerializer, UserSerializer, TaskCategorySerializer

# Create your views here.
@login_required(login_url='/login/')
def tasks(request):
	status_object = HiddenStatus.objects.get(id = 4)
	if status_object.status:
		page_data = fillpagedata(request.user, True)
		enable = True
	else:
		page_data = fillpagedata(request.user, False)
		enable = False

	return render(request, 'tasks/tasks.html', {"dat": page_data, "enabled" : enable})


def fillpagedata(uname, hidden):
	page_data = {}
	records = Tasks.objects.all().filter(username = uname)
	y = 1
	for x in records:
		row = "record{}".format(str(y))
		y = y + 1
		page_data[row] = []
		page_data[row].append(x.description)
		page_data[row].append(x.category.Category)
		page_data[row].append(x.completed)
		page_data[row].append(x.id)

	p_data = {}
	records = Tasks.objects.all().filter(username = uname).filter(completed = False)
	y = 1
	for x in records:
		row = "record{}".format(str(y))
		y = y + 1
		p_data[row] = []
		p_data[row].append(x.description)
		p_data[row].append(x.category.Category)
		p_data[row].append(x.completed)
		p_data[row].append(x.id)

	if hidden:
		return p_data
	else:
		return page_data	



def AddTasks(request):
	page_data = {"AddTask_form" : AddTask}
	if request.method == 'POST':
		AddTask_form = AddTask(request.POST)
		if(AddTask_form.is_valid()):
			desc = AddTask_form.cleaned_data["Description"]
			chois = AddTask_form.cleaned_data["Category"]
			task = Tasks()
			task.username = request.user
			task.description = desc
			task.completed = False
			sel_category = TaskCategory.objects.filter(id=str(int(chois)+10)).get()
			task.category = sel_category
			task.save()
			status_object = HiddenStatus.objects.get(id = 4)
			if status_object.status:
				page_data = fillpagedata(request.user, True)
				enable = True
			else:
				page_data = fillpagedata(request.user, False)
				enable = False
			return render(request, 'tasks/tasks.html', {"dat": page_data, "enabled" : enable})
	
	return render(request, 'tasks/AddTasks.html', context=page_data)




def edit(request):
	if request.method == 'POST':
		edit_task_form = edit_task(request.POST)
		if(edit_task_form.is_valid()):
			p_data = {}
			ids = edit_task_form.cleaned_data["ID"]
			category = edit_task_form.cleaned_data["Category"]
			completed = edit_task_form.cleaned_data["Completed"]
			description = edit_task_form.cleaned_data["Description"]
			sel_category = TaskCategory.objects.filter(id=str(int(category)+10)).get()
			record = Tasks.objects.get(id = ids)
			record.description = description
			record.category = sel_category
			record.completed = completed
			record.save()
			status_object = HiddenStatus.objects.get(id = 4)
			if status_object.status:
				page_data = fillpagedata(request.user, True)
				enable = True
			else:
				page_data = fillpagedata(request.user, False)
				enable = False
			return render(request, 'tasks/tasks.html', {"dat": page_data, "enabled" : enable})


	else:
		page_data = {}
		records = Tasks.objects.get(id = request.GET['id'])
		data_dict = {'Description': records.description, 'Category': records.category.id - 10, 'Completed': records.completed, 'ID' : request.GET['id']}
		et = edit_task(initial=data_dict)
		page_data["edit_task_form"] = et
	
	return render(request, 'tasks/edit.html', context=page_data)



def remove(request):
	remove_id = request.GET['id']
	record = Tasks.objects.get(id=remove_id)
	record.delete()
	status_object = HiddenStatus.objects.get(id = 4)
	if status_object.status:
		page_data = fillpagedata(request.user, True)
		enable = True
	else:
		page_data = fillpagedata(request.user, False)
		enable = False
	return render(request, 'tasks/tasks.html', {"dat": page_data, "enabled" : enable})



def hide(request):
	
	if request.method == 'POST' :
		status = request.POST.get('chk_ON')
		status_object = HiddenStatus.objects.get(id = 4)

		if status == "on":
			page_data = fillpagedata(request.user, True)
			enable = True
			status_object.status = True
			status_object.save()
		else:
			page_data = fillpagedata(request.user, False)
			status_object.status = False
			status_object.save()
			enable = False

		return render(request, 'tasks/tasks.html', {"dat": page_data, "enabled" : enable})






class TaskViewSet(viewsets.ModelViewSet):
	queryset = Tasks.objects.all()
	serializer_class = TaskSerializer
	permission_classes = [permissions.IsAuthenticated]


 

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]



class CategoryViewSet(viewsets.ModelViewSet):
	queryset = TaskCategory.objects.all()
	serializer_class = TaskCategorySerializer
	permission_classes = [permissions.IsAuthenticated]
