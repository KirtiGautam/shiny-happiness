from datetime import datetime
from fastapi import UploadFile
import logging
import os
import shutil

logger = logging.getLogger(__name__)


os.makedirs('/tmp/uploads', exist_ok=True)

class Processor:
    __file: UploadFile

    def __init__(self, file: UploadFile):
        self.__file = file

    def process(self) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_location = os.path.join('/tmp/uploads', f'{timestamp}_{self.__file.filename}')

        with open(file_location, 'wb') as buffer:
            shutil.copyfileobj(self.__file.file, buffer)

        return file_location
