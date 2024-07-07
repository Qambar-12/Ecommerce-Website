# urls.py
from django.urls import path
from . import views
#these urls are mapped to the views in the store app
#category/<int:category_id>/ shows the page for a specific category based on the category_id i.e using primary key
#product/<int:product_id>/ shows the page for a specific product based on the product_id i.e using primary key
urlpatterns = [
path('', views.storeHomepage, name='storeHome'),
path('about/', views.about, name='about'),
path('search/', views.search, name='search'),
path('category/<int:category_id>/', views.category_detail, name='category_detail'),
path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]