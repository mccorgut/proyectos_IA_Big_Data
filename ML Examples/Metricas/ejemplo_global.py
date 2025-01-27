import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.datasets import load_breast_cancer
from sklearn import svm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, log_loss, f1_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = load_breast_cancer()

# Convertir los datos a un Dataframe
'''
No es necesario tipar la variable para realizar la conversion (mirar si es cosa de la version de la API sklearn o de python)
df: DataFrame 
'''
df: DataFrame  = pd.DataFrame(np.c_[data['data'], data['target']], 
columns=np.append(data['feature_names'], ['target']))

print(df.head())
print(df.describe())

# Representar las muestras de las clase, vamos a seleccionar 4 variables
sns.pairplot(df, hue='target', vars=['mean radius', 'mean texture', 'mean perimeter', 'mean area'])

plt.figure(figsize=(20, 12))
sns.heatmap(df.corr(), annot=True)

# Cantidad de elementos de cada clase
print(df['target'].value_counts())

# Representar graficamente las cantidad de valores
plt.figure(figsize=(8,6))
sns.countplot(x='target', data=data, palette='Set2')
plt.xlabel('Diagnosis')
plt.title('Cantidad de muestras por clase')

# Volver a cargar los datos para el modelo
X, y = load_breast_cancer(return_X_y=True, as_frame=True)

# Separamos en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Entrenar y predecir con una SVM linear y C=0.01
classifier = svm.SVC(kernel='linear', C=0.01)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# Matriz de Confusion
cm_data = confusion_matrix(y_test, y_pred, labels=np.unique(y_test))
print("Matriz de Confusion")
print(cm_data)

# Grafica Matriz de Confusion usando ConfusionMatrixDisplay
class_names = data.target_names
title = "Matriz de Confusion"
disp = ConfusionMatrixDisplay.from_estimator (
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Greens
)
disp.ax_.set_title(title)

# Calculo de metricas 
print("Exactitud" + str(accuracy_score(y_test, y_pred)))
print("Precision: " + str(precision_score(y_test, y_pred, labels=[1,0], pos_label=1, average='binary')))
print("Recall: " + str(recall_score(y_test, y_pred, labels=[1, 0], pos_label=1, average='binary')))
print("Perdida Logarítmica: " + str(log_loss(y_test, y_pred)))
print("Valor-F: " + str(f1_score(y_test, y_pred, average='weighted')))

# Curva ROC y area AUC
RocCurveDisplay.from_estimator(classifier, X_test, y_test)
plt.show()

