from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from api_products.tests.basic_setup import BasicTestSetUp

from django.urls import reverse
import random


TEST_VALID_ID = "A105601864"


class ProductAddTestCase(BasicTestSetUp, APITestCase):
    client: APIClient
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.url = reverse('api:product-add')

    def test_add_product_is_not_authenticate(self):
        response = self.client.get(
            self.url,
            data={
                'product_ids': TEST_VALID_ID
                }
            )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_add_product_is_common_user(self):
        self.client.force_authenticate(user = self.common_user)
        response = self.client.get(
            self.url,
            data={
                'product_ids': TEST_VALID_ID
                }
            )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    # def test_add_product_is_super_user(self):
    #     self.client.force_authenticate(user = self.super_user)
    #     response = self.client.post(
    #         self.url,
    #         data={
    #             'product_ids': TEST_VALID_ID
    #             }
    #         )
    #     print(response.data)
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)