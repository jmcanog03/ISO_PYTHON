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
