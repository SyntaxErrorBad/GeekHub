from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from api_products.tests.basic_setup import BasicTestSetUp

from django.urls import reverse


TEST_CART_PRODUCT = 'Product 0'


class ShoppingCartAddOrRemoveTestCase(BasicTestSetUp, APITestCase):
    client: APIClient
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.client.force_authenticate(user=self.common_user)
        self.url = reverse('api:shopping-cart')

    def test_add_item_to_shopping_cart(self):
        response = self.client.post(
            self.url,
            data={
                'product_id': TEST_CART_PRODUCT
            }
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_remove_item_to_shopping_cart(self):
        self.test_add_item_to_shopping_cart()
        response = self.client.post(
            self.url,
            data={
                'product_id': TEST_CART_PRODUCT
            }
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_invalid_data(self):
        response = self.client.post(
            self.url,
            data={
                'product_id': ' '
            }
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)