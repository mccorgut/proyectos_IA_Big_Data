from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns 

y_real = [1,1,1,1,1,0,0,0,0,0]
y_pred = [1,1,1,1,0,1,1,0,0,0]

cm = confusion_matrix(y_real, y_pred)

print(cm)

# crear grafica
ax = plt.subplot()
sns.heatmap(cm, annot=True, fmt='g', ax=ax, cmap='Greens')
# annot=True para anotar el valor de la celda
# fmt='g' desabilita la notacion cientifica
ax.set_xlabel('Valores predichos')
ax.set_ylabel('Valores reales')
ax.set_title('Confusion matrix')
ax.xaxis.set_ticklabels(['1', '0'])
ax.yaxis.set_ticklabels(['1', '0'])

plt.show()