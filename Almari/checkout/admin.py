from django.contrib import admin
from .models import ShippingAddress, PaymentDetails
# Register your models here (for admin panel to make changes)
admin.site.register(ShippingAddress)
admin.site.register(PaymentDetails)