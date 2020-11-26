import mysql.connector

class Conexion_fetchdata():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="iot")

    def add_reg(self,val):
        sql="INSERT INTO reg (nombre, humedad, temperatura, luminosidad, fecha, hora) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor=self.mydb.cursor()
        mycursor.execute(sql,val)
        self.mydb.commit()

    def add_roc(self,val):
        sql="INSERT INTO roc (nombre, estado, fecha, hora) VALUES (%s, %s, %s, %s)"
        mycursor=self.mydb.cursor()
        mycursor.execute(sql,val)
        self.mydb.commit()