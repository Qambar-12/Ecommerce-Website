from django.db import models
from store.models import Product
# Create your models here.
"""class Cart(models.Model):
    
    #Represents a cart table in the e-commerce store database.
    
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')"""
    