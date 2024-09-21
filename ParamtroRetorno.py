#crear la funcion saludar

def saludar (nombre,peso,edad):
    print(f'Hola {nombre} mi peso es {peso} lbs y mi edad es : {edad}')


saludar(nombre='Jaime', peso='250', edad='25')

#funcion con parametros predeterminados

def saludar_con_saludo (nombre,peso,edad, saludo = "Hola que tal"):
    print(f'Hola {nombre} mi peso es {peso} lbs y mi edad es : {edad}')

saludar(nombre='Jaime', peso='250', edad='25')

#Funcion con numeros

def suma (a=20,b=10):
    resultado = a+b

    return resultado

respuesta = suma(100,30)
print(respuesta)

def calcular_descuento(monto_total, descuento=20):
    descuento=monto_total*descuento/100
    return descuento

descuento=calcular_descuento(20000)
print(f'el descuento es ', descuento)


### 1 forma de llamar
monto_total= float(input('Ingresa el monto'))

descuento=calcular_descuento(monto_total)
print(f'el descuento es ', descuento)


### 2 forma de llamar
monto_total2= float(input('Ingresa el monto'))

descuento2=calcular_descuento(monto_total2,50)

print("el monto total es: ")
print(f'el descuento es ', descuento2)
print("el valor neto es: ") 