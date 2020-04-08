from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from budget.models import Budget
from budget.forms import add_budget, edit_budget

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
	else:
		s = "There is a projected budget deficit of -$" + str((total_projected - total_actual)*-1)
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
		page_data[row].append(x.Category)
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
			choises = { '1' : 'Food', '2' : 'Clothing', '3' : 'Housing', '4' : 'Education',  '5' : 'Entertainment', '6' : 'Other'}
			budget = Budget()
			budget.Username = request.user
			budget.Description = desc
			budget.Projected = pred
			budget.Actual = act
			budget.Category = choises[chois]
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
			choises = { '1' : 'Food', '2' : 'Clothing', '3' : 'Housing', '4' : 'Education',  '5' : 'Entertainment', '6' : 'Other'}
			budget = Budget.objects.get(id=ids)
			budget.Description = desc
			budget.Projected = pred
			budget.Actual = act
			budget.Category = choises[chois]
			budget.save()
			page_data = fillpagedata(request.user)
			return render(request, 'budget/budget.html', {"dat": page_data, "data":calculate(request.user)})
	else:
		page_data = {}
		records = Budget.objects.get(id = request.GET['id'])
		choises = { 'Food' : 1, 'Clothing' : 2, 'Housing' : 3, 'Education' : 4,  'Entertainment' : 5, 'Other' : 6}
		data_dict = {'Description': records.Description, 'Category': choises[records.Category], 'Projected': records.Projected, 'Actual' : records.Actual, 'ID' : request.GET['id']}
		et = edit_budget(initial=data_dict)
		page_data["edit_budget_form"] = et
	return render(request, 'budget/editbudget.html', context=page_data)


def removebudget(request):
	remove_id = request.GET['id']
	record = Budget.objects.get(id=remove_id)
	record.delete()
	page_data = fillpagedata(request.user)
	return render(request, 'budget/budget.html', {"dat": page_data})
