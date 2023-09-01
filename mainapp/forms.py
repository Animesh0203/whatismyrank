from django import forms
from .models import links
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Account
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth import authenticate

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'flip-card__input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'flip-card__input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'flip-card__input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'style': 'width: 300px;', 'class': 'flip-card__input'}))

    class Meta:
        model = Account
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'name': TextInput(attrs={
                'class': 'flip-card__input',
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': 'flip-card__input', 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'password1': TextInput(attrs={
                'class': 'flip-card__input',
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
            'password2': TextInput(attrs={
                'class': 'flip-card__input',
                'style': 'max-width: 300px;',
                'placeholder': 'Confirm Password'
                })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = "Enter a valid email address"

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'flip-card__input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'flip-card__input'}))






class fetch(forms.Form):
    link = forms.CharField(max_length=100)
    class Meta:
        model = links
