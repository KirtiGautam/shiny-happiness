from typing import List
import pytesseract
import mimetypes
import logging
from PIL import Image
from logging.config import dictConfig

from core.ocr.image_converter import create_image_from_pdf
from server.assertions import assert_valid
from server.log import LogConfig

dictConfig(LogConfig().dict())

logger = logging.getLogger('mycoolapp')


class Extractor:
    __path: str
    __extension: str
    __valid_extensions = ['.jpg', '.png', '.jpeg', '.pdf']


    def __init__(self, *, path: str) -> None:
        self.__path = path
        file_type = mimetypes.guess_type(path)[0]
        self.__extension = mimetypes.guess_extension(file_type)

        # Check if the file extension is valid
        print(f'File extension: {self.__extension}')
        assert_valid(self.__extension in self.__valid_extensions, 'Invalid file extension')

    def __extract(self, *, pages: List[Image.Image]) -> None:
        text = ''
        for page in pages:
            text += pytesseract.image_to_string(page)

        return text

    def extract(self) -> str:
        image_path = self.__path

        if self.__extension == '.pdf':
            pages = create_image_from_pdf(image_path)
        else:
            pages = [Image.open(image_path)]

        extracted_text = self.__extract(pages=pages)

        return extracted_text
