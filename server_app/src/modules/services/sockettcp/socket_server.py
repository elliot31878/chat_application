"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class for handle socket server tcp protocol (0 - 0)
"""

from socket import (
    socket,AF_INET,SOCK_STREAM,
    SOL_SOCKET,SO_REUSEADDR
    )

from .clinet_handler import ClientHandler
from utils.config_manager import ConfigManager

class socket_server:
    """
    -----this class for create socket stream TCP protocol :)
    """

    def __init__(self):
        super().__init__()
        
        #initializar ConfigManager Class
        self.config_manager=ConfigManager()

        self.socket_connection=socket(AF_INET,SOCK_STREAM)
        self.socket_connection.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

        self.__start__()
    
    def __start__(self):
        """
        ---- this method try to bind to socket_connection ;)
        """
        self.socket_connection.bind(

            (
                self.config_manager.get.socket_server.IP,
                self.config_manager.get.socket_server.PORT
            )
        )

        self.socket_connection.listen(
            self.config_manager.get.socket_server.LISTEN_CLIENT
        )
        print(
            "=> [+] Server ready to listening ... "
        )

    def run(self):
        """
        ----- start server for listen clinets
        """
        client, client_address = self.socket_connection.accept()

        print(

            "=> [+] Some Client connected to server with (%s)"%str(client_address)
        )

        # initializer Client Handler Class for connect client to the server
        ClientHandler(
            client=client,
            client_address=client_address
        ).start()
        
        self.run()