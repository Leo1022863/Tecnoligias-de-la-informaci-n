##Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
##La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
##La función debe devolver el monto del descuento calculado

# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    # Devuelve el monto del descuento calculado
    return descuento

# Programa principal
monto1 = 1000  # Monto total de la primera compra
descuento1 = calcular_descuento(monto1)  # Uso del descuento predeterminado (10%)
print(f"El descuento para una compra de {monto1} es: {descuento1}")

monto2 = 2000  # Monto total de la segunda compra
porcentaje_descuento2 = 15  # Porcentaje de descuento personalizado
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)  # Uso de un descuento personalizado (15%)
print(f"El descuento para una compra de {monto2} con un {porcentaje_descuento2}% es: {descuento2}")
