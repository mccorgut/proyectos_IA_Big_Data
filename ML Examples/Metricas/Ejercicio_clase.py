import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.datasets import load_breast_cancer
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, log_loss, f1_score
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay
from sklearn.tree import DecisionTreeClassifier # Pa el arbol
import matplotlib.pyplot as plt
import seaborn as sns

""" 
Modificar el código de ejemplo del dataset Load Breast Cancer para añadir un segundo clasificador 
(por ejemplo, un Decission Tree), obtener sus métricas y compararlo con la SVM.
"""

# Cargar los datos
data = load_breast_cancer()

# Convertir los datos a un Dataframe
# Convertir los datos a un Dataframe
df: DataFrame  = pd.DataFrame(
    np.c_[data['data'], data['target']],
    columns=np.append(data['feature_names'], ['target'])
    )

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

# Clasificador 1: SVM lineal
classifier_svm = svm.SVC(kernel='linear', C=0.01, probability=True)
classifier_svm.fit(X_train, y_train)
y_pred_svm = classifier_svm.predict(X_test)

# Clasificador 2: Árbol de Decisión
classifier_tree = DecisionTreeClassifier(random_state=1)
classifier_tree.fit(X_train, y_train)
y_pred_tree = classifier_tree.predict(X_test)

# Matriz de Confusión para ambos modelos
for classifier, y_pred, name in zip([classifier_svm, classifier_tree], [y_pred_svm, y_pred_tree], ["SVM", "Decision Tree"]):
    cm_data = confusion_matrix(y_test, y_pred, labels=np.unique(y_test))
    print(f"\nMatriz de Confusión - {name}")
    print(cm_data)

    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        X_test,
        y_test,
        display_labels=data.target_names,
        cmap=plt.cm.Blues
    )
    disp.ax_.set_title(f"Matriz de Confusión - {name}")
    plt.show()

# Métricas de desempeño para ambos modelos
for classifier, y_pred, name in zip([classifier_svm, classifier_tree], [y_pred_svm, y_pred_tree], ["SVM", "Decision Tree"]):
    print(f"\nMétricas de desempeño - {name}")
    print(f"Exactitud: {accuracy_score(y_test, y_pred):.2f}")
    print(f"Precisión: {precision_score(y_test, y_pred):.2f}")
    print(f"Recall: {recall_score(y_test, y_pred):.2f}")
    print(f"Log-Loss: {log_loss(y_test, classifier.predict_proba(X_test)):.2f}")
    print(f"F1-Score: {f1_score(y_test, y_pred):.2f}")

# Curvas ROC para ambos modelos
plt.figure(figsize=(10, 6))
roc_display_svm = RocCurveDisplay.from_estimator(classifier_svm, X_test, y_test, name="SVM", ax=plt.gca())
roc_display_tree = RocCurveDisplay.from_estimator(classifier_tree, X_test, y_test, name="Decision Tree", ax=plt.gca())
plt.title("Curvas ROC de los clasificadores")
plt.show()