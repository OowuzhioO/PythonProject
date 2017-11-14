import uuid

def gen_Coupon(nums):
    codeList = []

    for num in range(nums):
        code = str(uuid.uuid4()).replace('-','').upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace('-', '').upper()
        codeList.append(code)

    for code in codeList:
        print(code)

if __name__ == '__main__':
    gen_Coupon(200)