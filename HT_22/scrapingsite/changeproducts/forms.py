from django import forms
from manageproducts.models import Product


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'brand', 'category', 'sears_link', 'img']