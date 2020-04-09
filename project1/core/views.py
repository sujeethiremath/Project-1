from django.shortcuts import render, redirect
from core.forms import JoinForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from tasks.models import Tasks
from budget.models import Budget
from journal.models import Journal
import datetime

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    records = Tasks.objects.all().filter(username = request.user)
    completed = 0
    pending = 0
    for x in records:
        if x.completed == True:
            completed = completed + 1
        else:
            pending = pending + 1

    records = Budget.objects.all().filter(Username = request.user)
    act_Food = 0
    act_Clothing = 0
    act_Housing = 0
    act_Education = 0
    act_Entertainment = 0
    act_Other = 0

    pre_Food = 0
    pre_Clothing = 0
    pre_Housing = 0
    pre_Education = 0
    pre_Entertainment = 0
    pre_Other = 0

    for x in records:
        if x.Category == 'Food':
            act_Food = act_Food + x.Actual
            pre_Food = pre_Food + x.Projected
        if x.Category == 'Clothing':
            act_Clothing = act_Clothing + x.Actual
            pre_Clothing = pre_Clothing + x.Projected
        if x.Category == 'Housing':
            act_Housing = act_Housing + x.Actual
            pre_Housing = pre_Housing + x.Projected
        if x.Category == 'Education':
            act_Education = act_Education + x.Actual
            pre_Education = pre_Education + x.Projected
        if x.Category == 'Entertainment':
            act_Entertainment = act_Entertainment + x.Actual
            pre_Entertainment = pre_Entertainment + x.Projected
        if x.Category == 'Other':
            act_Other = act_Other + x.Actual
            pre_Other = pre_Other + x.Projected

    series1 = [act_Food, act_Clothing, act_Housing, act_Education, act_Entertainment, act_Other]
    series2 = [pre_Food, pre_Clothing, pre_Housing, pre_Education, pre_Entertainment, pre_Other]

    records = Journal.objects.all().filter(Username = request.user)

    Total_Entries = 0

    for x in records:
        Total_Entries = Total_Entries + 1

    x = Journal.objects.all().filter(Username = request.user)

    if x.exists():
    	recent_date = Journal.objects.all().filter(Username = request.user).latest('Date').Date
    else:
    	recent_date = datetime.date.today()
    
    days = datetime.date.today() - recent_date
    return render(request, 'core/home.html', {"completed":completed, "pending" : pending, "series1" : series1, "series2" : series2, "Entries":Total_Entries, "Days": days})


def about(request):
    return render(request, 'core/About.html')

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            print(join_form.errors)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)


def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'core/login.html', {"login_form": LoginForm})


@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")