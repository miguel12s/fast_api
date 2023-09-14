from typing import Optional
from pydantic import BaseModel



class Program(BaseModel):
    id:Optional[int]=1
    program:str

