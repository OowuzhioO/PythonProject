import base64

coupon = {
    'id': '1234',
    'good': '0001',
}


def get_all():
    for i in range(1000, 1200):
        c_code = gen_coupon(str(i), str(int(i/2)))
        save_coupon(c_code)

def gen_coupon(id, good):
    coupon['id'] = id
    coupon['good'] = good
    raw = '/'.join(k + ':' + v for k, v in coupon.items())
    raw64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
    c_code = raw64.decode()
    return c_code

def save_coupon(c_code):
    with open('coupon.txt', 'a+') as file:
        file.write(c_code + '\n')

def show_coupon(c_code):
    print("coupon code： ", c_code)

def parse_coupon(c_code):
    print("parse code: ", base64.urlsafe_b64decode(c_code.encode('utf-8')))

if __name__ == "__main__":
    get_all()