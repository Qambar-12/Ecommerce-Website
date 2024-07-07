from django.contrib import admin
from .models import Category, Product
# Register your models here (for the admin panel to make them accessible).
admin.site.register(Category)
admin.site.register(Product)