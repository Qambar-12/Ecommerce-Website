from Almari.OOP.Category import Category
from store.models import Category as CategoryModel
def categories(request):
    
    category_models = CategoryModel.objects.all()
    categories = [Category.from_model(category_model) for category_model in category_models]
    return {'categories': categories}
