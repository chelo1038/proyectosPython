def obtener_edades():
    edades = []  
    for i in range(10):
        edad = int(input(f"Ingrese la edad maquina "))  
        edades.append(edad) 
    return edades 


def calcular_promedio(edades):
    suma = sum(edades) 
    promedio = suma / len(edades)  
    return promedio  


def main():
    edades = obtener_edades()  
    promedio = calcular_promedio(edades)  
    print("Lista de edades son:", edades) 
    print("El promedio de edades:", promedio)  

main()




























