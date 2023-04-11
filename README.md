# Entornos virtuales en Python 3
El curso se imparte en Linux, lo quiero hacer en Windows ya que en los proximos dias realizare un proyecto en Windows con interfaces graficas, la biblioteca serial de Python, un doungle USB de MTI RFID ME para escribir en etiquetas RFID codigos unicos apartir de una base de datos en MariaDB

## Game Project
Para poder jugar piedra, papel o tiejeras contra la maquina, primero nos posicionamos en la carpeta 'game' y ejecutamos el archivo 'main.py' acontinuacion se muestran los comando ejecutados en PoweShell
```powershell
cd .\game\
py .\main.py
```
## App Project
Para poder utilizar esta app, entramos en la carpeta app, creamos un entrono virtual con el nombre de env, instalamos las dependencias necesarias, y se ejecuta el archivo main.py, acontinuacion se muestran los comando ejecutados en PoweShell
```powershell
cd .\app\
python -m venv env
.\env\Scripts\Activate.ps1
pip3 install -r requirements.txt
py .\main.py
```
El script de `main.py` al ser ejecutado pedira el nombre de algun país, por ejemplo: México, pero al momento de escribirlo para el programa no se utiliza acentos, entonces la entrada para el programa seria Mexico sin acento.

## Web-server
En este proyecto se usa la biblioteca `Request` para realizar peticiones a las apis, en este caso de realiza una peticion a la fakeapi de Platzi.
```powershell
cd .\web-server\
python -m venv env
.\env\Scripts\Activate.ps1
pip3 install -r requeriments.txt
py .\main.py
```
### Utilizar Uvicorn y Fastapi
Esta seccion del proyecto se utiliza `Uvicorn` para crear un servidor web de desarrollo para `Fastapi`. En `Fastapi` se creaun un por de rutas para una api sencilla, las cuales se pueden consultar en el navegador.
Commando para levantar el servidor:
```powershell
(env)  j3r4ck: web-server on main [ env 3.11.0] 
❯ uvicorn main:app --reload
```
El comando creara un localhost en el puerto 8000, con lo que podemos ver los resultados de la api en cualquier navegador de nuestro sistema utilizando la siguiente URL: `http://127.0.0.1:8000`