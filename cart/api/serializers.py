from rest_framework import serializers



class CartAddSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()