from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView, UpdateView
from .forms import ProductForm, ProductModeratorForm
from .models import Product, Category
from .services import ProductService, get_products_from_cache


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.object.pk])

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return get_products_from_cache()


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def test_func(self):
        user = self.request.user
        return user == self.object.owner or user.has_perm('can_delete_product')


class Category1ListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = "catalog/category_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = '1'
        context['product_list'] = ProductService.get_category_list(category_id)
        return context


class Category2ListView(ListView):
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = '2'
        context['product_list'] = ProductService.get_category_list(category_id)
        return context