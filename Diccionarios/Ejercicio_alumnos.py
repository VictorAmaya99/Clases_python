notas = []

for i in range(3):
    d = {}
    auxInt = int(input("Ingrese nota 1: "))
    d["nota1"] = auxInt

    auxInt = int(input("Ingrese nota 2: "))
    d["nota2"] = auxInt

    d["promedio"] = (d["nota1"] + d["nota2"]) / 2

    notas.append(d)

# print(notas)

print("*** Listado de notas***")
print("Parcial 1      Parcial 2     Promedios")

for calificacion in notas:
    print(f"    {calificacion['nota1']:2d}            {calificacion['nota2']:2d}             {calificacion['promedio']:5.2f}")
