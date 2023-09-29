import mysql.connector

def conexion():
        try:
            mybd= mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_definitiva"
            )
            return mybd
        except (Exception) as e:
            print(e)
          