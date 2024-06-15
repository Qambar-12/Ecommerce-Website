# categories.py

class Product:
    def __init__(self, name, price, stock_quantity, description, image_url, category):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.description = description
        self.image_url = image_url
        self.category = category

    def __str__(self):
        return self.name

class Category:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        return self.name
