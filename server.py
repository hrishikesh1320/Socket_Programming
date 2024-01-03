import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket.sock_stream is used for tcp protocols 
# socket.AF_INET is used for all family internet(Ipv4,Ipv6)

hostname='localhost'
portnumber=1255

s.bind((hostname,portnumber))
#s.blind is used for starting the servers 
s.listen(5)#its is used for accepting the request of clines and 5 slows that only 5 client can send the request
socketclient, address = s.accept()
#here address means the client ip address and socketclient is used to recieve the message from client or sending the message to the client 
#s.accept() is the function used to return the address and scoketclient 
print('got connection with client',address)
con=True
while con:
    msg=socketclient.recv(1024)#here 1024 represent the size of the data recieved from the client.
    msg=msg.decode("utf-8")
    print(msg)
    if(msg =="quit"):
        con=False
        s.close()
