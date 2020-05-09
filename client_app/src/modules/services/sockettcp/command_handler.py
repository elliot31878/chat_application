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
    stdout , stdin ,
    executable , argv
)
from getpass import getpass
from threading import Thread
from time import sleep

from commons.constants.shape import Shape
from commons.constants.colors import Colors


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
            #conditions
            self.start_condition(self.json_data)
            #recursive
            self.start()
        except:
            pass
 
    def clientSend(self):

        """this method for send message to other clients
        """
        try:
            print(Colors().FORE_GREEN+"->"+Colors().FORE_GREEN,end='')
            message = input()
            if message=="{quite}":
                self.send_message_to_server("{quite}", "{quite}", "client", "server")
            self.send_message_to_server(message, "msg", "client", "server")
            #recurseive
            self.clientSend()
        except Exception as ex:
            return

    def __recived_caht(self):
        """this method for recive a message from server
        """
        try:
            
            recv_msg = self.client_socket.recv(8096).decode('utf-8')
            self.json_data: dict = json_loads(recv_msg)
            if self.json_data["message"] != "{quite}"  : 
                if self.json_data["message"].strip() !="":
                    if self.json_data["from"] != "server":
                        print(
                            Colors().FORE_CYAN + self.json_data["from"] + Colors().FORE_CYAN, Colors().FORE_YELLOW + ": " + Colors().FORE_YELLOW, self.json_data["message"]
                            )
                        print( Colors().FORE_GREEN + "->" + Colors().FORE_GREEN,end = "")
                    else:
                        self.restart_program()
                        return
                #recursive
                self.__recived_caht()
            # recv 'quite' to close 
            else:
                return
        except Exception as ex:
            return
        
    def start_condition(self, json_data: dict):

        """this method for check command  
        ----and reaction client to server
        Arguments:
            json_data {dict}
        """
        if json_data["command"] == "START":
            print(Colors.FORE_GREEN + "Connect is Successfully " + Colors.FORE_GREEN)
            print(Colors.FORE_CYAN+Shape().mrrobot+Colors.FORE_CYAN)
            sleep(2)
        elif json_data["command"] == "AUTH":
            print(chr(27) + "[2J")
            print(Colors().FORE_GREEN+Shape().welcome+Colors().FORE_GREEN)
            print(Colors().FORE_RED+"♦"*10,Colors().FORE_GREEN + "AUTHENTICATION" + Colors().FORE_GREEN , Colors().FORE_RED + "♦"*10)

            username: str = input("Enter your username☺ -> ")
            password: str = getpass(prompt='Enter your password☻ -> ')

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

        elif json_data["command"] == "LOGIN":
            print(Shape(json_data["message"]).prompt_sgape())
            sleep(2.5)

        elif json_data["command"] == "display":
            Thread(target = self.display, args = (json_data,)).start()

        elif json_data["command"]=="chat":
            try:
                print(chr(27) + "[2J")
                Thread(target = self.clientSend).start()
                self.__recived_caht()
            except:
                pass

        elif json_data["command"]=="request_chat":
            try:
                print(chr(27) + "[2J")
                print("You have request from {0} fro continue please write {0}: ".format(json_data["from"]))
                Thread(target = self.clientSend).start()
                self.__recived_caht()
            except:
                pass
            
    def display(self, json_data : dict):
        """this method for get username that clients can chat with to gether

        Arguments:
            json_data {dict} -- [description]
        """
        print(chr(27) + "[2J")
        print(Colors.FORE_CYAN+Shape().man+Colors.FORE_CYAN)
        print( json_data["message"] )
        print(Colors().FROE_MAGENTA +"select user from list -> "+Colors().FROE_MAGENTA , end="")
        select_user:str = input()
        self.send_message_to_server(str(select_user), "sleclet_user", "client", "server")
        del select_user

    def send_message_to_server(self, message : object, command : str, from_message : str , group : str):
        
        """this method for send message from clients to server

        Arguments:
            message {object} 
            command {str} 
            from_message {str}
            group {str} 
        """
        self.client_socket.sendall(str(
            json_dumps({
                "message": message,
                "command":  command,
                "from": from_message,
                "group": group
            })
        ).encode("utf-8"))
    

    def restart_program(self):
        from os import execl
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = executable
        execl(python, python, * argv)