welcome_message = """
Hello. Welcome to our store!
1. Question about existing products
2. Question about orders
3. Suggestions and Complaint
4. Other"""

egg = """
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \\
          |     |
         /       \\
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |"""

def reply_with_menu():
    return welcome_message

def welcome_message():
    print "Hello. Welcome to our store!"
    print "1. Question about existing products"
    print "2. Question about orders"
    print "3. Suggestions and Complaint"
    print "4. Other"


def connected():
    print "You have been connected to our spcial agent"
    print 'Enter ":q" to quit ":s" to save a copy of the chat ":e" to get a surprise'

def busy():
    print "The server is busy. Please wait......"

def fun_easter_egg():
    print egg

def print_message(sender,message):
    print sender +": " +message

def goodbye():
    print "You quit the talk, goodbye!"

def save_history():
    print "Your chat history has been saved to chat_history.txt!"