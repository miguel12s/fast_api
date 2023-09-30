from fastapi.responses import JSONResponse
from config.conexion import conexion
from models.admin import ModelUser
from schemas.Faculties import Faculties
bd = conexion()


class AdminController():
    def getFacultades():
        try:
            result = ModelUser.getFaculties()
            return JSONResponse(content={"data": result}, status_code=200)
        except Exception as e:
            print(e)
            return JSONResponse(content={"error": "the faculties dont exist "}, status_code=404)

    def createFacultie(facultad: Faculties):
        try:
            result = ModelUser.createFacultie(facultad)
            return JSONResponse(content={"success": "the facultie added","data":result},status_code=201)
        except Exception as e:
            print(e)
            return JSONResponse
