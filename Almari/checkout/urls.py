from django.urls import path
from . import views
urlpatterns = [ 
    path('shipping_info/', views.shipping_info, name='shipping_info'),
    path('payment_info/', views.payment_info, name='payment_info'),
]