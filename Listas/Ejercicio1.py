# 1-Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
# autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
# marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
# listas primero, y despues usando listas y comparar la composición del código.


marca = []
año = []
precio = []


for i in range(3):
    marca_auto = input("Ingrese la marca del auto: ")
    marca.append(marca_auto)
    
    año_auto = int(input("Ingrese el año del auto: "))
    año.append(año_auto)
    
    precio_auto = int(input("Ingrese precio del auto: "))
    precio.append(precio_auto)

print(marca)
print(año)
print(precio)

    
    
    
    
    
    
    
    

