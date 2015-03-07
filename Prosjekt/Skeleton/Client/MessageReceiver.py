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

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        super(MessageReceiver, self).__init__()
        # Flag to run thread as a deamon
        self.daemon = True
        self.client = client
        self.connection = connection
        thread = Thread(target = self.run, args = ())  
        thread.start()

    def run(self):
        while True:
            received_string = self.connection.recv(4096)
            payload = json.loads(received_string)
            self.client.receive_message(payload)