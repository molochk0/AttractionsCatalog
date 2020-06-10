import unittest
from django.test import TestCase, Client
from FirstPage.forms import *
from FirstPage.models import *


class TestClient(unittest.TestCase):
    def test_go_to_atr_page(self):
        self.client = Client()
        url = "/attraction/39/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_go_to_atr_page_invalid(self):
        self.client = Client()
        url = "/attraction/50/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)