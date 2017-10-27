#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    lista_usuarios = []

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        line = self.rfile.read().decode('utf-8').split(" ")
        usuarios = []
        if line[0] == "REGISTER":
            cliente = line[1][line[1].find(":") + 1:]
            expires = int(line[4])
            usuario = {
                "cliente": line[1][line[1].find(":") + 1:],
                "ip": self.client_address,
                "expires": expires#[:line[4].find("\")]
            }
            print(usuario)
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            expires_time = time.gmtime(int(time.time()) + expires)
            print (time.strftime("%Y-%m-%d %H:%M:%S", expires_time))
            print (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))

        #for line in self.rfile:
        #    print("El cliente nos manda ", line.decode('utf-8'))
        #    print (self.client_address)
    def register2json(self,usuario):
        #if namejson == "":
        #    namejson = "registered" + ".json"
        name_json = "registered.json"
        with open(name_json, "w") as fich_json:
            json.dump(
                self.lista,
                fich_json,
                sort_keys=True,
                indent=4, separators=(' ', ': '))



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
