#Actividad 1 - Sistemas Inteligentes IV
#Javier Ignacio Díaz López
#220839937
#25/08/2023

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv('pop.csv')
print(df)

x = np.asanyarray(df[['year']])
y = np.asanyarray(df[['pop']])

plt.figure()
plt.grid()
plt.title('Regresion lineal')
plt.xlabel('Year')
plt.ylabel('Population')
plt.plot(x,y,'bo')

model = linear_model.LinearRegression()
model.fit(x,y)

xp_1 = np.array([[2023]]);
yp_1 = model.predict(xp_1)

yp = model.predict(x)
plt.plot(x,yp,'r-')


print('Coeficientes(',model.intercept_,',',model.coef_,')')

plt.figure()
plt.grid()
plt.title('Predicción')
plt.xlabel('Year')
plt.ylabel('Population')

plt.plot(x,y,'bo')
plt.plot(x,yp,'r-')
plt.plot(xp_1,yp_1,'gs')

plt.legend(['datos','prediccion','(xp,yp)'])
plt.show()


# Métrica R^2

e = r2_score(y,yp)
print('R^2 =',e)

print('Predicción 2023 =',yp_1)
