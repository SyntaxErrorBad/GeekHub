from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    sears_link = models.URLField()
    img = models.URLField()

    def __str__(self):
        return self.name
