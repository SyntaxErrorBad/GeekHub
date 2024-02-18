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
        self.url = reverse('api:logout-user-api')

    def test_logout_get(self):
        self.client.force_authenticate(user=self.common_user)
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_logout_post(self):
        self.client.force_authenticate(user = self.common_user)
        response = self.client.post(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)