from django.core.mail import send_mail
from django.conf import settings
import time
def send_verification_email(user_email, verification_code):
    """Send verification email to user with the verification code. Return the start time of the email sending process.
    The start time is used to calculate the time taken to verify the code. If the time taken is more than 60 seconds"""
    subject = 'Your Verification Code'
    message = f'Almari ki Chaabi: {verification_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
    return time.time()