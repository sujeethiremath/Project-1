from django import forms
from django.core import validators


class add_journal(forms.Form):
	Description = forms.CharField(min_length=1, max_length=150, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Entry = forms.CharField(min_length=1, max_length=500, strip=True, widget= forms.Textarea(attrs={'style':'font-size:20px;font-family:Amatic SC'}))


class edit_journal(forms.Form):
	Description = forms.CharField(min_length=1, max_length=150, strip=True, widget= forms.TextInput(attrs={'style':'font-size:small'}))
	Entry = forms.CharField(min_length=1, max_length=500, strip=True, widget= forms.Textarea(attrs={'style':'font-size:20px;font-family:Amatic SC'}))
	ID = forms.CharField(widget=forms.HiddenInput())