# Modulo de Usuarios

usuarios = {}

def crear_usuario():
    print("Bienvenido al sistema de creación de usuarios.")
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya existe. Intente con otro nombre.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        usuarios[nombre_usuario] = contrasena
        print("Usuario", nombre_usuario, "creado con éxito.")

def verificar_contrasena():
    print("Bienvenido al sistema de verificación de usuarios.")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios:
        contrasena = input("Ingrese su contraseña: ")
        if usuarios[nombre_usuario] == contrasena:
            print("Contraseña verificada con éxito.")
            matricula_cursos()
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")

# Modulo de Matricula de Cursos

def matricula_cursos():
    print("Disponibles 3 cursos para matricular:")
    print("1. Curso de Python")
    print("2. Curso de Cocina")
    print("3. Curso de Inglés")

    varCurso = input("Digite 1 para Python, 2 para Cocina, 3 para Inglés, 4 para facturación: ")

    if varCurso == "1":  # Curso de Python
        varModalidad = input("Favor elegir la modalidad para el curso de Python, digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Python presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Python en línea.")
        else:
            print("Número incorrecto")

    elif varCurso == "2":  # Curso de Cocina
        varModalidad = input("Favor elegir la modalidad para el curso de Cocina, digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Cocina presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Cocina en línea.")
        else:
            print("Número incorrecto")

    elif varCurso == "3":  # Curso de Inglés
        varModalidad = input("Favor elegir la modalidad para el curso de Inglés, digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Inglés presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Inglés en línea.")
        else:
            print("Número incorrecto")

    elif varCurso == "4":  # Facturación
        print("Procesando facturación...")

    else:
        print("Número incorrecto")

    varContinuar = input("Si desea matricular más cursos, digite 1. Cualquier otra tecla para terminar: ")
    
    if varContinuar == "1":
        matricula_cursos()
    else:
        print("Gracias por usar nuestro sistema de matrícula de cursos.")

# Ejecución del sistema

print("Bienvenido al sistema de gestión de usuarios y matrícula.")
while True:
    print("\n1. Crear un nuevo usuario")
    print("\n2. Verificar usuario y matricular cursos")
    print("\n3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        verificar_contrasena()
    elif opcion == "3":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

