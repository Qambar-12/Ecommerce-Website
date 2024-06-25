from django.urls import path
from . import views
urlpatterns = [ 
    path('shipping_info/', views.shipping_info, name='shipping_info'),
    path('payment_info/', views.payment_info, name='payment_info'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('verify_code/', views.verify_code, name='verify_code')
]