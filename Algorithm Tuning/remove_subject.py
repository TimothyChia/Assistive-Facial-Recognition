import requests
import json

def print_json(r):
    parsed = json.loads(r.content)
    print( json.dumps(parsed, indent=4, sort_keys=True))


url_gallery_remove_subject = 'https://api.kairos.com/gallery/remove_subject'

# this one needs """"
subject_vals =  """{
    "subject_id": "Timothy Chia",
    "gallery_name": "People"
  }"""

#this one works without
headers = {
#   'Content-Type': 'application/json', # not sure why leaving this line in breaks the code.
  'app_id': 'a1731ed8',
  'app_key': 'd3a579a339de2805b54e53dcd72ee40c'
}

r = requests.post(url_gallery_remove_subject, data=subject_vals, headers=headers)
print_json(r)