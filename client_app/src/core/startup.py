"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- start app form this class (0 - 0)
"""

class StartUp:

    def __init__(self):
        super().__init__()

    def __start_sockettcp_service__(self):
        """
        ---- this method for start socket tcp service
        """
        from modules.services.sockettcp.sockettcp_client import SocketClientTCP

        SocketClientTCP()
    
    def start(self):
        """this method for start app 
        """
        self.__start_sockettcp_service__()