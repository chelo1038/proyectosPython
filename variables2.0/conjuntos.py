#creando un conjunto con set()
#los datos de set no son modificables

conjunto = set(["dato 1 ", "dato 2 "])

print(conjunto)

#metiendo un conjunto detro de otro conjunto 
#hay que crear un conjunto inmutable con "frozenset"
#se usa con parentesis y parentesis cuadrado ([])

conjunto1= frozenset(["dato 1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

# teoria de conjuntos 
# un sub conjunto con .issubset devuelve un true o false 

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

resultado = conjunto2.issubset(conjunto1)
print(resultado)


# super conjunto con .issuperset devuelve un true o false 
resultado2 = conjunto1.issuperset(conjunto2)
print(resultado2)

#verificando si hay numero en comun con isdisjoint
#entrega false SI hay numeros iguales 
#entrega true si NO hay numero iguales 

resultado3 = conjunto1.isdisjoint(conjunto2)
print(resultado3)



