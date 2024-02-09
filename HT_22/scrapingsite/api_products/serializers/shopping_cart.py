from rest_framework import serializers


class ShoppingCartSerializer(serializers.Serializer):
    product_id = serializers.CharField()
    quantity = serializers.IntegerField(min_value=1, default=1)


class ShoppingCartRemoveSerializer(serializers.Serializer):
    product_id = serializers.CharField()