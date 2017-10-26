#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    usuarios = []

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        line = self.rfile.read().decode('utf-8').split(" ")
        if line[0] == "REGISTER":
            usuario = {
                "cliente": line[1][line[1].find(":")+ 1:],
                "ip": self.client_address
            }
            print(usuario)
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

        #for line in self.rfile:
        #    print("El cliente nos manda ", line.decode('utf-8'))
        #    print (self.client_address)

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    try:
        PORT = int(sys.argv[1])
    except (IndexError):
        sys.exit("Usage:port")

    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
