from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False, help_text='Необязательное поле. Введите Ваш номер телефона')
    avatar = forms.ImageField(required=False, help_text='Необязательное поле. Загрузите изображение для Вашего профиля')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','phone', 'avatar', 'country', 'password1', 'password2')