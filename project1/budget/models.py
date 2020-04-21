from django.db import models

# Create your models here.

class BudgetCategory(models.Model):
	Category = models.CharField(max_length = 128)




class Budget(models.Model):
	 Username = models.CharField(max_length=100)
	 Description = models.CharField(max_length=100)
	 Category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
	 Projected = models.PositiveIntegerField()
	 Actual = models.PositiveIntegerField()