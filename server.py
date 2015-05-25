#!/usr/bin/env python
from network import Listener, Handler, poll
import sys
from threading import Thread

from time import sleep
import json
import server_view

 

 # map client handler to user name
 
class MyHandler(Handler):
   
    def on_open(self):
        pass
    

    #when close, pop the current client and send signal to the following client in line
    def on_close(self):
        global clients
        server_view.client_leave()
        clients.pop(0)
        clients[0].do_send({'busy': "false"})
        clients[0].do_send({'speak': "Agent", 'txt': "Thank you for your waiting. I help you now"})
        pass

     # when receiving message, print to the server 
    def on_msg(self, msg):
        if 'join' in msg:
            server_view.client_join(msg['join'])
        elif 'connect' in msg:
            pass
        elif 'choose' in msg:
            server_view.process(msg['speak'], msg['choose'])
        else:
            server_view.print_message(msg['speak'],msg['txt'])

# listen for incoming connection
class MyListener(Listener):
    def on_accept(self, h):
        global clients
        clients.append(h)
        if len(clients) == 1:
            clients[0].do_send({'busy': "false"})
        elif len(clients) > 1:
            clients[-1].do_send({'busy': "true"})
        
        
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
            mytxt = sys.stdin.readline().rstrip()
            clients[0].do_send({'speak': "Agent", 'txt': mytxt})
