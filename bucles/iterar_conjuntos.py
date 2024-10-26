#iterando conjunto 
# la cantidad de datos es la cantidad de veces que se ejecuta  

animales=["gato","perro","loro","cocodrilo"]
for animal in animales:
    print("ahora la variable animal es igual a: ", animal)
    
    
# recorriendo la lista numeros y multiplicando por 10 

numeros = (5,4,9,2)
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
# recorriendo 2 conjunto al mismoo tiempo 
# se necesita tener la misma cantidad de valores en ambas conjunto 

for animal,numero in zip(animales,numeros):
    print("recorriendo lista 1",animal)
    print("recorriendo lista 1",numero)
    
    
#recorriendo una lista de un parametro que yo le doy (10,15)
# si solo se ingrese un numero (10) arranca de 0 a 9

for num in range(10,15):
    print(num)
    
    
# forma optima de recorrer una lista por su indice 

for num in enumerate(animales):
    
    print(num)
    
#usando el for/else 
# de esta forma siempre se ejecuta el else (solo una vez) aunque no haya valor en la lista o tupla 


for numero in numeros: 
    print("ejecuntado el ultimo valor es: ", {numero})
    
else: 
    print("el bucle termino")

