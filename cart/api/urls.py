from django.urls import path
from . import api_views

app_name = 'cart'

urlpatterns = [
    path('cart_detail/',api_views.CartDetailView.as_view(), name='cart_detail'),
    path('cart_add/<str:code>/',api_views.CartAdd.as_view(), name='cart_add'),
    path('cart_remove/<str:code>/',api_views.CartRemoveView.as_view(), name='cart_remove'),

]