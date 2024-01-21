from django import template
from manageproducts.models import Product

register = template.Library()


@register.filter
def get_product_data(product):
    try:
        product_data = Product.objects.get(product_id=product)
        return product_data
    except Product.DoesNotExist:
        return None


@register.filter
def get_multiply(f_number, s_number):
    return float(f_number) * float(s_number)
