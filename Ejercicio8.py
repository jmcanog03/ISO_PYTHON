import os


def Convertir_A_Segundos(h, m, s):
    return h * 3600 + m * 60 + s


def Convertir_A_HMS(seg):
    # Horas = Divisíón entera de los segundos entre 3600
    h = seg//3600
    # Decremento los segundos que me quedan por convertir
    seg = seg - h*3600
    # Minutos = División entera de los segundos entre 60
    m = seg//60
    # Decremento los segundos que me quedan por convertir
    seg = seg - m*60
    # Lo que me quedan corresponden a los segundos
    s = seg
    return h, m, s


while True:

    print("\n1.- Convertir a segundos")
    print("2.- Convertir a horas, minutos y segundos")
    print("3.- Salir")
    opcion = int(input("\nIntroduce una opción: "))
    if opcion == 1:
        hor = int(input("Horas: "))
        minu = int(input("Minutos: "))
        seg = int(input("Segundos: "))
        print("Corresponde a", Convertir_A_Segundos(
            hor, minu, seg), "segundos.")
        tecla = input("\nPulsar una tecla para continuar: ")
        os.system("cls")

    elif opcion == 2:
        segund = int(input("\nSegundos: "))
        hor, minu, seg = Convertir_A_HMS(segund)
        print("Corresponde a ", hor, ":", minu, ":", seg)
        tecla = input("\nPulsar una tecla para continuar: ")
        os.system("cls")

    elif opcion == 3:
        print("Saliendo......")
        tecla = input("\nPulsar una tecla para continuar: ")
        os.system("cls")
        break
    else:
        print("Opción incorrecta")

