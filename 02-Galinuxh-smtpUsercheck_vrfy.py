# -*- encoding: utf-8 -*-
import sys
import socket
import argparse
import time

host = ""
port = 0

argumentos = argparse.ArgumentParser(description="Enumeracion de usuarios por medio del servicio de SMTP  utilizando VRFY")
argumentos.add_argument("-t","--target",help="direccion ip del target a validar",dest="host",required=True)
argumentos.add_argument("-p","--port",help="Numero del puerto del servicio a validar",dest="port",type=int,default=25)
argumentos.add_argument("-u","--userlist",help="Archivo de usuarios",dest="userlist",required=True)
argumentos.add_argument("-v","--vervose",help="Salida con intentos  fallidos",dest="vervose",action="store_true",default=False)


arg = argumentos.parse_args()#


def banner ():


    evilbanner = """

 ██████╗  █████╗ ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██╔════╝ ██╔══██╗██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
██║  ███╗███████║██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝
██║   ██║██╔══██║██║     ██║██║╚██╗██║██║   ██║ ██╔██╗
╚██████╔╝██║  ██║███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
----------------------------------------------------------
EvilPython : Enumeracion de Usarios por SMTP - VRFY
Autor      : José Luis Galindo Herrera
email      : galinuxh@gmail.com..
github     : https://github.com/galinuxh/EvilPython/
    """
    print(evilbanner)


def bruteforceSMTP(hosts,port,userlist):
        print("host :"+hosts+" puerto: "+str(port))
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((hosts,port))
        datos = s.recv(1024)
        usercheck = open(userlist,"r")
        print("Banner recibido del servidor remoto")
        print(datos)
        try:
            #s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #s.connect((hosts,port))
            for user in usercheck:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((hosts,port))
                #check = s.recv(1024)
                s.send("VRFY "+user)
                time.sleep(1)
                check = s.recv(1024)
                #print(check)
                if ("252") in check:
                    print("[+] Usuario Activo   : "+user)
                elif arg.vervose == True:
                    print("[-] Usuario Inactivo : "+user)
                else:
                    s.close()
                    pass

        except:
            print("Error  A conectar con el servidor")
            pass
banner()
bruteforceSMTP(arg.host,arg.port,arg.userlist)
