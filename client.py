#!/usr/bin/env python

from network import Handler, poll
import sys
from threading import Thread
from time import sleep
import json
import client_view
from model import chat

 
class Client(Handler): 
    
    def on_open(self):
        pass

    def on_close(self):
        pass
    
    def on_msg(self, msg):
        global busy
        if 'join' in msg:
            client_view.connected()

        #change the busy signal when receiving message
        elif 'busy' in msg:
            if msg['busy']=="true":
                busy = True
            else:
                busy = False
        else:
            history.add_message("Agent",msg['txt'])
            client_view.print_message(msg['speak'],msg['txt'])


def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds

#process commend line instruction that the user input
def process_local_cmd(mytxt,client):
    if mytxt:
        if mytxt[0] == ":":
            cmd = mytxt[1:].lstrip().rstrip()
            for i in cmd:
                if i == "q": 
                    client.do_send({'speak': myname,'quit':"true"})
                    return "quit"
                elif i == "s": 
                    client_view.save_history()
                    history.store_message()
                elif i == "e":
                    client_view.fun_easter_egg()
                else:
                    client_view.invalid_commend(cmd)
            return ''
        else:
            return mytxt
    return mytxt

#return until whether the input is valid (1-4)
def valid_answer():
    client_view.welcome_message()
    try:
        mytxt = sys.stdin.readline().rstrip()
        userInput = int(mytxt)
        if userInput>0 and userInput<5:
            return userInput
        else:
            client_view.invalid_choice()
            return valid_answer()
    except ValueError:
        client_view.invalid_int() 
        return valid_answer()

#ask basic information about name and question about 
def ask_infor(client):
    myname = raw_input('What is your name? ')
    client.do_send({'join': myname})
    mytxt = valid_answer()
    client.do_send({'speak': myname, 'choose': mytxt})
    return myname

#initial communication between  client and agent
def communicate(client):
    while 1:
        mytxt = sys.stdin.readline().rstrip()
        mytxt = process_local_cmd(mytxt,client)
        if mytxt:
            if mytxt =="quit":
                break;
            if not busy:
                history.add_message("Me", mytxt)
                client.do_send({'speak': myname, 'txt': mytxt})


if __name__ == "__main__":
    #try extablish connection
    myname =""
    busy = False;
    host, port = 'localhost', 8888
    client = Client(host, port)              
    thread = Thread(target=periodic_poll)
    thread.daemon = True  # die when the main thread dies 
    thread.start()

    #create a model for store messages
    history = chat()

    
    sleep(1)
    if busy:
        client_view.busy()

    #try reconnect every second
    while True:
        sleep(1)
        if not busy:
            client_view.connected()
            break

    myname = ask_infor(client)
    communicate(client)
    
    



