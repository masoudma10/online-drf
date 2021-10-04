from django.urls import path
from . import api_views


app_name = 'order'

urlpatterns = [
    path('order_create/', api_views.OrderCreateView.as_view(),),
    path('coupon_apply/', api_views.CouponApplyView.as_view(),),
]