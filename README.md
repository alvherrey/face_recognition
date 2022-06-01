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
ejecutamos el pip install...
```bash
pip install -r requirements.txt
```
