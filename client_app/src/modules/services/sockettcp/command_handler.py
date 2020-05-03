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

class CommandHandler:

    def __init__(self, client_socket: socket):
        super().__init__()

        self.client_socket = client_socket
        self.username: str = None
    
    def start(self):
        """ 
        ---- start command handler service
        """

        message: str = self.client_socket.recv(8096).decode("utf-8")
        json_data: dict = json_loads(message)

        #conditions
        self.start_condition(json_data)

        #recursive
        self.start()

    def start_condition(self, json_data: dict):
        """this method for check command  
        ----and reaction client to server
        Arguments:
            json_data {dict}
        """
        if json_data["command"]=="START":
            print(
                "[+] connecting to WhatsUp server was successfully ..."
            )

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