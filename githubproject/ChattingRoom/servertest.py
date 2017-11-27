# import socket, threading
# import time
#
# address = ('127.0.0.1', 9999)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # s = socket.socket()
# s.bind(address)
# s.listen(5)
# print("waiting for connection")
#
# def tcplink(sock, addr):
#     print("Accept new connect from %s:%s" %addr)
#     sock.send(b'Welcome')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print("this is :", sock)
#     print("type of sock is:", type(sock))
#     print("this is :", addr)
#     print("type of addr is :", type(addr))
#     print('connection from %s:%s closed' %addr)
#
#
# while True:
#     sock, addr = s.accept()
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()
#







# import socket,select
# import time
# import os
# #xiaorui.cc
# host = "localhost"
# port = 50000
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# s.listen(5)
# while 1:
#     print("something")
#     infds,outfds,errfds = select.select([s,],[],[],5)
#     print(type(infds))
#     print(infds)
#     if len(infds) != 0:
#         clientsock,clientaddr = s.accept()
#         # buf = clientsock.recv(8196).decode('utf-8')
#         # if len(buf) != 0:
#         #     print (buf)
#         #     os.popen('sleep 10').read()
#         clientsock.close()
#


#
import socket,time
host = socket.gethostname()
host = '127.0.0.1'
port = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
sock,addr = s.accept()
print('Connection built')
info = sock.recv(1024).decode()
while info != 'exit':
  print('MOOD:'+info)
  # send_mes = input()
  send_mes = 'server'
  sock.send(send_mes.encode())
  if send_mes =='exit':
    break
  info = sock.recv(1024).decode()
  time.sleep(10)
sock.close()
s.close()