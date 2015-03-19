# -*- coding: utf-8 -*-
from threading import Thread
from Client import *
import socket

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """

    # Reference to the client object.
    Client = None
    # Reference to the client connection.
    Connection = None

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """

        # Run parent class's init function first.
        super(MessageReceiver, self).__init__()

        # Flag to run thread as a deamon
        self.daemon = True
<<<<<<< HEAD

        # Store a reference to the client.
        self.Client = client

        # Store a reference to the client connection.
        self.Connection = connection
   
        # Starts a the thread object. (invokes run() function in a new thread)
        self.start()


    def run(self):

        # Wait for and process server messages
        while True:

            # Get server message and send to client for processing.
            message = self.Connection.recv(1024)
            self.Client.receive_message(message)

=======
        self.client = client
        self.connection = connection
        thread = Thread(target = self.run, args = ())  
        thread.start()

    def run(self):
        while True:
            received_string = self.connection.recv(4096)
            payload = json.loads(received_string)
            self.client.receive_message(payload)
>>>>>>> master
