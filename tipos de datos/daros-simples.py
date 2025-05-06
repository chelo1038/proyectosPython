
horario1 = [0] * 20
horario2 = [0] * 20
horario3 = [0] * 20
horario4 = [0] * 20


horario = int(input("Tenemos 4 horarios disponibles, cual desea reservar? (digite 1,2,3 o 4) "))

if horario == 1:
    asiento = int(input("Que asiento desea reservar en el horario 1?, tenemos disponible del asiento 1 al 20 ")) - 1
    horario1[asiento] = 1
    print(horario1)

elif horario == 2:
    asiento = int(input("Que asiento desea reservar en el horario 2?, tenemos disponible del asiento 1 al 20 ")) - 1
    horario2[asiento] = 1
    print(horario2)

elif horario == 3:
    asiento = int(input("Que asiento desea reservar en el horario 3?, tenemos disponible del asiento 1 al 20 ")) - 1
    horario3[asiento] = 1
    print(horario3)

elif horario == 4:
    asiento = int(input("Que asiento desea reservar en el horario 4?, tenemos disponible del asiento 1 al 20 ")) - 1
    horario4[asiento] = 1
    print(horario4)

else:
    print("Horario no válido.")
