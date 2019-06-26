from django.test import SimpleTestCase
from django.urls import reverse, resolve
from product.views import product_detail_view


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('product')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, product_detail_view)
