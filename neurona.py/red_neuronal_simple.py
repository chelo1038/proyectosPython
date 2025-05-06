import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

# Preguntas y respuestas para entrenamiento
preguntas = [
    "cuánto es 40-20", 
    "cuánto es 10 * 10", 
    "cuánto es 3 por 7", 
    "cuál es la capital de Francia", 
    "cuál es la capital de costa rica?",
    "cual es la capital de italia?",
    "cual es el mejor quipo de costa rica?",
    "cual es el mejor equipo de españa?",
    "cual numero es mayor 2 o 10",
    "cuantos huesos tienen los humanos?",
    "de que color es el mar?",
    "quien descubrio america?",
    "cuantos continentes existen?",
    "cuanto es 3*3",
    "2 + 2?",
    "cuanto es 10 + 10",
    "cual la raiz cuadrada de 25",
    "cuanto es 11-1",
    "cuanto es 12-1",
    "cuanto es 13-1",
    "cuanto es 14-1",
    "cuanto es 15-1",
    "cual es el mejor deporte del mundo?"
]

respuestas = [
    "20", 
    "100", 
    "21", 
    "París", 
    "san jose",
    "roma",
    "saprissa",
    "real madrid",
    "10",
    "206",
    "azul",
    "rojo",
    "cristobal colon",
    "5",
    "9",
    "4",
    "20",
    "5",
    "10",
    "11",
    "12",
    "13",
    "futbol"
]

# Función para limpiar las preguntas
def limpiar_pregunta(pregunta):
    # Asegura que haya un espacio entre números y palabras
    pregunta = re.sub(r"(\d)([a-zA-Z])", r"\1 \2", pregunta)
    pregunta = re.sub(r"([a-zA-Z])(\d)", r"\1 \2", pregunta)
    # Elimina caracteres especiales que no sean números o letras
    pregunta = re.sub(r"[^\w\s]", " ", pregunta)
    # Remueve espacios extra
    pregunta = re.sub(r"\s+", " ", pregunta).strip()
    return pregunta

# Limpieza de todas las preguntas
preguntas_limpias = [limpiar_pregunta(p) for p in preguntas]

# Vectorizamos las preguntas limpias
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(preguntas_limpias).toarray()

# Convertimos las respuestas a formato numérico para la red neuronal
unique_respuestas = list(set(respuestas))
y = np.array([unique_respuestas.index(r) for r in respuestas])

# Creamos y entrenamos la red neuronal
modelo = MLPClassifier(hidden_layer_sizes=(10,), max_iter=20000)
modelo.fit(X, y)

# Guardar los pesos y sesgos de la capa oculta
pesos_capa_oculta = modelo.coefs_[0]
sesgos_capa_oculta = modelo.intercepts_[0]

# Función para hacer preguntas al modelo
def preguntar_al_modelo(pregunta):
    pregunta_limpia = limpiar_pregunta(pregunta)  # Limpia la pregunta antes de procesarla
    X_nueva = vectorizer.transform([pregunta_limpia]).toarray()
    prediccion = modelo.predict(X_nueva)
    return unique_respuestas[prediccion[0]]

# Prueba con una pregunta
pregunta_prueba = "cual es la capital de china"
respuesta = preguntar_al_modelo(pregunta_prueba)
print(f"Pregunta: {pregunta_prueba}")
print(f"Respuesta: {respuesta}")
print("Preguntas limpias:")
print(preguntas_limpias)
print("Vocabulario generado:", vectorizer.vocabulary_)
print("Matriz resultante de las preguntas:")
print(X)
