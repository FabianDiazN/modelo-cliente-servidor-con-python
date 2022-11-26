import socket
import os
os.system("")

class style():
    GREEN = '\033[32m'
    YELLOW = '\033[33m'

host="LocalHost"
puerto=5656
objsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket.connect((host,puerto))
print("cliente ejecutado")
print("""
 _____  _  _               _          
/  __ \| |(_)             | |         
| /  \/| | _   ___  _ __  | |_   ___  
| |    | || | / _ \| '_ \ | __| / _ \ 
| \__/\| || ||  __/| | | || |_ |  __/ 
 \____/|_||_| \___||_| |_| \__| \___|
""")
while True:
    enviar=input(style.YELLOW+"Cliente: ")
    objsocket.send(enviar.encode(encoding="ascii",errors="ignore"))
    recibido=objsocket.recv(1024)
    print(style.GREEN+"Servidor:",recibido.decode(encoding="ascii",errors="ignore"))
objsocket.close()




