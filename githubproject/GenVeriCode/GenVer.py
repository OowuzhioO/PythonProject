from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random

def genColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def genChar():
    return random.choice(string.ascii_letters)

def genCharColor():
    return (random.randint(32, 127), random.randint(32, 127),random.randint(32, 127))

def genCode():
    width = 60 * 4
    height = 60

    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill = genColor())

    for i in range(4):
        draw.text((i * 60 + 10, 10), genChar(), fill = genCharColor(), font = font)
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')




if __name__ == '__main__':
    genCode()
    # print(genColor())