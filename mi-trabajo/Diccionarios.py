# 1. Inventario de producto y actualizacion de stock
producto = {
    "nombre": "Teclado Mecanico",
    "precio": 120000,
    "cantidad_en_stock": 15
}

# Simulo una venta restandole 1 a la cantidad en stock
producto["cantidad_en_stock"] -= 1

print("Stock actualizado tras la venta:", producto["cantidad_en_stock"])


# 2. Promedio de materias recorriendo valores
notas_materias = {
    "Matematicas": 8.5,
    "Ingles": 7.0,
    "Programacion": 9.2
}

# Acumulo las notas iterando unicamente sobre los valores del diccionario
suma_notas = 0
for nota in notas_materias.values():
    suma_notas += nota

promedio_materias = suma_notas / len(notas_materias)
print(f"Mi promedio final de materias es: {promedio_materias:.2f}")


# 3. Condicional de aprobacion
estudiante_dic = {"nombre": "Ana", "nota": 7.0}

# Verifico si la nota cumple el minimo de 6.0 para aprobar
if estudiante_dic["nota"] >= 6.0:
    print(f"{estudiante_dic['nombre']} ha Aprobado")
else:
    print(f"{estudiante_dic['nombre']} ha Reprobado")


# 4. Consultar materia por dia con .get()
horario = {
    "Lunes": "Matematicas",
    "Martes": "Ingles",
    "Miercoles": "Programacion"
}

dia_a_consultar = "Martes"

# Uso .get() para evitar que el programa falle si pongo un dia que no está en el horario
materia = horario.get(dia_a_consultar, "No hay clases asignadas para ese dia")
print(f"Para el dia {dia_a_consultar} me toca: {materia}")