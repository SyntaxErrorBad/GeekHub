from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from api_products.tests.basic_setup import BasicTestSetUp

from django.urls import reverse


TEST_CART_PRODUCT = 'Product 0'
QUANTITY = 5


class ShoppingCartAddQuantityTestCase(BasicTestSetUp, APITestCase):
    client: APIClient
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.client.force_authenticate(user=self.common_user)
        self.url = reverse('api:shopping-cart-add-api')

    def test_add_item_to_shopping_cart(self):
        response = self.client.post(
            self.url,
            data={
                'product_id': TEST_CART_PRODUCT,
                'quantity': QUANTITY
            }
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_add_if_in_shopping_cart(self):
        self.test_add_item_to_shopping_cart()
        response = self.client.post(
            self.url,
            data={
                'product_id': TEST_CART_PRODUCT,
                'quantity': QUANTITY
            }
        )
        self.assertEqual(status.HTTP_409_CONFLICT, response.status_code)

    def test_invalid_data(self):
        response = self.client.post(
            self.url,
            data={
                'product_id': ' ',
                'quantity': ' '
            }
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_single_data_product_id(self):
        response = self.client.post(
            self.url,
            data={
                'product_id': TEST_CART_PRODUCT
            }
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_single_data_quantity(self):
        response = self.client.post(
            self.url,
            data={
                'quantity': QUANTITY
            }
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)