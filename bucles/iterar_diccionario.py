
# recorriendo un diccionario para obtener las claves y el valor 

diccionario = {
    "nombre": "josue",
    "apellido": "mora",
    "edad": 28
}

#devolvera una tupla
for key in diccionario.items():

    print("la claves y el valor es:", key  )
    

#para solo obtener la clave es asi 

for key in diccionario:
    key
    print("la clave es ", key )
    
    
    
# recorriendo diccionario con .items() para imprimir de forma ordenada la clave y el valor 

for datos in diccionario.items():
    key = datos[0]
    value = datos [1]
    print(f"la clave es: {key} y el valor es: {value}" )
    