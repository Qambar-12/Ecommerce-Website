from django.shortcuts import render, redirect
from django.contrib import messages
from .verification_email import send_verification_email
from user.models import CustomerProfile
from cart.views import clear_cart
from Almari.OOP.User import CustomerUser
import random, time

# Create your views here.
def shipping_info(request):
    return render(request, 'checkout/shipping_info.html')

def payment_info(request):
    return render(request, 'checkout/payment_info.html')

def confirm_order(request):
    if request.method == 'POST':
        try:
            customer_user = CustomerProfile.objects.get(username=request.session['username'])
        except CustomerProfile.DoesNotExist:
            messages.error(request, 'Customer profile not found.')
            return redirect('payment_info')
        
        user_email = customer_user.email
        verification_code = random.randint(100000, 999999)
        
        try:
            start_time = send_verification_email(user_email, str(verification_code))
        except Exception as e:
            messages.error(request, f'Failed to send verification email. Error: {str(e)}')
            return redirect('payment_info')
        
        request.session['verification_code'] = verification_code
        request.session['verification_start_time'] = start_time
        return redirect('confirm_order')
    
    return render(request, 'checkout/confirm_order.html')

def verify_code(request):
    if request.method == 'POST':
        user_code = request.POST.get('verification_code')
        verification_code = request.session.get('verification_code')
        start_time = request.session.get('verification_start_time')
        stop_time = time.time()
        
        if not verification_code or not start_time:
            messages.error(request, 'Verification process not started or expired. Please try again.')
            return redirect('payment_info')
        
        if stop_time - start_time > 60:
            messages.error(request, 'Verification code has expired! Please try again.')
            confirm_order(request)
            return render(request, 'checkout/confirm_order.html')
        
        if user_code == str(verification_code):
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            customer.cart.save_cart_to_history()
            messages.success(request, 'Your order has been placed successfully!')
            clear_cart(request, show_message = False)
            return redirect('storeHome')
        else:
            messages.error(request, 'Invalid verification code! Please try again.')
            return redirect('confirm_order')
    return redirect('confirm_order')
