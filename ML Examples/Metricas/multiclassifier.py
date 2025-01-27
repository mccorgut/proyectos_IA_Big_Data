from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score
from matplotlib import pyplot

# Generamos un dataset sintetico de dos clases
X, y = make_classification(n_samples=1000, n_classes=2, random_state=1)

# Dividir en entranamiento y test
trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=2)

# Generar un clasificador sin entrenar, que asignara 0 a todas
ns_probs = [0 for _ in range(len(testy))]

# Entrenamos un modelo de regresión
model = LogisticRegression(solver='lbfgs')
model.fit(trainX, trainy)

# Hacemos las predicciones
lr_probs = model.predict_proba(testX)

# No quedamos con las predicciones de la clase positiva (la probabilidad de 1)
lr_probs = lr_probs[:, 1]

# Calculamos el AUC
ns_auc = roc_auc_score(testy, ns_probs)
lr_auc = roc_auc_score(testy, lr_probs)

# Imprimimos el AUC 
print('Sin entrenar: ROC AUC=%.3f'% (ns_auc))
print('Regesion Logistica: ROC AUC=%.3f'% (lr_auc))

# Calcular las curvas ROC
ns_fpr, ns_tpr, _ = roc_curve(testy, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(testy, lr_probs)

# Pintar las curvas ROC
pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='Sin entrenar')
pyplot.plot(lr_fpr, lr_tpr, marker='.', label='Regresion Logistica')

# Etiquetas de los ejes
pyplot.xlabel('Tasa de Falsos Positivos')
pyplot.ylabel('Tasa de Verdaderos Positivos')
pyplot.legend()
pyplot.show()