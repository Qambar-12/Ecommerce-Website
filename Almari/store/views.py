
# views.py
from django.shortcuts import render, get_object_or_404
from store.models import Product as ProductModel, Category as CategoryModel
from Almari.OOP.Category import Category, Product

# Create your views here.
def storeHomepage(request):
    # Query all products and categories from the database
    product_models = ProductModel.objects.all()
    category_models = CategoryModel.objects.all()

    # Create instances of OOP classes
    categories = []
    for category_model in category_models:
        category = Category(category_model.name, category_model.image_url.url)
        category.model_instance = category_model
        categories.append(category)

    products = []
    for product_model in product_models:
        category = next((c for c in categories if c.model_instance.id == product_model.category.id), None)
        if category:
            product = Product(product_model.name, product_model.price, product_model.stock_quantity,
                              product_model.description, product_model.image.url, category)
            product.id = product_model.id
            products.append(product)

    return render(request, 'store/storeHome.html', {'products': products, 'categories': categories})

def about(request):
    return render(request, 'store/about.html')

def category_detail(request, category_id):
    # Get the specific category by ID
    category_model = get_object_or_404(CategoryModel, id=category_id)
    category = Category(category_model.name, category_model.image_url.url)
    category.model_instance = category_model

    # Get all products related to this category
    product_models = ProductModel.objects.filter(category=category_model)
    products = []
    for product_model in product_models:
        product = Product(product_model.name, product_model.price, product_model.stock_quantity,
                          product_model.description, product_model.image.url, category)
        product.id = product_model.id
        products.append(product)

    return render(request, 'store/category_detail.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product_model = get_object_or_404(ProductModel, id=product_id)
    category_model = product_model.category
    category = Category(category_model.name, category_model.image_url.url)
    category.model_instance = category_model

    product = Product(product_model.name, product_model.price, product_model.stock_quantity,
                      product_model.description, product_model.image.url, category)
    product.id = product_model.id

    related_products = product.get_related_products()

    return render(request, 'store/product_detail.html', {'product': product, 'related_products': related_products})

def search(request):
    query = request.GET.get('q')
    if query:
        # Perform a search for products matching the query
        products = Product.search(query)
    else:
        products = ProductModel.objects.all()

    category_models = CategoryModel.objects.all()

    # Create Category instances
    categories = []
    for category_model in category_models:
        category = Category(category_model.name, category_model.image_url.url)
        category.model_instance = category_model
        categories.append(category)

    # Create Product instances associated with their respective categories
    searched_products = []
    for product_model in products:
        category = next((c for c in categories if c.model_instance.id == product_model.category.id), None)
        if category:
            product = Product(product_model.name, product_model.price, product_model.stock_quantity,
                              product_model.description, product_model.image.url, category)
            product.id = product_model.id
            searched_products.append(product)

    return render(request, 'store/search_result.html', {'products': searched_products, 'query': query, 'categories': categories})