# Lista de diccionarios con la informacion de cada estudiante
estudiantes = [
    {"nombre": "Carlos", "nota": 9.0},
    {"nombre": "Ana", "nota": 5.5},
    {"nombre": "Luis", "nota": 7.0}
]

suma_general = 0

print("--- Calificaciones de los estudiantes ---")

# Recorro cada estudiante de la lista
for est in estudiantes:
    # Sumo su nota al acumulador general
    suma_general += est["nota"]
    
    # Determino si aprobo o reprobo segun su nota individual
    if est["nota"] >= 6.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
        
    print(f"{est['nombre']}: {estado} (Nota: {est['nota']})")

# Calculo el promedio general del curso dividiendo entre el total de estudiantes
promedio_curso = suma_general / len(estudiantes)

print("-----------------------------------------")
print(f"El promedio general del curso fue: {promedio_curso:.2f}")