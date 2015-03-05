# -*- coding: utf-8 -*-
import SocketServer
import json
import string

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        print "Client connected: " + self.ip + ":" + str(self.port) 

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            
            payload = json.dumps(received_string)
            message = payload.split(' ')    
            # fant ingen switch().....
            if (message[1] == "login"):
                pass #set username

            elif (message[1] == "logout"):
                print "Client disconnected: "+ self.ip + ":" + str(self.port) 
                pass # selfdestruct!

            elif (message[1] == "names"):
                pass # get a list of names

            elif (message[1] == "msg"):
                pass # broadcast message

            elif (message[1] == "help"):
                pass # make a helpfull guide
            else:
                pass #command not found error message

            # TODO: Add handling of received payload from client


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
