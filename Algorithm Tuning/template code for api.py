#!/usr/bin/python

import requests
import json

url_enroll = 'https://api.kairos.com/enroll'
url_recognize = 'https://api.kairos.com/recognize'
url_gallery_list = 'https://api.kairos.com/gallery/list_all'
url_gallery_view = 'https://api.kairos.com/gallery/view'
url_view_subject = 'https://api.kairos.com/gallery/view_subject'
url_gallery_remove = 'https://api.kairos.com/gallery/remove'



def print_json(r):
    parsed = json.loads(r.content)
    print( json.dumps(parsed, indent=4, sort_keys=True))

# I clearly don't quite understand how HTTP works, but this won't work without the triple quotes.
gallery_name = """
  {
    "gallery_name": "People"
  }
"""
# this one works without
recognize =  {
    "gallery_name": "People",
    "threshold":"0"
  }

# this one works with the triple quotes
view_subject ="""
    {
    "subject_id": "Michael-Scott",
    "gallery_name": "Office"
    } """

#this one works without
enroll_vals =  {
    "subject_id": "Michael-Scott",
    "gallery_name": "Office"
  }

#this one works without
headers = {
#   'Content-Type': 'application/json', # not sure why leaving this line in breaks the code.
  'app_id': 'a1731ed8',
  'app_key': 'd3a579a339de2805b54e53dcd72ee40c'
}

#test 6 passes. test 3-5 do not.  Returns 
# files = {'image': open('fromAndroidCamera.jpg', 'rb')}


#enrollment code
# r = requests.post(url_enroll, data=enroll_vals, headers=headers, files=files)
# parsed = json.loads(r.content)
# print( json.dumps(parsed, indent=4, sort_keys=True))

# this does work. content is byte format.
# parsed = json.loads(r.content)
# print( json.dumps(parsed, indent=4, sort_keys=True))
 
# seems to return the python dictionary which is the json-encoded content of the response
# parsed = r.json()
# print(parsed["face_id"])

# code to see what galleries exist
# gal_list = requests.post(url_gallery_list,headers = headers)
# print(gal_list.text)

# code to list faces in a gallery
face_list = requests.post(url_gallery_view, data=gallery_name,headers=headers)
# print(face_list.text)
print_json(face_list)

# code to view something about a subject?
# subject = requests.post(url_view_subject,data = view_subject, headers=headers)
# parsed = json.loads(subject.content)
# print( json.dumps(parsed, indent=4, sort_keys=True))
# print(subject.text)

# code to delete gallery
# rem = requests.post(url_gallery_remove, data=gallery_name,headers=headers)
# print(rem.text)

# code to recognize a person
# subject = requests.post(url_recognize,data = recognize, headers=headers,files=files)
# print_json(subject)
# print(subject.json()["images"][0]["transaction"])
# print(subject.json()["images"]["transaction"]["confidence"])
# ["subject_id"]