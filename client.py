#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
#SERVER = 'localhost'
#PORT = 6001
#LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
def comunication (server,port,line):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((SERVER, PORT))
        print("Enviando:", line)
        info = line.split(" ")
        msg_to_send = "REGISTER " + "sip:" + info[1] +" SIP/2.0"
        my_socket.send(bytes(msg_to_send, 'utf-8') + b'\r\n\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))

    print("Socket terminado.")


if __name__ == '__main__':

    try:
        SERVER = sys.argv[1]
        PORT = int(sys.argv[2])
        line = " ".join(sys.argv[3:])

    except (IndexError):
        sys.exit("Usage: server,port,line")

    comunication(SERVER,PORT,line)
