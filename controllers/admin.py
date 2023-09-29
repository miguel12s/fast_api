from fastapi.responses import JSONResponse
from config.conexion import conexion
from models.admin import ModelUser
bd=conexion()

def getFacultades():
     try:
              result=ModelUser.getFaculties()
              return JSONResponse(content={"data":result},status_code=200)
     except Exception as e:
              print(e)
              return JSONResponse(content={"error":"the faculties dont exist "},status_code=404)