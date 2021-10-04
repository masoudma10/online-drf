from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    sub_category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'


class ProductSearchSerializer(serializers.Serializer):
    name = serializers.CharField()
