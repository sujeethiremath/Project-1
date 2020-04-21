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
from django.urls import include, path
from core import views as core_views
from journal import views as journal_views
from tasks import views as tasks_views
from budget import views as budget_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', tasks_views.TaskViewSet)
router.register(r'users', tasks_views.UserViewSet)
router.register(r'task-categories', tasks_views.CategoryViewSet)
router.register(r'budget', budget_views.BudgetViewSet)
router.register(r'budget-categories', budget_views.BudgetCategoryViewSet)
router.register(r'journal', journal_views.JournalViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.home, name='home'),
    path('journal/', journal_views.journal, name='journal'),
    path('editentry/', journal_views.editentry, name='edit_entry'),
    path('removeentry/', journal_views.removeentry, name='remove_entry'),
    path('addentry/', journal_views.addentry, name='add_entry'),
    path('tasks/', tasks_views.tasks, name='tasks'),
    path('budget/', budget_views.budget, name='budget'),
    path('addbudget/', budget_views.addbudget, name='add_budget'),
    path('editbudget/', budget_views.editbudget, name='edit_budget'),
    path('removebudget/', budget_views.removebudget, name='remove_budget'),
    path('about/', core_views.about, name='about'),
    path('join/', core_views.join, name='join'),
    path('login/', core_views.user_login, name='user_login'),
    path('logout/', core_views.user_logout, name='user_logout'),
    path('addtask/', tasks_views.AddTasks, name='add_task'),
    path('edit/', tasks_views.edit, name='tasks_edit'),
    path('hide/', tasks_views.hide, name='hide_tasks'),
    path('remove/', tasks_views.remove, name='tasks_remove'),
    path('api/v1/', include(router.urls)),
    path('api-auth/v1/', include('rest_framework.urls', namespace='rest_framework'))
]
