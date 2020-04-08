from django.db import models

# Create your models here.
class Tasks(models.Model):
	username = models.CharField(max_length=100)
	description = models.CharField(max_length=150)
	category = models.CharField(max_length=50)
	completed = models.BooleanField()


class HiddenStatus(models.Model):
	status =  models.BooleanField()