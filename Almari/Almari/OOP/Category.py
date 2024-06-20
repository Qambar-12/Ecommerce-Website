from store.models import Category as CategoryModel, Product as ProductModel
from django.db.models import Q

class Product:
    def __init__(self, name, price, stock_quantity, description, image_url, category=None):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.description = description
        self.image_url = image_url
        self.category = category
        self.id = None


    @classmethod
    def from_model(cls, product_model):
        category = Category.from_model(product_model.category)
        product = cls(
            product_model.name,
            product_model.price,
            product_model.stock_quantity,
            product_model.description,
            product_model.image.url,
            category
        )
        product.id = product_model.id
        return product

    @classmethod
    def search(cls, query):
        products = ProductModel.objects.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query)
        )
        return [cls.from_model(product) for product in products]

    #fetches the first 4 related products from the same category, excluding the current product
    def get_related_products(self):
        related_product_models = ProductModel.objects.filter(category=self.category.model_instance).exclude(id=self.id)[:4]
        return [Product.from_model(product) for product in related_product_models]

    def __str__(self):
        return self.name
    
class Category:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.products = []                  #list of products in the category shows aggregation relationship howver at database level it is composition due to cascade delete
        self.model_instance = None

    @classmethod
    def from_model(cls, category_model):
        #the cls parameter refers to the class itself, and is used to create an instance of the class.
        category = cls(category_model.name, category_model.image_url.url)
        category.model_instance = category_model
        return category

    def load_products(self):
        self.products = [Product.from_model(product) for product in ProductModel.objects.filter(category=self.model_instance)]

    def __str__(self):
        return self.name
    
