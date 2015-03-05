# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import *

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

        self.run()

        MessageReceiver(self, self.connection) #pass thread?

        # TODO: Finish init process with necessary code

    def run(self):
        # Initiate the connection to the server
        while True:
            userinput = raw_input()
            userinput = userinput.split(' ')
            if userinput[0] == "logout":    
                self.disconnect()
            payload = json.dumps(userinput)
            print payload
            self.send_payload(payload)

    def disconnect(self):
        self.connection.close()
        print "Disconnected from server"
        exit(0)
        # eller mener den hvis TCP connection "droppes"?
        # TODO: Handle disconnection

    def receive_message(self, message):
        print json.loads(message)
        # TODO: Handle incoming message

    def send_payload(self, data):
        self.connection.send(json.dumps(data))
        recv = json.loads(self.connection.recv(4048))
        #if recv != "whatever":
        #       self.disconnect()


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
