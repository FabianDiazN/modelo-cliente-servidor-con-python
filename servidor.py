import socket
import os
os.system("")

class style():
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    
host="LocalHost"
puerto=5656
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,puerto))
server.listen(1)
print(""" 
 _____                     _      _              
/  ___|                   (_)    | |             
\ `--.   ___  _ __ __   __ _   __| |  ___   _ __ 
 `--. \ / _ \| '__|\ \ / /| | / _` | / _ \ | '__|
/\__/ /|  __/| |    \ V / | || (_| || (_) || |   
\____/  \___||_|     \_/  |_| \__,_| \___/ |_| 
""")
print("Esperando conexiones")
active, addr=server.accept()
while True:
    recibido=active.recv(1024)
    print(style.YELLOW+"Cliente:",recibido.decode(encoding="ascii",errors="ignore"))
    enviar=input(style.GREEN+"Servidor:")
    active.send(enviar.encode(encoding="ascii",errors="ignore"))
active.close()








