#Javier Ignacio Díaz López      220839937
#Saul Alejandro Ayala Alaniz    220976969

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.kernel_ridge import KernelRidge
import pickle


df = pd.read_csv('Act_4_Javier_Ignacio_Diaz_Lopez.csv')
x = np.asanyarray(df[['V']])
y = np.asanyarray(df[['R']])
x_train, x_test, y_train, y_test = train_test_split(x,y)

model = Pipeline([('scaler',StandardScaler()),
                  ('reg',KernelRidge(alpha=0.00001, kernel='rbf'))])
model.fit(x_train,y_train)

pickle.dump(model,open('Trained_Model.sav','wb'))

yp = model.predict(x)

plt.figure()
plt.grid()
plt.title('Regresion Polinomial')
plt.xlabel('Voltaje (v)')
plt.ylabel('Resistencia (ohms)')

plt.plot(x,y,'bo')
plt.plot(x_test,y_test,'ro')
plt.plot(x,yp,'g-',lw=2)

plt.legend(['muestras','generalizacion', 'prediccion'])
plt.show()


R_2 = r2_score(y,yp)
print('R^2 =',R_2)
