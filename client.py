import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket.sock_stream is used for tcp protocols 
# socket.AF_INET is used for all family internet(Ipv4,Ipv6)

hostname='localhost'
portnumber=1255

s.connect((hostname,portnumber))
con=True
while con:
    msg=input("enter something here")
    s.send(msg.encode("utf-8"))#s.send is used to send the data to server, msg.encode is used to change the 
#data to computer langage (utf-8) 
    if msg=="quit":
        con = False
        s.close()#its used to close the connection.