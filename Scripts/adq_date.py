import subprocess
from datetime import date

def get_date():
    today = date.today()
    fecha = today.strftime("%d/%m/%Y")
    time = subprocess.run(['date', '+"%T"'], stdout=subprocess.PIPE)
    time = str(time.stdout.decode("utf8")).replace("\"","")
    return fecha,time