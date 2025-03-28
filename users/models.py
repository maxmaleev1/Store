from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите адрес Вашей электронной почты')
    phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Номер телефона', help_text='Введите номер Вашего телефона')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Аватар', help_text='Загрузите изображение для Вашего аватара')
    country = models.CharField(max_length=50, verbose_name='Страна проживания', help_text='Введите страну Вашего проживания')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email