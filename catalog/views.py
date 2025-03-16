from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView, UpdateView
from .forms import ProductForm
from .models import Product


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.object.pk])



class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')