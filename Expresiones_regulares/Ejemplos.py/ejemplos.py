import re

"""
- preguntar si un texto coincide con un patron
    
"""
#email = "juancito@gmail.com pepito@hotmail.com"
#patron_email = re.compile("[a-z0-9_]+@[a-z0-9_]+\.[a-z{3}]")

frase = "Esto es un 1#02. texto para #7practicar texto expresiones. regulares 94 regulares en textos y no hay pretexto contextos"

cadena = re.sub("##\d", "ocurrencia", frase, 1)
print(cadena)

lista = re.split("#\d", frase, 2)
print(lista)

# cadena = "te"
# f"\\b{cadena}"

#iterador = re.finditer("[^ ]+texto[^ ]*", frase)
#iterador = re.finditer("[a-z]*texto[a-z]*", frase)
#iterador = re.finditer(f"\\b{cadena}", frase)

#for coincidencia in iterador:
#    print(coincidencia.group())

# lista = re.findall("@([^ ]+)", email) 
# print(lista)

# frase2 = """esta es la primera linea
# esta es la segunda linea
# esta es la tercer linea
# esta es la ultima linea"""

# #patron_fin = re.compile("liena$", re.MULTILINE)
# lista = re.findall("linea$", frase2, flags= re.MULTILINE | re.IGNORECASE)




#patron_petente_vieja = re.compile("[A-Z]{3} \d{3}")
# #patron = re.compile("\d")

# # match = patron.match(texto)

# match = patron_petente_vieja.match("ABC 123")
# match = patron_email.match("juanperez89@gmail.com")
# if(match):
#     print("email valido: ", match.group())
# else:
#     print("No hubo coincidencias")

#lista = patron.findall(frase)

#lista = re.findall("\d", frase)

#print(patron_petente_vieja)

