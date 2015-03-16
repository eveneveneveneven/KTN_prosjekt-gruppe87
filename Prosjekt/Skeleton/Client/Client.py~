# -*- coding: utf-8 -*-
import socket
import json
import string
from MessageReceiver import *

class Client:
    """
    This is the chat client class
    """

    lastMessage = {'request': None, 'content': None}

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((host, server_port))

        # Start listening for server messages.
        MessageReceiver(self, self.connection) 

        #Start processing userinput. (Code blocked here forever)
        self.run()
        # CODE BELOW WON'T EXECUTE 


    def run(self):

        print "Connected to Server..."

        # Initiate the connection to the server
        while True:
            userinput = raw_input()
            self.processClientInput(userinput)
           
    def disconnect(self):
        self.connection.close()
        print "Disconnected from server"
        exit(0)


    # process input from server.
    def receive_message(self, message):

        # Convert the message to data.
        data = json.loads(message)

        # Process data
        # info message from server
        if data['response'] == 'info':
             print "--->" + data['timestamp'] + " Server Info: " + data['content']
            
        # message from a user
        elif data['response'] == 'message':
            print "--->" + data['timestamp'] + ' ' + data['sender'] + ": " + data['content']
             
        # error message from server 
        elif data['response'] == 'error':
            print "--->" + data['timestamp'] + " Server Error: " + data['content']
           
        # server message history 
        elif data['response'] == 'history':
            print "--->"
            print "====Server History:===="
            print data['content']
            print "======================="


        # otherwise
        else:
            print "Unable to interpret server response"




    # send object to server.
    def send_payload(self, data):

        # convert to json fomatted string
        message = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')) # Matches project description
        #message = json.dumps(data) #Compact form.

        # send the json formatted string to the server
        self.connection.send(message)


    #process input from client
    def processClientInput(self, userinput):

        #split the user input on space
        userinput = userinput.split(' ')

        if len(userinput) > 0:
            # extract the user command
            usercommand = string.lower(userinput[0])
            
            #remove the first user command
            userinput.pop(0)

            #rejoin the last elements into a string again
            if len(userinput) > 0:
                userinput = string.join(userinput)
            else:
                userinput = ""


        if usercommand == "login":    
            
            # Prepare the message data in the required format.
            self.lastMessage['request'] = 'login'
            self.lastMessage['content'] = userinput

            # Send the data to the server.
            self.send_payload(self.lastMessage)

        elif usercommand == "logout":    

            # Prepare the message date in the required format:
            self.lastMessage['request'] = 'logout' 
            self.lastMessage['content'] = None 
            
            # Send the data to the server.
            self.send_payload(self.lastMessage)

        elif usercommand == "history": 
            self.lastMessage['request'] = 'history' 
            self.lastMessage['content'] = None 
            
            # Send the data to the server.
            self.send_payload(self.lastMessage)

        elif usercommand == "msg":    

            # Prepare the message date in the required format:
            self.lastMessage['request'] = 'msg' 
            self.lastMessage['content'] = userinput 
            
            # Send the data to the server.
            self.send_payload(self.lastMessage)


        elif usercommand == "names":    

            # Prepare the message date in the required format:
            self.lastMessage['request'] = 'names' 
            self.lastMessage['content'] = None
            
            # Send the data to the server.
            self.send_payload(self.lastMessage)


        elif usercommand == "help":    

            # Prepare the message date in the required format:
            self.lastMessage['request'] = 'help' 
            self.lastMessage['content'] = None
            
            # Send the data to the server.
            self.send_payload(self.lastMessage)


        elif usercommand == "disconnect":    

            # Prepare the message date in the required format:
            self.lastMessage['request'] = 'disconnect' 
            self.lastMessage['content'] = None
            
            # Let the server know we disconnected
            self.send_payload(self.lastMessage)

            # Close connection.
            self.connection.close()

            # exit application
            exit(0)


        else:
            print "Invalid user input.."





# Main entry point.
if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """

    #create a client object.
    client = Client('localhost', 9998)
