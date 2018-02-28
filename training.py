import requests
import json
import os

url_enroll = 'https://api.kairos.com/enroll'
url_gallery_view = 'https://api.kairos.com/gallery/view'
url_gallery_remove = 'https://api.kairos.com/gallery/remove'


def print_json(r):
    parsed = json.loads(r.content)
    print( json.dumps(parsed, indent=4, sort_keys=True))

#this one works without
headers = {
#   'Content-Type': 'application/json', # not sure why leaving this line in breaks the code.
  'app_id': 'a1731ed8',
  'app_key': 'd3a579a339de2805b54e53dcd72ee40c'
}

#this one works without
enroll_vals =  {
    "subject_id": "Michael-Scott",
    "gallery_name": "People"
  }


# I clearly don't quite understand how HTTP works, but this won't work without the triple quotes.
gallery_name = """
  {
    "gallery_name": "People"
  }
"""
# code to delete gallery
rem = requests.post(url_gallery_remove, data=gallery_name,headers=headers)
print_json(rem)

# Creates a list of all the subject_id in the Training set, based on the folder structure.
subject_id_list = []
with os.scandir('.\Training Set') as it:
    for dir in it:
        if dir.is_dir():
            subject_id_list.append(dir.name)

# enroll all images for each person
for subject_id in subject_id_list:
    for training_img_path in os.scandir( os.path.join( '.\Training Set',subject_id  ) ):
        with open(training_img_path.path, 'rb') as f:
            training_img = {'image': f }
            enroll_vals['subject_id'] = subject_id
            #enrollment code
            r = requests.post(url_enroll, data=enroll_vals, headers=headers, files=training_img)


# code to list faces in a gallery
face_list = requests.post(url_gallery_view, data=gallery_name,headers=headers)
print_json(face_list)