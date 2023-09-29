from config.conexion import conexion

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
