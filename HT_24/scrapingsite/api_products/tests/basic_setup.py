from .factories import UserFactory
from .factories import ProductFactory


class BasicTestSetUp:
    def setUp(self):
        self.common_user = UserFactory.create()
        self.super_user = UserFactory.create(is_staff=True, is_superuser=True)
        self.products = ProductFactory.create_batch(1)