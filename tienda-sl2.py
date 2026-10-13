import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Cargo los datos desde el archivo Excel 
df = pd.read_excel("exel.joh.xlsx")

# 2. Separar las características (X) y la variable objetivo (y)
X = df[['Ingresos']]
y = df['Compro']

# 3. Entrenar el modelo de árbol de decisión
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)

# 4. Pedir el valor por consola para hacer la predicción
monto_ingresado = float(input("Ingrese el valor para predecir: "))

# 5. Realizar la predicción
prediction = modelo.predict([[monto_ingresado]])

# 6. Mostrar el resultado en pantalla
if prediction[0] == 1:
    print("El cliente puede comprar")
else:
    print("El cliente no podria comprar")