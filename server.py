import pickle
import socket
import threading
from _thread import *
from Snake import *

class Server:
    def __init__(self):
        self.ServerSocket = socket.socket()
        self.host = 'localhost'
        self.port = 5000
        self.ThreadCount = 0
        try:
            self.ServerSocket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))

        print('Waitiing for a Connection..')
        self.ServerSocket.listen(10)
        self.barrier = threading.Barrier(2)
        self.run()
    def run(self):
        while True:
            try:
                Client, address = self.ServerSocket.accept()
            except:
                continue
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            self.ThreadCount += 1
            start_new_thread(self.threaded_client, (Client,))

    def threaded_client(self,connection):

        global lost_1, lost_2
        global data_1, data_2
        data_2, data_1 = False, False
        lost_1, lost_2 = False, False
        thread_id = self.ThreadCount
        if thread_id == 1:
            self.setup_TCP_board()
        connection.send(str.encode(str(thread_id)))
        connection.send(pickle.dumps(self.pole))
        self.barrier.wait()
        connection.recv(1024).decode()
        self.barrier.wait()
        connection.send(str.encode("True"))
        self.barrier.wait()

        while not lost_1 and not lost_2:
            if thread_id == 1:
                data_1 = connection.recv(1024).decode()
                if data_1 == False:
                    data_1 = []
            self.barrier.wait()
            if thread_id == 2:
                data_2 = connection.recv(1024).decode()
                if data_2 == False:
                    data_2 = []
                if len(data_1) > 2:
                    lost_1 = ruch(self.pole, self.snake_1, self.owoc, data_1[-3], 1)
                if len(data_2) > 2:
                    if data_2[-3] == 'm':
                        move = 'c'
                    elif data_2[-3] == 'b':
                        move = 'z'
                    elif data_2[-3] == 'g':
                        move = 'a'
                    elif data_2[-3] == 'j':
                        move = 'd'
                    elif data_2[-3] == 't':
                        move = 'q'
                    elif data_2[-3] == 'u':
                        move = 'e'
                    lost_2 = ruch(self.pole, self.snake_2, self.owoc, move, 2)
            self.barrier.wait()
            connection.sendall(pickle.dumps(self.pole))
            self.barrier.wait()
        connection.close()
        self.ThreadCount = 0

    def setup_TCP_board(self):
        self.pole = Pole(70, 25)
        valid = False
        while not valid:
            x = random.randint(1, self.pole.x - 1)
            y = random.randint(1, self.pole.y - 1)
            valid, self.owoc = is_valid([x, y], 1, self.pole, 'owoc', 0)

        valid = False
        while not valid:
            x = random.randint(1, self.pole.x - 1)
            y = random.randint(1, self.pole.y - 1)
            valid, self.snake_1 = is_valid([x, y], 1, self.pole, 'snake', 1)

        valid = False
        while not valid:
            x = random.randint(1, self.pole.x - 1)
            y = random.randint(1, self.pole.y - 1)
            valid, self.snake_2 = is_valid([x, y], 1, self.pole, 'snake', 2)
server = Server()