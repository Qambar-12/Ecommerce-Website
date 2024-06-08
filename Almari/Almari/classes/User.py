from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, username='', email='', password=''):
        self.username = username
        self.email = email
        self.password = password
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def signup(self):
        pass
class Admin(User):
    pass
class Customer(User):
    def __init__(self, username, email, password, address, phone):
        super().__init__(username, email, password)
        self.address = address
        self.phone = phone
    def login(self):
        pass        
class Seller(User):
    pass