import numpy as np

# 2. Ventas de una tienda con aumento del 10%
ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])

ventas_con_aumento = ventas * 1.10
total_semana = np.sum(ventas_con_aumento)

print(f"Ventas con aumento: {ventas_con_aumento}")
print(f"Total de la semana: ${total_semana:,.2f}")