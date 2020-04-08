from django.db import models

# Create your models here.
class Budget(models.Model):
	 Username = models.CharField(max_length=100)
	 Description = models.CharField(max_length=100)
	 Category = models.CharField(max_length=100)
	 Projected = models.PositiveIntegerField()
	 Actual = models.PositiveIntegerField()