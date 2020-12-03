import mysql.connector
msc=[]
data=[]

class Conexion_fetchdata():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="iot")

    def fetch(self, db_type, op_type, data_type):
        if(db_type == "cons_reg"):
            if(op_type == "todos" or op_type == "all"): query = "SELECT * FROM reg"
            else: query = "SELECT * FROM reg WHERE nombre ='%s'"%(data_type)
        else:
            if(op_type == "todos" or op_type == "all"): query = "SELECT * FROM roc"
            else: query = "SELECT * FROM roc WHERE nombre ='%s'"%(data_type)

        msc.clear()
        data.clear()

        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for i in range(0,len(myresult)):
            for z in range(0,len(myresult[0])):
                msc.append(str(myresult[i][z]).replace(" ","_"))
                
            data.insert(i, msc.copy())
            msc.clear()
        return data


