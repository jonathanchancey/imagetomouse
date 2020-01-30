from PIL import Image
import os 
import numpy as np

def imageToList(imagename):
    img = Image.open(imagename)
    img = img.convert("L")
    img_bytes = img.tobytes()

    bytelist = []
    for byte in img_bytes:
        if byte > 150:
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


if __name__ == '__main__':
    imageToList('Mona1.jpg')


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