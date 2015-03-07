# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import *
import re

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect(("localhost", 9998))
        MessageReceiver(self, self.connection)
        self.run()

    def run(self):
        # Initiate the connection to the server
        while True:
            userinput = raw_input()
            if userinput.split(' ')[0] == "logout":    
                self.disconnect()

            if len(re.findall(r'\w+', userinput)) > 1: #Må fikses for names og help...
                splitted = userinput.split(' ', 1)
                cmd = splitted[0]
                message = splitted[1]
                payload = json.dumps({'request': cmd,
                                      'content' : message})
                self.send_payload(payload)
            else:
                print "Not valid"

    def disconnect(self):
        self.connection.close()
        print "Disconnected from server"
        exit(0)
        # eller mener den hvis TCP connection "droppes"?
        # TODO: Handle disconnection

    def receive_message(self, message):
        print message['sender']+': '+message['content'] 

    def send_payload(self, data):
        self.connection.send(data)
        #Dette skal mssageReciever gjøre, me måtte debugge stuff
        #recv = self.connection.recv(4096)
        #message = json.loads(recv)
        #print message['sender']+': '+message['content'] 



if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
