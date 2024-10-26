 
 #convierte a mayudcula y miniscula
 
 
cadena1 = "hola soy josue"
cadena2 = "bienvenido"

mayuscula = cadena1.upper()

minuscula = cadena1.lower()
#ejemplos
# se puede agregar texto en lugar de cadena1
#sustituir texto por cadena y viceversa
texto = "viva saprissa".upper()

print (texto)


# buscar una cadena en una cadena (find)
# devuelve la posicion de la cadena empezando de 0
# distingue de mayuscula y miniscula 
#si devuelve -1 no encontro el valor que se agrego

busqueda_find = cadena1.find("s")
print(busqueda_find)


# busqueda de cadena en una cadena (index)
#si no encuentra resultado da error (es la diferencia con find)

busqueda_index = cadena1.index("y")
print(busqueda_index)

#buscamos una cadena en otra cadena, devuelve la catntidad de veces que encontra una 


 #count

contar = cadena1.count("josue")
print(contar)


#startswith para verificar con que inicia un texto, devuelve true o falce

empieza = cadena1.startswith("hola")
print(empieza)


#endswith para verificar con que termina un texto

termina = cadena1.endswith("e")
print(termina)



#replace para remplazar texto, espacios,comas, numeros

cadenReplace = cadena1.replace("josue","maria")
print(cadenReplace)   


#separar cadenas con lo que le pasemos
#crea una lista de todo lo que hay en la cadena 
#sirve para contar palabras en un texto

separarCadena= cadena1.split("j")
print(separarCadena)


