# -*- encoding: utf-8 -*-
import sys
import socket
import argparse
import time

host = ""
port = 0

argumentos = argparse.ArgumentParser(description="Banner Gabing Captura banderas de los servicios espesificados")
argumentos.add_argument("-t","--target",help="direccion ip del target a validar",dest="host",required=True)
argumentos.add_argument("-p","--port",help="Numero del puerto del servicio a validar",dest="port",type=int,required=True)
arg = argumentos.parse_args()#


def banner ():


    evilbanner = """



  /$$$$$$            /$$ /$$                               /$$   /$$
 /$$__  $$          | $$|__/                              | $$  | $$
| $$  \__/  /$$$$$$ | $$ /$$ /$$$$$$$  /$$   /$$ /$$   /$$| $$  | $$
| $$ /$$$$ |____  $$| $$| $$| $$__  $$| $$  | $$|  $$ /$$/| $$$$$$$$
| $$|_  $$  /$$$$$$$| $$| $$| $$  \ $$| $$  | $$ \  $$$$/ | $$__  $$
| $$  \ $$ /$$__  $$| $$| $$| $$  | $$| $$  | $$  >$$  $$ | $$  | $$
|  $$$$$$/|  $$$$$$$| $$| $$| $$  | $$|  $$$$$$/ /$$/\  $$| $$  | $$
 \______/  \_______/|__/|__/|__/  |__/ \______/ |__/  \__/|__/  |__/
--------------------------------------------------------------------
EvilPython : Banner Grabbing  by José Luis Galindo Herrera
email      :  galinuxh@gmail.com..
github     :  https://github.com/galinuxh/EvilPython/
    """
    print(evilbanner)


def conexion(hosts,port):
    vulnerable = False
    try:
        print("host :"+hosts+" puerto: "+str(port))
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((hosts,port))
        datos = s.recv(1024)


        print("Banner recibido del servidor remoto")
        print(datos)
        print("Verificando si es  Existe una vulnerabilidad\n")
        time.sleep(3)
        vul = open("ban.txt","r")
        #vulcon = vul.readline()
        for vul in vul:
            if datos.strip() in vul.strip():
                print("Happy Hack  *  El Servicio  es Vulnerable * \n")
                vulnerable = True
        if vulnerable == False:
            print("No se encontraron vulnerabilidades Conocidas.\n")



    except socket.error, msg: # manejo de errores de conexion con socket
        print("Error al conectar con el servidor :"+ str(msg))
        sys.exit(1)
banner()
conexion(arg.host,arg.port)
