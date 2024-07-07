from Almari.OOP.User import CustomerUser
def cart_length(request):
    """Used as context processor to display cart length on every page after login and is registered in settings.py."""
    if 'logged_in' in request.session:
        username = request.session['username']
        customer = CustomerUser(username, '', '', '', request=request)
        cart = customer.cart
        return {'cart_length': len(cart)}
    return {'cart_length': 0}