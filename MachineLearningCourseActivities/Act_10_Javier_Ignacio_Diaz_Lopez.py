#Javier Ignacio Díaz López      220839937

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

df = pd.read_csv('country.csv')

df = pd.read_csv('crime_data.csv')

#   >>>For pokemon:

#df = pd.read_csv('POKEMON.csv', encoding='utf-8')
#LE = LabelEncoder()
#df['Type_1'] = LE.fit_transform(df['Type_1'])

print(df)

target = np.asanyarray(df[['Name']])
x = np.asanyarray(df.drop(columns=['Name'])) 

n = 3;
model = KMeans(n_clusters=n)
model.fit(x)

y = model.predict(x)

for i in range(n):
    print('grupo',i+1)
    print(target[y==i].transpose())