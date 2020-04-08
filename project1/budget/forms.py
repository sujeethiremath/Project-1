from django import forms
from django.core import validators


class add_budget(forms.Form):
	CHOICES = [('1', 'Food'), ('2', 'Clothing'), ('3', 'Housing'), ('4', 'Education'), ('5', 'Entertainment'), ('6', 'Other')]
	Description = forms.CharField(min_length=1, max_length=150, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Category = forms.CharField(widget=forms.Select(choices=CHOICES))
	Projected = forms.CharField(min_length=1, max_length=8, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Actual = forms.CharField(min_length=1, max_length=8, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))



class edit_budget(forms.Form):
	CHOICES = [('1', 'Food'), ('2', 'Clothing'), ('3', 'Housing'), ('4', 'Education'), ('5', 'Entertainment'), ('6', 'Other')]
	Description = forms.CharField(min_length=1, max_length=150, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Category = forms.CharField(widget=forms.Select(choices=CHOICES))
	Projected = forms.CharField(min_length=1, max_length=8, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Actual = forms.CharField(min_length=1, max_length=8, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))
	ID = forms.CharField(widget=forms.HiddenInput())