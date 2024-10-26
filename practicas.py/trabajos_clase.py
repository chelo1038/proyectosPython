
# suponga que el servicio de bus es de una zona lejana y solo hay 4 horarios 
# int son valores enteros 

horario1= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
horario2= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
horario4= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
horario3= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
horario= int (input("tenemos 4 horarios disponibles, cual desea reservar? (digite 1,2,3 o 4) "))


#asignacion al indice horario[asiento]= 1

if horario ==1:
    asiento = int (input("que asiento desea reservar en horario 1?, tenermos disponible del asiento 1 al 20 ")) -1 
    horario1[asiento] =1 
    print("felicidades, reservo el asiento numero", (asiento+1) , "en el primer horario, lista de horaios", horario1)
    
    
elif horario==2:
    asiento2= int (input("que asiento desea reservar en horario 2?, tenermos disponible del asiento 1 al 20 "))-1
    horario2[asiento2] =1 
    print("felicidades, reservo en el asiento numero", (asiento2+1), "lista de asientos disponibles", horario2)
    
elif horario==3:
    asiento3= int (input("que asiento desea reservar en el horario 3?, tenemos disponible del asiento 1 al 20 "))-1
    horario3[asiento3] =1 
    print("felicidades, reservo en el asiento numero", (asiento3+1),"lista de asientos disponibles", horario3)
    
elif  horario==4:
    asiento4= int (input("que asiento desea reservar en el horario 4?, tenemos disponible del asiento 1 al 20 "))-1
    horario4[asiento4] =1 
    print("felicidades, reservo en el asiento numero", (asiento4+1), "lista de asientos disponibles",horario4) 
    
    
else:
 print("digito un numero incorrecto, los horarios correctos son 1,2,3 y 4 ")
    
#funciona bien 















