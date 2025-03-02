from django.urls import path
from catalog.views import home
from catalog.views import contacts
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
