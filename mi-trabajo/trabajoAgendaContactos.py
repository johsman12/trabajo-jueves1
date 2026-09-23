# Mi agenda de contactos estructurada en una lista de diccionarios
# Aqui almaceno los datos basicos: nombre, numero, fecha de nacimiento y si es favorito
contactos = [
    {"Nombre": "Ana", "Numero": "3001234567", "F. Nacimiento": "15/05/2000", "Favorito": True},
    {"Nombre": "Carlos", "Numero": "3119876543", "F. Nacimiento": "22/10/1995", "Favorito": False},
    {"Nombre": "Sofia", "Numero": "3201112233", "F. Nacimiento": "10/05/1998", "Favorito": True},
    {"Nombre": "Mateo", "Numero": "3154445566", "F. Nacimiento": "03/12/2001", "Favorito": False}
]


# 1. Recorro la lista para imprimir el nombre y el número de cada contacto

print("--- 1. MIS CONTACTOS ---")
for contacto in contactos:
    print(f"Nombre: {contacto['Nombre']} | Numero: {contacto['Numero']}")



# 2. Filtro y muestro unicamente mis contactos favoritos

print("\n--- 2. MIS CONTACTOS FAVORITOS ---")
for contacto in contactos:
    if contacto["Favorito"] == True:
        print(f"- {contacto['Nombre']}")



# 3. Calculo cuantos contactos cumplen años en un mes especifico (ej: mes 05 / Mayo)

print("\n--- 3. CUMPLEAÑOS EN EL MES ---")
mes_a_buscar = "05"  # Mes que quiero consultar
contador_cumples = 0

for contacto in contactos:
    # Corto la cadena de la fecha para extraer solo el mes (posiciones 3 y 4)
    mes_nacimiento = contacto["F. Nacimiento"][3:5]
    if mes_nacimiento == mes_a_buscar:
        contador_cumples += 1

print(f"Tengo {contador_cumples} contactos que cumplen años en el mes {mes_a_buscar}")



# 4. Creo una lista nueva vacía y guardo únicamente los nombres de todos los contactos

print("\n--- 4. NUEVA LISTA SOLO CON NOMBRES ---")
lista_nombres = []

for contacto in contactos:
    lista_nombres.append(contacto["Nombre"])

print(lista_nombres)



# 5. Busco un contacto por su nombre para imprimir su numero

print("\n--- 5. BUSQUEDA DE CONTACTO ---")
nombre_a_buscar = "Sofia"  # Nombre que voy a buscar
encontrado = False

for contacto in contactos:
    if contacto["Nombre"].lower() == nombre_a_buscar.lower():
        print(f"El número de {contacto['Nombre']} es: {contacto['Numero']}")
        encontrado = True
        break  # Detengo el ciclo porque ya encontre el contacto

# Si la bandera sigue en falso, significa que no existe
if not encontrado:
    print("Contacto no existe")