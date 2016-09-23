#!/usr/bin/python        

import socket             

s = socket.socket()        
host = socket.gethostname() 
port = 12345               
s.bind((host, port))    

msgs = "Hello"
s.listen(5)             
c, addr = s.accept()
while msgs!="end":
   
   print c.recv(1024)
   msgs=input("Messege for client")
   c.send(msgs)
  
c.close()            
