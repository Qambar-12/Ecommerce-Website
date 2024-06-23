from Almari.OOP.Category import Category
from store.models import Category as CategoryModel
from django.shortcuts import render, get_object_or_404
def categories(request):
    categories = CategoryModel.objects.all()
    return {'categories': categories}
def category_detail(request, category_id):
    category_model = get_object_or_404(CategoryModel, id=category_id)
    category = Category.from_model(category_model)
    category.load_products()
    return render(request, 'store/category_detail.html', {'category': category, 'products': category.products})
