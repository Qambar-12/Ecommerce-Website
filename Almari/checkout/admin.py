from django.contrib import admin
from .models import ShippingAddress, PaymentDetails
# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(PaymentDetails)