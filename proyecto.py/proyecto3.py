# Diccionario de usuarios vacio para asociar usuarios y sus respectivas claves 
usuarios = {}

# Función para crear un nuevo usuario
def crearUsuario():
    print("Bienvenido al sistema de creación de usuarios.")
    nombreUsuario = input("Ingrese un nombre de usuario: ")
    if nombreUsuario in usuarios:
        print("El nombre de usuario ya existe. Intente con otro nombre.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        usuarios[nombreUsuario] = contrasena
        print("Usuario", nombreUsuario, "creado con éxito.")

# Función para verificar la contraseña y matricular cursos
def verificarContrasena():
    print("Bienvenido al sistema de verificación de usuarios.")
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    if nombreUsuario in usuarios:
        contrasena = input("Ingrese su contraseña: ")
        if usuarios[nombreUsuario] == contrasena:
            print("Contraseña verificada con éxito.")
            matriculaCursos()
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")

# Función para matricular cursos
def matriculaCursos():
    print("Disponibles 3 cursos para matricular:")
    print("1. Curso de Python")
    print("2. Curso de Cocina")
    print("3. Curso de Inglés")

    varCurso = input("Digite 1 para Python, 2 para Cocina, 3 para Inglés, 4 para facturación, 5 para más información: ")

#matricula del Curso de Python

    if varCurso == "1":  
        varModalidad = input("Favor elegir la modalidad para el curso de Python(solo esta diponible el horario de 2pm a 5pm), digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Python presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Python en línea.")
        else:
            print("Número incorrecto")
# matricula del Curso de Cocina
    elif varCurso == "2":  
        varModalidad = input("Favor elegir la modalidad para el curso de Cocina(solo esta diponible el horario de 8am a 11am), digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Cocina presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Cocina en línea.")
        else:
            print("Número incorrecto") 
            
# matricula del Curso de Inglés 

    elif varCurso == "3":  
        varModalidad = input("Favor elegir la modalidad para el curso de Inglés(solo esta diponible el horario de 6pm a 9pm), digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Inglés presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Inglés en línea.")
        else:
            print("Número incorrecto")
            
# Facturación 

    elif varCurso == "4":  
        procesofacturacion()
        
# Más Información

    elif varCurso == "5":  
        informacionCursos()

    else:
        print("Número incorrecto")

    varContinuar = input("Si desea matricular más cursos, digite 1. Cualquier otra tecla para terminar: ")
    
    if varContinuar == "1":
        matriculaCursos()
    else:
        print("Gracias por usar nuestro sistema de matrícula de cursos.")

# Función de Facturación, pago en linea y presencial 
def procesofacturacion():
    varPago =   input("Favor ingresar el método de pago, 1 para pagar en línea, 2 para pagar presencial:")
 

def procesofacturacion():
    varPago = input("Favor ingresar el método de pago, 1 para pagar en línea, 2 para pagar presencial: ")
    
    if varPago == '1':
        # Proceso para pago en línea
        numTarjeta = input("Favor ingresar el número de tarjeta completo: ")
        nombre = input("Favor ingresar el nombre completo: ")
        codigo = input("Favor ingresar el código de seguridad, se encuentra en la parte posterior de la tarjeta y son 3 dígitos: ")
        varCorreo = input("Su pago se realizó con éxito. Si desea la factura digital, favor ingresar el correo electrónico o digite 0 para terminar: ")
        if varCorreo != '0':
            print("Su factura electrónica se le enviará al correo", varCorreo, "¡Gracias por su confianza!")
        else:
            print("¡Gracias por su confianza!")
    elif varPago == '2':
        # Proceso para pago presencial
        print("Para pagar en efectivo se le cobrará el primer día de clases. ¡Gracias por su preferencia!")
    else:
        print("Número incorrecto, intente de nuevo")
        procesofacturacion()

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

# el sistema pricipal, menu y sus opciones 
print("Bienvenido al sistema de gestión de usuarios y matrícula.")
while True:
    print("\n1. Crear un nuevo usuario")
    print("\n2. Verificar usuario y matricular cursos")
    print("\n3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crearUsuario()
    elif opcion == "2":
        verificarContrasena()
    elif opcion == "3":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
