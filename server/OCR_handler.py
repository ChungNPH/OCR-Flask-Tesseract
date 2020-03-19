import pytesseract
from PIL import Image

def handler(filename):
    return pytesseract.image_to_string(Image.open(filename))