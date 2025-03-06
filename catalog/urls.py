from django.urls import path
from catalog.apps import CatalogConfig
from .views import contacts, ProductDetailView, ProductListView



app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
