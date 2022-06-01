import os
import face_recognition
from PIL import Image, ImageDraw
import random

# Assign directory this will be the user identifier gived in the request 
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

# Load test image
test_image = face_recognition.load_image_file('img/unknown/steve_elon.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Conver to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

i = 0
feces = []

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

    feces.append(face)
    ++i

    # Draw Box
    draw.rectangle(((left, top), (right, bottom)), outline = (0,0,0), width=5)

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill = (0,0,0), outline = (0,0,0))
    draw.text((left + 6, bottom - text_height -5), name, fill = (255,255,255,255))

del draw

# Display image
# pil_image.show()

# Save image
pil_image.save(f'out/result.jpg')

# Print result dataset
print(feces)