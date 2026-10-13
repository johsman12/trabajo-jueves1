import numpy as np

notas = np.array([
    [4.5, 3.8, 4.0],  # Estudiante 1
    [3.0, 2.5, 3.5],  # Estudiante 2
    [5.0, 4.8, 4.9],  # Estudiante 3
    [2.8, 3.2, 3.0]   # Estudiante 4
])

print("--- MATRIZ DE NOTAS (Estudiantes x Materias) ---")
print(notas)
print()

# 1. Calcular el promedio por estudiante (promedio de cada fila -> axis=1)
promedio_estudiantes = np.mean(notas, axis=1)

print("--- PROMEDIO POR ESTUDIANTE ---")
for i, prom in enumerate(promedio_estudiantes, start=1):
    print(f"Estudiante {i}: {prom:.2f}")

print()

# 2. Calcular el promedio por materia (promedio de cada columna -> axis=0)
promedio_materias = np.mean(notas, axis=0)

print("--- PROMEDIO POR MATERIA ---")
for j, prom in enumerate(promedio_materias, start=1):
    print(f"Materia {j}: {prom:.2f}")