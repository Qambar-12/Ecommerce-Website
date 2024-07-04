from django.shortcuts import render, redirect
from django.contrib import messages
from .verification_email import send_verification_email
from user.models import CustomerProfile
from .models import ShippingAddress, PaymentDetails
from cart.views import clear_cart
from Almari.OOP.User import CustomerUser
from Almari.OOP.Checkout import ShippingValidator, PaymentValidator
import random, time

def shipping_info(request):
    username = request.session.get('username')
    already_info = ShippingAddress.objects.filter(username=username)
    
    if request.method == 'POST':
        shipping_full_name = request.POST.get('shipping_full_name')
        shipping_email = request.POST.get('shipping_email')
        shipping_address1 = request.POST.get('shipping_address1')
        shipping_address2 = request.POST.get('shipping_address2')
        shipping_city = request.POST.get('shipping_city')
        shipping_state = request.POST.get('shipping_state')
        shipping_zipcode = request.POST.get('shipping_zipcode')
        shipping_country = request.POST.get('shipping_country')

        validator = ShippingValidator(
            email=shipping_email,
            address1=shipping_address1,
            zipcode=shipping_zipcode
        )

        is_valid, message = validator.validate()
        if is_valid:
            try:
                if already_info:
                    already_info.delete()
                    messages.success(request, 'Shipping address updated successfully!')
                else:
                    messages.success(request, 'Shipping address saved successfully!')
                    
                shipping_address = ShippingAddress(
                    username=username, 
                    shipping_full_name=shipping_full_name, 
                    shipping_email=shipping_email, 
                    shipping_address1=shipping_address1, 
                    shipping_address2=shipping_address2, 
                    shipping_city=shipping_city, 
                    shipping_state=shipping_state, 
                    shipping_zipcode=shipping_zipcode, 
                    shipping_country=shipping_country
                )
                shipping_address.save()
                return redirect('payment_info')
            except Exception as e:
                messages.error(request, f'Failed to save shipping address. Error: {str(e)}')
        else:
            messages.error(request, message)
            return render(request, 'checkout/shipping_info.html', {
                'already_info': already_info,
                'shipping_full_name': shipping_full_name,
                'shipping_email': shipping_email,
                'shipping_address1': shipping_address1,
                'shipping_address2': shipping_address2,
                'shipping_city': shipping_city,
                'shipping_state': shipping_state,
                'shipping_zipcode': shipping_zipcode,
                'shipping_country': shipping_country,
            })

    return render(request, 'checkout/shipping_info.html', {'already_info': already_info})

def payment_info(request):
    username = request.session.get('username')
    already_info = PaymentDetails.objects.filter(username=username)

    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        cardholder_name = request.POST.get('cardholder_name')
        cvv = request.POST.get('cvv')

        validator = PaymentValidator(card_number=card_number, cardholder_name=cardholder_name, cvv=cvv)

        is_valid, message = validator.validate()
        if is_valid:
            try:
                if already_info:
                    already_info.delete()
                    messages.success(request, 'Payment details updated successfully!')
                else:
                    messages.success(request, 'Payment details saved successfully!')

                payment_details = PaymentDetails(
                    username=username,
                    card_number=card_number,
                    cardholder_name=cardholder_name,
                    cvv=cvv
                )
                payment_details.save()
                confirm_order(request)
                return redirect('confirm_order')
            except Exception as e:
                messages.error(request, f'Failed to save payment details. Error: {str(e)}')
        else:
            messages.error(request, message)
            return render(request, 'checkout/payment_info.html', {
                'already_info': already_info,
                'card_number': card_number,
                'cardholder_name': cardholder_name,
                'cvv': cvv,
            })

    return render(request, 'checkout/payment_info.html', {'already_info': already_info})

# Confirm order and verify_code functions remain the same

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
        else:
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
