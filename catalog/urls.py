from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductDetailView, ProductListView, ProductTemplateView


app_name = CatalogConfig.name


urlpatterns = [
    path('home/', ProductListView.as_view(), name='product_list'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
