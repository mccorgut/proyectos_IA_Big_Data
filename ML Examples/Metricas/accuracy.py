from sklearn.metrics import accuracy_score, precision_score, recall_score, log_loss, f1_score

# Predicciones
y_pred = ['A','A','A','A','A','A','A','A','B','A','A','B','B','B','B','B','B','B','B','B']

# Aciertos
y_true = ['A','A','A','A','A','A','A','A','A','B','B','B','B','B','B','B','B','B','B','B']

# Exactitud (accuracy)
print(accuracy_score(y_true, y_pred))

# Precisión
print(precision_score(y_true, y_pred, labels=['A', 'B'], pos_label='A', average='binary')) # precision de los resultados positivos
print(precision_score(y_true, y_pred, labels=['A', 'B'], pos_label='B', average='binary')) # precision de los resultados negativos

#Exhaustividad (Recall)
print(recall_score(y_true, y_pred, labels=['A', 'B'], pos_label='A', average='binary')) 

# Valor-F o Media-F (F1-Score)
print(f1_score(y_true, y_pred, average='weighted'))


# Pérdida Logarítmica (Log Loss)
y_real = [1,1,1,1,1,0,0,0,0,0]
y_pred = [1,1,1,1,0,1,1,0,0,0]

print(log_loss(y_true, y_pred))