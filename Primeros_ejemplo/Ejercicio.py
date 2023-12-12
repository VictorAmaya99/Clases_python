#/**1-Un bar nos contrato para administrar el consumo de los clientes en las distintas 
#* mesas del local. 
 #* Para esto debemos desarrollar un algoritmo que nos permita el ingreso de los siguientes datos de varias mesas:
#Nombre del cliente (no puede ser un número)
#la edad,
#Tipo de bebida (validar cerveza, limonada, gaseosa, ninguno)
#Tipo de comida (papitas, hamburguesa, rabas, ninguno)
#Importe total

#Necesitamos saber:
#a-El tipo de bebida más vendida
#b-la edad del que pago el importe total
#c-#Cuanta gente mayor a 18 no pidio bebida */

# Primero plantear la solucion
# while ---- controlar seguir
# nombre; edad, bebida, comida, importe
# contador por bebida
# flag edad mayor y el importe mayor
# contador mayores sin bebida

cont_mayores_sin_bebida = 0
flag_mayor = False
cont_cerveza = 0
cont_limonada = 0
cont_gaseosa = 0
cont_ninguna = 0
importe_mayor = None
edad_mayor = None
bebida_mas_vendida = None
seguir = "s"

while(seguir == "s"):
    
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    while(edad < 18):
        edad = int(input("Edad invalidad. Reingrese edad: "))
    
    bebida = input("Ingrese bebida: ")
    while(bebida != "cerveza" and bebida != "limonada" and bebida != "gaseosa" and bebida != "ninguna"):
        bebida = input("bebida invalidad. Reingrese bebida: ")
    print(bebida)
    
    comida = input("ingrese comida: ")
    while(comida != "papitas" and comida != "hamburguesa" and comida != "rabas" and comida != "ninguna"):
        comida = input("Comida invalida. Reingrese comida: ")
    print(comida)
    
    importe = float(input("Ingrese el importe a pagar: "))
    
    #b-la edad del que pago el importe total
    if(flag_mayor == False):
        flag_mayor = True
        edad_mayor = edad
        importe_mayor = importe
    elif(importe_mayor < importe):
        edad_mayor = edad
        importe_mayor = importe
    
    #c-#Cuanta gente mayor a 18 no pidio bebida */
    if(edad > 18 and bebida == "ninguna"):
        cont_mayores_sin_bebida += 1 
    
    match(bebida):
        case "cerveza":
            cont_cerveza += 1
        
        case "gaseosa":
            cont_gaseosa += 1
        
        case "limonada":
            cont_limonada += 1                     
        
    seguir = input("Quiere continuar? ")
    
#a-El tipo de bebida más vendida
if(cont_cerveza > cont_gaseosa and cont_cerveza > cont_limonada):
    bebida_mas_vendida = "cerveza"
elif(cont_gaseosa > cont_limonada):
    bebida_mas_vendida = "gaseosa"
else:
    bebida_mas_vendida = "limonada"
    
print("El tipo de bebida mas vendido es", bebida_mas_vendida)
print("La edad del que pago mayor importe es: ", edad_mayor)
print("La cantidad de gente mayor de 18 que no pidio bebida es: ", cont_mayores_sin_bebida)


print("Fin del programa")
