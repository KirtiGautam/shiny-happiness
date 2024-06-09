from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from PIL import Image
from db.models.solution_step import SolutionStep
import io

router = APIRouter()

@router.post("/upload", response_model=List[SolutionStep])
async def upload_image(image: UploadFile = File(...)):
    try:
        # Read the uploaded image file
        contents = await image.read()
        image = Image.open(io.BytesIO(contents))

        # Process the image (this is where you would add your processing logic)
        # For demonstration, we'll just return dummy solution steps
        solution_steps = [
            SolutionStep(step_number= 1, title="Step 1", description="This is the first step."),
            SolutionStep(step_number= 2, title="Step 2", description="This is the second step."),
            SolutionStep(step_number= 3, title="Step 3", description="This is the third step.")
        ]

        return solution_steps

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
