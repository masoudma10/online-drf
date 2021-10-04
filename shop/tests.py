from django.test import TestCase
from rest_framework import status
from .models import Product,Category, SubCategory
from rest_framework.test import APITestCase
from django.urls import reverse
from unittest.mock import patch, Mock, MagicMock
from rest_framework.permissions import AllowAny
from .api.api_views import SearchProductView



class ListProductTest(APITestCase):

    def setUp(self):
        category_data = dict(name='mobile', slug='mobile')
        self.category = Category.objects.create(**category_data)
        subcategory_data = dict(category=self.category, name='sumsung', slug='sumsung')
        self.subcategory = SubCategory.objects.create(**subcategory_data)
        product_data = dict(sub_category=self.subcategory, name='a71',
                            slug='a71',
                            price=11000)
        Product.objects.create(**product_data)



    def test_product_list_ok(self):
        url = reverse('shop:products')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    @patch.object(SearchProductView, 'permission_classes')
    def test_product_search_succeed(self, mock):
        mock.permission_classes = None
        url = reverse('shop:product_search')
        response = self.client.post(url, data={'name':'71'})
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)



