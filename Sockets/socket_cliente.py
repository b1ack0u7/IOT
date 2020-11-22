import socket
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def send_data(op):
    if(op == 1): message="off"
    if(op == 2): message="on"
    if(op == 3): message="quit"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1",4444))
    sock.send(message.encode())
    
    print("[ok]: Solicitud enviada\n")
    pausa=str(input("Enter para continuar"))

def menu():
    op=0
    while True:
        clear()
        print("1) Apagar riego")
        print("2) Encender riego")
        print("3) Salir\n")
        op=int(input("Ingrese su opcion: "))
        if(op == 3): 
            send_data(op)
            break
        else: send_data(op) 

menu()
