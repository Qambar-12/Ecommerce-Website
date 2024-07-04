# checkout.py

import re

class ShippingValidator:
    def __init__(self, full_name, email, address1, city, country, zipcode=None):
        self.full_name = full_name
        self.email = email
        self.address1 = address1
        self.city = city
        self.country = country
        self.zipcode = zipcode

    def validate_email(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, self.email) is not None

    def validate_zipcode(self):
        if self.zipcode:
            return self.zipcode.isdigit() and len(self.zipcode) in [5, 6, 7, 10]
        return True  # Zipcode is optional

    def validate(self):
        return all([
            self.full_name,
            self.email and self.validate_email(),
            self.address1,
            self.city,
            self.country,
            self.validate_zipcode()
        ])


class PaymentValidator:
    def __init__(self, card_number, cardholder_name, cvv):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.cvv = cvv

    def validate_card_number(self):
        card_regex = r'^\d{13,19}$'
        return re.match(card_regex, self.card_number) is not None

    def validate_cvv(self):
        return self.cvv.isdigit() and len(self.cvv) in [3, 4]

    def validate(self):
        return all([
            self.card_number and self.validate_card_number(),
            self.cardholder_name,
            self.cvv and self.validate_cvv()
        ])
