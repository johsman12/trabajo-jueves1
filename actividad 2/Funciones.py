# 1. Calculadora de propina en un restaurante
def calcular_propina(cuenta, porcentaje=10):
    return cuenta * (porcentaje / 100)

# 2. Validador de contraseña
def es_valida(contrasena):
    return len(contrasena) >= 8

# 3. Conversor de unidades (Km a millas)
def km_a_millas(km):
    return km * 0.621