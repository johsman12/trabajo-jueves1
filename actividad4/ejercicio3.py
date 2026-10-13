import numpy as np

# 3. Pronóstico del clima: Celsius a Fahrenheit (F = C * 9/5 + 32)
celsius = np.array([18, 22, 25, 19, 30])
fahrenheit = celsius * 9 / 5 + 32

print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")