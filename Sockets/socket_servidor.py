import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4444
server.bind(("192.168.0.35",port))
server.listen(4)
print("[!]: Socket iniciado")

while(True):
    serverSock, clienteAddr = server.accept()    
    message = serverSock.recv(1024).decode("utf-8")
    if(message == "off" or message == "apagar"):
        tmp=subprocess.run(["curl", "-s", "192.168.0.45/water_off"], stdout=subprocess.PIPE)
        print(tmp.stdout)
    if(message == "on" or message == "encender"):
        tmp=subprocess.run(["curl", "-s", "192.168.0.45/water_on"], stdout=subprocess.PIPE)
        print(tmp.stdout)
    if(message == "exit" or message == "salir" or message == "quit"):
        print("[!]: Saliendo")
        break
        
serverSock.close()
server.close()
