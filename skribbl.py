from PIL import Image
import os 
import numpy as np
from pynput.mouse import Button, Controller
import time 

IMAGERESDIV = 20
IMAGESPACING = 4

# TODO add invert option
# TODO add gui with options and preview

def imageToList(imagename):
    img = Image.open(imagename) # opens the image as RGB
    img = img.convert("L") # converts the image to 8-bit pixels, black and white
    imgsize0 = int(img.size[0]/IMAGERESDIV)
    imgsize1 = int(img.size[1]/IMAGERESDIV)
    
    img = img.resize((imgsize0, imgsize1))
    img_bytes = img.tobytes() 
    
    
    bytelist = []
    for byte in img_bytes:
        if byte > 180:
            byte = 255
        else:
            byte = 0
        bytelist.append(byte)

    # arr = np.arange(img.size[0],img.size[1]).reshape(img.size[0],img.size[1])

    np_bytes_arr = np.array(bytearray(bytelist)).reshape(img.size[1],img.size[0])

    print(np_bytes_arr[:,:5])

    img_bytes_new = bytes(bytearray(bytelist))
    print(img_bytes[1])

    img2 = Image.frombytes(img.mode, img.size ,img_bytes_new)
    img2.show()
    print("type(img_bytes) = " + str(type(img_bytes)))

    return np_bytes_arr

def mouseMover(npr):
    mouse = Controller()
    # print("mouse.position() = " + mouse.position())

    # mouse to follow a printing like pattern draw an x then increment y
    print("about to use the mouse")
    print("sleeping for 3 seconds")
    time.sleep(3)

    # og_mpos = mouse.position()


    # TODO swap x and y because they're swapped
    for x in range(len(npr)):
        for y in range(len(npr[x])):
            mouse.move(IMAGESPACING,0) # move the mouse right 1 pixel on the x axis
            if (npr[x][y] == 0):
                # print("x,y = {},{}".format(x,y))
                mouse.click(Button.left, 1)
        
        resetxunitsback = -1 * int(len(npr[x])*IMAGESPACING)
        mouse.move(resetxunitsback, IMAGESPACING) 

def convertToFauxcode(npr):
    pass

def runFauxcode(npr):
    pass

    # # swap x and y because they're swapped
    # for x in range(len(npr)):
    #     if (x % 5 == 0):
    #         for y in range(len(npr[x])):
    #             mouse.move(1,0) # move the mouse right 1 pixel on the x axis

    #             if (y % 5 == 0):
    #                 if (npr[x][y] == 0):
    #                     print("x,y = {},{}".format(x,y))
    #                     mouse.click(Button.left, 1)
    #         resetxunitsback = -1 * len(npr[x])
    #         mouse.move(resetxunitsback, 5) 


if __name__ == '__main__':
    # npr = imageToList('Mona1.jpg')
    npr = imageToList('image.jpg')
    mouseMover(npr)




# # Concept Test

# >>> import random
# >>> import numpy as np
# >>> bytearray(random.getrandbits(8) for _ in range(3 * 4))
# bytearray(b'g?\x7fgQ\x1fdVJ\x8e\xcay')
# >>> rgb = bytearray(random.getrandbits(8) for _ in range(3 * 4))
# >>> rgb
# bytearray(b'\xff\x8d#\xeb\xfb^\x93\xee\x8a\xd9lT')
# >>> np.array(rgb)
# array([255, 141,  35, 235, 251,  94, 147, 238, 138, 217, 108,  84],
#       dtype=uint8)
# >>> np.array(rgb).reshape(4,3)
# array([[255, 141,  35],
#        [235, 251,  94],
#        [147, 238, 138],
#        [217, 108,  84]], dtype=uint8)




# eventally want to be able to have the use specify the image and the drawing area from gui or clicking
