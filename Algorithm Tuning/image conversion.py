from PIL import Image
import os

index = 0



with os.scandir('BMP Images') as subjects:
    for subject in subjects:
        if subject.is_dir():
            index = 0
            with os.scandir( subject.path ) as subject_images:
                for subject_image in subject_images:
                    index += 1
                    # print(subject.name)
                    img = Image.open(subject_image.path )
                    path = os.path.join( 'JPG Images',subject.name,subject.name+str(index)+'.jpg' ) 
                    # print(path)
                    img.save(path,'jpeg')





