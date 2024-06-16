from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#To reference or reverse these admin URLs programmatically, you typically use the built-in view names provided by the admin interface.
from django.urls import reverse
from django.contrib import messages
from .captcha import generate_image_captcha
from Almari.OOP.User import CustomerUser
# Create your views here.
#Posting the data from the form to the server and saving it in the database if data is valid.

def admin_login(request):
    admin_login_url = reverse('admin:login')
    return redirect(admin_login_url)
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

