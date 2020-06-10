# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import auth
from loginsys.forms import *


def login(request):
    args = {}
    args['form'] = LoginForm()
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/', permanent=True)
        else:
            args['valid_error'] = 'Введен неверный адрес электронной почты или пароль.'
            return render(request, 'pageLogin.html', args)

    else:
        return render(request, 'pageLogin.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args['form'] = RegForm()
    if request.method == 'POST':
        newuser_form = RegForm(request.POST)
        agreement = bool(request.POST.get('personal_data_agreement', ''))
        if newuser_form.is_valid() and agreement:
            newuser_form.save()
            return redirect('/auth/login')
        else:
            args['form'] = newuser_form
            args['valid_error'] = 'При Регистрации произошла ошибка. Пожалуйста, проверьте правильность введенных данных.'
    return render(request, 'register.html', args)
