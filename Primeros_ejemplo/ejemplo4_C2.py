#valor = 20
#print("El numero del valor es: " + str(valor))

#variable = "12345"
#print(variable.isdigit())

while True:
    edad = input("Ingrese edad: ")

    if(edad.isdigit()):
        edad = int(edad)
        if(not(edad < 18 or edad > 65)):
            break
        else:
            print("Edad fuera del rango")
    else:
        print("Eso no es un numero")
        
print(edad)
