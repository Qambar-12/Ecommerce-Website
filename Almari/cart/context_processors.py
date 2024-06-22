from Almari.OOP.User import CustomerUser
def cart_length(request):
    if 'logged_in' in request.session:
        username = request.session['username']
        customer = CustomerUser(username, '', '', '', request=request)
        cart = customer.cart
        return {'cart_length': len(cart)}
    return {'cart_length': 0}