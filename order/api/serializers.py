from rest_framework import serializers

class CouponSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)