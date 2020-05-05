"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class for read posted commands  (0 - 0)
"""

from socket import (
    socket,AF_INET,SOCK_STREAM,
    SOL_SOCKET,SO_REUSEADDR
)

from json import (
    loads as json_loads,
    dumps as json_dumps
)

from sys import ( 
    stdout , stdin
)
from threading import Thread

class CommandHandler:

    def __init__(self, client_socket: socket):
        super().__init__()

        self.client_socket = client_socket
        self.username: str = None
        self.msg : str = None
        self.json_data : dict = None
        
    def start(self):
        """ 
        ---- start command handler service
        """
        try:
            self.msg: str = self.client_socket.recv(8096).decode("utf-8")
            self.json_data: dict = json_loads(self.msg)
        except:
            pass
        
    
        #conditions
        self.start_condition(self.json_data)

        #recursive
        self.start()

    def clientSend(self):
        try:
            message = input('you -> ')
            
            self.client_socket.sendall(str(
                    json_dumps({
                        "message": message,
                        "command":"msg",
                        "from": "client",
                        "group": "server"
                        })
                    ).encode("utf-8"))
            
            #recurseive
            self.clientSend()
        except Exception as ex:
            return

    def __recived_caht(self):
        try:
            recv_msg = self.client_socket.recv(8096).decode('utf-8')
            self.json_data: dict = json_loads(recv_msg)
            
            if self.json_data["message"] != "{Exit}" : 
                print( '\n' , self.json_data["message"])
                self.__recived_caht()
            # recv 'quite' to close 
            else:
                print("I left chat")
                return
        except:
            print()
        
    def start_condition(self, json_data: dict):

        """this method for check command  
        ----and reaction client to server
        Arguments:
            json_data {dict}
        """
        if json_data["command"]=="START":
            print("[+] connecting to server was successfully ...")

        elif json_data["command"] == "AUTH":
            print("-" * 10 + " AUTHENTICATION " + "-" * 10)
            username: str = input("Enter your username:: ")
            password: str = input("Enter your password:: ")

            self.client_socket.sendall(str(
                json_dumps({
                    "message": {
                        "username": username,
                        "password": password
                    },
                    "command": "AUTH",
                    "from": "client",
                    "group": "server"
                })
            ).encode("utf-8"))
            del username, password

        elif json_data["command"]=="LOGIN":
            print(json_data["message"] )

        elif json_data["command"]=="display":
            print( json_data["message"] )
            
            select_user:str = input("select user from list : ")

            self.client_socket.sendall(str(
                json_dumps({
                    "message": str(select_user),
                    "command": "VAL",
                    "from": "client",
                    "group": "server"
                })
            ).encode("utf-8"))

            del select_user
        
        elif json_data["command"]=="chat":
            Thread(target = self.clientSend).start()
            self.__recived_caht()
 