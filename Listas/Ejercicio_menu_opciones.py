# Ejercicio con Menú de Opciones
# Realizar un programa utilizando los conceptos de la clase del lunes:
# Opciones del menú:
# 1 cargar una lista con 10 números
# 2 mostrar el total de los números ingresados
# 3 mostrar el promedio
# 4 mayor
# 5 menor
# 6 pedir un número y decir si está en la lista
# 7 pedir un número e informar todos los índices donde aparece
# 8 informar cuantos números pares y cuantos impares hay en la lista
#9 informar cuantos positivos, cuantos negativos y cuantos ceros hay en la lista
# 10 vaciar lista
#11 Salir
# Para utilizar las opciones 2 a la 10 hay que cargar los números en la opción 1
# Si se vacía la lista con la opción 10 se deben bloquear nuevamente las opciones hasta que se
# cargue de nuevo los números con la opción 1

lista = [23, 43, 89, 21, 77, 35, 17, 29, 62, 53]
acumulador = 0

print(lista)
    

for numero in lista:
    acumulador += numero
    
print("La suma de los numeros es {}".format(acumulador))

promedio = acumulador / 10
print("El promedio es: ", promedio)

flag_mayor = False
for numero in lista:
    if flag_mayor == False or numero > numero_mayor:
        flag_mayor = True
        numero_mayor = numero
print("El numero mayor es: ", numero_mayor)
        
flag_menor = False
for numero in lista:
    if flag_menor == False or numero < numero_menor:
        flag_menor = True
        numero_menor = numero

print("El numero menor es: ", numero_menor)


numero_en_lista = int(input("Ingrese numero: "))

if numero_en_lista in lista:
    print("El numero esta en la lista")
else:
    print("El numero no esta en la lista")


    


