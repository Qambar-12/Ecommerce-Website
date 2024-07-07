from Almari.OOP.Category import Category
from store.models import Category as CategoryModel
def categories(request):
    """This context processor adds the list of categories to the context of all templates."""
    category_models = CategoryModel.objects.all()
    categories = [Category.from_model(category_model) for category_model in category_models]
    return {'categories': categories}
