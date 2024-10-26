import numpy as np
import matplotlib.pyplot as plt

# Neurona 1: Celsius a Fahrenheit
peso1 = np.random.rand()
bias1 = np.random.rand()

def activacion_lineal1(x):
    return x

def derivada_lineal1(x):
    return 1

# Neurona 2: Fahrenheit a Kelvin
peso2 = np.random.rand()
bias2 = np.random.rand()

def activacion_lineal2(x):
    return x + 273.15  # Para convertir de Celsius a Kelvin

def derivada_lineal2(x):
    return 1

# Datos de entrenamiento para la Neurona 1
celsius = np.array([0, 100])
fahrenheit = np.array([32, 212])

# Datos de entrenamiento para la Neurona 2
kelvin = fahrenheit + 273.15  # Simplificación para el ejemplo

# Entrenamiento de la Neurona 1
tasa_aprendizaje1 = 0.01
epocas = 10000
errores1 = []

for _ in range(epocas):
    total_error1 = 0
    for i in range(len(celsius)):
        z1 = np.dot(celsius[i], peso1) + bias1
        salida1 = activacion_lineal1(z1)

        error1 = fahrenheit[i] - salida1
        total_error1 += error1 ** 2

        ajuste1 = error1 * derivada_lineal1(salida1)

        peso1 += tasa_aprendizaje1 * ajuste1 * celsius[i]
        bias1 += tasa_aprendizaje1 * ajuste1

    errores1.append(total_error1 / len(celsius))

# Entrenamiento de la Neurona 2
tasa_aprendizaje2 = 0.01
errores2 = []

for _ in range(epocas):
    total_error2 = 0
    for i in range(len(fahrenheit)):
        z2 = np.dot(fahrenheit[i], peso2) + bias2
        salida2 = activacion_lineal2(z2)

        error2 = kelvin[i] - salida2
        total_error2 += error2 ** 2

        ajuste2 = error2 * derivada_lineal2(salida2)

        peso2 += tasa_aprendizaje2 * ajuste2 * fahrenheit[i]
        bias2 += tasa_aprendizaje2 * ajuste2

    errores2.append(total_error2 / len(fahrenheit))

# Prueba
celsius_prueba = 37  # Ejemplo: 37 grados Celsius

# Neurona 1: Celsius a Fahrenheit
z1 = np.dot(celsius_prueba, peso1) + bias1
fahrenheit_predicho = activacion_lineal1(z1)

# Neurona 2: Fahrenheit a Kelvin
z2 = np.dot(fahrenheit_predicho, peso2) + bias2
kelvin_predicho = activacion_lineal2(z2)

print(f"Temperatura en Celsius: {celsius_prueba}")
print(f"Predicción de Fahrenheit: {fahrenheit_predicho}")
print(f"Predicción de Kelvin: {kelvin_predicho}")

# Graficar la evolución del error
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(errores1)
plt.title("Evolución del Error (Neurona 1: Celsius a Fahrenheit)")
plt.xlabel("Épocas")
plt.ylabel("Error Medio Cuadrado")

plt.subplot(1, 2, 2)
plt.plot(errores2)
plt.title("Evolución del Error (Neurona 2: Fahrenheit a Kelvin)")
plt.xlabel("Épocas")
plt.ylabel("Error Medio Cuadrado")

plt.show()
