import os
flag_saludo = False
flag_brindis = False

while True:
    os.system("cls")
    print("*** Menu de Opciones***")
    print("-----------------------")
    print("1 - Saludar")
    print("2 - Brindar")
    print("3 - Despedir")
    print("4 - Salir")   
    opcion = input("Ingrese opcion: ") 
    
    match(opcion):
        case "1":
            print("Hola")
            flag_saludo = True
        
        case "2":
            if flag_saludo:
                print("Chin, Chin..")
                flag_brindis = True
            else:
                print("Antes de brindar primero saludame")
        
        case "3":
            if flag_brindis:
                print("Chau")
                flag_saludo = False
                flag_brindis = False
            elif flag_saludo:
                print("Antes de despedirnos primero bridemos")
            else:
                print("Antes de despedirnos primero saludame")
        
        case "4":
            salir = input("Confirma salida? s/n:")
            if(salir == "s"):
                break
        
    os.system("pause")
    