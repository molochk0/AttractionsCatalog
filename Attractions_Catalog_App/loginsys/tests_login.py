import unittest
from django.test import TestCase
from loginsys.forms import *
from FirstPage.models import *


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='mail@mail.ru', nickname='nickname', password='password')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(email='mail@mail.ru', password='password')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_email(self):
        user = authenticate(email='wrong@test.com', password='password')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(email='mail@mail.ru', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class TestLoginForm(unittest.TestCase):
    def test_valid_form(self):
        data = {'email': 'testmail@mail.test', 'password': 'password'}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'password': 'password'}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_max_length_email(self):
        data = {'email': 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq@qqq.qqq', 'password': '111111'}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_max_length_password(self):
        data = {'email': 'testmail@mail.test', 'password': 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())


class TestRegisterForm(unittest.TestCase):
    def test_valid_form(self):
        data = {'email': 'new@mail.ru', 'nickname': 'nickname', 'password1': '12121212', 'password2': '12121212'}
        form = RegForm(data=data)
        self.assertTrue(form.is_valid())

    def test_mismatch_password(self):
        data = {'email': 'new@mail.ru', 'nickname': 'nickname', 'password1': '12121212', 'password2': '111111'}
        form = RegForm(data=data)
        self.assertFalse(form.is_valid())

    def test_empty_field(self):
        data = {'email': '', 'nickname': 'nickname', 'password1': '12121212', 'password2': '111111'}
        form = RegForm(data=data)
        self.assertFalse(form.is_valid())

    def test_short_password(self):
        data = {'email': 'new@mail.ru', 'nickname': 'nickname', 'password1': '12', 'password2': '12'}
        form = RegForm(data=data)
        self.assertFalse(form.is_valid())

    def test_max_length_field(self):
        data = {'email': 'new@mail.ru', 'nickname': 'ninininininininininininininini', 'password1': '111111',
                'password2': '111111'}
        form = RegForm(data=data)
        self.assertFalse(form.is_valid())
