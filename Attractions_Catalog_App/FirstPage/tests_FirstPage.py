import unittest
from django.test import TestCase, Client
from FirstPage.forms import *
from FirstPage.models import *


class TestCreateAttractionForm(unittest.TestCase):
    def test_valid_form(self):
        data = {'name': 'Название', 'address': 'Адрес', 'descriptions': 'Описание', 'city_name': 'Город',
                'type': 'Музеи'}
        form = CreateAttractionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': 'Название', 'address': 'Адрес', 'descriptions': 'Описание', 'city_name': 'Город',
                'type': 'шутка'}
        form = CreateAttractionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_long_name(self):
        data = {
            'name': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
            'address': 'Адрес', 'descriptions': 'Описание', 'city_name': 'Город',
            'type': 'Музеи'}
        form = CreateAttractionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_long_address(self):
        data = {
            'name': 'Название',
            'address': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
            'descriptions': 'Описание', 'city_name': 'Город',
            'type': 'Музеи'}
        form = CreateAttractionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_long_descriprion(self):
        data = {
            'name': 'Название',
            'address': 'Адрес',
            'descriptions': '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'city_name': 'Город',
            'type': 'Музеи'}
        form = CreateAttractionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_long_city_name(self):
        data = {
            'name': 'Название',
            'address': 'Адрес',
            'descriptions': 'Описание', 'city_name': '000000000000000000000000000000000000000000000000000',
            'type': 'Музеи'}
        form = CreateAttractionForm(data=data)
        self.assertFalse(form.is_valid())


class TestAttachment(unittest.TestCase):
    def test_invalid_form(self):
        data = {'photo': 'text'}
        form = CreatePhotoAttachmentsForm(data=data)
        self.assertFalse(form.is_valid())


class TestClient(unittest.TestCase):
    def test_go_to_login_page(self):  # Доступ к странице логина
        self.client = Client()
        url = "/auth/login/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_go_to_register_page(self):  # Доступ к странице регистрации
        self.client = Client()
        url = "/auth/registration/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_go_to_profile_page_no_auth(self):  # Доступ к странице мой профиль без логина
        self.client = Client()
        url = "/profile/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 403)

    def test_go_to_profile_page_auth(self):  # Доступ к странице мой профиль с логином
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(email='testuser', password='password')[0])
        url = "/profile/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    # def test_go_to_register(self):  # Доступ к странице мой профиль с логином
    #   self.client = Client()
    #  resp = self.client.post("/auth/registration/",
    #                          {'email': 'new@mnnn.com', 'nickname': 'nicknickname', 'password1': 'password',
    #                          'password2': 'password', 'personal_data_agreement': 'True'})
    # self.assertEqual(resp.status_code, 302)
