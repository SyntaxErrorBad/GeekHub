from api_products.tests.basic_setup import BasicTestSetUp
from api_products.tests.factories import TEST_PASSWORD

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.urls import reverse


class UserLoginTestCase(BasicTestSetUp, APITestCase):
    client: APIClient
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.url = reverse('api:login-user-api')

    def test_login_common_user_success(self):
        response = self.client.post(
            path=self.url,
            data={
                'username': self.common_user.username,
                'password': TEST_PASSWORD
            }
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_login_super_user_success(self):
        response = self.client.post(
            path = self.url,
            data = {
                'username': self.super_user.username,
                'password': TEST_PASSWORD
            }
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_login__failure(self):
        response = self.client.post(
            path = self.url,
            data = {
                'username': '{}_fake'.format(self.common_user.username),
                'password': TEST_PASSWORD
            }
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_invalid_data(self):
        response = self.client.post(
            path = self.url,
            data = {
                'username': ' ',
                'password': ''
            }
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_single_data(self):
        response = self.client.post(
            path = self.url,
            data = {
                'username': ' '
            }
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
