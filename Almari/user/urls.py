from django.urls import path
from . import views
#these urls route to the views in the user app
urlpatterns = [
	path('customer_logout/', views.customer_logout, name='customer_logout'),
	path('customer_login/', views.customer_login, name='customer_login'),
	path('customer_signup/', views.customer_signup, name='customer_signup'),
    path('seller_signup/', views.seller_signup, name='seller_signup'),
    path('seller_login/', views.seller_login, name='seller_login'),
	path('admin_login/',views.admin_login, name='admin_login'),
    path('retrieve_all_history/', views.retrieve_all_history, name='retrieve_all_history'),
    path('retrieve_by_prod_history/', views.retrieve_by_prod_history, name='retrieve_by_prod_history'),
    path('retrieve_by_date_history/', views.retrieve_by_date_history, name='retrieve_by_date_history'),
    path('change_customer_email/', views.change_customer_email, name='change_customer_email'),
    path('change_customer_password/', views.change_customer_password, name='change_customer_password'),
]
"""path('admin_signup/', views.admin_signup, name='admin_signup'),
path('admin_login/', views.admin_login, name='admin_login'),"""