# fd_name = {'client_conn': 'hello' , '123': 'hihihi'}
# str = fd_name['client_conn'] + " joined the chatroom"
#
# str_helper = ''
# for v in fd_name.values():
#     # print(v)
#     # print(type(v))
#     v = v + ' '
#     str_helper = str_helper + v
# str = 'current members in chatting room are: %s' % str_helper
# str = b'%s' % str
#
# str = b'hello'
# print(str.decode('utf-8'))
# print(type(str))
# #
# # print(fd_name.values())

#
# for data in [b'Mike', b'Tracy', b'Sarah']:
#     print(data)
#     print(type(data))
#     data.decode()
#     print(data)
#     print(type(data))


# str = b'abcde'
# print(str)
#
# str1 = str.decode('utf-8')
# print(str.decode('utf-8'))



# inputs = []


import queue

message_queue = {}
message = 'qwer'
message_queue[1] = queue.Queue()
message_queue[1].put(message)

# print(message_queue[1].get_nowait())
print(type(message_queue[1].get_nowait()))