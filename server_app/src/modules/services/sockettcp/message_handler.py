"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class handle all message 
     server tcp  (0 - 0)
"""
from json import ( 
    dumps as json_dumps ,loads as json_loads
)
from socket import socket

from modules.models.user import User

clients : dict = {}
class MessageHandler:
    def __init__(self, socket_client: socket):
        super().__init__()        
        self.socket_client=socket_client
        
    def start(self):

        global clients
        """
        ---- this method start Message Hanldleing
        """
        try:
            message: str = self.socket_client.recv(8096).decode("utf-8")
        
            data_json=json_loads(message)

            #conditions
            self.condition_auth(data_json)
            
            clients[self.socket_client]=self.socket_client
            print(clients)
            self.__broadcast("{} has entered chat".format("new User") ,con1 = self.socket_client ,cmd="new_User") 
            
            #recursive
            self.start()

            del message
        except:
            pass

    def display(self):

        """this method for show members in dbd

        Returns:
            [str] -- [return your select user]
        """
        ret : str = ""
        users=User.select()

        for count,user in enumerate(users):

            if count%2 == 0 and count !=0:
                ret += str(user.username+" || ")+"\n"
            else:
                ret += str(user.username+" || ")

        ret = ret.strip(" || ")
        self.send_message_to_client("User : "+ret,"display","server","broadcast")

    def condition_auth(self, data_json : object):

        """this method for coditions method start

        Arguments:
            data_json {dict}
        """

        if data_json["command"]=="VAL":

            select_user=data_json["message"]
            user_isvalid=User.select().where(
                (User.username==select_user)
            )

            if len(user_isvalid) > 0:
                self.__broadcast("",None,"chat")
            else:
                self.send_message_to_client("this username not valid","LOGIN","server","broadcast")
                self.display()

        elif data_json["command"]=="AUTH":

            username: str = data_json["message"]["username"]
            password: str = data_json["message"]["password"]

            try:
                signin=User.select().where(
                    (User.username == username) &(User.password == password)
                )
                auth=User.select().where(
                    (User.username == username) &(User.password != password)
                )
                if len(auth) > 0 :
                    print("User (%s) Password Is Wrong " %username)
                    self.send_message_to_client("[-] Your Password is Wrong ","LOGIN","server","broadcast")

                if len(signin) > 0:
                    print("User SignIn successfully (%s) " %username)
                    self.send_message_to_client("[+] Your SignIn is Successfully ","LOGIN","server","broadcast")
                    self.display()

                else:
                    User.create(
                    username=username,
                    password=password
                    )
                    print("User SignUp successfully (%s) " %username)

                    self.send_message_to_client("[+] Your SignUp is Successfully ","LOGIN","server","broadcast")
                    self.display()

            except Exception as identifier:
                pass
        elif data_json["command"] == "msg" :
            self.__broadcast( data_json["message"] , con1 =self.socket_client,cmd="send_message")
            print(" Recived this {0} Message From Server ".format(data_json["message"]))
        
            
    def send_message_to_client(self, message : object, command : str, from_message : str , group : str):

        """this method for send message from server to clients

        Arguments:
            message {object} 
            command {str} 
            from_message {str}
            group {str} 
        """
        self.socket_client.sendall(str(
            json_dumps({
                "message": message,
                "command":  command,
                "from": from_message,
                "group": group
            })
        ).encode("utf-8"))

    def __broadcast(self, msg : str , con1 = None, cmd = None):
        global clients
        for con in clients:
            if con != con1:
                con.sendall(str(
                    json_dumps({
                        "message": msg,
                        "command":cmd,
                        "from": "server",
                        "group": "broadcast"
                        })
                    ).encode("utf-8"))
            

