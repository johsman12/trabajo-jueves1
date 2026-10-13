import numpy as np
from sklearn.linear_model import LinearRegression

X_metros_cuadrados = np.array([[50], [60], [80], [100], [120], [150]])
y_precios = np.array([150, 175, 220, 270, 310, 390])

modelo_prediccion = LinearRegression()
modelo_prediccion.fit(X_metros_cuadrados, y_precios)

nueva_casa = np.array([[90]])
precio_predicho = modelo_prediccion.predict(nueva_casa)

print(f"Para una casa de 90 m², el precio estimado es: ${precio_predicho[0]:.2f} millones") 