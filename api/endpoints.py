from fastapi import APIRouter, UploadFile
from typing import List

from core.files.processor import Processor
from core.ocr.extract import Extractor
from db.models.solution_step import SolutionStep

router = APIRouter()

@router.post("/extract_text")
async def upload_image(image: UploadFile) -> List[SolutionStep]:

    # Save the file to disk
    processor = Processor(file=image)
    path = processor.process()

    # Extract text from the image
    extractor = Extractor(path=path)
    extracted_text = extractor.extract()

    extracted_lines = extracted_text.split('\n')

    solution_steps = []
    for i, line in enumerate(extracted_lines):
        solution_steps.append(SolutionStep(step_number=i+1, title=f"Step {i+1}", description=line))

    return solution_steps
