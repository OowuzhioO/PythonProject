


# with open('coupon.txt', 'r') as file:
#     for line in file:
#         print(line)
#
# fo = open("coupon.txt", "r")
# print ("Name of the file: ", fo.name)
#
# # Assuming file has following 5 lines
# # This is 1st line
# # This is 2nd line
# # This is 3rd line
# # This is 4th line
# # This is 5th line
# #
# # line = fo.readlines()
# # print ("Read Line: %s" % (line))
#
# # line = fo.readlines(2)
# # print ("Read Line: %s" % (line))
#
# # for line in fo:
# #     line = line.split('=')[0]
# #     print(line)
#
#
#
# # Close opend file
# fo.close()

DB_info = {
    'database': 'mysql',
    'database_driver': 'mysqlconnector',
    'user': 'test',
    'passward': 'testpw',
    'ip': '127.0.0.1',
    'port': '3306',
}

str = '{database}+{database_driver}://{user}:{passward}@{ip}:{port}/{database}'.format_map(DB_info)
print(type(str))

print('{database}+{database_driver}://{user}:{passward}@{ip}:{port}/{database}'.format_map(DB_info))