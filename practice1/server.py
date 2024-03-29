import threading
import socket
import argparse
import os

class Server(threading.Thread):

    def __init__(self,host,port):
        super().__init__()
        self.connections = []
        self.host = host
        self.port = port

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host,self.port))

        sock.listen(1)
        print('Listening at', sock.getsockname())

        while True:


            sc, sockname = sock.accept()
            print('Accepted a new connection from {} to {}'.format(sc.getpeername(),sc.getsockname()))
            server_socket = ServerSocket(sc,sockname,self)
            server_socket.start()

            self.conections.append(server_socket)
            print('Ready to receive messages from', sc.getpeername())


    def broadcast(self,message,source):

        for connection in self.connections:

            if connection.sockname != source:
                connection.send(message)


class ServerSocket(threading.Thread):

    def __init__(self,sc,sockname,server):
        super().__init__()
        self.sc = sc
        self.sockname = sockname
        self.server = server

    def run(self):

        while True:
            message = self.sc.recv(1024).decode('ascii')
            if message:
                print('{} says {!r}'.format(self.sockname,message))
                self.server.broadcast(message,self.getsockname)
            else:
                print('{} has closed the connection'.format(self.sockname))
                self.sc.close()
                server.remove_connection(self)
                return

    def send(self,message):
        self.sc.sendall(message.encod('ascii'))

def exit(server):

    while True:
        ipt = input('')
        if ipt == 'q':
            print('Closing all connections...')
            for connection in server.connections:
                connect.sc.close()

            print('Shutting down the server...')
            os.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chatroom Server')
    parser.add_argument('host',help='Interface the servr listens at')
    parser.add_argument('-p',metavar='PORT',type=int,default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    server = Server(args.host, args.p)
    server.start()

    exit = threading.Thread(target = exit, args = (server,))
    exit.start()
