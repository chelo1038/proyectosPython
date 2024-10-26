def obtener_edades ():
    edades = []
    for i in range(10):
     edad = int(input("ingrese la edad titan "))
     edades.append(edad)
    return edades

def calcular_promedio (edades):
    suma = sum (edades)
    promedio = suma /len(edades)
    return promedio

def main():
    edades = obtener_edades()
    promedio = calcular_promedio(edades)
    print("las edades son " , edades)
    print ("el promedio es de; ", promedio)

main()
    

