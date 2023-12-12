
class Persona: #El nombre de una class va en PascalCase
    def __init__(self, id:int, nombre:str, apellido:str, edad:int) -> None: #Self es la direccion de memoria y recibe los valores y asignarlos.
        self.id = id         #publico
        self.__nombre = nombre.capitalize() #protegido
        self._apellido = apellido  #privado
        self.__edad = edad   #Si al atributo se pone dobre guion bajo, lo pone en privado
        #print(self.id)
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str):
        self.__nombre = value.capitalize()
    
    
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        if(value > 0):
            self.__edad = value
    
    # def set_edad(self, value):   #Para validad y que no cualquiera me cambie el valor
    #     if(value > 0):
    #         self.__edad = value
        
    # def get_edad(self):
    #     return self.__edad 
    
    def saludar(self):
        print("hola gente como va?")
    
    def presentarse(self):
        return f"Hola, me llano {self.nombre} y tengo {self.__edad} años"
    
#Herencia: Forma de heredar clases

class Empleado(Persona):
    def __init__(self, id: int, nombre: str, apellido: str, edad: int, sueldo: float) -> None:
        super().__init__(id, nombre, apellido, edad)
        self.sueldo = sueldo
        
    def presentarse(self):
        return f"Hola, soy un empleado {self.nombre} y gano {self.sueldo} por mes"
#lista = []
     
persona_1 = Persona(1234, "Juan", "Perez", 34)
empleado_1 = Empleado(3456, "sofia", "garcia", 37,540)
#persona_2 = Persona(1245, "Valeria", "Gomez", 28)

# lista.append(persona_1)
# lista.append(persona_2)

#print(persona_1.id)


# persona_1.nombre = "JOSE" 
# print(persona_1.presentarse())
# #print(persona_2.presentarse())

# print(persona_1.edad)
# print(persona_1._apellido)



# print(persona_1.nombre)
# #persona_1.saludar()
# #persona_2.saludar()

print(empleado_1.presentarse())
        
        
        
        