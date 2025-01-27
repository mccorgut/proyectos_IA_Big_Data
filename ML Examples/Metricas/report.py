from sklearn.metrics import classification_report

# Predicciones
y_pred = ['A','A','A','A','A','A','A','A','B','A','A','B','B','B','B','B','B','B','B','B']

# Aciertos
y_true = ['A','A','A','A','A','A','A','A','A','B','B','B','B','B','B','B','B','B','B','B']

print(classification_report(y_true, y_pred, labels=['A', 'B']))