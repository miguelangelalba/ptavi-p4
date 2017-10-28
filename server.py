#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    users = {}
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        line = self.rfile.read().decode('utf-8').split(" ")
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
        del_users = []
        if line[0] == "REGISTER":
            cliente = line[1][line[1].find(":") + 1:]
            expires_time = time.gmtime(int(time.time()) + int(line[4]))
            usuario = {
                "address": self.client_address[0],
                "expires":time.strftime("%Y-%m-%d %H:%M:%S",expires_time)
                }
            self.users[cliente] = usuario

            if int(line[4]) == 0:
                del self.users[cliente]
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        for user in self.users:
            if self.users[user]["expires"] < time_now:
                del_users.append(user)
        for user in del_users:
            del self.users[user]

        self.register2json()


    def register2json(self):

        with open("registered.json", "w") as fich_json:
            json.dump(
                self.users,
                fich_json,
                sort_keys=True,
                indent=4, separators=(',', ': '))

    @classmethod #Gracias a esto puedo acceder al método
    def json2registered (self):
        try:
            fich_json = open("registered.json", "r")
            self.users = json.load(fich_json)
            print ("lo he pillado")
            print (self.users)
        except:
            self.users = {}

if __name__ == "__main__":

    try:
        port = int(sys.argv[1])
    except (IndexError):
        sys.exit("Usage:port")

    SIPRegisterHandler.json2registered()
    serv = socketserver.UDPServer(('', port), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()

    except KeyboardInterrupt:
        print("Finalizado servidor")
