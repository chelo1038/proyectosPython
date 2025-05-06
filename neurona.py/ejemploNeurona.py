from transformers import pipeline

# Crear un pipeline de preguntas y respuestas
qa_pipeline = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

# Contexto sobre el que el modelo responderá preguntas
contexto = """
El fútbol es considerado el mejor deporte del mundo por millones de personas. 
Fue creado en Inglaterra y ha evolucionado hasta convertirse en una pasión mundial.
"""

# Hacer una pregunta
pregunta = "¿Cuál es el mejor deporte del mundo?"
respuesta = qa_pipeline(question=pregunta, context=contexto)

# Mostrar el resultado
print(f"Pregunta: {pregunta}")
print(f"Respuesta: {respuesta['answer']}")
