## Notas parcial de 5 alumnos y promedio

notas_p1 = []
notas_p2 = []
promedios = []

for i in range(3):
    while True:
        auxInt = int(input("Ingrese nota parcial 1: "))
        notas_p1.append(auxInt)
        if(auxInt > 0 and auxInt < 11):
            break
        else:
            print("Error, ingrese nota parcial 1, nuevamente: ")
        
    while True: 
        auxInt = int(input("Ingrese nota parcial 2: "))
        notas_p2.append(auxInt)
        if(auxInt > 0 and auxInt < 11):
            break
        else:
            print("Error, ingrese nota parcial 2, nuevamente: ")
        
        
    promedios.append((notas_p1[i] + notas_p2[i]) / 2)
    
print("***Listado de Notas")
print("parcial1      parcial2      promedios")

for i in range(len(notas_p1)):
    print(f"    {notas_p1[i]:2d}           {notas_p2[i]:2d}          {promedios[i]:5.2f}")