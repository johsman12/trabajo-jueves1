# Definir la lista con las temperaturas en Celsius
celsius = [18, 22, 25, 19, 30]

# Calcular las temperaturas en Fahrenheit aplicando la fórmula
fahrenheit = [(c * 9/5) + 32 for c in celsius]

# Mostrar los resultados con print
print("Temperaturas en Celsius:", celsius)
print("Temperaturas en Fahrenheit:", fahrenheit)