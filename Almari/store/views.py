#views.py
from django.shortcuts import render, get_object_or_404
from store.models import Product, Category
# Create your views here.
def storeHomepage(request):
    #Query all products from the Product model and store them in the products variable passed to the template.
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/storeHome.html',{'products':products, 'categories':categories})
#The about view renders the about.html template that extends the base.html template in turn.
def about(request):
    return render(request, 'store/about.html')

# Category Detail View
def category_detail(request, category_id):
    # Get the specific category by ID
    category = get_object_or_404(Category, id=category_id)
    # Get all products related to this category
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_detail.html', {'category': category, 'products': products})

# Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]  # Example related products query
 
    return render(request, 'store/product_detail.html', {'product': product, 'related_products': related_products})

def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/search_results.html', {'products': products, 'query': query, 'categories': categories})