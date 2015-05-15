from network import Listener, Handler, poll
import sys
from threading import Thread

from time import sleep
import json



handlers = {}  # map client handler to user name
 
class MyHandler(Handler):
     
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        if 'join' in msg:
            print msg['join'] + " join the chat room!"
        else:
            print msg['speak']+": "+msg['txt']
 

class MyListener(Listener):

    def on_accept(self, h):
        global connection
        connection = h

port = 8888
host = 'localhost'
server = MyListener(port, MyHandler)
connection = None



def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()


while 1:
    if connection!=None:
        mytxt = sys.stdin.readline().rstrip()
        connection.do_send({'speak': "agent", 'txt': mytxt})
