# =========================================
# Script completo generado
# Guía Interactiva de Minería de Datos
# =========================================

# --- Preprocesamiento ---
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, OneHotEncoder, LabelEncoder

# Cargar datos
df = pd.read_csv("student-por.csv")
print("Filas x Columnas:", df.shape)



# One-Hot Encoding
cat_cols = df.select_dtypes(include=[object, category]).columns
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

print("Después de preprocesar:", df.shape)
print(df.head())

# --- Modelado ---
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Definir X e y
y = df['G3']
X = df.drop(columns=['G3'])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo: Árbol de Decisión
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Predicciones (primeras 10):", y_pred[:10])

# --- Evaluación ---
from sklearn import metrics

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
print("R²:", r2_score(y_test, y_pred))