import sys
from sql_conexion import Conexion_fetchdata
CLSS_CON=Conexion_fetchdata()

arr=[]
ars=[]
name = sys.argv[1]
type_op = sys.argv[2]

arr=CLSS_CON.fetch(type_op,name,name)
for i in range(0,len(arr)):
    tmp=",".join(arr[i])
    ars.append(tmp)

out=";".join(ars)
print(out)