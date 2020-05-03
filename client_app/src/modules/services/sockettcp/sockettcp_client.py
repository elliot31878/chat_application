"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class for  connect client to server (0 - 0)
"""

from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)

from utils.config_manager import ConfigManager
from modules.services.sockettcp.command_handler import CommandHandler

class SocketClientTCP:

    def __init__(self):
        super().__init__()

        #initializar ConfigManager Class
        self.config_manager = ConfigManager()
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.__connect__()

    def __connect__(self):
        """
        ---- this method try connect to the server
        """
        
        print(

            "[+] Try connecting to server ..."
        )

        response_code = self.sock.connect_ex(
            (
                self.config_manager.get().socket_server.IP,
                self.config_manager.get().socket_server.PORT,
            )
        )

        if response_code == 0:
            CommandHandler(client_socket=self.sock).start()

        elif response_code == 111:
            print(
                "[-] server no responed maybe it is down ..."
            )

