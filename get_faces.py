import os
import face_recognition
from PIL import Image, ImageDraw
import random

def get_faces(file):

    # Define empty result 
    faces = []
    i = 0

    # Assign directory this will be gived in the request 
    directory = 'img/known'

    # Create array of encodings and names
    known_faces_encodings = []
    known_faces_names = []

    # Encode known faces
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            image = face_recognition.load_image_file(f)
            face_encoding = face_recognition.face_encodings(image)[0]
            known_faces_encodings.append(face_encoding)
            known_faces_names.append(os.path.splitext(filename)[0])

    # Find faces in file
    face_locations = face_recognition.face_locations(file)
    face_encodings = face_recognition.face_encodings(file, face_locations)

    # Loop throught faces in test image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding) 

        name = 'Desconocido'

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_faces_names[first_match_index]

            face = {
                "id": i,
                "name": name,
                "known": True,
                "bbox": [top, right, bottom, left]
            }
        else:
            face = {
                "id": i,
                "name": name,
                "known": False,
                "bbox": [top, right, bottom, left]
            }

        faces.append(face)
        i+=1
     
    return faces