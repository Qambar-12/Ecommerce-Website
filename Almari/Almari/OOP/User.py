import re
from abc import ABC, abstractmethod
#for password hashing
from django.contrib.auth.hashers import make_password, check_password
from user.models import CustomerProfile, AdminProfile
from django.contrib.auth.models import User

#Abstract class for user and its subclasses CustomerUser and AdminUser to implement abstract methods login and signup.
#Inheritance feature used
class AbstractUser(ABC):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def signup(self):
        pass

    def hash_password(self):
        return make_password(self.password)

    def check_password(self, password):
        return check_password(password, self.password)

class CustomerUser(AbstractUser):
    logged_in = False
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def validate_signup(self,confirm):
        if not self.username or not self.email or not self.password or not confirm or not self.address :
            return "All fields are required."
        if self.password and confirm != self.password:
            return "The passwords must match" 
        if self.email:
            return None
            
        if CustomerProfile.objects.filter(username=self.username).exists():
            return "Username already exists.\nPlease try another one"
        if len(self.password) < 8 or not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password):
            return "Password must be at least 8 characters long and contain a special character."
        return None

    def signup(self,confirm):
        error = self.validate_signup(confirm)
        if error:
            return error
        self.password = self.hash_password()
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        user.save()
        #filing in database
        customer = CustomerProfile(user=user,username=self.username, email=self.email, password=self.password, address=self.address)
        customer.save()
        return None
    
    def validate_login(self):
        if  self.username and  self.password:
            return None
        elif not self.username and not self.password:
            return "All fields are required."
        elif not self.username:
            return "Username is a required field"
        else:
            return "Password is a required field"
            

    def login(self, username, password):
        error = self.validate_login()
        if error:
            return None,error
        else:
            try:
                customer = CustomerProfile.objects.get(username=username)
                #if the customer is created by django admin the check_password is not called because the password directly stored in database is not hashed .
                if customer.created_by_admin:
                    if self.password == customer.password:
                        CustomerUser.logged_in = True
                        return customer, None
                    else:
                        return None, "Invalid password"
                else:
                    if check_password(password, customer.password):
                        CustomerUser.logged_in = True
                        return customer, None    
                    else:
                        return None, "Invalid password"
            except CustomerProfile.DoesNotExist:
                return None, "Username does not exist."

"""class AdminUser(AbstractUser):
    def validate_signup(self):
        if not self.username or not self.email or not self.password:
            return "All fields are required."
        if AdminProfile.objects.filter(username=self.username).exists():
            return "Username already exists."
        if len(self.password) < 8 or not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password):
            return "Password must be at least 8 characters long and contain a special character."
        return None

    def signup(self):
        error = self.validate_signup()
        if error:
            return error
        self.password = self.hash_password()
        admin = AdminProfile(username=self.username, email=self.email, password=self.password)
        admin.save()
        return None

    def login(self, username, password):
        try:
            admin = AdminProfile.objects.get(username=username)
            if self.check_password(password):
                return admin, None
            else:
                return None, "Invalid password."
        except AdminProfile.DoesNotExist:
            return None, "Username does not exist."""
