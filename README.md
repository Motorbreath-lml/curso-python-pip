# Entornos virtuales en Python 3
El curso se imparte en Linux, lo quiero hacer en Windows ya que en los proximos dias realizare un proyecto en Windows con interfaces graficas, la biblioteca serial de Python, un doungle USB de MTI RFID ME para escribir en etiquetas RFID codigos unicos apartir de una base de datos en MariaDB

## Game Project
Para poder jugar piedra, papel o tiejeras contra la maquina, primero nos posicionamos en la carpeta 'game' y ejecutamos el archivo 'main.py' acontinuacion se muestran los comando ejecutados en PoweShell
```powershell
cd .\game\
py .\main.py
```
## App Project
Para poder utilizar esta app, entramos en la carpeta app, instalamos las dependencias necesarias, y se ejecuta el archivo main.py, acontinuacion se muestran los comando ejecutados en PoweShell
```powershell
cd .\app\
.\env\Scripts\Activate.ps1
pip3 install -r requirements.txt
py .\main.py
```
El script de `main.py` al ser ejecutado pedira el nombre de algun país, por ejemplo: México, pero al momento de escribirlo para el programa no se utiliza acentos, entonces la entrada para el programa seria Mexico sin acento.