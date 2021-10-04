from django.urls import path
from . import api_views

app_name = 'shop'

urlpatterns = [
    path('products/', api_views.ListProductView.as_view(),),
    path('products_search/', api_views.SearchProductView.as_view(),),
]