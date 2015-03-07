# -*- coding: utf-8 -*-
import SocketServer
import json
import time
import datetime

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
        username = self.ip
        ts = time.time()

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            payload = json.loads(received_string)
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            if (payload['request'] == "login"):
            	username = payload['content']
            	print "Hello "+payload['content']
            	welcome = json.dumps({'timestamp': timestamp,
            						  'sender': username,
                					  'response': '200 OK',            						  
                                      'content' : "Hello "+username})
            	self.connection.send(welcome)

            elif (payload['request'] == "logout"):
                pass # selfdestruct!

            elif (payload['request'] == "names"):
                pass # get a list of names

            elif (payload['request'] == "msg"):
                print username+' '+payload['content']
            	message = json.dumps({'timestamp': timestamp,
            						  'sender': username,
                					  'response': '200 OK',          						  
                                      'content' : payload['content']})
            	self.connection.send(message)

            elif (payload['request'] == "help"):
                print 'Something, something...'
                message = json.dumps({'timestamp': timestamp,
                					  'sender': 'Server',
                					  'response': '200 OK',
                					  'content' : 'Something, somethin'})
            	self.connection.send(message)

            else:
                print 'Command not found!'
                message = json.dumps({'timestamp': timestamp,
                					  'sender': 'Server',
                					  'response': '200 OK',
               						  'content' : 'Command not found!'})
            	self.connection.send(message)


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
