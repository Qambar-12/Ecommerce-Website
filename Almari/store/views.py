from django.shortcuts import render
from store.models import Product
# Create your views here.
def storeHomepage(request):
    #Query all products from the Product model and store them in the products variable passed to the template.
    products = Product.objects.all()
    return render(request, 'store/storeHome.html',{'products':products})