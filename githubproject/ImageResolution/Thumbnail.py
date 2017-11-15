import os
from PIL import Image

ext = ['jpg', 'jpeg', 'png']

files = os.listdir('.')

def redResolution(file, count):
    name = str(count) + 'jpeg'
    image = Image.open(file)
    image.thumbnail((1136, 640))
    print(image.format, image.size, image.mode)
    image = image.convert("RGB")
    image.save(name, 'JPEG')

if __name__ == '__main__':
    # imag = Image.open('0.png')
    # print(imag.size)
    count = 0
    for file in files:
        if file.split('.')[-1] in ext:
            # print(file)
            count += 1
            redResolution(file, count)