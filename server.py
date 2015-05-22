#!/usr/bin/env python

from network import Listener, Handler, poll
import sys
from threading import Thread

from time import sleep
import json
import view

 

 # map client handler to user name
 
class MyHandler(Handler):
   
    def on_open(self):
    #     handlers[msg['join']] = msg['join']
        pass
         
    def on_close(self):
        pass

     
    def on_msg(self, msg):
        global clients
        if 'join' in msg:
            print msg['join'] + " join the chat room!"
            clients[0].do_send({'busy': "false"})
        elif 'choose' in msg:
            print msg['speak'] + process(msg['choose'])


        elif 'quit' in msg:
            print msg['speak'] + " quit the chat room!"
            clients.pop(0)
            clients[0].do_send({'busy': "false"})
            clients[0].do_send({'speak': "Agent", 'txt': "Thank you for your waiting. I help you now"})

        else:
            print msg['speak']+": "+msg['txt']

class MyListener(Listener):


    def on_accept(self, h):
        global clients
        clients.append(h)
        if len(clients) > 1:
            clients[-1].do_send({'busy': "true"})
        
def process(choice):
    if choice =="1":
        return " have question about existing products"
    elif choice=="2":
        return " have question about orders"
    elif choice== "3":
        return " have suggestions and complaint"
    else:
        return " have general questions"
        

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds

if __name__ == "__main__":
    
    clients = []
    handlers = {} 
    port = 8888
    host = 'localhost'
    
    server = MyListener(port, MyHandler)
    
                                
    thread = Thread(target=periodic_poll)
    thread.daemon = True  # die when the main thread dies 
    thread.start()


    while 1:
        if clients!=[]:
            # print connection
            # print handlers
            mytxt = sys.stdin.readline().rstrip()

            # for client in clients:
            #     client.do_send({'speak': "Agent", 'txt': mytxt})
            clients[0].do_send({'speak': "Agent", 'txt': mytxt})
