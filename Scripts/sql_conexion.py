import mysql.connector

class Conexion_fetchdata():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="iot")

    def add(self,table,val):
        sql=""
        if(table == "fetch" or table == "fetch_data"):
            sql="INSERT INTO reg (humedad, temperatura, luminosidad, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
        if(table == "regado" or table == "rociado"):
            sql="INSERT INTO reg_rociado (ID, temperatura, luminosidad, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
        mycursor=self.mydb.cursor()
        mycursor.execute(sql,val)
        self.mydb.commit()
