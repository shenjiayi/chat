def client_leave():
    print "the client leave"


def client_join(client):
    print client + " join the chat room!"


def print_message(sender,message):
    print sender +": " +message


def process(client, choice):
    if choice =="1":
        print client + " have question about existing products"
    elif choice=="2":
        print client + " have question about orders"
    elif choice== "3":
        print client + " have suggestions and complaint"
    else:
        print client +  " have general questions"