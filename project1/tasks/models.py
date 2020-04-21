from django.db import models

# Create your models here.


class TaskCategory(models.Model):
	Category = models.CharField(max_length = 128)



class Tasks(models.Model):
	username = models.CharField(max_length=100)
	description = models.CharField(max_length=150)
	category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
	completed = models.BooleanField()


class HiddenStatus(models.Model):
	status =  models.BooleanField()


