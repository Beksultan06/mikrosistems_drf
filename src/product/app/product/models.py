from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Заголовка')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Продукты'