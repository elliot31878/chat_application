"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class handle all message 
     server tcp  (0 - 0)
"""
from json import ( 
    dumps as json_dumps ,loads as json_loads
)
from socket import socket

from modules.data.app_context import AppContext
from modules.models.user import User
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

        condition_auth(data_json)

        del message
    
    def condition_auth(self, data_json : object):
        if data_json["command"]=="AUTH":
            username: str = data_json["message"]["username"]
            password: str = data_json["message"]["password"]

            try:
                AppContext.select().where(
                    (User.username == username) &(User.password == password)
                )
                print("User Authenticated successfully")
            except Exception as identifier:
                AppContext.create(
                    username=username,
                    password=password
                )


