from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#To reference or reverse these admin URLs programmatically, you typically use the built-in view names provided by the admin interface.
from django.urls import reverse
from django.contrib import messages
from .captcha import generate_image_captcha
from Almari.OOP.User import CustomerUser
import ast
# Create your views here.
#Posting the data from the form to the server and saving it in the database if data is valid.
def customer_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']
        captcha = request.POST['captcha']
        if captcha:
            if captcha == request.session.get('captcha', ''):
                customer_user = CustomerUser(username, email, password, address, request = request)
                error = customer_user.signup(confirm_password)

                if error:
                    # Regenerate CAPTCHA if form is not valid
                    captcha_image, captcha_str = generate_image_captcha()
                    request.session['captcha'] = captcha_str
                    messages.error(request, error)
                    request.session['form_data'] = request.POST.dict()
                    #so that the form data is not lost when the page is reloaded
                    return render(request, 'user/customer_signup.html',{
                        'username': username,
                        'email': email,
                        'address': address,
                        'captcha_image': captcha_image})
                
                else:
                    if 'form_data' in request.session:
                        del request.session['form_data']    
                    request.session['logged_in'] = True    
                    messages.success(request, 'You have signed up successfully') 
                    #storing username in session dictionary to retrieve it while adding to cart
                    request.session['username'] = username   
                    return redirect('storeHome')
            else:
                messages.error(request, 'Invalid CAPTCHA')
                # Regenerate CAPTCHA if form is not valid
                captcha_image, captcha_str = generate_image_captcha()
                request.session['captcha'] = captcha_str
                return render(request, 'user/customer_signup.html', {
                    'username': username,
                    'email': email,
                    'password': password,
                    'captcha_image': captcha_image})    
        else:
            messages.error(request, 'All fields are required.')
            # Regenerate CAPTCHA if form is not valid
            captcha_image, captcha_str = generate_image_captcha()
            request.session['captcha'] = captcha_str
            return render(request, 'user/customer_signup.html', {
                'username': username,
                'email': email,
                'password': password,
                'captcha_image': captcha_image})    
    else:
        #initially the captcha is generated and stored in the session
        captcha_image, captcha_str = generate_image_captcha()
        request.session['captcha'] = captcha_str
        form_data = request.session.get('form_data', {})
        return render(request, 'user/customer_signup.html', {'form_data': form_data, 'captcha_image': captcha_image,'request': request})

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        captcha = request.POST['captcha']
        if captcha:
            if captcha == request.session.get('captcha', ''):
                customer_user = CustomerUser(username, '', password, '',request = request)
                customer, error = customer_user.login(username, password)
                if customer:
                    # Log in the customer
                    #login(request, customer)
                    #so the navbar can show the logout button and hide the login and signup buttons
                    request.session['logged_in'] = True
                    #storing it in session dictionary to use it later while adding to cart
                    request.session['username'] = username
                    messages.success(request, 'You have been logged in')
                    return redirect('storeHome')  
                else:
                    # Regenerate CAPTCHA if form is not valid
                    captcha_image, captcha_str = generate_image_captcha()
                    request.session['captcha'] = captcha_str
                    request.session['form_data'] = request.POST.dict()
                    messages.error(request, error)
                    return render(request, 'user/customer_login.html', {'username': username, 'password': password, 'captcha_image': captcha_image})
            else:
                messages.error(request, 'Invalid CAPTCHA')
                # Regenerate CAPTCHA if form is not valid
                captcha_image, captcha_str = generate_image_captcha()
                request.session['captcha'] = captcha_str
                return render(request, 'user/customer_login.html', {'username': username, 'password': password, 'captcha_image': captcha_image})
        else:
            messages.error(request, 'All fields are required.')
            # Regenerate CAPTCHA if form is not valid
            captcha_image, captcha_str = generate_image_captcha()
            request.session['captcha'] = captcha_str
            return render(request, 'user/customer_login.html', {'username': username, 'password': password, 'captcha_image': captcha_image})    
    else:
        #initially the captcha is generated and stored in the session
        captcha_image, captcha_str = generate_image_captcha()
        request.session['captcha'] = captcha_str
        form_data = request.session.get('form_data', {})
        return render(request, 'user/customer_login.html', {'form_data': form_data, 'captcha_image': captcha_image,'request': request})
