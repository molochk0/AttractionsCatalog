from django import forms
from django.contrib.auth.forms import *
from FirstPage.models import User

my_default_errors = {
    'required': 'Это поле является обязательным',
    'invalid': 'Введите корректное значение',
    'unique': 'Пользователь с таким адресом электронной почты уже существует.',
}


class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Обязательное поле', label='Адрес электронной почты',
                             error_messages=my_default_errors)
    nickname = forms.CharField(max_length=30, help_text='Обязательное поле', label='Никнейм',
                               error_messages=my_default_errors)
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Пароль',
                                help_text='Ваш пароль должен содержать как минимум 6 символов.',
                                error_messages=my_default_errors)
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Подтверждение пароля',
                                help_text='Введите пароль ещё раз', error_messages=my_default_errors)

    class Meta:
        model = User
        fields = ('email', 'nickname', 'password1', 'password2',)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, help_text='Обязательное поле', label='Адрес электронной почты',
                             error_messages=my_default_errors)
    password = forms.CharField(max_length=50, help_text='Обязательное поле', widget=forms.PasswordInput, label='Пароль',
                               error_messages=my_default_errors)

    class Meta:
        model = User
        fields = ('email', 'password')
