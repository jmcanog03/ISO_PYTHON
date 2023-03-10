# def Intercambiar(mayor,menor):
# 	if mayor<menor:
# 		return menor,mayor
# 	else:
# 		return mayor,menor


# def CalcularMCD(num1,num2):
# 	# Se divide el número mayor entre el menor.
# 	num1, num2 = Intercambiar(num1,num2)
# 	resto = num1 % num2
# 	if resto == 0: # Si la división es exacta, el divisor es el MCD.
# 		return num2
# 	else:
# 		# Si la división no es exacta, dividimos el divisor entre el resto obtenido y 
# 		# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# 		return CalcularMCD(num2,resto)


# def LeerFraccion():
# 	num = int(input("Numerador:"))
# 	den = int(input("Denominador:"))
# 	num,den = SimplificarFraccion(num,den)
# 	return num,den

# def SimplificarFraccion(num,den):
# 	mcd = CalcularMCD(num,den)
# 	num = num / mcd
# 	den = den / mcd
# 	return num,den


# def EscribirFraccion(num,den):
# 	if den!= 1:
# 		print(num)
# 		print("---")
# 		print(den)
# 	else:
# 		print("")
# 		print(num)
# 		print("")



# def SumarFracciones(n1,d1,n2,d2):
# 	nr = n1*d2 + d1*n2
# 	dr = d1 * d2
# 	nr,dr = SimplificarFraccion(nr,dr)
# 	return nr,dr



# def RestarFracciones(n1,d1,n2,d2):
# 	nr = n1*d2 - d1*n2
# 	dr = d1 * d2
# 	nr,dr = SimplificarFraccion(nr,dr)
# 	return nr,dr



# def MultiplicarFracciones(n1,d1,n2,d2):
# 	nr = n1 * n2
# 	dr = d1 * d2
# 	nr,dr = SimplificarFraccion(nr,dr)
# 	return nr,dr


# def DividirFracciones(n1,d1,n2,d2):
# 	nr = n1 * d2
# 	dr = d1 * n2
# 	nr,dr = SimplificarFraccion(nr,dr)
# 	return nr,dr



# while True:
# 	print("1.- Sumar dos fracciones")
# 	print("2.- Restar dos fracciones")
# 	print("3.- Multiplicar dos fracciones")
# 	print("4.- Dividir dos fracciones")
# 	print("5.- Salir")
# 	opcion = int(input())
# 	if opcion>=1 and opcion <=4:
# 		print("Fracción 1:")
# 		num1,den1= LeerFraccion()
# 		print("Fracción 2:")
# 		num2,den2= LeerFraccion()
# 	if opcion == 1:
# 		print("Sumar fracciones")
# 		numr,denr = SumarFracciones(num1,den1,num2,den2)
# 		EscribirFraccion(numr,denr)
# 	elif opcion == 2:
# 		print("Restar fracciones")
# 		numr,denr = RestarFracciones(num1,den1,num2,den2)
# 		EscribirFraccion(numr,denr)
# 	elif opcion == 3:
# 		print("Multiplicar fracciones")
# 		numr,denr = MultiplicarFracciones(num1,den1,num2,den2)
# 		EscribirFraccion(numr,denr)
# 	elif opcion == 4:
# 		print("Dicidir fracciones")
# 		numr,denr = DividirFracciones(num1,den1,num2,den2)
# 		EscribirFraccion(numr,denr)
# 	elif opcion == 5:
# 		break
# 	else:
# 		print("Opción incorrecta")
	

def leer_fraccion():
    """
    Lee por teclado una fracción en formato a/b y devuelve una tupla (numerador,
    denominador) simplificada.
    """
    fraccion = input("Ingrese una fracción en formato a/b: ")
    numerador, denominador = map(int, fraccion.split('/'))
    mcd = calcular_mcd(numerador, denominador)
    return numerador // mcd, denominador // mcd


def escribir_fraccion(fraccion):
    """
    Escribe en pantalla una fracción en formato a/b. Si el denominador es 1, se
    muestra sólo el numerador.
    """
    numerador, denominador = fraccion
    if denominador == 1:
        print(numerador)
    else:
        print(numerador, "/", denominador)


def calcular_mcd(a, b):
    """
    Recibe dos números enteros a y b y devuelve su máximo común divisor.
    """
    while b != 0:
        a, b = b, a % b
    return a


# Programa principal
fraccion = leer_fraccion()
print("La fracción ingresada es:")
escribir_fraccion(fraccion)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
mcd = calcular_mcd(num1, num2)
print("El máximo común divisor de", num1, "y", num2, "es:", mcd)
