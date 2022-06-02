from fastapi import FastAPI, UploadFile
from io import BytesIO
from PIL import Image
import numpy as np

from face_identify import face_identify

app = FastAPI()

def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))

@app.post("/face/identify/{user_id}")
async def identify(user_id: str, file: UploadFile):
    img = load_image_into_numpy_array(await file.read())
    return {"faces": face_identify(user_id, img)}