import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import pickle
from sklearn import metrics

# Load data
df = pd.read_csv(r'D:\ARCHIVOSSS\UDG INRO\PROGRAMAS\_xX_pishulita_Xx_\sensor_data.csv')  

# Prepare data
X = np.asanyarray(df.drop(columns=['Speed_X', 'Speed_Y']))  # Assuming 'output1' and 'output2' are the output columns
y = np.asanyarray(df[['Speed_X', 'Speed_Y']])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)

# Create and train the neural network model
model = MLPRegressor(hidden_layer_sizes=(100, 100), activation='relu', solver='adam', max_iter=100000, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model.fit(X_train_scaled, y_train)

# Evaluate the model
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)
print('Train score:', train_score)
print('Test score:', test_score)

# Save the trained model
with open(r'D:\ARCHIVOSSS\UDG INRO\PROGRAMAS\_xX_pishulita_Xx_\neural_network_model.pkl', 'wb') as file:
    pickle.dump((model, scaler), file)
