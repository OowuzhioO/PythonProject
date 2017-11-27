import socket,select,threading,sys

host = socket.gethostname()
port = 5964
host = "192.168.3.10"
client_addr = (host, port)


def listening(cs):
    inputs = [cs]
    while True:
        rlist, wlist, elist = select.select(inputs, [], [])
        if cs in rlist:
            try:
                print(cs.recv(1024).decode('utf-8'))
            except socket.error:
                print("socket is error")
                exit()

def speak(cs):
    while True:
        try:
            data = input()
            print("got input")
        except Exception as e:
            print("can't input")
            exit()

        try:
            cs.send(b'%s' % data)
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