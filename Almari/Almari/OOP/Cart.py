"""class Cart:
    def __init__(self):
        #list of dictionaries used to store the products in the cart
        self.products = []      #aggregation feature used with products because the cart can exist without products
        self.total = 0    
    def add_product(self, product,qty=1):
        try:
            if qty <= 0:
                raise ValueError("Quantity must be positive.")
            if qty > product.stock_quantity:
                raise ValueError("Quantity exceeds available stock.")
            for p in self.products:
                if p.key() == product.id:
                    p[product.id] += qty
                    self.total += product.price * qty
                    return
            self.products.append({product.id:qty})
        except ValueError as e:
            print(f"Error adding item to cart: {e}")
    def remove_product(self, product):
        pass      
    def cart_summary(self):
        pass
    def clear_cart(self):
       pass
    def load_cart(self):
        pass       
    def save_cart(self):
        pass
    #since cart is sort of container class
    def __len__(self):
        return len(self.products)                   #operartor overloading used to return the length of the cart i.e 
                                                    #the number of unique products in the cart
"""
class Cart:
	def __init__(self, request):
		self.session = request.session
		# Get request
		self.request = request
		# Get the current session key if it exists
		cart = self.session.get('session_key')

		# If the user is new, no session key!  Create one!
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}
		# Make sure cart is available on all pages of site
		self.cart = cart
    def add_to_cart(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save carty to the Profile Model
            current_user.update(old_cart=str(carty))