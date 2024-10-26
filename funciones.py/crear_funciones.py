
#creando una funcion simple 
def saludar():
    print("hola, como estas")

saludar()


    




# creando ua funcion que tenga parametros (variables dentro de la funcion que solo funcionan dentro del def)

 #el parametro es nombre
 
def saludo(nombre,genero):
    genero= genero.lower()
       
    if (genero =="hombre"):
        adjetivo =  "maestro"
    
    elif genero == "mujer":
        adjetivo = "maestra"
        
        
        
    print(f"hola {nombre}, mi {adjetivo} como estas?")
    
saludo ("josue", "hombre")
saludo("karol", "mujer")



