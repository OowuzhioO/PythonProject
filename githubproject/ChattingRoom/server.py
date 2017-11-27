import socket,threading
import time
import queue
from chatstart import *

port = 5966
host = "10.194.36.188"
server_addr = (host, port)
print(server_addr)

client_exist = {}
client_names = []

message_queues = {}


def serverInit():
    ss = socket.socket()
    ss.bind(server_addr)
    ss.listen(10)
    return ss

class client_join_thread(threading.Thread):

    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr

    # def

    def run(self):
        global client_names
        global client_exist
        global message_queues
        self.sock.send(b'welcome to chatroom, please set up your name!')
        client_name = self.sock.recv(1024).decode('utf-8')
        client_exist[self.sock] = client_name
        client_names.append(client_name)
        print(client_name)
        str_helper = ''
        for v in client_exist.values():
            v = v + ' '
            str_helper = str_helper + v
        str = 'current members in chatting room are: %s' % str_helper
        # self.sock.send(b'%s' % str)
        self.sock.send(str.encode())
        while True:
            self.sock.send(b'set up your friend name')
            friend = self.sock.recv(1024).decode('utf-8')
            if friend in client_exist:
                self.sock.send(b'you guys can talk to each other')
                break
            else:
                self.sock.send(b'your friend is not online')

        while True:
            message = self.sock.recv(1024).decode('utf-8')
            message_queues[self.sock] = queue.Queue()
            message_queues[self.sock].put(message)
            print(client_name, "says: ", message)


# def client_join(sock, addr):
#     print("client join circle")
#     sock.send(b'Hi, client, we can talk to each other now')
#     while True:

def test():
    global message_queues
    for i in range(100):
        message_queues[i] = 'test queues'
        time.sleep(1)
    print("this is a test")

def server_start():
    ss = serverInit()
    print("server is running, waiting for clients...")

    while True:
        sock, addr = ss.accept()

        t= client_join_thread(sock, addr)
        # t = threading.Thread(target=client_join, args=(sock, addr))
        t.start()

    client_exist.clear()
    client_names.clear()
    ss.close()

    # test()


if __name__ == "__main__":
    server_start()