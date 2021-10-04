from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from ..cart import Cart
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from shop.models import Product
from django.core.exceptions import EmptyResultSet
from .serializers import CartAddSerializer
import json
from .exception import ProductDoesNotExist



class CartDetailView(APIView):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            serialize = json.dumps(item)
            return Response(serialize, status=status.HTTP_200_OK)


class CartAdd(APIView):
    def post(self, request, code):
        cart = Cart(request)
        try:
            product = Product.objects.get(code=code)
        except ProductDoesNotExist as e:
            raise EmptyResultSet(e)
        serializer = CartAddSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            quantity = valid_data.get('quantity')
            cart.add(product=product, quantity=quantity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRemoveView(APIView):
    def get(self, request, code):
        cart = Cart(request)
        product = get_object_or_404(Product, code=code)
        cart.remove(product)
        return Response(data='remove', status=status.HTTP_204_NO_CONTENT)



