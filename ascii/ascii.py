from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from ascii.api import search
import math
from ascii.File import filecount, clear_files
from ascii.colormanage import manage

def ascii_art(num,ch):
    print('------------------------------------------------------')
    print("Generating ASCII art for image number {}".format(num))
    chars=ch
    # chars = "#Wo- "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256

    scaleFactor = 0.4

    oneCharWidth = 10
    oneCharHeight = 18

    def getChar(inputInt):
        return charArray[math.floor(inputInt*interval)]

    text_file = open("./outputs/metadata/metadata"+str(num)+".bin", "w")

    add = './inputs/nft_input'+str(num)+'.jpg'

    im = Image.open(add)
    # im.resize((100,100))
    fnt = ImageFont.truetype('ascii/firacode.ttf', 15)

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

    outputImage = manage(outputImage)
    outputImage.save('./outputs/nft'+str(num)+'.jpg')
    print("NFT"+str(num)+" created")
# print(ascii.charlist())



def run(tokex, maxn, ch):
    print('------------------------------------------------------------------------------')
    token = tokex
    print("Token : "+ token)
    max_results = maxn
    print("Number of NFTs in progress : "+ str(max_results))

    #Searching and saving the input images
    clear_files('./inputs')
    clear_files('./outputs')
    clear_files('./outputs/metadata')
    search(token,max_results)
    files=filecount('./inputs')

    chars = "$@B%8&WM#*"+("oahkbdpqwmZO0QLCJUYXzcvunxrjft").upper()+"/\\|()1{}[]?-_+~<>i!lI"[::-1]
    addon=ch.upper()
    chars += addon
    print('Characters used : '+chars)
    print('------------------------------------------------------------------------------')

    
    for i in range(files):
        ascii_art(i,chars)
    print("Done! Enjoy!")


if __name__ == '__main__':
    run()