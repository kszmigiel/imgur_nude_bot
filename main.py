import string
import random

import requests

BASE_URL = 'https://i.imgur.com/'

def get_url():
    counter = 0
    url_hash = ''
    while counter < 5:
        random_letter = random.choice(string.ascii_letters)
        url_hash += random_letter
        counter += 1
    return BASE_URL + url_hash + '.jpg'


print('START')

while True:
    img_url = get_url()
    r = requests.get(img_url + '.jpg')

    while r.url == 'https://i.imgur.com/removed.png':
        img_url = get_url()
        r = requests.get(img_url)

    filename = img_url.split("/")[-1]

    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        data={
            'image': img_url + '.jpg',
        },
        headers={'api-key': 'your deepAI api key goes here'}
    )
    json_response = r.json()
    if len(json_response['output']['detections']):
        print(img_url)
