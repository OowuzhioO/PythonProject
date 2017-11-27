import socket,select,threading,sys
import time

host = socket.gethostname()
port = 5966
host = "10.194.36.188"
client_addr = (host, port)


def listening(cs):
    while True:
        data = cs.recv(1024).decode('utf-8')
        print(data)
        time.sleep(1)

def speak(cs):
    while True:
        try:
            data = input()
            print("got input")
        except Exception as e:
            print("can't input")
            exit()

        try:
            # cs.send(b'%s' % data)
            cs.send(data.encode())
            print("send successfully")
        except Exception as e:
            exit()


def main():
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect(client_addr)
    # data = cs.recv(1024).decode('utf-8')
    # print("data from server", data)
    # cs.send(b'this is client')
    t = threading.Thread(target=listening, args=(cs,))
    t.start()

    t1 = threading.Thread(target=speak, args=(cs,))
    t1.start()

if __name__ == "__main__":
    main()