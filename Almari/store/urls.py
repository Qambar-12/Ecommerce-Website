from django.urls import path
from . import views
urlpatterns = [
path('', views.storeHomepage, name='storeHome'),
]