import os
from PIL import Image, ImageDraw
import random

def face_upload(user_id, img, name):

    directory = 'img/known/' + user_id
    f = os.path.join(directory, name)

    if not os.path.isdir(directory):
        os.mkdir(directory)

    # Conver to PIL format
    pil_img = Image.fromarray(img)

    # Save image
    pil_img.save('{}.jpg'.format(f))

    if os.path.isfile(f + '.jpg'):
        upload = {  
            "uploaded" : True,
            "user_id": user_id,
            "name": name,
            "path" : f + '.jpg',
        }
    else:
        upload = {
            "uploaded" : False,
            "user_id": user_id,
            "name": name,
            "path" : f + '.jpg',
        }

    # Return dict
    return upload