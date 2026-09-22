# 4. Sistema de descuentos en una tienda
precios = [45000, 120000, 8000, 300000]
print("--- Ejercicio 4: Descuentos ---")
for p in precios:
    if p > 100000:
        precio_final = p * 0.85  # Aplica 15% de descuento
        print(f"Precio original: ${p:,.0f} -> Precio con descuento: ${precio_final:,.0f}")
    else:
        print(f"Precio sin descuento: ${p:,.0f}")

# 5. Control de acceso a un evento
edades = [16, 20, 15, 30, 12, 25]
print("\n--- Ejercicio 5: Control de acceso ---")
for edad in edades:
    if edad > 18:
        print(f"Edad {edad}: Acceso permitido")
    else:
        print(f"Edad {edad}: Acceso denegado")

# 6. Contador de inasistencias
asistencias = [1, 1, 0, 1, 0, 0, 1]
print("\n--- Ejercicio 6: Control de inasistencias ---")
faltas = asistencias.count(0)
print(f"Total de faltas: {faltas}")
if faltas > 2:
    print("¡Alerta! El aprendiz faltó más de 2 veces.")