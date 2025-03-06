from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Product


def contacts(request):
    return render(request, 'contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'