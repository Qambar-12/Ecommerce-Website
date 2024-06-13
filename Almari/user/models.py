from django.db import models
from django.contrib.auth.models import User
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

class AdminProfile(UserProfile):
    """
    Represents an admin profile table in the e-commerce store database.
    """
    pass