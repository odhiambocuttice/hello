from django.test import TestCase, Client
from product.models import Product
from django.urls import reverse
import json


class TestViews(TestCase):

    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/detail.html')