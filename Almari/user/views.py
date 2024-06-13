from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Almari.OOP.User import CustomerUser
# Create your views here.
#Posting the data from the form to the server and saving it in the database if data is valid.
def customer_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']

        customer_user = CustomerUser(username, email, password, address)
        error = customer_user.signup(confirm_password)

        if error:
            messages.error(request, error)
            request.session['form_data'] = request.POST.dict()
            #return render(request, 'user/customer_signup.html',{
                #'username': username,
                #'email': email,
                #'address': address})
            return redirect("customer_signup")    
        
        else:
            if 'form_data' in request.session:
                del request.session['form_data']
            return redirect('storeHome')
    else:
        form_data = request.session.get('form_data', {})
        # return render(request, 'user/customer_signup.html',form_data)
        return render(request, 'user/customer_signup.html', {'form_data': form_data, 'request': request})

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        customer_user = CustomerUser(username, '', password, '')
        customer, error = customer_user.login(username, password)

        if customer:
            # Log in the customer
            #login(request, customer)
            request.session['logged_in'] = True
            messages.success(request, 'You have been logged in')
            return redirect('storeHome')  
        else:
            messages.error(request, error)
            return render(request, 'user/customer_login.html')
    return render(request, 'user/customer_login.html')

def customer_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('storeHome')
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

