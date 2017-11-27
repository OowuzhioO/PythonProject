# import socket
#
# address = ('127.0.0.1', 9999)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(address)
#
#
# print(s.recv(1024).decode('utf-8'))
#
# for data in [b'Mike', b'Tracy', b'Sarah']:
#     s.send((data))
#     print(s.recv(1024).decode('utf-8'))
#
# s.send(b'exit')
# s.close()







# import socket,select,time
# #xiaorui.cc
# host = "localhost"
# port = 50000
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((host,port))
# while True:
#     # s.send(b"coming from select client")
#     time.sleep(3)
# s.close()




#
import socket, time
s= socket.socket()
# host = socket.gethostname()
port = 9999
host = '127.0.0.1'
s.connect((host,port))
print('Linked')
info = ''
while info != 'exit':
  print('SCIENCE:'+info)
  # send_mes=input()
  send_mes = "client"
  s.send(send_mes.encode())
  if send_mes =='exit':
    break
  info = s.recv(1024).decode()
  time.sleep(2)
  # print("do not wait")
s.close()