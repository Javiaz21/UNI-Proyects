
#Saul Alejandro Ayala Alaniz
#Javier Ignacio Díaz López 220839937
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import metrics
#from sklearn.inspection import DecisionBoundaryDisplay
import pickle

from sklearn.neighbors import KNeighborsClassifier


#
df = pd.read_csv('df - Copy.csv') 

x = np.asanyarray(df.drop(columns=['gesture']))
y = np.asanyarray(df['gesture'])

x_train, x_test, y_train, y_test = train_test_split(x, y)


#
model = Pipeline([('scaler',StandardScaler()),('cla',KNeighborsClassifier(n_neighbors=10))])
model.fit(x_train, y_train)

print('Train score:',model.score(x_train,y_train))
print('Test score:',model.score(x_test,y_test))

pickle.dump(model,open('proyecto-training.sav','wb'))

#
yp = model.predict(x)

'''
disp = DecisionBoundaryDisplay.from_estimator(model,x,response_method="predict",alpha=0.5,eps=0.2,cmap=plt.cm.RdBu,xlabel='x1',ylabel='x2')
disp.ax_.scatter(x[y==0,0],x[y==0,1],color='r',edgecolor='k')
disp.ax_.scatter(x[y==1,0],x[y==1,1],color='b',edgecolor='k')
'''

# Métricas
print('Metricas: \n', metrics.classification_report(y,yp))

# Matriz de Confusión
print('Confusion matrix: \n', metrics.confusion_matrix(y,yp))