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
def comunication (server,port,sip_type,name,expires_value):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((server, port))
        #print("Enviando:", line)
        #info = line.split(" ")
        msg_to_send = "REGISTER " + "sip:" + name +" SIP/2.0" + "\r\n"
        msg_to_send = msg_to_send + " Expires: " + expires_value + "\r\n"
        my_socket.send(bytes(msg_to_send, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))

    print("Socket terminado.")


if __name__ == '__main__':

    if len(sys.argv) != 6:
        sys.exit("Usage: client.py ip puerto register sip_address " + \
        "expires_value")
    try:
        server = sys.argv[1]
        port = int(sys.argv[2])
        sip_type = sys.argv[3]
        name = sys.argv[4]
        expires_value = sys.argv[5]
        #line = " ".join(sys.argv[3:])

    except (IndexError):
        sys.exit("Usage: server,port,line")

    comunication(server,port,sip_type,name,expires_value)
