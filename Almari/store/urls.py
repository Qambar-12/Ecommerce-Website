from django.urls import path
from . import views
urlpatterns = [
path('', views.storeHomepage, name='storeHome'),
path('about/', views.about, name='about'),
]