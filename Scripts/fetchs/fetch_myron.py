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

text = subprocess.run(['curl', '-m', '6','http://mcmb.ddns.net/fetch'], stdout=subprocess.PIPE)
r=str(text.stdout)

arr.append("Myron")
arr.append(r[r.find("Humedad:"):len(r)])
arr[1] = arr[1][0:arr[1].find("\\n")]
arr[1] = arr[1][arr[1].find(":")+2:len(arr[1])]

arr.append(r[r.find("Temperatura:"):len(r)])
arr[2] = arr[2][0:arr[2].find("\\n")]
arr[2] = arr[2][arr[2].find(":")+2:len(arr[2])]

arr.append(r[r.find("Luz:"):len(r)])
arr[3] = arr[3][0:arr[3].find("\\n")]
arr[3] = arr[3][arr[3].find(":")+2:len(arr[3])]
if(arr[3] == "0"): arr[3] = "No"
else: arr[3] = "Si"

arr.append("N/D")

td.join()
arr.append(fecha)
arr.append(time.rstrip("\n"))

if(arr[1] == "" and arr[2] == ""):
    print("humd=N/C&temp=N/C&lumi=N/C")
else:
    CLSS_CON.add_reg(arr)
    print("humd=%s&temp=%s&lumi=%s"%(arr[1],arr[2],arr[3]))