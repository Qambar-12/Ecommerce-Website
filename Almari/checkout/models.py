from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ShippingAddress(models.Model):
	"""
	Represents a shipping address table in the e-commerce store database.
	"""
	#indirectly also related to customer table
	username = models.CharField(max_length=100,default="")
	shipping_full_name = models.CharField(max_length=255)
	shipping_email = models.CharField(max_length=255)
	shipping_address1 = models.CharField(max_length=255)
	shipping_address2 = models.CharField(max_length=255, null=True, blank=True)
	shipping_city = models.CharField(max_length=255)
	shipping_state = models.CharField(max_length=255, null=True, blank=True)
	shipping_zipcode = models.CharField(max_length=255, null=True, blank=True)
	shipping_country = models.CharField(max_length=255)
	class Meta:
		verbose_name_plural = "Shipping Address"
	def __str__(self):
		return f'Shipping Address - {str(self.shipping_full_name)}'    

class PaymentDetails(models.Model):
	"""
	Represents a payment details table in the e-commerce store database.
	"""
	username = models.CharField(max_length=100,default="")
	card_number = models.CharField(max_length=255)
	cardholder_name = models.CharField(max_length=255)
	cvv = models.CharField(max_length=255)
	class Meta:
		verbose_name_plural = "Payment Details"
	def __str__(self):
		return f'Payment Details - {str(self.cardholder_name)}'