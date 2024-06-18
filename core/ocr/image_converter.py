import pytesseract
from PIL.Image import Image
from pdf2image import convert_from_path
from typing import List

# Path to tesseract executable (update this path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


def create_image_from_pdf(path: str) -> List[Image]:
    # Convert PDF to images
    pages = convert_from_path(path, 300)
    return pages
