from django.db import models

# Create your models here.
class Journal(models.Model):
	Username = models.CharField(max_length=150)
	Date = models.DateField(auto_now=True)
	Description = models.CharField(max_length=100)
	Entry = models.CharField(max_length=500)

	 