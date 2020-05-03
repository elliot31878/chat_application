"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class handle all message 
     server tcp  (0 - 0)
"""
from json import ( 
    dumps as json_dumps ,loads as json_loads
)
from socket import socket

from modules.models.user import (
    User
)
class MessageHandler:
    def __init__(self, socket_client: socket):
        super().__init__()
        
        self.socket_client=socket_client

    def start(self):
        """
        ---- this method start Message Hanldleing
        """
        message: str = self.socket_client.recv(8096).decode("utf-8")
        data_json=json_loads(message)

        #conditions

        self.condition_auth(data_json)

        del message
    
    def condition_auth(self, data_json : object):
        if data_json["command"]=="AUTH":
            username: str = data_json["message"]["username"]
            password: str = data_json["message"]["password"]
            try:
                user=User.select().where(
                    (User.username == username) &(User.password == password)
                )
                if len(user) > 0:
                    print("User Authenticated successfully")
                else:
                    User.create(
                    username=username,
                    password=password
                    )
            except Exception as identifier:
                print(identifier)
            
