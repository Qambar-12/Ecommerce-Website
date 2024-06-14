from django.contrib import admin
from .models import UserProfile, CustomerProfile, SellerProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CustomerProfile)
admin.site.register(SellerProfile)