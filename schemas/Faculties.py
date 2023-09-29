from pydantic import BaseModel
from typing import Optional

class Faculties(BaseModel):
    id:Optional[int]
    faculty:str