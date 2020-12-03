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

text = subprocess.run(['curl', '-m', '5','http://javieriot.dyndns.org/fetch'], stdout=subprocess.PIPE)
r=str(text.stdout)

arr.append("Javier")
arr.append("N/D")
arr.append("N/D")

arr.append(r[r.find("Luz:"):len(r)])
arr[3] = arr[3][0:arr[3].find("\\n")]
arr[3] = arr[3][arr[3].find(":")+2:len(arr[3])]

arr.append("N/D")

td.join()
arr.append(fecha)
arr.append(time.rstrip("\n"))

if(arr[1] == "" and arr[2] == ""):
    print("lumi=N/C")
else:
    CLSS_CON.add_reg(arr)
    print("lumi=%s"%(arr[3]))