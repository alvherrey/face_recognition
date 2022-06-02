# Face Recognition
Reconocer y manipular caras desde Python o desde la línea de comandos con
la biblioteca de reconocimiento facial más simple del mundo.

## Requerimientos
### Crear un entorno virtual con Miniconda
Creamos un entorno nuevo con python 3.8
```bash
conda create --name face_recognition python=3.8
```
Activamos el entorno
```bash
conda activate face_recognition
```
### Instalar CMake
Para instalar la dependencia face_recognition es necesario tener instalado CMake
En ubuntu:
```bash
sudo apt install -y build-essential
sudo apt install -y cmake
```
### Instalar dlib
En ubuntu:
```bash
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
cd ..
python setup.py install
```
### Instalar el requerimientos
Ejecutamos el pip install...
```bash
pip install -r requirements.txt
```
## Ejecucion
### Identificar los rostros en una imagen (test)
Necesitamos la estructura de "img/known/*.jpg" con las imagenes conocidas (etiquetadas por su nombre)
Necesitamos la estructura de "out/" donde se guarda la imagen resultante
Obtenemos los resultados en el diccionario faces imprimido al final
```bash
python test_api.py
```
Ejemplo del resultado faces:
```bash
[{'id': 0, 'name': 'Steve Jobs', 'known': True, 'bbox': [76, 135, 166, 46]}, {'id': 0, 'name': 'Desconocido', 'known': False, 'bbox': [60, 304, 103, 261]}]
```
### Identificar los rostros en una imagen (api)
Levantar el api con uvicorn
```bash
uvicorn main:app --reload
```
Acceder al swagger para probar
```bash
http://127.0.0.1:8000/docs#/
```
### Docker
```bash
sudo docker-compose build
sudo docker-compose up -d
```
If you want to create a soft link of img_known volume
```bash
sudo docker inspect face-recognition | grep img_known | grep Source
sudo ln -s /dockers_servicios/volumes/face_recognition_img_known/_data ./img_known
```
Important all requests must include user_id in the path request, and must exists a dir with that name under img_known volume, with the known faces images properly named with the person name and surname. like: "Alvaro Hernandez.jpg"
Example:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/face/identify/1a' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@000001.jpg;type=image/jpeg'
```