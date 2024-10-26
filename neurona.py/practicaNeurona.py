import numpy as np

# Inicializamos los pesos y el bias aleatoriamente
peso = np.random.rand()  # Peso de la neurona
bias = np.random.rand()  # Bias de la neurona

# Definimos la función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide para el paso de entrenamiento
def sigmoid_derivative(x):
    return x * (1 - x)

# Simulamos una entrada (puede ser cualquier número)
entrada = np.array([0.5])

# Calculamos la salida de la neurona
z = np.dot(entrada, peso) + bias  # Producto punto de la entrada y el peso + bias
salida = sigmoid(z)

print("Entrada:", entrada)
print("Peso:", peso)
print("Bias:", bias)
print("Salida antes de entrenamiento:", salida)

# Definimos el aprendizaje
tasa_aprendizaje = 0.1
epocas = 10000  # Número de veces que se repetirá el entrenamiento

# Definimos la salida deseada
salida_deseada = np.array([1])

# Proceso de entrenamiento
for _ in range(epocas):
    # Forward pass
    z = np.dot(entrada, peso) + bias
    salida = sigmoid(z)
    
    # Calculamos el error
    error = salida_deseada - salida
    
    # Backpropagation
    ajuste = error * sigmoid_derivative(salida)
    
    # Actualizamos los pesos y el bias
    peso += tasa_aprendizaje * ajuste * entrada
    bias += tasa_aprendizaje * ajuste

# Resultado final después del entrenamiento
z = np.dot(entrada, peso) + bias
salida = sigmoid(z)

print("Salida después de entrenamiento:", salida)













