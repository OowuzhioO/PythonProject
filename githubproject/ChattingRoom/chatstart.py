import threading
import queue
import time
from server import *

# message_queues = {'2': '2 is value'}
# class message:


def server_thread():
    server_start()

def sendinfo():
    while True:
        for sock, q in message_queues.items():
            if not q.empty():
                str = q.get_nowait()
                # sock.send(b'%s' % str)
                sock.send(str.encode())
        time.sleep(1)


if __name__ == '__main__':
    # s = server('127.0.0.1', 9999)
    # s.serverstart()
    # server_start()
    t = threading.Thread(target=server_thread)
    t.start()
    # while True:
    #     print(message_queues)
    #     time.sleep(3)

    t2 = threading.Thread(target=sendinfo())
    t2.start()