import socket,select

host = socket.gethostname()
port = 5964
host = "192.168.3.10"
server_addr = (host, port)
print(server_addr)

inputs = []
fd_name = {}

def serverInit():
    ss = socket.socket()
    ss.bind(server_addr)
    ss.listen(10)
    return ss


def newConnection(ss):
    client_conn, client_addr = ss.accept()
    try:
        client_conn.send(b'welcome to chatroom, please set up your name!')
        client_name = client_conn.recv(1024).decode('utf-8')
        inputs.append(client_conn)
        fd_name[client_conn] = client_name
        str_helper = ''
        for v in fd_name.values():
            v = v + ' '
            str_helper = str_helper + v

        str = 'current members in chatting room are: %s' % str_helper
        client_conn.send(b'%s' % str)

        for other in fd_name.keys():
            if other != client_conn and other != ss:
                other.send(fd_name[client_conn] + " joined the chatroom")
                str = fd_name[client_conn] + " joined the chatroom"
                other.send(b'%s' % str)
    except Exception as e:
        print(e)

def run():
    ss = serverInit()
    inputs.append(ss)
    print('server is running, waiting for clinet')
    while True:
        rlist, wlist, elist = select.select(inputs, [], [])

        if not rlist:
            print('time out ...')
            ss.close()
            break
        for r in rlist:
            if r is ss:
                newConnection(ss)
            else:
                disconnect = False

                try:
                    data = r.recv(1024).decode('utf-8')
                    data = fd_name[r] + " : " + data

                except socket.error:
                    data = fd_name[r] + "leaved the room"
                    disconnect = True

                else:
                    pass

                if disconnect:
                    inputs.remove(r)
                    print(data)
                    for other in inputs:
                        if other != ss and other != r:
                            try:
                                other.send(b'%s' % data)
                            except Exception as e:
                                print(e)
                            else:
                                pass

                        del fd_name[r]
                else:
                    print(data)
                    for other in inputs:
                        if other != ss and other != r:
                            try:
                                other.send(b'%s' % data)
                            except Exception as e:
                                print(e)

if __name__ == "__main__":
    run()