from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from .views import (ProductDetailView, ProductListView, ProductTemplateView, ProductCreateView, ProductUpdateView,
ProductDeleteView, Category1ListView, Category2ListView)


app_name = CatalogConfig.name


urlpatterns = [
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/category/1/', Category1ListView.as_view(), name="product_category_1"),
    path('products/category/2/', Category2ListView.as_view(), name="product_category_2")
]