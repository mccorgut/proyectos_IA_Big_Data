## Instrucciones para la ejecución del caso práctico

### Pasos

1. python -m virtualenv .
2. source bin/activate
3. pip install -r requirements.txt
4. python application.py
5. Sube alguna de las imágenes de la carpeta /imgs al S3 de origen.
6. curl -H "Content-Type: application/json" -X POST -d '{"key": "image-name-uploaded"}' localhost:5000/api/analyze