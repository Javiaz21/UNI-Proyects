#Actividad 2 - Sistemas Inteligentes IV
#Javier Ignacio Díaz López
#220839937
#03/09/2023

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv(r'D:\ARCHIVOSSS\UDG INRO\CLASSES\Inteligentes 4\Act2\salary.csv')
print(df)

x = np.asanyarray(df[['YearsExperience']])
y = np.asanyarray(df[['Salary']])

plt.figure()
plt.grid()
plt.title('Regresion lineal')
plt.xlabel('Year')
plt.ylabel('Population')
plt.plot(x,y,'bo')

model = linear_model.LinearRegression()
model.fit(x,y)
yp = model.predict(x)
plt.plot(x,yp,'r-')

print('Coeficientes(',model.intercept_,',',model.coef_,')')


plt.legend(['datos','prediccion','(xp,yp)'])
plt.show()


# Métrica R^2
e = r2_score(y,yp)
print('R^2 =',e)
