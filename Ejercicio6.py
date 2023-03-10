# numero1=int(input("Introduce el primer numero: "))
# numero2=int(input("Introduce el segundo numero: "))
# def MCD(numero1,numero2):
#     resto=numero1 % numero2
#     if resto == 0:
#         print(f"{numero2} es MCD")
#     else:
#         while numero2%resto != 0:
#             resto=numero2%resto

#         print(f"El MCD es {resto}")
# MCD(numero1,numero2)


import math
import os


def calcularIMCfcmZodiacocontraseña():

    limpiar = (os.system("cls"))
    return(limpiar)

i = 0
while i != 1:
    print("1. Calcular el IMC")
    print("2. Calcular el FCM")
    print("3. Signo del Zodiaco")
    print("4. Contraseña")
    print("5. Todo")
    print("6. Salir")
    numero = int(input("Introduce un número: "))

    if numero == 1:
        peso = float(input("\nIngrese su peso en Kilogramos: "))
        estatura = float(input("Ingrese su estatura en metros: "))
        IMC = round(peso/math.pow(estatura, 2), 1)
        print("Su IMC es de "+str(IMC))
        tecla = input("Pulsar una tecla para continuar: ")
        os.system("cls")
    
    if numero == 2:
        edad=int(input("\nIntroduce tu edad: "))
        fcm=(222-0.775*edad)
        print("Su frecuencia cardiaca máxima es: "+str(fcm))
        tecla = input("Pulsar una tecla para continuar: ")
        os.system("cls")
    
    if numero == 3:
     dia=int(input("\nIntroduce tu día de nacimiento: "))
     mes=int(input("Introduce tu mes de nacimiento: "))
        
   
    

calcularIMCfcmZodiacocontraseña()


