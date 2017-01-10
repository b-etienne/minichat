import socket
import threading


class ThreadReception(threading.Thread):
    """
	Receiving thread
	cl : client socket
	"""
	def __init__(self, cl):
		threading.Thread.__init__(self)
		self.cl = cl

	def run(self):
		nom = self.getName()

		while True:
			msg_recu = self.cl.recv(1024).decode()

			if "EXIT" in msg_recu:
				break

			print("{}".format(msg_recu))
			msg_envoi = msg_recu.encode()

			for name in clients:
				if name != nom:					
					clients[name].send(msg_envoi)

		self.cl.close()
		del clients[name]
		print("{} left the conversation".format(name))


if __name__ == '__main__':
	clients = {}
	rep = ''

	s = socket.socket()
	host = socket.gethostname()
	port = 12345
	s.bind((host, port))

	s.listen(5)


	print("Starting Server...")

	while True:
		c, addr = s.accept()
		print("Connection from {:}".format(addr))
		th = ThreadReception(c)
		th.start()
		name = th.getName()
		clients[name] = c
		# c.send("Hello ! What is your name ?".encode())
		# data = c.recv(1024).decode()	
		# if data:	
		# 	print("Client says :: {:}".format(data))
		# 	c.send(data.encode())
		# else:
		# 	break	

	# c.close()
