# urls.py
from django.urls import path
from . import views
urlpatterns = [
path('', views.storeHomepage, name='storeHome'),
path('about/', views.about, name='about'),
path('search/', views.search, name='search'),
path('category/<int:category_id>/', views.category_detail, name='category_detail'),
path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]