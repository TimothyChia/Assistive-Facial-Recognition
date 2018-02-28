import requests
import json
import os

url_recognize = 'https://api.kairos.com/recognize'
url_gallery_view = 'https://api.kairos.com/gallery/view'


def print_json(r):
    parsed = json.loads(r.content)
    print( json.dumps(parsed, indent=4, sort_keys=True))

#this one works without
headers = {
#   'Content-Type': 'application/json', # not sure why leaving this line in breaks the code.
  'app_id': 'a1731ed8',
  'app_key': 'd3a579a339de2805b54e53dcd72ee40c'
}

# this one works without
data_recognize =  {
    "gallery_name": "People"
  }

# I clearly don't quite understand how HTTP works, but this won't work without the triple quotes.
gallery_name = """
  {
    "gallery_name": "People"
  }
"""

# Creates a list of all the true subject_id in the Testing set, based on the folder structure.
subject_id_list_true = []
with os.scandir('.\Testing Set') as it:
    for dir in it:
        if dir.is_dir():
            subject_id_list_true.append(dir.name)

subject_id_recognized = {}
# recognize all images for each person
# not sure what would happen if there were multiple test images in a person's folder. check later?
for subject_id in subject_id_list_true:
    for testing_img_path in os.scandir( os.path.join( '.\Testing Set',subject_id  ) ):
        with open(testing_img_path.path, 'rb') as f:
            test_img = {'image': f }
            subject_id_recognized[subject_id] = requests.post(url_recognize,data = data_recognize, headers=headers,files=test_img)

for subject in subject_id_recognized:
    print_json(subject_id_recognized[subject])