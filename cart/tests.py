from django.test import TestCase
from rest_framework import status
from shop.models import Product,Category, SubCategory
from rest_framework.test import APITestCase
from django.urls import reverse
from unittest.mock import patch, Mock, MagicMock
from .api.api_views import CartDetailView, CartAdd, CartRemoveView




class CartTest(APITestCase):
    def setUp(self):
        category_data = dict(name='mobile', slug='mobile')
        self.category = Category.objects.create(**category_data)
        subcategory_data = dict(category=self.category, name='sumsung', slug='sumsung')
        self.subcategory = SubCategory.objects.create(**subcategory_data)
        product_data = dict(sub_category=self.subcategory, name='a71',
                            slug='a71',
                            price=11000)
        self.product = Product.objects.create(**product_data)



    @patch.object(CartAdd, 'permission_classes')
    def test_cart_add_succeed(self, mock):
        mock.permission_classes = []
        url = reverse('cart:cart_add', kwargs={'code':self.product.code})
        response = self.client.post(url, data={'quantity':3})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    @patch.object(CartRemoveView, 'permission_classes')
    def test_cart_remove_succeed(self, mock):
        mock.permission_classes = None
        url = reverse('cart:cart_remove', kwargs={'code':self.product.code})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


