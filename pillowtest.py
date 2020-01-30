from PIL import Image
import os 

import numpy as np

img = Image.open('Mona1.jpg')

img = img.convert("L")

img_bytes = img.tobytes()

print(img_bytes[1])

bytelist = []

for byte in img_bytes:
    if byte > 150:
        byte = 255
    else:
        byte = 0
    bytelist.append(byte)

img_bytes_new = bytes(bytearray(bytelist))

print(img_bytes[1])


# img = Image.frombytes(img.mode, img.size ,img_bytes)
img2 = Image.frombytes(img.mode, img.size ,img_bytes_new)

# img.show()
img2.show()
print("type(img_bytes) = " + str(type(img_bytes)))


## Interesting stuff

# img_b = img.convert(mode='L').show()


# bytelist = []

# for byte in bytelist:
#     if byte > 155:
#         byte = 255
#     else:
#         byte = 0
#     bytelist.append(byte)

# img_bytes = bytes(bytelist)