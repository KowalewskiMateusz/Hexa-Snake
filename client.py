from __future__ import print_function
import socket
import pickle

class Client:
    def __init__(self,host,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.client_number = self.s.recv(1024).decode()
        self.pole = self.s.recv(20000)
        self.pole = pickle.loads(self.pole)
        self.s.send(str.encode("Ready"))

    def send_mes(self,mes):
        self.s.send(str.encode(str(mes)))

    def recv_mes(self):
        return self.s.recv(1024).decode()

    def recv_pole(self):
        self.pole = self.s.recv(20000)
        self.pole = pickle.loads(self.pole)
        return self.pole
