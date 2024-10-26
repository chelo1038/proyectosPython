import numpy as np
import matplotlib.pyplot as plt

# Inicializamos los pesos y el bias aleatoriamente
peso = np.random.rand()
bias = np.random.rand()

# Definimos la función de activación (lineal en este caso)
def activacion_lineal(x):
    return x

# Derivada de la función lineal
def derivada_lineal(x):
    return 1

# Datos de entrenamiento
celsius = np.array([0,15,25,80,100])
fahrenheit = np.array([32,77, 59,176,212])

# Proceso de entrenamiento
tasa_aprendizaje = 0.01
epocas = 10000
errores = []

for _ in range(epocas):
    total_error = 0
    for i in range(len(celsius)):
        z = np.dot(celsius[i], peso) + bias
        salida = activacion_lineal(z)
        
        error = fahrenheit[i] - salida
        total_error += error**2
        
        ajuste = error * derivada_lineal(salida)
        
        peso += tasa_aprendizaje * ajuste * celsius[i]
        bias += tasa_aprendizaje * ajuste
    
    errores.append(total_error / len(celsius))  # Guardamos el error medio cuadrado

# Prueba
celsius_prueba = 37  # Ejemplo: temperatura del cuerpo humano en Celsius
z = np.dot(celsius_prueba, peso) + bias
fahrenheit_predicho = activacion_lineal(z)

print(f"Temperatura en Celsius: {celsius_prueba}°C")
print(f"Predicción de Fahrenheit: {fahrenheit_predicho}°F")

# Graficar la evolución del error
plt.plot(errores)
plt.title("Evolución del Error durante el Entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Error Medio Cuadrado")
plt.show()

