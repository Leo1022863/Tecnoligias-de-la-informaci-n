def calcular_temperatura_promedio(datos_temperaturas, ciudad, semanas=None):

    #Calcula la temperatura promedio de una ciudad durante un período de tiempo.

   #Parámetros:
    #datos_temperaturas (dict): Diccionario con datos de temperaturas. La clave es el nombre de la ciudad
     #                          y el valor es una lista de listas, donde cada sublista representa una semana.

    #ciudad (str): Nombre de la ciudad para la cual se desea calcular la temperatura promedio.

    #semanas (list, opcional): Lista de índices de semanas específicas a considerar. Si no se proporciona,
     #                         se considerarán todas las semanas.

    #Retorna:
    #float: La temperatura promedio de la ciudad durante las semanas especificadas.


    # Verificar si la ciudad está en los datos
    if ciudad not in datos_temperaturas:
        raise ValueError(f"No se encontraron datos para la ciudad '{ciudad}'")

    # Obtener las temperaturas de la ciudad
    temperaturas_ciudad = datos_temperaturas[ciudad]

    # Si no se especifican semanas, considerar todas las semanas
    if semanas is None:
        semanas = range(len(temperaturas_ciudad))

    # Recoger las temperaturas de las semanas indicadas
    temperaturas_seleccionadas = []
    for semana in semanas:
        if semana < len(temperaturas_ciudad):
            temperaturas_seleccionadas.extend(temperaturas_ciudad[semana])
        else:
            raise ValueError(f"La semana {semana} no está disponible para la ciudad '{ciudad}'")

    # Calcular la temperatura promedio
    if not temperaturas_seleccionadas:
        raise ValueError(f"No hay temperaturas disponibles para las semanas indicadas en '{ciudad}'")

    promedio = sum(temperaturas_seleccionadas) / len(temperaturas_seleccionadas)

    return promedio


# Ejemplo de uso:
# Diccionario de temperaturas de ciudades (cada sublista representa una semana de temperaturas)
datos = {
    "CiudadA": [[25, 28, 30], [26, 29, 31], [24, 27, 29]],  # Tres semanas de temperaturas
    "CiudadB": [[20, 22, 21], [23, 24, 22], [19, 21, 20]]  # Tres semanas de temperaturas
}

# Calcular la temperatura promedio de CiudadA en todas las semanas
promedio_ciudad_a = calcular_temperatura_promedio(datos, "CiudadA")
print(f"Promedio CiudadA: {promedio_ciudad_a}")

# Calcular la temperatura promedio de CiudadB en las semanas 1 y 2
promedio_ciudad_b = calcular_temperatura_promedio(datos, "CiudadB", semanas=[0, 1])
print(f"Promedio CiudadB (semanas 1 y 2): {promedio_ciudad_b}")


#datos_temperaturas: Diccionario donde la clave es el nombre de la ciudad,
#y el valor es una lista de listas que representa las temperaturas por semana.

#ciudad: El nombre de la ciudad para la cual se quiere calcular la temperatura promedio.

#semanas: Lista opcional de índices de semanas. Si no se proporciona, se consideran todas las semanas.
