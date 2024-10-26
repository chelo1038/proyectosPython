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
dolares = np.array([7,8,9])
colones = np.array([3500,4000,4500])

# Proceso de entrenamiento
tasa_aprendizaje = 0.01
epocas = 10000
errores = []

for _ in range(epocas):
    total_error = 0
    for i in range(len(dolares)):
        z = np.dot(dolares[i], peso) + bias
        salida = activacion_lineal(z)
        
        error = colones[i] - salida
        total_error += error ** 2
        
        ajuste = error * derivada_lineal(salida)
        
        peso += tasa_aprendizaje * ajuste * dolares[i]
        bias += tasa_aprendizaje * ajuste

    errores.append(total_error / len(dolares))

# Prueba
dolares_prueba = 10 # Ejemplo: 2 dólares
z = np.dot(dolares_prueba, peso) + bias
colones_predicho = activacion_lineal(z)

print(f"para la cantidad de: {dolares_prueba} dolares ")
print(f"la Predicción de colones es : {colones_predicho}")

# Graficar la evolución del error
plt.plot(errores)
plt.title("Evolución del Error durante el Entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Error Medio Cuadrado")
plt.show()
