# 1. Notas de estudiantes
notas = [3.5, 4.0, 2.8, 4.5, 3.9]

# Añado una nota extra al final con .append()
notas.append(4.2)

# Busco la nota más pequeña con min() y la borro con .remove()
nota_minima = min(notas)
notas.remove(nota_minima)

print("Así quedó la lista de notas final:", notas)


# 2. Conteo de asistencias con un bucle
asistencias = [1, 0, 1, 1, 0, 1, 1]

# Inicio mi contador en cero
total_asistencias = 0

# Recorro la lista y sumo 1 cada vez que encuentro un 1
for asistencia in asistencias:
    if asistencia == 1:
        total_asistencias += 1

print("El estudiante asistió un total de:", total_asistencias, "veces")


# 3. Ordenar nombres alfabéticamente
nombres = ["Zoe", "Carlos", "Ana", "Luis", "Beatriz"]

# Uso .sort() para ordenar la lista directamente de la A a la Z
nombres.sort()
print("Nombres ordenados:", nombres)


# 4. Total y promedio de precios sin usar sum()
precios = [15000, 8000, 22000, 5000]

# Variable acumuladora para ir sumando cada precio
total = 0
for precio in precios:
    total += precio

# Calculo el promedio dividiendo entre la cantidad de elementos (len)
promedio = total / len(precios)

print(f"El total gastado es: ${total}")
print(f"El promedio de precios es: ${promedio}")


# 5. Clasificar edades en dos listas
edades = [15, 22, 17, 30, 16, 25]

# Creo dos listas vacías para guardar la clasificación
mayores = []
menores = []

# Evalúo cada edad con un if y la mando a la lista correspondiente
for edad in edades:
    if edad >= 18:
        mayores.append(edad)
    else:
        menores.append(edad)

print("Lista de mayores de edad:", mayores)
print("Lista de menores de edad:", menores)