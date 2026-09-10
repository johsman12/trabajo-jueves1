# 1. Coordenadas GPS de Popayán
# Guardo la latitud y longitud en una tupla porque las coordenadas no van a cambiar
coordenadas = (2.4382, -76.6132)

# Imprimo cada valor accediendo a sus posiciones (0 para latitud, 1 para longitud)
print("Latitud:", coordenadas[0])
print("Longitud:", coordenadas[1])


# 2. Representacion de un estudiante
# Creo la tupla con los datos iniciales
estudiante = ("Juan", 20, "Matematicas")

# Intento cambiar el curso dentro de un try-except para que el programa no se rompa
try:
    estudiante[2] = "Física"
except TypeError as error:
    # Capturo el error y explico por que ocurrio
    print("Me salio este error:", error)
    print("Esto pasa porque las tuplas son inmutables; una vez creadas no puedo modificar sus datos.")


# 3. Consultar el tercer día de la semana
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")

# Como los indices en Python empiezan en 0, el tercer dia está en la posicion 2
print("El tercer dia es:", dias[2])