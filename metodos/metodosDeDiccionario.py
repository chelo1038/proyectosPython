diccionario={
    "nombre": 'josue',
    "apellido":'mora',
    "profeccion":'ingeniero'}


# .keys devuelve las claves (nombre;apellido;profeccion)

clave= diccionario.keys()
print(clave)


# .get obtener un valor

valor= diccionario.get("nombre")
print(valor)

#eliminado todo de una diccionario 

#diccionario.clear()
#print(diccionario)




#eliminando un elemento de un diccionario (puede ser un elemento o varios)

diccionario.pop("apellido")
print(diccionario)


#items obtener un elemento de un dict_items (iterable)

diccionario_iterable= diccionario.items()

print(diccionario_iterable)



