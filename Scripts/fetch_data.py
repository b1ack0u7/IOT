import subprocess
from datetime import date
from sql_conexion import Conexion_global
CLSS_CON=Conexion_global()
arr=[]


today = date.today()
fecha = today.strftime("%d/%m/%Y")
time = subprocess.run(['date', '+"%T"'], stdout=subprocess.PIPE)
time = str(time.stdout.decode("utf8")).replace("\"","")

text = subprocess.run(['curl', 'http://192.168.0.45/fetch'], stdout=subprocess.PIPE)
r=str(text.stdout)

arr.append(r[r.find("Agua:"):len(r)])
arr[0] = arr[0][0:arr[0].find("\\n")]
arr[0] = arr[0][arr[0].find(":")+2:len(arr[0])]

arr.append(r[r.find("Temperatura:"):len(r)])
arr[1] = arr[1][0:arr[1].find("\\n")]
arr[1] = arr[1][arr[1].find(":")+2:len(arr[1])]

#luminosidad
arr.append("luminosidad")

arr.append(fecha)
arr.append(time)

CLSS_CON.add(arr)
print("humd=%s&temp=%s"%(arr[0],arr[1]))