from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="наименование категории")
    description = models.TextField(verbose_name='описание категории', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта', blank=True, null=True)
    image = models.ImageField(upload_to='photos/', verbose_name='изображение продукта', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(verbose_name='дата создания карточки продукта', auto_now_add=True)
    updated_at = models.DateField(verbose_name='дата последнего изменения карточки продукта', auto_now=True)
    publication_status = models.BooleanField(default=False, verbose_name='статус публикации')
    owner = models.ForeignKey(User, verbose_name='владелец продукта', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price']
        permissions = [('can_unpublish_product', 'Can unpublish product'),]