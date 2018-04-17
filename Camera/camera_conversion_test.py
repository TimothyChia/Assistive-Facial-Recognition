# assuming you've captured the binary output of the camera, now tries to convert it.
from PIL import Image

size = (320,240)

with open("image","rb") as image_file: # open in binary mode.
    image_bytes = image_file.read()
    print(len(image_bytes))
    converted = Image.frombytes("L", size,image_bytes )
    converted.save('converted.bmp')

