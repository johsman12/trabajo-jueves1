import numpy as np

# 4. Calificaciones por estudiante y materia
calificaciones = np.array([
    [8.5, 7.0, 9.0, 8.0],  # Carlos
    [6.0, 7.5, 8.0, 7.0],  # Ana
    [9.0, 8.5, 9.5, 9.0]   # Luis
])

promedios_estudiantes = calificaciones.mean(axis=1)
promedios_materias = calificaciones.mean(axis=0)

print(f"Promedio de cada estudiante (por fila): {promedios_estudiantes}")
print(f"Promedio de cada materia (por columna): {promedios_materias}")