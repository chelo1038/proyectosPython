#praticas 
# Función para calcular el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Solicitar al usuario su peso y altura
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

# Determinar la categoría del IMC
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Mostrar el resultado
print(f"Tu IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")

    





