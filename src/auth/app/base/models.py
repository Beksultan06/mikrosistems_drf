from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=155,
        verbose_name="номер телефона"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Пользователи'