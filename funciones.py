import os
import math

# Función que calcula el IMC

def Calcularimc():
    peso = float(input("\nIngrese su peso en Kilogramos: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    IMC = round(peso/math.pow(estatura, 2), 1)
    print("Su IMC es de "+str(IMC))
    

    return(IMC)

# Función que calcula la frecuancia cardiaca máxima según la edad
def calcularFCM():
    edad=int(input("\nIntroduce tu edad: "))
    fcm=(212-0.775*edad)
    print("Su frecuencia cardiaca máxima es: "+str(fcm))
    

    return(edad)

# Función que calcula el signo del zodiaco
def SignoDelzodiaco():
    dia=int (input ("\nIntroduce tu día de nacimiento: "))
    mes=int (input ("Introduce tu mes de nacimiento: "))

    if (dia>=21 and mes==3) or (dia<=20 and mes==4):
        print ("Aries")
    
    if (dia>=24 and mes==9) or (dia<=23 and mes==10):
        print ("Libra")

    if (dia>=21 and mes==4) or (dia<=21 and mes==5):
        print ("Tauro")
    
    if (dia>=24 and mes==10) or (dia<=22 and mes==11):
        print ("Escorpio")
    
    if (dia>=22 and mes==5) or (dia<=21 and mes==6):
        print ("Geminis")

    if (dia>=23 and mes==11) or (dia<=21 and mes==12):
        print ("Sagitario")
    
    if (dia>=21 and mes==6) or (dia<=23 and mes==7):
        print ("Cancer")

    if (dia>=22 and mes==12) or (dia<=20 and mes==1):
        print ("Capricornio")

    if (dia>=24 and mes==7) or (dia<=23 and mes==8):
        print ("Leo")

    if (dia>=21 and mes==1) or (dia<=19 and mes==2):
        print ("Acuario")

    if (dia>=24 and mes==8) or (dia<=23 and mes==9):
        print ("Virgo")

    if (dia>=20 and mes==2) or (dia<=20 and mes==3):
        print ("Piscis")

    

    return (dia,mes)

# Función que genera una contraseña al usuario
def GenerarContraseña():
    nombre=input("\nIntroduce tu nombre: ")
    apellidos=input("Introduce tus apellidos: ")
    contraseña=nombre[:1] + apellidos[:3] + apellidos[-3:]
    print(f"Tu contreaseña es: {contraseña}")
   

    return(contraseña)


# Función que calcula el menú 
def menu():    

    i=0
    while i!=1:

        print ("1. Calcular IMC.")
        print ("2. Calcular FMC")
        print ("3. Signo zodiaco")
        print ("4. Contraseña")
        print ("5. Todo")
        print ("6. Salir")

        numero=int(input("\nIntroduce un número: "))

        if numero == 1:
           
           Calcularimc()
           tecla = input("\nPulsar una tecla para continuar: ")
           os.system("cls") # Aquí he metido una función dentro de otra
        
        if numero == 2:
            calcularFCM()
            tecla = input("\nPulsar una tecla para continuar: ")
            os.system("cls")
        
        if numero == 3:
            SignoDelzodiaco()
            tecla = input("\nPulsar una tecla para continuar: ")
            os.system("cls")

        
        if numero == 4:

            GenerarContraseña()
            tecla = input("\nPulsar una tecla para continuar: ")
            os.system("cls")

        if numero == 5:

            Calcularimc()
            calcularFCM()
            SignoDelzodiaco()
            GenerarContraseña()
            tecla = input("\nPulsar una tecla para continuar: ")
            os.system("cls")
        

        if numero == 6:
            print("Saliendo......")
            tecla = input("\nPulsar una tecla para continuar: ")
            os.system("cls")
            break
menu()





