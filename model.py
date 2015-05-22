import time

class chat:
	def __init__(self):
		self.chat = []

	def add_message(self,sender,message):
		sentence = "["+time.asctime()+"]" + "\n" + sender +": "+message
		self.chat.append(sentence)

	def store_message(self):
		f = open("chat_history.txt","w")
		f.write("Chat history:\n")
		for message in self.chat:
			f.write(message)
			f.write("\n")