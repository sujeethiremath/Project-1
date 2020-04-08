from django.contrib import admin
from tasks.models import Tasks
from tasks.models import HiddenStatus

# Register your models here.
admin.site.register(Tasks)
admin.site.register(HiddenStatus)