def change_customer_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('new_email')
        try:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            error = customer.change_email(new_email)
        except Exception as e:
            messages.error(request,f"Something went wrong please try again {e}")
            return redirect('storeHome')
        else:
            if error:
                messages.error(request, error)
                return render(request, 'user/change_email.html')
            else:
                messages.success(request, 'Email changed successfully')
                return redirect('storeHome')
    return render(request, 'user/change_email.html')
def change_customer_password(request):
    if request.method == 'POST':
        previous_password = request.POST.get('previous_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        try:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            error = customer.change_password(previous_password, new_password, confirm_password)
        except Exception as e:
            messages.error(request,f"Something went wrong please try again {e}")
            return redirect('storeHome')
        else:
            if error:
                messages.error(request, error)
                return render(request, 'user/change_password.html')
            else:
                messages.success(request, 'Password changed successfully')
                return redirect('storeHome')
    return render(request, 'user/change_password.html')


def customer_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('storeHome')
def admin_login(request):
    admin_login_url = reverse('admin:login')
    return redirect(admin_login_url)
def seller_signup(request):
    return render(request, 'user/seller_signup.html')
def seller_login(request):
    return render(request, 'user/seller_login.html')

def retrieve_all_history(request):
    if request.method == 'GET':
        try :
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            history = customer.history.retrieve_all_history()
            #converting the cart from string to dictionary back again when passing it to the template via context dictionary
            for record in history:
                record['cart'] = ast.literal_eval(record['cart'])
        except Exception as e:
            messages.error(request,f"Something went wrong please try again {e}")
            return redirect('storeHome')
        else:
            if history:
                return render(request, 'user/retrieve_all_history.html', {'history': history})
            else:
                return render(request, 'user/retrieve_all_history.html', {'history': None})
def retrieve_by_prod_history(request):
    if request.method == 'POST':
        prod = request.POST.get('prod')
        try:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            history = customer.history.retrieve_by_prod_history(prod)
            if isinstance(history, list):
                #converting the cart from string to dictionary back again when passing it to the template via context dictionary
                for record in history:
                    record['cart'] = ast.literal_eval(record['cart'])
            else:
                messages.error(request, history)
                return render(request, 'user/retrieve_by_prod_history.html')        
        except Exception as e:
            messages.error(request,f"Something went wrong please try again {e}")
            return redirect('storeHome')
        else:
            if history:
                return render(request, 'user/retrieve_by_prod_history.html', {'history': history})
            else:
                return render(request, 'user/retrieve_by_prod_history.html', {'history': None})
    return render(request, 'user/retrieve_by_prod_history.html')

def retrieve_by_date_history(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        try:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            history = customer.history.retrieve_by_date_history(date)
            print(history)
            if isinstance(history, list):
                #converting the cart from string to dictionary back again when passing it to the template via context dictionary
                for record in history:
                    record['cart'] = ast.literal_eval(record['cart'])
            else:
                messages.error(request, history)
                return render(request, 'user/retrieve_by_date_history.html')        
        except Exception as e:
            messages.error(request,f"Something went wrong please try again {e}")
            return redirect('storeHome')
        else:
            if history:
                return render(request, 'user/retrieve_by_date_history.html', {'history': history})
            else:
                return render(request, 'user/retrieve_by_date_history.html', {'history': None})
    return render(request, 'user/retrieve_by_date_history.html')

"""def admin_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        admin_user = AdminUser(username, email, password)
        error = admin_user.signup()

        if error:
            messages.error(request, error)
            return render(request, 'signup.html')
        return redirect('login')
    return render(request, 'signup.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        admin_user = AdminUser(username, '', password)
        admin, error = admin_user.login(username, password)

        if admin:
            # Log in the admin
            return redirect('admin_home')
        else:
            messages.error(request, error)
            return render(request, 'login.html', {
                'show_signup_button': error == "Username does not exist.",
                'show_forgot_password': True
            })
    return render(request, 'login.html')
"""

