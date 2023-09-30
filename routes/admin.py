from fastapi import APIRouter
from controllers.admin import AdminController
from typing import List
from schemas.Faculties import Faculties
admin=APIRouter(prefix="/admin")


@admin.get('/faculties',response_model=List[Faculties],status_code=200)

async def faculties():
      return  AdminController.getFacultades()

@admin.post('/faculties',status_code=201)

async def createFaculties(facultie:Faculties):
      return AdminController.createFacultie(facultie)


       
            


