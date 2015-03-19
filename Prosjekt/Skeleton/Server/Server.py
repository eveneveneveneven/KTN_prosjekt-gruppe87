# -*- coding: utf-8 -*-
import SocketServer
import string
import json
import time
import datetime
<<<<<<< HEAD
import re

# Need some way of storing the server state (what clients are connected, users logged in, etc...)
class ServerState:
   
    ClientList = []
    UserDictionary = {}
    MessageHistory = []

    # Registers a ClientHandler object in the ClientList
    def registerClient(self, Client):
        self.ClientList.append(Client)

    # Removes a ClientHandler from the ClientList
    def unregisterClient(self, Client):
        self.ClientList.remove(Client)

    # Create a mapping between a username and a client
    def createUserClientMap(self, User, Client):
        self.UserDictionary[User] = Client

    # Remove a user to client mapping
    def removeUserClientMap(self, User):
        del self.UserDictionary[User]

    # Record message in message history
    def logMessage(self, Message):
        #TODO: restrict the maximum size of the log.

        self.MessageHistory.append(Message)

    # Broadcast message to all users
    def broadcastMessage(self, username, message, timestamp):
        # loop over every client in the list and send message from username
        for client in self.ClientList:
            client.sendResponse(timestamp, username, 'message', message)


=======
>>>>>>> master

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    lastMessage = {'timestamp': None, 'sender': None, 'response': None, 'content': None}

    # send a response to client in the appropriate format
    def sendResponse(self, timestamp, sender, response, content):
        self.lastMessage['timestamp'] = timestamp
        self.lastMessage['sender'] = sender
        self.lastMessage['response'] = response
        self.lastMessage['content'] = content

        # Serialize the object to a json formatted string and send it to the client.
        message = json.dumps(self.lastMessage, sort_keys=True, indent=4, separators=(',', ': ')) # Matches project description
        #message = json.dumps(self.lastMessage) #Compact form
        self.connection.send(message)


    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        username = self.ip
        ts = time.time()

        #initially we are not logged in and have no username.
        self.loggedin = False
        self.username = None

        #register this client with the state object (in main).
        state.registerClient(self)

        # get time and print to console
        print self.getCurrentTime() + " Client connected (" + self.ip + ")"

        # Loop that listens for messages from the client
        while True:
<<<<<<< HEAD
            
            #retreive the json formatted message from the client
            message = self.connection.recv(4096)

            #converts the message to a dictionary object in our case
            data = json.loads(message)

            # Get the time
            timestamp = self.getCurrentTime()
      
            #process the message (dictionary object)
            if (data['request'] == "login"):

                # Allready logged in?
                if self.loggedin:
                    self.sendResponse(timestamp, None, 'error', 'Already logged in')

                # if we are not logged in
                else:

                    # Check that the username is good
                    if re.match('^\w+$', data['content']):

                        #get username and add a mapping to state object.
                        self.username = data['content']
                        state.createUserClientMap(self.username, self)

                        #output to server console
                        print timestamp + " " + str(self.username) + " logged in."

                        #set us as logged in.
                        self.loggedin = True

                        #send response veryfying successful login.
                        self.sendResponse(timestamp, None, 'info', 'Login successful')
                    else:
                        self.sendResponse(timestamp, None, 'error', 'Bad username, use only A-Z, a-z, 0-9')



            elif (data['request'] == "logout"):
                
                # Check that we are logged in.
                if self.loggedin:
                    # Unmap the user from the state class
                    state.removeUserClientMap(self.username)

                    # Output to server console
                    print timestamp + " " + "User " + self.username + " logged out."

                    # Reset variables
                    self.username = None
                    self.loggedin = False

                    # Send a response to client informing of the successful logout
                    self.sendResponse(timestamp, None, 'info', 'You are logged out')

                    # ? Close Connection and unregister client ?

                else:
                    
                    # Send error message.
                    self.sendResponse(timestamp, None, 'error', 'You are not logged in')



            elif (data['request'] == "names"):

                # Get a list of names from the dictionary keys
                users = state.UserDictionary.keys()

                # Create a string from the user list
                users = string.join(users, ', ')

                # Send the string of names to the client
                self.sendResponse(timestamp, None, 'info', users)



            elif (data['request'] == "msg"):
                
                if self.loggedin:
                    # Log the message in the server history
                    message = timestamp + " " + self.username + ": " + data['content']
                    print message
                    state.logMessage(message)

                    # Broadcast the message to all clients
                    state.broadcastMessage(self.username, data['content'], timestamp)
                else:

                    # Send error message to client
                    self.sendResponse(timestamp, None, 'error', "You need to login to send messages")



            elif (data['request'] == "help"):

                # The help message to send back
                message = "Type: login <username> to login, logout to logout, msg <message> to send message, names to get a list of logged in users, help for help, history for the server message history, and disconnect to exit client."

                # Send response with help message
                self.sendResponse(timestamp, None, 'info', message)

            elif (data['request'] == "history"):
                # Create a string from the list
                users = string.join(state.MessageHistory, '\n')
                self.sendResponse(timestamp, None, 'history', users)


            # Client was nice and informed us it disconnected
            elif (data['request'] == "disconnect"):

                # Break out of the loop (finish() will get called after)
                break;



            else:
                self.sendResponse(timestamp, None, 'error', 'Unknown request')
                print timestamp + " Unknown Request: " + data['request']





    # Gets called after handle()
    def finish(self):


        # Get current time
        timestamp = self.getCurrentTime()

        # Clean up login state
        if self.loggedin:
            state.removeUserClientMap(self.username)

            # Output to server console
            print timestamp + " " + "User " + self.username + " logged out."


        # Make sure to unregister this client from the state
        state.unregisterClient(self)

        # Output to server console
        print timestamp + " Client disconnected (" + self.ip + ")"

        #Close the socket.
        self.connection.close()



    # Returnst the current time in h/m/s as a string
    def getCurrentTime(self):
 
        # Get the current time.
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

        return timestamp
       

=======
            received_string = self.connection.recv(4096)
            payload = json.loads(received_string)
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            if (payload['request'] == "login"):
            	username = payload['content']
            	print "Hello "+payload['content']
            	welcome = json.dumps({'timestamp': timestamp,
            						  'sender': 'Server',
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
>>>>>>> master


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True



# Main program entry
if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Initialize state
    state = ServerState()

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()


