# 10. Filtrar productos en oferta (menores a 50.000)
productos = [
    {"nombre": "Camisa", "precio": 45000}, 
    {"nombre": "Pantalón", "precio": 89000}, 
    {"nombre": "Media", "precio": 8000}
]
nombres_oferta = [p["nombre"] for p in productos if p["precio"] < 50000]
print("Productos en oferta (< 50.000):", nombres_oferta)

# 11. Convertir temperaturas de Celsius a Fahrenheit
temperaturas_celsius = [18, 22, 25, 19, 30]
temperaturas_fahrenheit = [(c * 9/5) + 32 for c in temperaturas_celsius]
print("Temperaturas en Fahrenheit:", temperaturas_fahrenheit)

# 12. Lista de correos válidos (que contengan "@")
correos = ["ana@gmail.com", "luis", "carlos@hotmail.com", "sena"]
correos_validos = [c for c in correos if "@" in c]
print("Correos válidos:", correos_validos)