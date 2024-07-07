from django.contrib import admin
from .models import UserProfile, CustomerProfile,CustomerHistory, SellerProfile
# Register your models here (for admin site access)
admin.site.register(UserProfile)
admin.site.register(CustomerProfile)
admin.site.register(CustomerHistory)
admin.site.register(SellerProfile)