from fastapi import APIRouter,Depends,HTTPException
from config.db import conn,get_db
from sqlalchemy import select, insert,update
from models.models import facultades
from schemas.User import Facultie
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
admin=APIRouter(prefix="/admin")


@admin.get('/faculties')

async def faculties(db:Session=Depends(get_db)):
       try:
              result= db.execute(select(facultades)).fetchall()
              list_faculties=[ facultades.to_dict(row) for row in result ]
              return JSONResponse(content={"data":list_faculties},status_code=200)
       except Exception as e:
             
              return JSONResponse(content={"error":"the faculties dont exist "},status_code=404)
       
@admin.post('/faculties')       
async def add_faculty(faculty_add:Facultie,db:Session=Depends(get_db)):
      try:
       newFaculty={"id_facultad":0,"facultad":faculty_add.faculty}
       result=db.execute(insert(facultades).values(newFaculty))
       db.commit()
       newFaculty['id_facultad']=result.lastrowid
       return {"data":newFaculty}
      except Exception as e:
           raise HTTPException(status_code=500,detail=f"error adding faculty to the database {e} ",)
      
@admin.patch('/faculties/{id_facultad}')

def updateFaculties(id_facultad:int,faculty:Facultie,db:Session=Depends(get_db)):
      try:
            facultad_update={"facultad":faculty.faculty}
            facultad_find=db.execute(select(facultades).where(facultades.id_facultad==id_facultad)).first()
            if facultad_find:
              db.execute(update(facultades).values(facultad_update).where(facultades.id_facultad==id_facultad))
              db.commit()
              return {"message":"update faculty"}
            return {"error":"the faculty don't exist"}

      except Exception as e:
            raise HTTPException(status_code=500,detail=f"error updating faculty to the database {e} ",)



            


