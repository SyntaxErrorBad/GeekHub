import factory

from django.contrib.auth.models import User
from manage_products.models import Product

TEST_PASSWORD = 'testpassword123'

class ProductFactory(factory.django.DjangoModelFactory):
    product_id = factory.Sequence(lambda n: 'Product_ID: {}'.format(n))
    name = factory.Faker('company')
    price = factory.Faker('random_number', digits=2)
    description = factory.Faker('sentence')
    brand = factory.Faker('word')
    category = factory.Iterator(['Books', 'IT', 'Computer'])
    sears_link = factory.Faker('url')
    img = factory.Faker('url')

    class Meta:
        model = Product


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('first_name')
    password = factory.PostGenerationMethodCall('set_password', TEST_PASSWORD)

    class Meta:
        model = User
