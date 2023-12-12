import json

persona_string = '{"id": 1, "nombre": "juan", "edad": 40}'
print(type(persona_string))
print(persona_string)

persona_dict = json.loads(persona_string)
print(type(persona_dict))
print(persona_dict)
print(persona_dict['nombre'])

persona_json = json.dumps(persona_dict, indent=4)
print(persona_json)
print(type(persona_json))