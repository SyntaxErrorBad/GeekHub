from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from api_products.tests.basic_setup import BasicTestSetUp

from django.urls import reverse
import random


class ProductInfoTestCase(BasicTestSetUp, APITestCase):
    client: APIClient
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.url = reverse('api:product-list-json')

    def test_get_product_info(self):
        products_response = self.client.get(self.url)
        url = reverse('api:product-info-list-json', kwargs = {
            'product_id': random.choice(products_response.data)['product_id']
        })
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
