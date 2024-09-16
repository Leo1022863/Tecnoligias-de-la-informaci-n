import numpy as np;

# Definir parámetros
ciudades = ["CiudadA", "CiudadB", "CiudadC"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 3  # Número de semanas
dias = len(dias_semana)

# Generar una matriz 3D para las temperaturas (ciudades x días de la semana x semanas)
# Para el ejemplo, vamos a generar temperaturas aleatorias entre 20 y 35 grados.
temperaturas = np.random.randint(20, 36, (len(ciudades), dias, semanas))


# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedios(temperaturas, ciudades, dias_semana, semanas):
    promedios = {}  # Diccionario para almacenar los promedios por ciudad y semana

    # Recorrer ciudades
    for i, ciudad in enumerate(ciudades):
        promedios[ciudad] = []

        # Recorrer semanas
        for semana in range(semanas):
            suma_temperaturas = 0
            count_dias = 0

            # Recorrer días de la semana
            for dia in range(len(dias_semana)):
                temperatura_dia = temperaturas[i][dia][semana]
                suma_temperaturas += temperatura_dia
                count_dias += 1

            # Calcular el promedio de la semana para la ciudad
            promedio_semana = suma_temperaturas / count_dias
            promedios[ciudad].append(promedio_semana)

            # Mostrar el promedio de temperaturas por ciudad y semana
            print(f"Promedio de {ciudad} en la semana {semana + 1}: {promedio_semana:.2f}°C")

    return promedios


# Mostrar la matriz generada de temperaturas
print("Matriz de temperaturas (Ciudades x Días x Semanas):")
print(temperaturas)

# Calcular y mostrar los promedios
print("\nPromedios de temperatura por ciudad y semana:")
promedios_temperaturas = calcular_promedios(temperaturas, ciudades, dias_semana, semanas)
