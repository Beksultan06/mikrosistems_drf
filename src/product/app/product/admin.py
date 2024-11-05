from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'created_by']
    list_filter = ['name', 'description', 'price', 'created_by']
    search_fields = ['name', 'description', 'price', 'created_by']