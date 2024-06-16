# categories.py
from store.models import Category as CategoryModel, Product as ProductModel
from django.db.models import Q

class Product:
    def __init__(self, name, price, stock_quantity, description, image_url, category):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.description = description
        self.image_url = image_url
        self.category = category

    def save_to_db(self):
        product_model = ProductModel(
            name=self.name,
            price=self.price,
            stock_quantity=self.stock_quantity,
            description=self.description,
            image=self.image_url,
            category=self.category.model_instance
        )
        product_model.save()
        self.id = product_model.id
        return product_model

    def __str__(self):
        return self.name
    
    @classmethod
    def search(cls, query):
        # Perform a search query on the Product model
        products = ProductModel.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return products
    
    def get_related_products(self):
        # Fetch related products from the same category, excluding this product
        related_product_models = ProductModel.objects.filter(category=self.category.model_instance).exclude(id=self.id)[:4]
        related_products = []
        for related_product_model in related_product_models:
            related_product = Product(
                related_product_model.name, related_product_model.price,
                related_product_model.stock_quantity, related_product_model.description,
                related_product_model.image.url, self.category
            )
            related_product.id = related_product_model.id
            related_products.append(related_product)
        return related_products

class Category:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.products = []
        self.model_instance = None

    def save_to_db(self):
        category_model = CategoryModel(name=self.name, image_url=self.image_url)
        category_model.save()
        self.model_instance = category_model
        return category_model

    def add_product(self, product):
        product.category = self
        self.products.append(product)
        product.save_to_db()

    def search_products(self, query):
        # Search products within this category
        products = Product.search(query).filter(category=self.model_instance)
        return products
    
    def __str__(self):
        return self.name
