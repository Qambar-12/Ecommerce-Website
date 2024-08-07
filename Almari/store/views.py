from django.shortcuts import render, get_object_or_404
from store.models import Product as ProductModel, Category as CategoryModel
from django.contrib import messages
from Almari.OOP.Category import Category, Product
from Almari.OOP.Cart import Cart
from user.views import CustomerUser

def storeHomepage(request):
    """This function is used to render the homepage of the store. It fetches the categories and products from the database and passes them to the template."""
    category_models = CategoryModel.objects.all()
    #list of Category objects created from the CategoryModel objects (database records)
    #how these objects are created is defined in the from_model method of the Category class.
    categories = [Category.from_model(category_model) for category_model in category_models]
    product_models = ProductModel.objects.all()[:8]
    products = [Product.from_model(product_model) for product_model in product_models]

    return render(request, 'store/storeHome.html', {'categories': categories, 'products': products})

def about(request):
    """This function is used to render the about page of the store. """
    return render(request, 'store/about.html')

def category_detail(request, category_id):
    """This function is used to render the page for a specific category. It fetches the category and its products from the database and passes them to the template. It also handles sorting of products based on price."""
    category_model = get_object_or_404(CategoryModel, id=category_id)
    category = Category.from_model(category_model)
    category.load_products()
    #get the sort option from request
    sort_option = request.GET.get('sort','default')
    if sort_option == 'price_low_to_high':
        category.products = sorted(category.products, key=lambda p: p.price)
    elif sort_option == 'price_high_to_low':
        category.products = sorted(category.products, key=lambda p: p.price, reverse=True)

    return render(request, 'store/category_detail.html', {'category': category, 'products': category.products,'sort_option':sort_option})

def product_detail(request, product_id):
    """This function is used to render the page for a specific product. It fetches the product and its related products from the database and passes them to the template. It also calculates the available quantity of the product based on the quantity in the cart."""
    product_model = get_object_or_404(ProductModel, id=product_id)
    product = Product.from_model(product_model)
    related_products = product.get_related_products()
    if 'logged_in' in request.session:
        username = request.session['username']
        customer = CustomerUser(username, '', '', '', request=request)
        cart = customer.cart
        if str(product.id) in cart.cart:
            cart_quantity = cart.cart[str(product.id)][0]
        else:
            cart_quantity = 0
        available_quantity = product.stock_quantity - cart_quantity
        return render(request, 'store/product_detail.html', {'product': product, 'related_products': related_products , 'available_quantity': available_quantity})
    else:
        return render(request, 'store/product_detail.html', {'product': product, 'related_products': related_products})
def search(request):
    """This function is used to handle the search functionality. It fetches the search query from the request and returns the search results based on the query."""
    query = request.GET.get('q')
    category_models = CategoryModel.objects.all()
    categories = [Category.from_model(category_model) for category_model in category_models]

    if query:
        searched_products = Product.search(query)
        return render(request, 'store/search_result.html', {'products': searched_products, 'query': query, 'categories': categories})
    else:
        messages.error(request, 'No search query entered. Please enter a search query.')
        return render(request, 'store/storeHome.html', {'categories': categories})

