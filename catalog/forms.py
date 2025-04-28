from django import forms
from django.core.exceptions import ValidationError
from .models import Product
from . import constanta


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category', 'publication_status']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите фото продукта',
            'type': 'image'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену продукта',
            'type': 'integer'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean(self):
        cleaned_data = super().clean()
        block_list = constanta.BLOCK_LIST

        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and name.lower() in block_list:
            raise ValidationError('Имя содержит запрещенное слово')

        if description and description.lower() in block_list:
            raise ValidationError('Описание содержит запрещенное слово')

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['publication_status']