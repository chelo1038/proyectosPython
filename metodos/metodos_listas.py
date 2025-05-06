#creando lista con list
lista = list ([True, False,778,96,13])
print(lista)

#devuelve la cantidad de elementos de una lista 
cantidad_de_elemntos = len(lista)
print(cantidad_de_elemntos)


#se puede con texto
#agregando elementos  a una lista con append 
lista.append(55)
print(lista)


#se puede con texto
#agregando un elemento a la lista en una posicion especifica
#el primer numero significa la pocicion
lista.insert(1, 8)
print(lista)


#se puede con texto
#agregando una lista ([]) a una lista 
lista.extend([4,70,100])
print(lista)


#eleiminando un alementos de una lista (por su pocicion) .pop
#.pop y un -1 elimina el ultimo elemento de la lista
#.pop y un -2 elimina el anteultimo y asi sucesivamente 
lista.pop(3)
print(lista)



#removiendo un elemento de una lista por su valor entre "comillas"
lista.remove(8)
print(lista)



#eliminando todo lo de una lista 
#lista.clear()
#print(lista)

# ordena numeros acendentes 
#ordenando elementos de una lista de forma acendente .sort (si usamos el parametro reverse=true lo ordena en reversa )
#los falsos vienen primero luego los true y despues lo numeros de menor a mayor.sort
lista.sort()
print (lista) 



#.reverse() para darle vuelta a una lista sin importar si estan en orden o desorden

lista.reverse()
print (lista)


#verificando si un elemento se encuentra en una lista 
#devuelve la pocicion donde esta el elemento

buscando_index = lista.index(13)

print(buscando_index)


# esto sirve para ver que se puede obtener una lista de acciones 
#que se le pueden aplicar objeto(lista,tupla y mas.. )
print(dir(lista))












