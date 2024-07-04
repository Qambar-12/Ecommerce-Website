import re

class ShippingValidator:
    def __init__(self, full_name, email, address1, city, zipcode, country):
        self.email = email or ''
        self.zipcode = zipcode or ''

    def validate(self):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$", self.email):
            return False, "Invalid email address."
        if not self.zipcode.isdigit() or len(self.zipcode) != 5:
            return False, "Invalid zipcode."
        return True, "Shipping details are valid."

class PaymentValidator:
    def __init__(self, card_number, cardholder_name, cvv):
        self.card_number = card_number or ''
        self.cardholder_name = cardholder_name or ''
        self.cvv = cvv or ''

    def validate(self):
        if not self.card_number.isdigit() or len(self.card_number) not in [13, 16]:
            return False, "Invalid card number."
        if not self.cvv.isdigit() or len(self.cvv) != 3:
            return False, "Invalid CVV."
        return True, "Payment details are valid."
