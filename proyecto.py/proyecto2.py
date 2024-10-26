usuarios ={}


def crearUsuario ():
    print("bienbenido al sistema de creacion de usuario ")
    nombreDeUsuario= input("favor ingrese un usuario")
    if nombreDeUsuario in usuarios:
        print("el usuario ya existe")
    else:
        contraseña= input("favor ingresar una contraseña")
        usuarios[nombreDeUsuario] = contraseña 
        print("Usuario", nombreDeUsuario, "creado con éxito.")
        
def verificarContraseña():
    print("Bienvenido al sistema de verificación de usuarios.")
    nombreDeUsuario = input("Ingrese su nombre de usuario: ")
    if nombreDeUsuario in usuarios:
        contrasena = input("Ingrese su contraseña: ")
        if usuarios[nombreDeUsuario] == contrasena:
            print("Contraseña verificada con éxito.")
            matricula_cursos()
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")
        

 
def matricula_cursos():
    print("Disponibles 3 cursos para matricular:")
    print("1. Curso de Python")
    print("2. Curso de Cocina")
    print("3. Curso de Inglés")       
    
varCurso= input("digite 1 para curso de python. 2 para curse de cocina. 3 para curso de ingles. 4 para facturacion")


# matricula del curso de python
if varCurso =="1":
    varModalidad=("favor elegir la modalidad del curso, 1 para presencial. 2 para matricular en linea: ")
    if varModalidad =="1":
           print("Se matriculó con éxito en Python presencial.")
    elif varModalidad == "2":
            print("Se matriculó con éxito en Python en línea.")
    else:
            print("Número incorrecto")
            
            
# matricula del Curso de Cocina
     
            
elif varCurso == "2":  
        varModalidad = input("Favor elegir la modalidad para el curso de Cocina, digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Cocina presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Cocina en línea.")
        else:
            print("Número incorrecto")
            
# matricula del Curso de Inglés   
            
elif varCurso == "3": 
        varModalidad = input("Favor elegir la modalidad para el curso de Inglés, digite 1 para presencial o 2 para en línea: ")

        if varModalidad == "1":
            print("Se matriculó con éxito en Inglés presencial.")
        elif varModalidad == "2":
            print("Se matriculó con éxito en Inglés en línea.")
        else:
            print("Número incorrecto")
            
    # proseso de facturacion  de Facturación        
            

elif varCurso == "4":  # Facturación
        proceso_facturacion()

elif varCurso == "5":  # Más Información
        informacion_cursos()
else:
        print("Número incorrecto")

varContinuar = input("Si desea matricular más cursos, digite 1. Cualquier otra tecla para terminar: ")
    
if varContinuar == "1":
        matricula_cursos()
else:
        print("Gracias por usar nuestro sistema de matrícula de cursos.")
def proceso_facturacion():
    print("Favor ingresar el método de pago, 1 para pagar en línea, 2 para pagar presencial:")
    varPago = int(input())  # Obtener el método de pago

    if varPago == 1:
        # Proceso para pago en línea
        print("Favor ingresar el número de tarjeta completo:")
        numTarjeta = input()

        print("Favor ingresar el nombre completo:")
        nombre = input()

        print("Favor ingresar el código de seguridad, se encuentra en la parte posterior de la tarjeta y son 3 dígitos:")
        codigo = input()

        print("Su pago se realizó con éxito. Si desea la factura digital, favor ingresar el correo electrónico o digite 0 para terminar:")
        varCorreo = input()

        if varCorreo != '0':
            print(f"Su factura electrónica se le enviará al correo {varCorreo}. ¡Gracias por su confianza!")
    elif varPago == 2:
        # Proceso para pago presencial
        print("Para pagar en efectivo se le cobrará el primer día de clases. ¡Gracias por su preferencia!")
            
            

        
    

             
    