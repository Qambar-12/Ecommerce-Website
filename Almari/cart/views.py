from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from user.models import CustomerProfile
from store.models import Product as ProductModel
from Almari.OOP.Category import Product
from Almari.OOP.Cart import Cart
from user.views import CustomerUser
#from Almari.OOP.User import CustomerUser


# Create your views here.
def cart_summary(request):
    if request.method == 'GET':
        if 'logged_in' not in request.session:
            messages.error(request, 'You must be logged in or sign up first.')
            return redirect('storeHome')
        else:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            cart = customer.cart
            #using overloaded __len__ method to check if the cart is empty or not
            if len(cart) == 0:
                 cart = None
                 return render(request, 'cart/cart_summary.html', {'cart': cart})
            else:
                total = cart.total()
                total = str(total)          #because the total is of type Decimal that is not serializable 
                cart = cart.load_cart()
                return render(request, 'cart/cart_summary.html', {'cart': cart, 'total': total})
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
                customer = CustomerUser(username, '', '', '', request=request)
                error = customer.cart.add_to_cart(product, qty)
                if not error:
                    messages.success(request, f'Added to cart successfully !!!.')
                    return redirect('product_detail', product_id=product_id)
                else:
                    messages.error(request, error)
            except ValueError as e:
                messages.error(request, str(e))

def remove_from_cart(request, product_id):
    if request.method == 'POST':
        product_model = get_object_or_404(ProductModel, pk=product_id)
        product = Product.from_model(product_model)
        try:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            cart = customer.cart

            if str(product.id) not in cart.cart:
                messages.error(request, 'Product not in cart.')
            else:
                customer.cart.remove_product(product, 1)
                if cart.cart[str(product.id)][0] <= 0:
                    del cart.cart[str(product.id)]  # Remove product from cart if quantity is 0
                messages.success(request, 'Removed from cart successfully.')

        except Exception as e:
            messages.error(request, str(e))

        return redirect('cart_summary')

def update_cart(request, product_id):
    if request.method == 'POST':
        product_model = get_object_or_404(ProductModel, pk=product_id)
        product = Product.from_model(product_model)
        try:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            cart = customer.cart
            cart_quantity = cart.cart[str(product.id)][0]
            available_quantity = product.stock_quantity - cart_quantity
            if str(product.id) not in cart.cart:
                messages.error(request, 'Product not in cart.')
            else:
                cart_quantity = cart.cart[str(product.id)][0]
                available_quantity = product.stock_quantity - cart_quantity
                if cart_quantity < product.stock_quantity:
                    customer.cart.update_product(product, 1)
                    messages.success(request, 'Updated cart successfully.')
                else:
                    messages.error(request, f'The entered quantity exceeds the available quantity. Please enter a quantity less than or equal to {available_quantity}.')

        except Exception as e:
            messages.error(request, str(e))

        return redirect('cart_summary')

def clear_cart(request):
    if request.method == 'POST':
        try:
            username = request.session['username']
            customer = CustomerUser(username, '', '', '', request=request)
            customer.cart.clear_cart()
            messages.success(request, 'Cart cleared successfully.')
        except Exception as e:
            messages.error(request, f'An error occurred while clearing the cart: {str(e)}')

        return redirect('cart_summary')
        
def save_cart(request):
    pass    
"""
from Almari.OOP.Cart import Cart
from django.contrib import messages
from django import get_object_or_404
def add_to_cart(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Product Added To Cart..."))
		return response
"""