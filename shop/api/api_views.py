from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Product
from .serializers import ProductSerializer, ProductSearchSerializer
from rest_framework.exceptions import ValidationError
from .exception import ProductDoesNotExist
from rest_framework.permissions import IsAuthenticated


class ListProductView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class SearchProductView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSearchSerializer(data=request.data)
        try:
            serializer.is_valid()
            valid_data = serializer.validated_data
            name = valid_data.get('name')
        except:
            raise ValidationError('Not valid')
        try:
            product = Product.objects.get(name__icontains=name)
        except ProductDoesNotExist as e:
            raise ValidationError(e)
        if product:
            product_data = ProductSerializer(instance=product)
            return Response(product_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


