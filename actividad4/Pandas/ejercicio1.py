import pandas as pd


# Aquí tengo mis datos de partida para armar el inventario de la tienda
inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

# Voy a explorar el inventario creando un DataFrame para ver las primeras filas, la forma, las columnas y las estadísticas
print("\n Explorar el inventario ")
df = pd.DataFrame(inventario)
print("Primeras filas (head):")
print(df.head())
print("\nForma (shape):", df.shape)
print("Nombres de las columnas:", df.columns.tolist())
print("\nEstadísticas rápidas (describe):")
print(df.describe())


# Aquí filtro y muestro solo los productos que tienen un stock menor a 10
print("\n Productos por reponer ")
productos_reponer = df[df["stock"] < 10]
print(productos_reponer)


# En esta parte calculo el valor total multiplicando el precio por el stock, y agrego la columna reponer
print("\n Valor del inventario ")
df["valor_inventario"] = df["precio"] * df["stock"]
df["reponer"] = df["stock"] < 10
print(df)


# Aquí ordeno mis productos del más caro al más barato y calculo el precio promedio de todos
print("\n Ordenar y resumir ")
df_ordenado = df.sort_values(by="precio", ascending=False)
print("Inventario ordenado por precio (más caro a más barato):")
print(df_ordenado)

precio_promedio = df["precio"].mean()
print(f"\nPrecio promedio de todos los productos: ${precio_promedio:,.2f}")


# Por último, guardo mi DataFrame como un archivo CSV, lo vuelvo a leer y verifico que los datos sean iguales
print("\n Leer datos desde un archivo ")
df.to_csv("inventario.csv", index=False)
print("DataFrame guardado exitosamente como 'inventario.csv'.")

df_leido = pd.read_csv("inventario.csv")
print("\nDatos leídos de nuevo desde el archivo CSV:")
print(df_leido)

son_iguales = df.equals(df_leido)
print(f"\n¿Los datos originales y los leídos del CSV son idénticos?: {son_iguales}")