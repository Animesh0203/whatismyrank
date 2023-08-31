from django import forms
from .models import links

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class fetch(forms.Form):
    link = forms.CharField(max_length=100)
    class Meta:
        model = links
