# user/utils.py
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
# for encoding the image data to be used in HTML
import base64

def generate_image_captcha():
    # Generate a random string of 6 uppercase letters and digits for the CAPTCHA text
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    # Create a new image with white background, 100 pixels wide and 40 pixels tall
    image = Image.new('RGB', (100, 40), color = (255, 255, 255))
    
    # Load the default font
    font = ImageFont.load_default()
    
    # Create a drawing object to modify the image
    draw = ImageDraw.Draw(image)
    
    # Draw the CAPTCHA text on the image at position (10, 10) with black color
    draw.text((10, 10), captcha_text, font=font, fill=(0, 0, 0))
    
    # Create a BytesIO object to hold the image data in memory
    buffered = BytesIO()
    
    # Save the image to the BytesIO object in JPEG format
    image.save(buffered, format="JPEG")
    
    # Encode the image data in base64 to include it in an HTML img tag
    captcha_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    # Return the base64-encoded image and the CAPTCHA text
    return captcha_image, captcha_text
