 
def leer_fecha():
    """
    Lee por teclado una fecha en formato dd/mm/aaaa y devuelve una tupla
    (dia, mes, anio).
    """
    fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
    dia, mes, anio = map(int, fecha.split('/'))
    return dia, mes, anio


def dias_del_mes(mes, anio):
    """
    Recibe un mes (entero entre 1 y 12) y un año (entero) y devuelve la cantidad
    de días que tiene ese mes en ese año.
    """
    dias_por_mes = [31, 28 + es_bisiesto(anio), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias_por_mes[mes - 1]


def es_bisiesto(anio):
    """
    Recibe un año (entero) y devuelve True si es bisiesto, False en caso contrario.
    """

    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True


def calcular_dia_juliano(fecha):
    """
    Recibe una fecha en formato (dia, mes, anio) y devuelve el día juliano correspondiente.
    """
    dia, mes, anio = fecha
    dias_totales = 0
    for m in range(1, mes):
        dias_totales += dias_del_mes(m, anio)
    dias_totales += dia
    return dias_totales


# Programa principal
fecha = leer_fecha()
dia_juliano = calcular_dia_juliano(fecha)
print("\nEl día juliano correspondiente a la fecha", fecha, "es:", dia_juliano)




