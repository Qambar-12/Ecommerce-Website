from django.db import models

# Create your models here.

# Categories of Products
#In Django, each model automatically gets an id field as a primary key unless explicitly specified otherwise.
class Category(models.Model):
    """
    Represents a category table  in the e-commerce store database.
    """
    name = models.CharField(max_length=100)
    #string representation of the object returned by the __str__ method when querying the Category model.
    def __str__(self):
        return self.name
    class Meta:
        """
        Provides additional options for the Category model.
        """
        verbose_name_plural = "categories"
class Product(models.Model):
    """
    Represents a product table in the e-commerce store database.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #PositiveIntegerField is used to store positive integers.
    stock_quantity = models.PositiveIntegerField(default=0)
    #ForeignKey is used to establish a many-to-one relationship between the Product and Category models.
    #on_delete=models.CASCADE specifies that when a Category is deleted, all associated Products will be deleted as well.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #blank=True specifies that the field is not required.
    description = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to='uploads/products/')
    #string representation of the object returned by the __str__ method when querying the Product model.
    def __str__(self):
        return self.name  


	