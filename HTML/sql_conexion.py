import mysql.connector

class Conexion_global():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="iot")

    def add(self,val):
        sql="INSERT INTO reg (humedad, temperatura, luminosidad, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
        mycursor=self.mydb.cursor()
        mycursor.execute(sql,val)
        self.mydb.commit()
