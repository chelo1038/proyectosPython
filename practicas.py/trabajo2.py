#Un profesor necesita un programa que calcule la nota final de 
#sus estudiantes. Tiene 5 estudiantes que realizan 4 actividades
#evaluativas
#Utilice una matriz para almacenar las calificaciones donde 
#cada fila representará un estudiante y las columnas 
#almacenarán la información de las actividades evaluativas



josue = [0,0,0,0]
maria = [0,0,0,0]
andres = [0,0,0,0]
pedro = [0,0,0,0]
Gilberth= [0,0,0,0]


#NOTAS Y PROMEDIO DE JOSUE 

nota1= int(input("ingrese la nota de la primer actividad evaluativa del josue "))
josue [0] = nota1
nota2= int(input("ingrese la nota de la segunda actividad evaluativa de josue "))
josue [1] = nota2
nota3= int(input("ingrese la nota de la tercer actividad evaluativa de josue "))
josue [2] = nota3
nota4= int(input("ingrese la nota de la cuarta actividad evaluativa de josue "))
josue [3] = nota4

notaFinal = int((nota1 + nota2 + nota3 + nota4) /4)
print("las notas son: ", josue, "y el promedio es de: ", notaFinal)

if notaFinal>=70:
    print("felicidades josue, aprovo el curso ")
else:
    print("lo siento josue, reprobo el curso")

#NOTAS Y PROMEDIO DE maria

notaE1= int(input("ingrese la nota de la primer actividad evaluativa de maria  "))
maria [0] = notaE1
notaE2= int(input("ingrese la nota de la segunda actividad evaluativa maria "))
maria [1] = notaE2
notaE3= int(input("ingrese la nota de la tercer actividad evaluativa maria "))
maria [2] = notaE3
notaE4= int(input("ingrese la nota de la cuarta actividad evaluativa maria "))
maria [3] = notaE4

notaFinalM = int((notaE1+ notaE2 + notaE3 + notaE4) /4)

print("las notas son: ", maria, "y el promedio es de: " ,notaFinalM)
if notaFinalM>=70:
    print("felicidad maria, es aprovo el curso ")
else:
    print("lo siento maria, reprobo el curso")
    
#NOTAS Y PROMEDIO DE ANDRES
    
notaA1= int(input("ingrese la nota de la primer actividad evaluativa de andres "))
andres [0] = notaA1
notaA2= int(input("ingrese la nota de la segunda actividad evaluativa andres "))
andres [1] = notaA2
notaA3= int(input("ingrese la nota de la tercer actividad evaluativa andres "))
andres [2] = notaA3
notaA4= int(input("ingrese la nota de la cuarta actividad evaluativa andres "))
andres [3] = notaA4

notaFinalA = int((notaA1 + notaA2 + notaA3 + notaA4) /4)
print("la notas son: ", andres, "y el promedio es de ", notaFinalA)
if notaFinalA>=70:
    print("felicidades andres, aprovo el curso ")
else:
    print("lo siento andres, reprobo el curso")

notaP1= int(input("ingrese la nota de la primer actividad evaluativa de Pedro  "))
pedro [0] = notaP1
notaP2= int(input("ingrese la nota de la segunda actividad evaluativa Pedro "))
pedro [1] = notaP2
notaP3= int(input("ingrese la nota de la tercer actividad evaluativa Pedro "))
pedro [2] = notaP3
notaP4= int(input("ingrese la nota de la cuarta actividad evaluativa Pedro "))
pedro[3] = notaP4

notaFinalP = int((notaP1 + notaP2+ notaP3 + notaP4) /4)

print("las notas son: ", pedro, "y el promedio es de: " ,notaFinalP)
if notaFinalP>=70:
    print("felicidades pedro, aprovo el curso ")
else:
    print("lo siento pedro, reprobo el curso")
    
    
notaG= int(input("ingrese la nota de la primer actividad evaluativa del Gilberth "))
Gilberth [0] = notaG
notaG2= int(input("ingrese la nota de la segunda actividad evaluativa de Gilberth "))
Gilberth [1] = notaG2
notaG3= int(input("ingrese la nota de la tercer actividad evaluativa de Gilberth "))
Gilberth [2] = notaG3
notaG4= int(input("ingrese la nota de la cuarta actividad evaluativa de Gilberth "))
Gilberth [3] = notaG4

notaFinalG = int((notaG + notaG2 + notaG3+ notaG4) /4)
print("las notas son: ", Gilberth, "y el promedio es de: ", notaFinalG)

if notaFinalG>=70:
    print("felicidades Gilberth , aprovo el curso ")
else:
    print("lo siento Gilberth, reprobo el curso")

    





