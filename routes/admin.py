from fastapi import APIRouter
from controllers.admin import getFacultades
from typing import List
from schemas.Faculties import Faculties
admin=APIRouter(prefix="/admin")


@admin.get('/faculties',response_model=List[Faculties])

async def faculties():
      return getFacultades()
       
            


