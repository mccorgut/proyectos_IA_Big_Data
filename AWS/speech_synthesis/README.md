### Instrucciones para ejectuar el ejemplo

### Pasos

#### Crear entorno virtual desde el cmd (global)
1. pip install virtualenv
2. python -m virtualenv . --> crea un entorno virtual sin nombre
3. source bin/activate (ubuntu)
4. .\Scripts\activate (windows)

#### Abrir el IDE (en la carpeta del proyecto)
5. pip install -r requirements.txt 
6. Reemplaza los tokens aws_access_key_id, aws_secret_access_ke y my-bucket
7. python speech_synthesis.py