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

text = subprocess.run(['curl', '-m', '5', 'http://192.168.0.45/fetch'], stdout=subprocess.PIPE)
r=str(text.stdout)
r_check=r.replace("'","").replace("b","")

if(r_check == ""):
    print("humd=N/C&temp=N/C&lumi=N/C")
else:
    arr.append("Axel")
    arr.append(r[r.find("Agua:"):len(r)])
    arr[1] = arr[1][0:arr[1].find("\\n")]
    arr[1] = arr[1][arr[1].find(":")+2:len(arr[1])]

    arr.append(r[r.find("Temperatura:"):len(r)])
    arr[2] = arr[2][0:arr[2].find("\\n")]
    arr[2] = arr[2][arr[2].find(":")+2:len(arr[2])]

    arr.append(r[r.find("Luminosidad:"):len(r)])
    arr[3] = arr[3][0:arr[3].find("\\n")]
    arr[3] = arr[3][arr[3].find(":")+2:len(arr[3])]
    if(arr[3] == "0"): arr[3] = "No"
    else: arr[3] = "Si"

    arr.append("N/D")

    td.join()
    arr.append(fecha)
    arr.append(time.rstrip("\n"))

    CLSS_CON.add_reg(arr)
    print("humd=%s&temp=%s&lumi=%s"%(arr[1],arr[2],arr[3]))