import socket
import threading



class ThreadReception(threading.Thread):

	def __init__(self, cl):
		threading.Thread.__init__(self)
		self.cl = cl

	def run(self):
		while True:
			msg_recu = self.cl.recv(1024).decode()
			print(msg_recu)


class ThreadEmission(threading.Thread):

	def __init__(self, cl, user):
		threading.Thread.__init__(self)
		self.cl = cl
		self.user = user

	def run(self):
		while True:
			envoi = input()
			msg_envoi = "(" + self.user + ") " + envoi
			self.cl.send(msg_envoi.encode())


if __name__ == '__main__':

	s = socket.socket()
	host = '163.113.191.25'#socket.gethostname()
	port = 12345
	s.connect((host, port))

	pseudo = input("Enter your pseudo : ")
	ThE = ThreadEmission(s, pseudo)
	ThR = ThreadReception(s)
	ThE.start()
	ThR.start()

	


	