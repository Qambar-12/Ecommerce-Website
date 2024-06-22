from django.shortcuts import render, get_object_or_404
from store.models import Product as ProductModel, Category as CategoryModel
from django.contrib import messages
from Almari.OOP.Category import Category, Product
from Almari.OOP.Cart import Cart
from user.views import CustomerUser

def storeHomepage(request):
    category_models = CategoryModel.objects.all()
    #list of Category objects created from the CategoryModel objects (database records)
    #how these objects are created is defined in the from_model method of the Category class.
    categories = [Category.from_model(category_model) for category_model in category_models]

    return render(request, 'store/storeHome.html', {'categories': categories})

def about(request):
    return render(request, 'store/about.html')

def category_detail(request, category_id):
    category_model = get_object_or_404(CategoryModel, id=category_id)
    category = Category.from_model(category_model)
    category.load_products()
    return render(request, 'store/category_detail.html', {'category': category, 'products': category.products})

def product_detail(request, product_id):
    product_model = get_object_or_404(ProductModel, id=product_id)
    product = Product.from_model(product_model)
    related_products = product.get_related_products()
    username = request.session['username']
    customer = CustomerUser(username, '', '', '', request=request)
    cart = customer.cart
    if str(product.id) in cart.cart:
        cart_quantity = cart.cart[str(product.id)][0]
    else:
        cart_quantity = 0
    
    available_quantity = product.stock_quantity - cart_quantity
    return render(request, 'store/product_detail.html', {'product': product, 'related_products': related_products , 'available_quantity': available_quantity})

def search(request):
    query = request.GET.get('q')
    category_models = CategoryModel.objects.all()
    categories = [Category.from_model(category_model) for category_model in category_models]

    if query:
        searched_products = Product.search(query)
        return render(request, 'store/search_result.html', {'products': searched_products, 'query': query, 'categories': categories})
    else:
        messages.error(request, 'No search query entered. Please enter a search query.')
        return render(request, 'store/storeHome.html', {'categories': categories})

