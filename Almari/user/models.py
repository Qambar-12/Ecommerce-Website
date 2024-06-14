from django.db import models
from django.contrib.auth.models import User
from store.models import Category
# Create your models here.
class UserProfile(models.Model):
    """
    Represents a user profile table in the e-commerce store database.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #unique=True specifies that the username and email fields must be unique.
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    #stores hashed passwords
    password = models.CharField(max_length=20)
    created_by_admin = models.BooleanField(default=False)
    def __str__(self):
        return f'Username : {self.username}'

class CustomerProfile(UserProfile):
    """
    Represents a customer profile table in the e-commerce store database.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    def __str__(self):
        return f"Username: {self.username}\nEmail: {self.email}\nName: {self.first_name + self.last_name}\nAddress: {self.address}"

class SellerProfile(UserProfile):
    """
    Represents a seller profile table in the e-commerce store database.
    """
    company_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    bank_account_number = models.CharField(max_length=100, unique=True)
    bank_name = models.CharField(max_length=100)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_orders = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name='sellers')

    def __str__(self):
        return f"Company Name: {self.company_name}\nUsername: {self.username}\nEmail: {self.email}\nContact: {self.contact_number}\nAddress: {self.address}\nTotal Sales: {self.total_sales}\nTotal Orders: {self.total_orders}"
