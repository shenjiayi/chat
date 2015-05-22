#!/usr/bin/env python

from network import Handler, poll
import sys
from threading import Thread
from time import sleep
import json
import view
from model import chat



class Client(Handler): 
    
    def on_open(self):
        view.welcome_message()

    def on_close(self):
        pass
    
    def on_msg(self, msg):
        global busy
        if 'join' in msg:
            view.connected()
        elif 'busy' in msg:
            print(msg['busy'] =="true")
            if msg['busy']=="true":
                busy = True
            else:
                busy = False
        else:
            history.add_message("Agent",msg['txt'])
            view.print_message(msg['speak'],msg['txt'])


def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds

#process commend line instruction that the user input
def process_local_cmd(mytxt):
    if mytxt:
        if mytxt[0] == ":":
            cmd = mytxt[1:].lstrip().rstrip()
            for i in cmd:
                if   i == "q": 
                    return "quit"
                elif i == "s": 
                    view.save_history()
                    history.store_message()
                elif i == "e":
                    view.fun_easter_egg()
                else:
                    print cmd, "is an invalid command!"
            return ''
        else:
            return mytxt
    return mytxt



if __name__ == "__main__":
    myname = raw_input('What is your name? ')
    busy = False;
    host, port = 'localhost', 8888
    client = Client(host, port)
    client.do_send({'join': myname})
                               
    thread = Thread(target=periodic_poll)
    thread.daemon = True  # die when the main thread dies 
    thread.start()
    history = chat()

    #get info about what question the customer has
    mytxt = sys.stdin.readline().rstrip()
    client.do_send({'speak': myname, 'choose': mytxt})
    if not busy:
        view.connected()
    else:
        view.busy()


    while 1:
        mytxt = sys.stdin.readline().rstrip()
        mytxt = process_local_cmd(mytxt)
        if mytxt:
            if mytxt =="quit":
                 client.do_send({'speak': myname,'quit':"true"})
                 break;
            if not busy:
                
                history.add_message("Me", mytxt)
                client.do_send({'speak': myname, 'txt': mytxt})

