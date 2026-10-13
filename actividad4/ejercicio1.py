import numpy as np

# 1. Notas de un grupo
notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])

print(f"Notas: {notas}")
print(f"Promedio: {np.mean(notas):.2f}")
print(f"Máximo: {np.max(notas)}")
print(f"Mínimo: {np.min(notas)}")
print(f"Desviación estándar: {np.std(notas):.2f}")