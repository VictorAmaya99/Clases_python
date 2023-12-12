import csv
import re

ruta = "consigina_primer_parcial\\insumos.csv"

def csv_como_lista_dict(ruta):
    separador = ","
    with open(ruta, encoding="UTF=8") as archivo:
        #next(archivo)
        insumos = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            columnas = linea.split(separador)
            id = columnas[0]
            nombre = columnas[1]
            marca = columnas[2]
            precio = columnas[3]
            caract = columnas[4]
            insumos.append({
                "Id": id,
                "Nombre": nombre,
                "Marca": marca,
                "Precio": precio,
                "Caracteristicas": caract,
            })
        return insumos

def main():
    insumos = csv_como_lista_dict(ruta)
    for insumo in insumos:
        id = insumo["Id"]
        nombre = insumo["Nombre"]
        marca = insumo["Marca"]
        precio = insumo["Precio"]
        caract = insumo["Caracteristicas"]
        print("Id: ", id, "|", "Nombre: ", nombre, "|", "Marca: ", marca, "|", "Precio: ", precio, "|", "Caracteristicas: ", caract)
        #print(f"Id: {id} | Nombre: {nombre} | Marca: {marca} | Precio: {precio} | Caracteristicas: {caract}")
        
main()


# 4. Buscar insumo por característica: El usuario ingresa una
# característica (por ejemplo, "Sin Granos") y se listarán todos los
# insumos que poseen dicha característica.

def buscar_insumos():
    insumos = csv_como_lista_dict(ruta)
    busqueda = []
    
    seguir = "si"

    while seguir == "si":
        #for i in range:
        palabra_ingresada = input("Ingrese lo que busca: ")
        busqueda.append(palabra_ingresada)
        
        if busqueda in insumos:
            print("True")
        else:
            print("False")
        
        seguir = input("Desea continuar?")

buscar_insumos()

x = re.search(r"\bS\w+", txt)
print(x.group())
    
    


# español = []
# ingles = []
# seguir = "si"

# while seguir == "si":
#     palabra_español = input("Ingrese palabra en español: ")
#     español.append(palabra_español)
    
#     palabra_traducida = input("Ingrese traduccion al ingles: ")
#     ingles.append(palabra_traducida)
    
#     seguir = input("Desea continuar: ")

# for i in range(len(español)):
#     print(f"{español[i]}       {ingles[i]}")