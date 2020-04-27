from django import forms
from django.contrib.auth.forms import *
from Attractions_Catalog_App.FirstPage import User


class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Обязательное поле', label='Адрес электронной почты')
    nickname = forms.CharField(max_length=20, help_text='Обязательное поле', label='Имя пользователя')

    class Meta:
        model = User
        fields = ('email', 'nickname', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, help_text='Обязательное поле', label='Адрес электронной почты')
    password = forms.CharField(max_length=50, help_text='Обязательное поле', widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        fields = ('email', 'password')
