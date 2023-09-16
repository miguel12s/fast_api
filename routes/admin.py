from fastapi import APIRouter,Depends,HTTPException
from config.db import conn
from sqlalchemy import select, insert,update
from models.models import Faculties
from schemas.User import Facultie
from fastapi.responses import JSONResponse
admin=APIRouter(prefix="/admin")


@admin.get('/faculties')

async def faculties():
       try:
              result= conn.execute(select(Faculties)).fetchall()
              list_faculties=[ Faculties.to_dict(row) for row in result ]
              return JSONResponse(content={"data":list_faculties},status_code=200)
       except Exception as e:
             
              return JSONResponse(content={"error":"the faculties dont exist"},status_code=404)
       
@admin.post('/faculties')       
async def add_faculty(faculty_add:Facultie):
      try:
       newFaculty={"id_facultad":0,"facultad":faculty_add.faculty}
       result=conn.execute(insert(Faculties).values(newFaculty))
       conn.commit()
       newFaculty['id_facultad']=result.lastrowid
       return {"data":newFaculty}
      except Exception as e:
           raise HTTPException(status_code=500,detail=f"error adding faculty to the database {e} ",)
      
@admin.patch('/faculties/{id_facultad}')

def updateFaculties(id_facultad:int,faculty:Facultie):
      try:
            facultad_update={"facultad":faculty.faculty}
            facultad_find=conn.execute(select(Faculties).where(Faculties.id_facultad==id_facultad)).first()
            if facultad_find:
              conn.execute(update(Faculties).values(facultad_update).where(Faculties.id_facultad==id_facultad))
              conn.commit()
              return {"message":"update faculty"}
            return {"error":"the faculty don't exist"}

      except Exception as e:
            raise HTTPException(status_code=500,detail=f"error updating faculty to the database {e} ",)



            


