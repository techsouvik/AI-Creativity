from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def rescale():
    im = Image.open("../inputs/car.jpg")
    size = im.size
    print(size)
    # basewidth = 50
    # wpercent = (basewidth/float(im.size[0]))
    # hsize = int((float(im.size[1])*float(wpercent)))
    # im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    # print(im.size)
    scaleFactor = 0.4
    width, height = im.size
    oneCharWidth = 10
    oneCharHeight = 18
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    print(im.size)
    outputImage = Image.new('RGB', (int(oneCharWidth * width), int(oneCharHeight * height)), color = (0, 0, 0))
    print(outputImage.size)

rescale()