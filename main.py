# from datetime import datetime
# from get_faces import get_faces
# import time

# def main():
#     start_time = datetime.now()
#     print(get_faces())
#     print(f"Tiempo: {str((datetime.now() - start_time).total_seconds())}")

# if __name__ == '__main__':
#     main()

from fastapi import FastAPI, UploadFile
from PIL import Image
from io import BytesIO
import numpy as np
from get_faces import get_faces

app = FastAPI()

def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))

@app.post("/faces")
async def faces(file: UploadFile):
    image = load_image_into_numpy_array(await file.read())
    return {"faces": get_faces(image)}
