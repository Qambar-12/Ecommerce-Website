"""from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import CustomerProfile
from store.models import Product as ProductModel
from Almari.OOP.Category import Product
from Almari.OOP.Cart import Cart
from Almari.OOP.User import CustomerUser

# Create your views here.
def cart_summary(request):
    if request.method == 'GET':
        if 'logged_in' not in request.session:
            messages.error(request, 'You must be logged in or sign up first.')
            return redirect('storeHome')
        else:
            cart = Cart.load_cart()
            return render(request, 'cart/cart_summary.html', {'cart':cart})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        if 'logged_in' not in request.session:
            messages.error(request, 'You must be logged in or sign up first.')
            return redirect('product_detail', product_id=product_id)
        else:
            product_model = ProductModel.objects.get(pk=product_id)
            #creating a Product object from the product_model object
            product = Product.from_model(product_model)
            qty  = int(request.POST['quantity'])
            #exception handling to handle possible exceptions
            try:
                #adding the product to cart of the logged in customer
                #using the add_to_cart method of the cart object 
                #since the CustomerUser owns the cart (composition) , the cart is instantiated in the CustomerUser class
                #i.e if None returned from Cart class
                username = request.session['username']
                customer_model = CustomerProfile.objects.get(username = username)
                customer = CustomerUser(customer_model.username,'','','')
                error = customer.cart.add_product(product, qty)
                if not error:
                    messages.success(request, f'Added to cart successfully !!!.')
                else:
                    messages.error(request, error)
            except ValueError as e:
                messages.error(request, str(e))

def remove_from_cart(request):
    pass
def update_cart(request):
    pass
def clear_cart(request):
    pass
def save_cart(request):
    pass    """