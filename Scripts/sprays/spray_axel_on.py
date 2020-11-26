import subprocess
import threading
from sql_conexion import Conexion_fetchdata
from adq_date import get_date

CLSS_CON=Conexion_fetchdata()
arr=[]
fecha=""
time=""

def date():
    global fecha,time
    fecha,time=get_date()

td=threading.Thread(target=date)
td.start()

text = subprocess.run(['curl', 'http://192.168.0.45/water_on'], stdout=subprocess.PIPE)
td.join()
arr.append("Axel")
arr.append("Encendido")
arr.append(fecha)
arr.append(time.rstrip("\n"))

CLSS_CON.add_roc(arr)