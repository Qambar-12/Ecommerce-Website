from django.urls import path
from . import views
urlpatterns = [
	path('customer_logout/', views.customer_logout, name='customer_logout'),
	path('customer_login/', views.customer_login, name='customer_login'),
	path('customer_signup/', views.customer_signup, name='customer_signup'),
    path('seller_signup/', views.seller_signup, name='seller_signup'),
    path('seller_login/', views.seller_login, name='seller_login'),
	path('admin_login/',views.admin_login, name='admin_login'),
    path('retrive_all_history/', views.retrieve_all_history, name='retrieve_all_history'),
    path('retrive_by_prod_history/', views.retrive_by_prod_history, name='retrive_by_prod_history'),
    path('retrive_by_date_history/', views.retrive_by_date_history, name='retrive_by_date_history'),
]
"""path('admin_signup/', views.admin_signup, name='admin_signup'),
path('admin_login/', views.admin_login, name='admin_login'),"""