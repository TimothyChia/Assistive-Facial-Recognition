# https://petrimaki.com/2013/04/28/reading-arduino-serial-ports-in-windows-7/
# http://pyserial.readthedocs.io/en/latest/pyserial_api.html
# have to use time.sleep() if you're trying to debug using print(). print is too slow.
# set timeout=None to stop read from returning early.
# see Python bytes type. note that a bytes object is a sequence. not a byte.

import serial
import time
from PIL import Image
import os

# ser = serial.Serial('COM4', 1000000, timeout=None)  # open serial port
ser = serial.Serial('COM4', 115200, timeout=None)  # open serial port
print(ser.name)         # check which port was really used
# ser.write(b'hello')     # write a string

# checking if the whole image can be read
# while(1):
#     image = ser.read(320*240) # this is 76,800. However the serial buffer seems to be only about 12,300.
#     print(len(image))
#     time.sleep(1)

# attempting to parse the stream one byte at a time until the separator is encountered.
# seems to be prone to the entire image occasionally sliding to the left/right?
# separator = "*RDY*"
# for char_sep in separator:
#     while(1):
#         char = ser.read(1)
#         if( char[0] == ord(char_sep) ):
#             break
# # print("found the separator")
# image = ser.read(320*240) # this is 76,800. However the serial buffer seems to be only about 12,300.
# with open("image","wb") as image_file: # open in binary mode.
#     image_file.write(image)

# # This version simply reads in more bytes than 2 images combined, then searches for the first seperator.
# # shifting is still occuring. Seems like the VSYNC or HREF on the camera must be behaving strangely.
# time.sleep(5)# unclear if the pyserial is resetting the arduino everytime this py file is executed. attempting to let it run for a while. did not seem to help with exposure or shifting problems.
# ser.reset_input_buffer() # ah forgot to do this after sleeping.

# image = ser.read(10* 320*240 + 500) # 500 is an arbitrary amount for the other random stuff being sent
# separator = "*RDY*"
# byte_itx= 0

# for image_itx in range(8):
#     for char_sep in separator:
#         while(1):
#             char = image[byte_itx]
#             byte_itx += 1
#             if( char == ord(char_sep) ):
#                 break
#     image_frame = image[byte_itx:byte_itx+320*240]
    
# with open("image","wb") as image_file: # open in binary mode.
#     image_file.write(image_frame)


# Yet another version for many frames and built in image output.
# This version simply reads in more bytes than 2 images combined, then searches for the first seperator.
# shifting is still occuring. Seems like the VSYNC or HREF on the camera must be behaving strangely.
# by printint byte_itx, can confirm the #bytes between seperators is sometimes far less than 76,800
# this is probably because of the way I was looking for the separator.
# can confirm, it was actually just "finding" it on random bytes which corresponded to pixels
# need to look for the consecutive sequence *RDY*, while my code just looked for the sequence, allowing any #bytes in between chars.

# time.sleep(5)# unclear if the pyserial is resetting the arduino everytime this py file is executed. attempting to let it run for a while. did not seem to help with exposure or shifting problems.
# ser.reset_input_buffer() # ah forgot to do this after sleeping.

# image = ser.read(10* 320*240 + 500) # 500 is an arbitrary amount for the other random stuff being sent
# separator = "*RDY*"
# byte_itx= 0
# size = (320,240)

# with open("image","wb") as image_file: # open in binary mode.
#     image_file.write(image)

# for image_itx in range(8):
#     for char_sep in separator:
#         while(1):
#             char = image[byte_itx]
#             byte_itx += 1
#             if( char == ord(char_sep) ):
#                 break
#         print(byte_itx)        
#     image_frame = image[byte_itx:byte_itx+320*240]
#     print(byte_itx)

#     path = os.path.join( 'converted'+str(image_itx)+'.jpg' ) 
#     converted = Image.frombytes("L", size,image_frame )
#     converted.save(path)


## Final version hopefully
# was incrementing byte_itx too early, so it could never find the string. now fixed.
# image = ser.read(8 * 320*240 + 500) # 500 is an arbitrary amount for the other random stuff being sent
# image = ser.read(38900) # 500 is an arbitrary amount for the other random stuff being sent 8 * 320*240/16  + 500
image = ser.read(90000) # a little over 6 80 by 60 images.
print("serial read finished")
# print("image is", len(image))

separator = "*RDY*"
byte_itx= 0
# size = (320,240)
size = (80,60)

print(len(image))

with open("image","wb") as image_file: # open in binary mode.
    image_file.write(image)
image_start_itx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for image_itx in range(12):
    while byte_itx <  len(image) :
        # print(byte_itx)
        char = image[byte_itx]
        if( char == ord(separator[0]) ):
            # print("found a candidate at",byte_itx)
            if(
                
                image[byte_itx] == ord(separator[0])   and
                image[byte_itx+1] == ord(separator[1]) and    
                image[byte_itx+2] == ord(separator[2]) and
                image[byte_itx+3] == ord(separator[3]) and
                image[byte_itx+4] == ord(separator[4])   ):
                
                print("found a separator",byte_itx)
                byte_itx += 5 # forgot this earlier. skip the *RDY* now that it's been found.                
                
                image_start_itx[image_itx] = byte_itx
                # image_frame = image[byte_itx:byte_itx+320*240]                
                image_frame = image[byte_itx:byte_itx+80*60]                
                path = os.path.join( 'converted'+str(image_itx)+'.jpg' ) 
                converted = Image.frombytes("L", size,image_frame ) # decoder = raw by default.
                converted.save(path)
                print(image_start_itx)        
                print(byte_itx)
                byte_itx += 1                
                break
        byte_itx += 1
    



ser.close()             # close port


# import serial
# import time
# ser = serial.Serial('COM4', 1000000, timeout=0)
 
# while 1:
#     try:
#         # print( ser.readline())
#         image = ser.read(320*240)
#         print(image)
#         time.sleep(1)
#     except serial.SerialTimeoutException:
#         print('Data could not be read')
#         time.sleep(1)
