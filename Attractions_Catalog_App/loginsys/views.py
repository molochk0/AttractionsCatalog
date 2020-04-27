# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import auth
from Attractions_Catalog_App.loginsys.forms import *


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
            args['login_error'] = "Пользователь не найден"
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
        if newuser_form.is_valid():
            newuser_form.save()
            return redirect('/auth/login')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)
