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
   
        connection.listen(5)
        self.run(connection)

        # TODO: Finish initialization of MessageReceiver

    def run(self,connection):
        streng = ""
        while True:
            streng = streng + connection.recv(1024)
            if streng.endswith(u"\r\n"):
                receive_message(self.data)
                streng = ""
        # TODO: Make MessageReceiver receive and handle payloads

