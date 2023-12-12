# 2-La real academia española nos pide desarrollar un pequeño programa que contenga el
# diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
# algoritmo que nos permita el ingreso de una palabra en español y su traducción al
# ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
# palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
# esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
# debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
# inglés. Recordar validar los datos de forma correcta.


español = []
ingles = []
seguir = "si"

while seguir == "si":
    palabra_español = input("Ingrese palabra en español: ")
    español.append(palabra_español)
    
    palabra_traducida = input("Ingrese traduccion al ingles: ")
    ingles.append(palabra_traducida)
    
    seguir = input("Desea continuar: ")

for i in range(len(español)):
    print(f"{español[i]}       {ingles[i]}")