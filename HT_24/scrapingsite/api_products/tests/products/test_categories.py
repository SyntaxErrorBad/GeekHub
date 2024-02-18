from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from api_products.tests.basic_setup import BasicTestSetUp

from django.urls import reverse


class ProductCategoriesTestCase(BasicTestSetUp, APITestCase):
    client: APIClient
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.url = reverse('api:product-categories-list-json')

    def test_get_product_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)