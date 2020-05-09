"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class handle all client that connect to the
     server tcp  (0 - 0)
"""

from threading import Thread
from json import dumps as json_dumps
from time import sleep

from .message_handler import MessageHandler

class ClientHandler(Thread):
    def __init__(self, client : object, client_address: object):
        Thread.__init__(self)

        self.client = client
        self.client_address = client_address
        self.first_message = False

    def run(self):
        """
        ---- run new client thread from this method
        """
        if not self.first_message:
            
            #send welcome message to server
            self.send_message_to_client("Welcome to Server , Dude","START","server","broadcast")
            sleep(.1)
            self.send_message_to_client("","AUTH","server","broadcast")

            self.first_message = False

        # Add Class Message Handler

        MessageHandler(socket_client=self.client).start()
        
    def send_message_to_client(self, message : object, command : str, from_message : str , group : str):
    
        """this method for send message from server to clients

        Arguments:
            message {object} 
            command {str} 
            from_message {str}
            group {str} 
        """
        try:
            self.client.sendall(str(
                json_dumps({
                    "message": message,
                    "command":  command,
                    "from": from_message,
                    "group": group
                })
            ).encode("utf-8"))
        except:
            pass
    