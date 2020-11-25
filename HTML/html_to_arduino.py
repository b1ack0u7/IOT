# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:13:35 2020

@author: axelm
"""
arr=[]


def output_file():
    arch = open("Arduino_html.txt","w")
    msc = "String ptr = " + arr[0]
    arch.write(msc +"\n")
    
    for i in range(1,len(arr)):
        msc = "ptr += " + arr[i]
        arch.write(msc + "\n")
    arch.write("return ptr;")
    arch.close()
        

def load_file():
    text = str(input("Ingrese el nombre del archivo: "))
    arch = open(text,"r")
    lines = arch.readlines()
    arch.close()
    
    for i in range(0,len(lines)):
        if (str(lines[i]) != "\n"):
            msc = ' '.join(lines[i].split())
            if (lines[i].find("##VAR") != -1):
                msc = msc + ";"
            else:
                msc = msc.replace("\"", "\\\"")
                msc = "\"" + msc + "\\n" + "\"" +";"
            
            arr.append(msc)
        else:
            pass
        
    output_file()

load_file()
print("Archivo convertido")
