import re

class ShippingValidator:
    def __init__(self, email = '', address1='',  zipcode=''):
        self.email = email  
        self.address1 = address1
        self.zipcode = zipcode


    def validate(self):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$", self.email):
            return False, "Invalid email address."
        if self.zipcode and (not self.zipcode.isdigit() or len(self.zipcode) != 5):
            return False, "Invalid zipcode (should be 5 digits)."
        if self.address1 and len(self.address1) < 5:
            return False, "Address should be at least 5 characters (meaningful)"
        return True, "Shipping details are valid."

class PaymentValidator:
    def __init__(self, card_number, cardholder_name, cvv):
        self.card_number = card_number or ''
        self.cardholder_name = cardholder_name or ''
        self.cvv = cvv or ''

    def validate(self):
        if not self.card_number.isdigit() or len(self.card_number) not in range(13, 17):
            return False, "Invalid card number.Card number should be between 13 and 16 digits."
        if not self.cvv.isdigit() or len(self.cvv) != 3:
            return False, "Invalid CVV (should be 3 digits)."
        return True, "Payment details are valid."
