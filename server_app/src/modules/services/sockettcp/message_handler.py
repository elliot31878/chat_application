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

#----------------------
# global varible
clients : dict = {}
private_clients : dict = {}
#----------------------
class MessageHandler:
    
    def __init__(self, socket_client: socket):
        super().__init__()        
        self.socket_client = socket_client
        self.username : str = str()
        self.password :str = str()
        self.select_user :str = str()

    def start(self):

        """
        ---- this method start Message Hanldleing
        """
        global clients
        try:
            message: str = self.socket_client.recv(8096).decode("utf-8")
            data_json=json_loads(message)
            #conditions
            self.condition_auth(data_json)
            #recursive
            self.start()
            del message
        except:
            self.__exit()

    def display(self, username : str):

        """this method for show members in dbd

        Arguments :
            username {str} -- [this argument for get username current user]
        """
        count : int = int(1) # this counter return number users
        ret : str = str()
        for user in clients.values():
            print(private_clients.values())
            if user != username and not(user in private_clients.values()):
                if count % 2 == 0:
                    ret+="\n"
                count+=1
                ret += str(user+"-")
        ret = ret.strip("-")
        if ret == "":
            self.send_message_to_client("user not found for research pleas push enter","display","server","broadcast")
        else:
            self.send_message_to_client("Online User : "+ret,"display","server","broadcast")

    def condition_auth(self, data_json : object):
        
        """this method for coditions method start

        Arguments:
            data_json {dict}
        """

        if data_json["command"]=="AUTH":
            
            self.username = data_json["message"]["username"]
            self.password = data_json["message"]["password"]

            try:
                signin=User.select().where(
                    (User.username == self.username) &(User.password == self.password)
                )
                auth=User.select().where(
                    (User.username == self.username) &(User.password != self.password)
                )
                if len(auth) > 0 :
                    print("User (%s) Password Is Wrong " %self.username)
                    self.send_message_to_client("[-] Your Password is Wrong ","LOGIN","server","broadcast")
                    self.send_message_to_client( "","AUTH","server","broadcast")
                if len(signin) > 0:
                    for client in clients.values():
                        if self.username==client:
                            self.send_message_to_client("[-] Your account is online Now ","LOGIN","server","broadcast")
                            self.send_message_to_client( "","AUTH","server","broadcast")
                            return
                    print("User SignIn successfully (%s) " %self.username)
                    self.send_message_to_client("[+] Your SignIn is Successfully ","LOGIN","server","broadcast")
                    self.display(self.username)
                    clients[self.socket_client]=self.username

                else:
                    User.create(
                    username=self.username,
                    password=self.password
                    )

                    print("User SignUp successfully (%s) " %self.username)
                    self.send_message_to_client("[+] Your SignUp is Successfully ","LOGIN","server","broadcast")
                    self.display(self.username)
                    clients[self.socket_client]=self.username
            except Exception as identifier:
                print(identifier)

        elif data_json["command"]=="sleclet_user":
            self.select_user=data_json["message"]

            if ( not(self.select_user in clients.values() ) or ( self.username==self.select_user )  or ( self.select_user in private_clients.values() ) or not ( len( private_clients.values() ) <=2) and len(private_clients.values())%2==0):
                print("values :",private_clients.values())
                self.send_message_to_client("this username not valid","LOGIN","server","broadcast")
                self.display(self.username)
                return
            self.send_message_to_client("","chat","server","broadcast")
            
            try:
                self.__send_private_message_between_tow_clients( "{} entered in the chat".format(self.username), self.select_user, con1 =self.socket_client,cmd="",frm="server")
            except Exception as ex:
                print(ex)
        elif data_json["command"] == "msg" :
            try:
                self.__send_private_message_between_tow_clients( data_json["message"], self.select_user, con1 =self.socket_client,cmd="send_message",frm=self.username)
            except Exception as ex:
                print(ex)
        elif data_json["command"] == "{quite}":
            self.__exit()
        
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

    def __broadcast(self, msg : str , con1 : object = None, cmd : str = None, frm : str = ""):

        """this method for send message for all clients

        Arguments:
            msg {str} -- [this argument message for send clients]

        Keyword Arguments:
            con1 {[Dict]} -- [this argument connection clients] (default: {None})
            cmd {[str]} -- [this argumnet command send to clients] (default: {None})
            frm {[str]} -- [this argumnet username message sender] (default: {None})
        """
        global clients
        for con in clients.keys():
            if con != con1:
                con.sendall(str(
                    json_dumps({
                        "message": msg,
                        "command":cmd,
                        "from": frm,
                        "group": "broadcast"
                        })
                    ).encode("utf-8"))

    def __send_private_message_between_tow_clients(self, msg : str, client_username : str = None, con1 : object = None, cmd : str = None, frm : str = ""):
        """this method got send message between tow clients

        Arguments:
            msg {str} -- [description]

        Keyword Arguments:
            con1 {[Dict]} -- [this argument connection clients] (default: {None})
            cmd {[str]} -- [this argumnet command send to clients] (default: {None})
            frm {[str]} -- [this argumnet username message sender] (default: {None})
            client_username {[str]} -- [this argumnet username  client you wnat send message] (default: {None})
        """
        global clients, private_clients
        key_list = list(clients.keys())
        value_list = list(clients.values())
        connection : str =  key_list[value_list.index(client_username)]
        
        if connection != con1:
            private_clients[connection] = client_username
            connection.sendall(str(
                        json_dumps({
                            "message": msg,
                            "command":cmd,
                            "from": frm,
                            "group": "private"
                            })
                        ).encode("utf-8"))

    def __exit(self):

        """
        this method for exit user from this program
        """
        try:
            del clients[self.socket_client]
            private_clients=clients
            self.__send_private_message_between_tow_clients( "{} has left chat".format(self.username), self.select_user, con1 = None,cmd="{quite}",frm="server")             
            self.socket_client.close()
        except:
            pass