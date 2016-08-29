from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('Futura.ttf', size=int(x / 3))
    draw = ImageDraw.Draw(img)
    draw.text((2 * x / 3, 0), str(num), font=myfont, fill='blue')
    img.save('{}_withnum.jpg'.format(picPath))


def randChar():
    return chr(random.randint(65, 90))


def randColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def randColor2():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def creatP():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Futura.ttf', 40)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randColor())
    for t in range(4):
        draw.text((60 * t + 10, 10), randChar(), font=font, fill=randColor2())

    # blur
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


if __name__ == '__main__':
    #add_num('100.png', 99)
    creatP()
