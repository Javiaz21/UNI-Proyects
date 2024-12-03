#Actividad 1 - Sistemas Inteligentes IV
#Javier Ignacio Díaz López
#220839937
#25/08/2023

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv('df_regresion_lineal_3.csv')
print(df)

x = np.asanyarray(df[['x']])
y = np.asanyarray(df[['y']])

plt.figure()
plt.grid()
plt.title('Regresion lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'bo')

model = linear_model.LinearRegression()
model.fit(x,y)

yp = model.predict(x)
plt.plot(x,yp,'r-')

print('Coeficientes(',model.intercept_,',',model.coef_,')')

plt.plot(x,y,'bo')
plt.plot(x,yp,'r-',lw=3)
plt.legend(['datos','prediccion'])

# Métrica R^2

e = r2_score(y,yp)
print('R^2 =',e)
plt.show()
