from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from api import search
import math
from File import filecount, clear_files


def ascii_art(num):
    print('------------------------------------------------------')

    # chars = "#Wo- "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256

    scaleFactor = 0.4

    oneCharWidth = 10
    oneCharHeight = 18

    def getChar(inputInt):
        return charArray[math.floor(inputInt*interval)]

    text_file = open("./outputs/metadata"+str(num)+".bin", "w")

    add = './inputs/api_outputs/nft_input'+str(num)+'.jpg'

    im = Image.open(add)
    # im.resize((100,100))
    fnt = ImageFont.truetype('firacode.ttf', 15)

    width, height = im.size

    # basewidth = 50
    # wpercent = (basewidth/float(im.size[0]))
    # hsize = int((float(im.size[1])*float(wpercent)))
    # im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    # # im=im.resize(resi, Image.ANTIALIAS)

    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

        text_file.write('\n')

    outputImage = ImageEnhance.Brightness(outputImage).enhance(1.2)
    outputImage = ImageEnhance.Color(outputImage).enhance(5)
    outputImage = ImageEnhance.Sharpness(outputImage).enhance(0.5)
    outputImage.save('./outputs/nft'+str(num)+'.jpg')
    print("NFT"+str(num)+" created")
# print(ascii.charlist())




print('------------------------------------------------------------------------------')
token = input("\nEnter your token: ")
max_results = int(input("Enter the max number of NFTs: "))
print('\n------------------------------------------------------------------------------')

#Searching and saving the input images
clear_files('./inputs/api_outputs')
clear_files('./outputs')
search(token,max_results)
files=filecount('./inputs/api_outputs')

check = input("Add Characters? (y/n): ")

if (check=='y' or check=='Y'):
    chars=input("Enter characters to be added: ")
else:
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

for i in range(files):
    ascii_art(i)
print("Done! Enjoy!")


