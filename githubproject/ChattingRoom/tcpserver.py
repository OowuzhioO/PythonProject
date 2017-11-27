import threading
import socket

class server():
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.client_exist = {}
        self.client_names = []
        self.server_addr = (host, port)

    def serverInit(self):
        ss = socket.socket()
        ss.bind(self.server_addr)
        ss.listen(10)
        return ss


    def serverstart(self):
        # print(self.client_exist)
        # print(self.client_names)
        # print(self.server_addr)

        ss = self.serverInit()
        print("server is running, waiting for clients...")

        while True:
            sock, addr = ss.accept()

            t = self.client_join_thread(sock, addr)
            # t = threading.Thread(target=client_join, args=(sock, addr))
            t.start()

        client_exist.clear()
        client_names.clear()
        ss.close()



if __name__ == '__main__':
    s = server('127.0.0.1', 9999)
    s.serverstart()