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

text = subprocess.run(['curl', '-m', '6','http://jonhrh.ddns.net/fetch'], stdout=subprocess.PIPE)
r=str(text.stdout)

arr.append("Johna")
arr.append("N/D")
arr.append("N/D")

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
    print("lumi=%s"%(arr[1]))