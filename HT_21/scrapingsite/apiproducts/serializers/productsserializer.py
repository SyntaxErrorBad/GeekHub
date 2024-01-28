from rest_framework import serializers
from manageproducts.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'description', 'brand', 'category', 'sears_link', 'img']


class ProductsCaregoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category']


class ProductAddProductsSerializer(serializers.Serializer):
    product_ids = serializers.ListField(child=serializers.CharField())
