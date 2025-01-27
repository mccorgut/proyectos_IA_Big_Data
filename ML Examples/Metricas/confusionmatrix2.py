import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay

# Importacion dataset Iris
iris = datasets.load_iris()

# Conjunto de datos sin etiquetar
X = iris.data

# Clases o etiquetas
y = iris.target

# Nombre de las clases
class_names = iris.target_names

# Divison entre entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Clasificador SVM
clf = svm.SVC(kernel='linear', C=0.01).fit(X_train, y_train)
np.set_printoptions(precision=2) # redondea los valores

# 2 graficas cm sin normalizar y otra normalizada
titles_options = [
    ('Confusion matrix without normalization', None),
    ('Confusion matrix with normalization', 'true'),
]

for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        clf,
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize    
    )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

plt.show()    
    