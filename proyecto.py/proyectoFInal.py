# Diccionario de usuarios vacío para asociar usuarios y sus respectivas claves 
usuarios = {}

# Diccionario para almacenar los cursos matriculados por cada usuario
cursosMatriculados = {}

# Función para crear un nuevo usuario
def crearUsuario():
    print("\nBienvenido al sistema de creación de usuarios.")
    print("\n===========================================================")
    nombreUsuario = input("\nIngrese un nombre de usuario: ")
    if nombreUsuario in usuarios:
        print("\nEl nombre de usuario ya existe. Intente con otro nombre.")
    else:
        contrasena = input("\nIngrese una contraseña: ")
        usuarios[nombreUsuario] = contrasena
        cursosMatriculados[nombreUsuario] = ""  # Inicializar cadena vacía para los cursos
        print("\nUsuario", nombreUsuario, "creado con éxito.")
        print("\n===========================================================")

# Función para verificar la contraseña y matricular cursos
def verificarContrasena():
    print("\nBienvenido al sistema de verificación de usuarios.")
    print("\n===========================================================")
    nombreUsuario = input("\nIngrese su nombre de usuario: ")

    if nombreUsuario in usuarios:
        contrasena = input("\nIngrese su contraseña: ")

        if usuarios[nombreUsuario] == contrasena:
            print("\nContraseña verificada con éxito.")
            print("\n===========================================================")
            matriculaCursos(nombreUsuario)
        else:
            print("\nContraseña incorrecta.")
            print("\n===========================================================")
    else:
        print("\nEl usuario no existe.")
        print("\n===========================================================")

# Función para matricular cursos
def matriculaCursos(nombreUsuario):
    print("\nDisponibles 3 cursos para matricular:")
    print("\n1. Curso de Python")
    print("\n2. Curso de Cocina")
    print("\n3. Curso de Inglés")
    print("\n4. Ver cursos matriculados")
    print("\n5. Facturación")
    print("\n6. Más información")

    varCurso = input("\nDigite 1 para Python, 2 para Cocina, 3 para Inglés, 4 para ver cursos matriculados, 5 para facturación, 6 para más información: ")
    print("\n===========================================================")

    # Matricula del Curso de Python
    if varCurso == "1":
        varModalidad = input("\nFavor elegir la modalidad para el curso de Python (solo está disponible el horario de 2pm a 5pm), digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            cursosMatriculados[nombreUsuario] += "Python presencial, "
            print("\nSe matriculó con éxito en Python presencial.")
        elif varModalidad == "2":
            cursosMatriculados[nombreUsuario] += "Python en línea, "
            print("\nSe matriculó con éxito en Python en línea.")
        else:
            print("\nNúmero incorrecto")

    # Matricula del Curso de Cocina
    elif varCurso == "2":
        varModalidad = input("\nFavor elegir la modalidad para el curso de Cocina (solo está disponible el horario de 8am a 11am), digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            cursosMatriculados[nombreUsuario] += "Cocina presencial, "
            print("\nSe matriculó con éxito en Cocina presencial.")
        elif varModalidad == "2":
            cursosMatriculados[nombreUsuario] += "Cocina en línea, "
            print("\nSe matriculó con éxito en Cocina en línea.")
        else:
            print("\nNúmero incorrecto")

    # Matricula del Curso de Inglés
    elif varCurso == "3":
        varModalidad = input("\nFavor elegir la modalidad para el curso de Inglés (solo está disponible el horario de 6pm a 9pm), digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            cursosMatriculados[nombreUsuario] += "Inglés presencial, "
            print("\nSe matriculó con éxito en Inglés presencial.")
        elif varModalidad == "2":
            cursosMatriculados[nombreUsuario] += "Inglés en línea, "
            print("\nSe matriculó con éxito en Inglés en línea.")
        else:
            print("\nNúmero incorrecto")

    # Ver cursos matriculados
    elif varCurso == "4":
        if cursosMatriculados[nombreUsuario]:
            print("\nCursos matriculados por", nombreUsuario + ":")
            print(cursosMatriculados[nombreUsuario])  
        else:
            print("\nNo ha matriculado ningún curso aún.")
        print("\n===========================================================")

    # Facturación
    elif varCurso == "5":
        procesofacturacion()

    # Más información
    elif varCurso == "6":
        informacionCursos()

    else:
        print("\nNúmero incorrecto")

    varContinuar = input("\nSi desea seguir navegando en el sistema digite 1. Cualquier otra tecla para terminar: ")

    if varContinuar == "1":
        matriculaCursos(nombreUsuario)
    else:
        print("\nGracias por usar nuestro sistema de matrícula de cursos.")
        print("\n===========================================================")

# Función de Facturación, pago en línea y presencial 
def procesofacturacion():
    varPago = input("\nFavor ingresar el método de pago, 1 para pagar en línea, 2 para pagar presencial: ")
    print("\n===========================================================")
    
    if varPago == '1':
        # Proceso para pago en línea
        numTarjeta = input("\nFavor ingresar el número de tarjeta completo: ")
        nombre = input("\nFavor ingresar el nombre completo: ")
        codigo = input("\nFavor ingresar el código de seguridad, se encuentra en la parte posterior de la tarjeta y son 3 dígitos: ")
        varCorreo = input("\nSu pago se realizó con éxito. Si desea la factura digital, favor ingresar el correo electrónico o digite 0 para terminar: ")

        if varCorreo != '0':
            print("\nSu factura electrónica se le enviará al correo", varCorreo, "¡Gracias por su confianza!")
        else:
            print("\n¡Gracias por su confianza!")
    elif varPago == '2':
        # Proceso para pago presencial
        print("\nPara pagar en efectivo se le cobrará el primer día de clases. ¡Gracias por su preferencia!")
    else:
        print("\nNúmero incorrecto, intente de nuevo")
        procesofacturacion()

# Función para obtener más información sobre los cursos
def informacionCursos():
    print("\nPara más información de los cursos que brindamos, 1 para cocina, 2 para Python, 3 para inglés, 0 para terminar:")

    varMasInformacion = int(input())

    if varMasInformacion == 1:
        print("\nAcá tienes la página web para conocer los detalles del curso de cocina: https://cocina.tec.ac.cr/")
    elif varMasInformacion == 2:
        print("\nLa página web del curso de Python: https://educacr.uc.ac.cr/curso-de-programacion-python/")
    elif varMasInformacion == 3:
        print("\nLa página web del curso de inglés: https://ingles.uc.cr/cursos/")
    elif varMasInformacion == 0:
        print("\nGracias por usar nuestro sistema.")
    else:
        print("\nNúmero incorrecto.")

# El sistema principal, menú y sus opciones 
print("===========================================================")
print("\nBienvenido al sistema de gestión de usuarios y matrícula.")
print("===========================================================")
while True:
    print("\n1. Crear un nuevo usuario")
    print("\n2. Verificar usuario y matricular cursos")
    print("\n3. Salir")

    opcion = input("\nSeleccione una opción: ")
    print("\n===========================================================")

    if opcion == "1":
        crearUsuario()
    elif opcion == "2":
        verificarContrasena()
    elif opcion == "3":
        print("\nSaliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Intente nuevamente.")
