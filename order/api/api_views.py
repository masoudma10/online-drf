from rest_framework.views import APIView
from ..models import Order, OrderItem, Coupon
from cart.cart import Cart
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from .serializers import CouponSerializer
from rest_framework import status
from django.core import serializers




class OrderCreateView(APIView):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=self.request.user)
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return Response(status=status.HTTP_201_CREATED)




class CouponApplyView(APIView):
    def post(self, request, order_id):
        now = timezone.now()
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            code = valid_data.get('code')
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                order = Order.objects.get(id=order_id)
                order.discount = coupon.discount
                order.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            except Coupon.DoesNotExist:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)








