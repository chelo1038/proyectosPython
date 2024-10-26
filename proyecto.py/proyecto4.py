# Diccionario de usuarios y sus respectivas claves
usuarios = {}

# Diccionario para almacenar los cursos matriculados por cada usuario
cursos_usuario = {}

# Espacios disponibles en los cursos (arreglo bidimensional)
# Cada fila representa un curso y cada columna una modalidad (0: Presencial, 1: En línea)
espacios_disponibles = {
    "Python": [5, 5],  # 5 espacios para presencial, 5 para en línea
    "Cocina": [5, 5],
    "Inglés": [5, 5]
}

# Función para crear un nuevo usuario
def crearUsuario():
    print("\n" + "="*50)
    print("Bienvenido al sistema de creación de usuarios.")
    print("="*50)
    nombreUsuario = input("Ingrese un nombre de usuario: ")
    if nombreUsuario in usuarios:
        print("El nombre de usuario ya existe. Intente con otro nombre.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        usuarios[nombreUsuario] = contrasena
        cursos_usuario[nombreUsuario] = []  # Inicializar lista de cursos
        print("Usuario", nombreUsuario, "creado con éxito.")
    print("="*50 + "\n")

# Función para verificar la contraseña y matricular cursos
def verificarContrasena():
    print("\n" + "="*50)
    print("Bienvenido al sistema de verificación de usuarios.")
    print("="*50)
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    if nombreUsuario in usuarios:
        contrasena = input("Ingrese su contraseña: ")
        if usuarios[nombreUsuario] == contrasena:
            print("Contraseña verificada con éxito.")
            matriculaCursos(nombreUsuario)
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")
    print("="*50 + "\n")

# Función para matricular cursos
def matriculaCursos(nombreUsuario):
    print("\n" + "="*50)
    print("Disponibles 3 cursos para matricular:")
    print("1. Curso de Python")
    print("2. Curso de Cocina")
    print("3. Curso de Inglés")
    print("="*50)

    varCurso = input("Digite 1 para Python, 2 para Cocina, 3 para Inglés: ")
    curso = None

    if varCurso == "1":
        curso = "Python"
    elif varCurso == "2":
        curso = "Cocina"
    elif varCurso == "3":
        curso = "Inglés"
    else:
        print("Número incorrecto.")
        return

    varModalidad = input("Elija la modalidad (1 para presencial, 2 para en línea): ")
    modalidad = None

    if varModalidad == "1":
        modalidad = 0
    elif varModalidad == "2":
        modalidad = 1
    else:
        print("Número incorrecto.")
        return

    # Verificar si hay espacios disponibles
    if espacios_disponibles[curso][modalidad] > 0:
        espacios_disponibles[curso][modalidad] -= 1
        cursos_usuario[nombreUsuario].append((curso, "Presencial" if modalidad == 0 else "En línea"))
        print(f"Se matriculó con éxito en {curso} ({'Presencial' if modalidad == 0 else 'En línea'}).")
    else:
        print(f"No hay espacios disponibles en {curso} ({'Presencial' if modalidad == 0 else 'En línea'}).")

    varContinuar = input("Si desea matricular más cursos, digite 1. Cualquier otra tecla para terminar: ")
    
    if varContinuar == "1":
        matriculaCursos(nombreUsuario)
    else:
        print("Gracias por usar nuestro sistema de matrícula de cursos.")
    print("="*50 + "\n")

# Función para procesar el pago y generar factura
def procesofacturacion(nombreUsuario):
    print("\n" + "="*50)
    varPago = input("Favor ingresar el método de pago, 1 para pagar en línea, 2 para pagar presencial: ")
    
    if varPago == '1':
        # Proceso para pago en línea
        numTarjeta = input("Favor ingresar el número de tarjeta completo: ")
        nombre = input("Favor ingresar el nombre completo: ")
        codigo = input("Favor ingresar el código de seguridad (3 dígitos): ")
        varCorreo = input("Su pago se realizó con éxito. Si desea la factura digital, favor ingresar el correo electrónico o digite 0 para terminar: ")
        if varCorreo != '0':
            print("Su factura electrónica se le enviará al correo", varCorreo)
        else:
            print("¡Gracias por su confianza!")
    elif varPago == '2':
        # Proceso para pago presencial
        print("Para pagar en efectivo se le cobrará el primer día de clases. ¡Gracias por su preferencia!")
    else:
        print("Número incorrecto, intente de nuevo.")
        procesofacturacion(nombreUsuario)
    
    # Imprimir factura
    print("\n" + "="*50)
    print(f"Factura para el usuario: {nombreUsuario}")
    print("Cursos matriculados:")
    for curso, modalidad in cursos_usuario[nombreUsuario]:
        print(f"- {curso} ({modalidad})")
    print("="*50 + "\n")

# Función para obtener más información sobre los cursos
def informacionCursos():
    print("Para más información de los cursos que brindamos, 1 para cocina, 2 para Python, 3 para inglés, 0 para terminar:")
    varMasInformacion = int(input())

    if varMasInformacion == 1:
        print("Acá tienes la página web para conocer los detalles del curso de cocina: https://cocina.tec.ac.cr/")
    elif varMasInformacion == 2:
        print("La página web del curso de Python: https://educacr.uc.ac.cr/curso-de-programacion-python/")
    elif varMasInformacion == 3:
        print("La página web del curso de inglés: https://ingles.uc.cr/cursos/")
    elif varMasInformacion == 0:
        print("Gracias por usar nuestro sistema.")
    else:
        print("Número incorrecto.")

# Sistema principal, menú y sus opciones
print("Bienvenido al sistema de gestión de usuarios y matrícula.")
while True:
    print("\n1. Crear un nuevo usuario")
    print("2. Verificar usuario y matricular cursos")
    print("3. Visualizar cursos matriculados")
    print("4. Imprimir factura")
    print("5. Mostrar espacios disponibles")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crearUsuario()
    elif opcion == "2":
        verificarContrasena()
    elif opcion == "3":
        nombreUsuario = input("Ingrese su nombre de usuario: ")
        if nombreUsuario in cursos_usuario:
            print(f"Cursos matriculados por {nombreUsuario}: {cursos_usuario[nombreUsuario]}")
        else:
            print("Usuario no encontrado.")
    elif opcion == "4":
        nombreUsuario = input("Ingrese su nombre de usuario: ")
        if nombreUsuario in cursos_usuario:
            procesofacturacion(nombreUsuario)
        else:
            print("Usuario no encontrado.")
    elif opcion == "5":
        print("\nEspacios disponibles en los cursos:")
        for curso, espacios in espacios_disponibles.items():
            print(f"{curso}: {espacios[0]} en presencial, {espacios[1]} en línea")
    elif opcion == "6":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
