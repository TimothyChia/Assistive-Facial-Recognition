import os

index = 0
for fname in os.listdir("."):
    if fname.endswith('.py')==False:
        os.rename(fname,"test_"+str(index)+".jpg")
        index+=1