import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import base64

def generate_image_captcha():
    """Generate a random image captcha and return the image and the text of the captcha."""
    # Generate a random string of 6 characters (letters and digits)
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Create an image with white background
    image = Image.new('RGB', (150, 50), color=(255, 255, 255))

    # Load a font
    font = ImageFont.truetype("arial.ttf",20)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Add noise
    for _ in range(random.randint(150, 200)):
        draw.point((random.randint(0, 150), random.randint(0, 50)), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    text_x = random.randint(0,50)
    text_y = random.randint(0,10)
    text_position = (text_x, text_y)

    # Draw the text
    draw.text(text_position, captcha_text, font=font, fill=(0, 0, 0))

    # Add some lines for more noise
    for _ in range(10):
        draw.line((random.randint(0, 150), random.randint(0, 50), random.randint(0, 150), random.randint(0, 50)), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=1)

    # Apply a filter to distort the image
    image = image.filter(ImageFilter.GaussianBlur(1))

    # Save the image to a byte buffer
    buffered = BytesIO()
    image.save(buffered, format="JPEG")

    # Encode the image to base64
    captcha_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return captcha_image, captcha_text

