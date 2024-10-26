# creando una lista 
#saltarse un dato con la sentencia continue
# saltara lo que esta dentro del if 

frutas = ("manzana","pera","papaya","piña","limon","sandia")
cadena = "hola josue"
numeros = [2,5,8,10]


for fruta in frutas:
    if fruta ==  ("mazana"):
        continue
    print("me voy a comer ", fruta)
    
    
frutas = ("manzana","pera","papaya","piña")



# evitar que el bucle siga ejecutandose con la sentecia break
# cuando el valor es igual a (piña) rompe el bucle 


for fruta in frutas:
    if fruta ==  ("piña"):
        break
    print("me voy a comer ", fruta)
    
    
    
# recorrer una cadena de texto = es lo mismo que iterar 
# lo recorre letra por letra 

for letra in cadena:
    print(letra)
    


# for en una sola linea de codigo (duplicamos los numeros)

numero_duplidados = [x*2 for x in numeros]
print(numero_duplidados)

    
    
    