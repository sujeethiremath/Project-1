from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from budget.models import Budget, BudgetCategory
from budget.forms import add_budget, edit_budget
from rest_framework import viewsets
from rest_framework import permissions
from budget.serializers import UserSerializer, BudgetSerializer, BudgetCategorySerializer


# Create your views here.
@login_required(login_url='/login/')
def budget(request):
	page_data = fillpagedata(request.user)
	return render(request, 'budget/budget.html', {"dat": page_data, "data":calculate(request.user)})





def calculate(uname):
	records = Budget.objects.all().filter(Username = uname)
	total_actual = 0
	total_projected = 0
	for x in records:
		total_actual = total_actual + x.Actual
		total_projected = total_projected + x.Projected
	if total_projected - total_actual > 0:
		s = "There is a projected budget surplus of $" + str(total_projected - total_actual)
	elif total_projected - total_actual < 0:
		s = "There is a projected budget deficit of -$" + str((total_projected - total_actual)*-1)
	else:
		s = ""
	return s



def fillpagedata(uname):
	page_data = {}
	records = Budget.objects.all().filter(Username = uname)
	y = 1
	for x in records:
		row = "record{}".format(str(y))
		y = y + 1
		page_data[row] = []
		page_data[row].append(x.Description)
		page_data[row].append(x.Category.Category)
		page_data[row].append(x.Projected)
		page_data[row].append(x.Actual)
		page_data[row].append(x.id)
	return page_data


def addbudget(request):
	page_data = {"add_budget_form" : add_budget}
	if request.method == 'POST':
		add_budget_form = add_budget(request.POST)
		if(add_budget_form.is_valid()):
			desc = add_budget_form.cleaned_data["Description"]
			act = add_budget_form.cleaned_data["Actual"]
			pred = add_budget_form.cleaned_data["Projected"]
			chois = add_budget_form.cleaned_data["Category"]
			sel_category = BudgetCategory.objects.filter(id=chois).get()
			budget = Budget()
			budget.Username = request.user
			budget.Description = desc
			budget.Projected = pred
			budget.Actual = act
			budget.Category = sel_category
			budget.save()
			page_data = fillpagedata(request.user)
			return render(request, 'budget/budget.html', {"dat": page_data, "data":calculate(request.user)})
	return render(request, 'budget/addbudget.html', context=page_data)


def editbudget(request):
	if request.method == 'POST':
		edit_budget_form = edit_budget(request.POST)
		if(edit_budget_form.is_valid()):
			desc = edit_budget_form.cleaned_data["Description"]
			ids = edit_budget_form.cleaned_data["ID"]
			act = edit_budget_form.cleaned_data["Actual"]
			pred = edit_budget_form.cleaned_data["Projected"]
			chois = edit_budget_form.cleaned_data["Category"]
			sel_category = BudgetCategory.objects.filter(id=chois).get()
			budget = Budget.objects.get(id=ids)
			budget.Description = desc
			budget.Projected = pred
			budget.Actual = act
			budget.Category = sel_category
			budget.save()
			page_data = fillpagedata(request.user)
			return render(request, 'budget/budget.html', {"dat": page_data, "data":calculate(request.user)})
	else:
		page_data = {}
		records = Budget.objects.get(id = request.GET['id'])
		data_dict = {'Description': records.Description, 'Category': records.Category.id, 'Projected': records.Projected, 'Actual' : records.Actual, 'ID' : request.GET['id']}
		et = edit_budget(initial=data_dict)
		page_data["edit_budget_form"] = et
	return render(request, 'budget/editbudget.html', context=page_data)


def removebudget(request):
	remove_id = request.GET['id']
	record = Budget.objects.get(id=remove_id)
	record.delete()
	page_data = fillpagedata(request.user)
	return render(request, 'budget/budget.html', {"dat": page_data})








class BudgetViewSet(viewsets.ModelViewSet):
	queryset = Budget.objects.all()
	serializer_class = BudgetSerializer
	permission_classes = [permissions.IsAuthenticated]


 

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]



class BudgetCategoryViewSet(viewsets.ModelViewSet):
	queryset = BudgetCategory.objects.all()
	serializer_class = BudgetCategorySerializer
	permission_classes = [permissions.IsAuthenticated]