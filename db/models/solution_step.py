from pydantic import BaseModel

class SolutionStep(BaseModel):
    step_number: int
    title: str
    description: str
    image_url: str = None
