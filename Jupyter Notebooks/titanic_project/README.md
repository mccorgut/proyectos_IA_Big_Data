# Programación de IA: Proyecto Titanic

Este proyecto utiliza Scikit-learn en Python para crear modelos de regresión, SVM (Support Vector Machine) y/o árboles de decisión (Decision Tree) para predecir la supervivencia de los pasajeros del Titanic.

## Requisitos

- Python 3.x
- Scikit-learn
- Pandas
- NumPy
- Matplotlib (opcional, para visualización)

## Instalación

Puedes instalar las dependencias necesarias utilizando pip:

```bash
pip install scikit-learn pandas numpy matplotlib
```

## Uso

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/titanic_project.git
cd titanic_project
```

2. Ejecuta el script principal para entrenar y evaluar los modelos:

```bash
python main.py
```

## Modelos

Este proyecto incluye la implementación de los siguientes modelos:

- **Regresión Logística**
- **Máquina de Vectores de Soporte (SVM)**
- **Árbol de Decisión (Decision Tree)**

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Dataset

Para este proyecto, utilizaremos el dataset "Titanic - Machine Learning from Disaster" disponible en Kaggle. Este dataset es ideal para demostrar el preprocesamiento de datos y la creación de modelos predictivos.

### Descripción del Dataset

- **Descripción**: El clásico dataset para predecir la supervivencia de pasajeros del Titanic.
- **Target**: Survived (0: No sobrevivió, 1: Sobrevivió).
- **Atributos interesantes**:
    - Categóricos: Sex, Embarked, Pclass.
    - Numéricos: Age, Fare.
    - Valores nulos: Age, Cabin, Embarked.

### Tareas de Preprocesamiento

- Imputar valores nulos en Age y Embarked.
- Convertir atributos categóricos como Sex y Embarked en numéricos.

## Herramientas

Este proyecto utiliza las siguientes herramientas:

- **Poetry**: Para la gestión de librerías y dependencias mediante un entorno virtual.
- **Visual Studio Code**: Para la creación del proyecto, incluyendo la posibilidad de usar cuadernos de Jupyter.

## Pasos a Realizar

1. **Preparación de los datos**: Cargar y limpiar el dataset.
2. **Análisis de importancia de propiedades**: Identificar las características más relevantes.
3. **Ingeniería de propiedades**: Crear nuevas características a partir de las existentes.
4. **Entrenamiento del modelo**: Entrenar los modelos de regresión, SVM y árbol de decisión.
5. **Serialización del modelo**: Guardar el modelo entrenado para su uso posterior.
6. **Pruebas**: Evaluar el modelo y realizar predicciones.

## Servidor Flask

Se implementará un servidor Flask con un endpoint para realizar las peticiones al modelo. A continuación, se muestra un ejemplo de llamada desde Postman:

```bash
POST /predict
Content-Type: application/json

{
    "Pclass": 3,
    "Sex": "male",
    "Age": 22,
    "Fare": 7.25,
    "Embarked": "S"
}
```

## Documentación de Pruebas

Se entregará un pequeño documento para el paso de pruebas, indicando un par de llamadas de ejemplo y las predicciones obtenidas, así como el análisis de las mismas. Se pueden incluir capturas de pantalla si se considera oportuno.