with open("image","rb") as image_file: # open in binary mode.
    image = image_file.read()
    print("numbytes",len(image))


    separator = "*RDY*"
    byte_itx= 0

    # for char in separator:
    #     print(ord(char))
    # print(ord(separator[0]))
    # print(ord(separator[1]))
    # print(ord(separator[2]))
    # print(ord(separator[3]))
    # print(ord(separator[4]))


    image_start_itx = 0
    # for image_itx in range(3):
    for _ in range( len(image) ):
    # for _ in range( 100 ):    
        char = image[byte_itx]
        # print(char)
        if( char == ord(separator[0]) ):
            # print("found a candidate at",byte_itx)
            # print(image[byte_itx] )
            # print(image[byte_itx+1]  )   
            # print(image[byte_itx+2])
            # print(image[byte_itx+3]) 
            # print(image[byte_itx+4]) 


            if(
                
                image[byte_itx] == ord(separator[0])   and
                image[byte_itx+1] == ord(separator[1]) and    
                image[byte_itx+2] == ord(separator[2]) and
                image[byte_itx+3] == ord(separator[3]) and
                image[byte_itx+4] == ord(separator[4])   ):
                
                print("found a separator",byte_itx)
                image_start_itx = byte_itx
                break
        byte_itx += 1
                