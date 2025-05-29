from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="телефон")
    name = models.CharField(max_length=35, **NULLABLE, verbose_name="Имя")
    surname = models.CharField(max_length=35, **NULLABLE, verbose_name="Фамилия")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
