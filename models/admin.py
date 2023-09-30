from config.conexion import conexion
from schemas.Faculties import Faculties

bd = conexion()


class ModelUser():
    def getFaculties():
        cursor = bd.cursor()
        cursor.execute("select * from facultades")
        result = cursor.fetchall()
        content = {}
        facultades = []
        for data in result:
            content = {
                "id_facultad": data[0],
                "facultad": data[1]

            }
            facultades.append(content)
            content = {}

        return facultades
    
    def createFacultie(facultie:Faculties):
        try:
            cursor=bd.cursor()
            cursor.execute("insert into facultades (facultad) values(%s)",(facultie.faculty,))
            bd.commit()
            return facultie
        except (Exception) as e:
            print(e)
            return {"error":"the facultie existed in the system"}