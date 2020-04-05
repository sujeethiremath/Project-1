"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from journal import views as journal_views
from tasks import views as tasks_views
from budget import views as budget_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.home, name='home'),
    path('journal/', journal_views.journal, name='journal'),
    path('tasks/', tasks_views.tasks, name='tasks'),
    path('budget/', budget_views.budget, name='budget'),
    path('about/', core_views.about, name='about')
]
