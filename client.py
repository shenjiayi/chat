from network import Handler, poll
import sys
from threading import Thread
from time import sleep
import json
import view
from model import chat

myname = raw_input('What is your name? ')

class Client(Handler):
    def on_open(self):
        view.welcome_message()

    def on_close(self):
        pass
    
    def on_msg(self, msg):
        if 'join' in msg:
            view.connected()
        else:
            history.add_message("Agent",msg['txt'])
            view.print_message(msg['speak'],msg['txt'])

        
host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': myname})

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()
history = chat()

#get info about what question the customer has
mytxt = sys.stdin.readline().rstrip()
client.do_send({'speak': myname, 'txt': mytxt})
view.connected()



while 1:
    mytxt = sys.stdin.readline().rstrip()
    if mytxt == ":e":
        view.fun_easter_egg()
    elif mytxt ==":q":
        view.goodbye()
        break
    elif mytxt ==":s":
        view.save_history()
        history.store_message()
    else:
        history.add_message("Me",mytxt)
        client.do_send({'speak': myname, 'txt': mytxt})