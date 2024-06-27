from user.models import CustomerHistory
import datetime
class Cart:
    def __init__(self, request):
        # list of dictionaries used to store the products in the cart
        self.session = request.session
        # Get request
        self.request = request
        # Get the current cart if it exists or create a new one if it doesn't for newly logged in user
        cart = self.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        # Make sure cart is available on all pages of site
        self.cart = cart
        self.session.modified = True
    def add_to_cart(self, product, qty=1):
        product_id = str(product.id)        
        product_name = product.name
        product_image = product.image_url
        product_qty = int(qty)              
        subtotal = float(product.price) * int(product_qty)          #typecasting the price to float because JSON does not support Decimal type (not serializable)
        # Logic
        if product_id in self.cart:
            self.cart[product_id][0] += int(product_qty)
            self.cart[product_id][2] += subtotal
        else:
            # adding the products to the cart is aggregration feature (dictionary of lists used to store the products in the cart)
            self.cart[product_id] = [int(product_qty),float(product.price),subtotal, product_name, product_image]        

        # Deal with logged in user
        # if self.request.user.is_authenticated:
        #     # Get the current user profile
        #     current_user = CustomerProfile.objects.filter(user__id=self.request.user.id)
        #     # Convert {'3':1, '2':4} to {"3":1, "2":4}
        #     carty = str(self.cart)
        #     carty = carty.replace("\'", "\"")
        #     # Save carty to the Profile Model
        #     current_user.update(old_cart=str(carty))
    
    def total(self):
        return sum(float(product[2]) for product in self.cart.values()) 
    
    def remove_product(self, product, qty):
        product_id = str(product.id)
        product_qty = int(qty)
        if product_id in self.cart:
            self.cart[product_id][0] -= product_qty
            self.cart[product_id][2] -= float(product.price) * product_qty
            self.session.modified = True     

    def update_product(self,product,qty):
        product_id = str(product.id)
        product_qty = int(qty)
        if product_id in self.cart:
            self.cart[product_id][0] += product_qty
            self.cart[product_id][2] += float(product.price) * product_qty
            self.session.modified = True

    def clear_cart(self):
        self.cart.clear()
        self.session['cart'] = {}
        self.session.modified = True
    def load_cart(self):
        return self.cart       
    
    def save_cart_to_history(self):
        history = CustomerHistory(username = self.request.session['username'],date = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S") ,cart = self.cart, total = self.total())       
        history.save() 
    
    # since cart is sort of container class
    def __len__(self):                              # operartor overloading used to return the length of the cart i.e 
                                                    # the number of unique products in the cart
        return len(self.cart)                       