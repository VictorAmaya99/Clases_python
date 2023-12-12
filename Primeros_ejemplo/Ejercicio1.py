# Ejercicio 01
# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de
# una compra de productos de prevención de contagio, de cada una debe obtener los
# siguientes datos:
# · El tipo ("barbijo", "jabón" o "alcohol")
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de
# stock.

seguir = "si"

while seguir == "si":
    
    tipo_producto = input("Ingrese tipo de producto(barbijo, jabon o alcohol): ")
    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
        tipo_producto = input("Producto invalido, reingrese tipo de producto(barbijo, jabon o alcohol): ")
    print(tipo_producto)
    
    while True:
        precio = input("Ingrese precio: ")
        
        if(precio.isdigit()):
            precio = int(precio)
            break
        else:
            print("Eso no es un numero")
    print(precio)
    
    while True:
        cantidad = input("Ingrese cantidad: ")
        
        if(cantidad.isdigit()):
            cantidad = int(cantidad)
            break
        else:
            print("Eso no es un numero")
    print(cantidad)
    
    
    seguir = input("Quiere continuar: ")
    
