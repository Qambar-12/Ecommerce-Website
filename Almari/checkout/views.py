from django.shortcuts import render

# Create your views here.
def shipping_info(request):
    return render(request, 'checkout/shipping_info.html')
def payment_info(request):
    return render(request, 'checkout/payment_info.html')