from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    """ Это модель пользователя """
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон', **NULLABLE)
    city = models.TextField(max_length=50, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта')
    telegram_chat_id = models.CharField(max_length=100, verbose_name='Telegram chat ID', blank=True)

    # Смена авторизации с имени пользователя на электронную почту
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telegram_chat_id']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
