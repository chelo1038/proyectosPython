
#con la funcion de .split se pueden contar las palabras contando los espacios vacios (" ")

texto = input("favor digite un texto ")
cantidad_de_palabras= texto.split(" ")
cantidad_total = len(cantidad_de_palabras)

print("dijiste ", texto,"y te tomaria ", (cantidad_total/2), "de segundos")






