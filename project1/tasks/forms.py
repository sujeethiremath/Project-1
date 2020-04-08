from django import forms
from django.core import validators

class AddTask(forms.Form):
	CHOICES = [('1', 'Home'), ('2', 'School'), ('3', 'Work'), ('4', 'Self Improvement'), ('5', 'Other')]
	Description = forms.CharField(min_length=1, max_length=150, strip=True,
        widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Category= forms.CharField(widget=forms.Select(choices=CHOICES))


class edit_task(forms.Form):
	CHOICES = [('1', 'Home'), ('2', 'School'), ('3', 'Work'), ('4', 'Self Improvement'), ('5', 'Other')]
	Description = forms.CharField(min_length=1, max_length=150, strip=True,
        widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Category= forms.CharField(widget=forms.Select(choices=CHOICES))
	Completed = forms.BooleanField()
	ID = forms.CharField(widget=forms.HiddenInput())
