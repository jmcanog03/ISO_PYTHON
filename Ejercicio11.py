# 11. Implementa una función que dibuje un menú en la pantalla con distintas opciones.
# 1. Acción 1.
# 2. Acción 2.
# 3. Acción 3.
# 4. Salir
# Introduzca una opción:
# Si se introduce ‘1’, se llamará a una función que muestre “Se ha pulsado 1”, lo
# mismo con las demás.
# Limpia la pantalla cada vez que se vaya a imprimir el menú.


def dibujar_menu():
    """Dibuja un menú en la pantalla con distintas opciones."""
    print("\nMenú:")
    print("1. Acción 1.")
    print("2. Acción 2.")
    print("3. Acción 3.")
    print("4. Salir")
    opcion = input("\nIntroduzca una opción: ")
    return opcion

while True:
    opcion = dibujar_menu()

    if opcion == "1":
        print("\nHa elegido la Acción 1.")
        # Aquí puedes añadir el código para realizar la Acción 1.
    elif opcion == "2":
        print("\nHa elegido la Acción 2.")
        # Aquí puedes añadir el código para realizar la Acción 2.
    elif opcion == "3":
        print("\nHa elegido la Acción 3.")
        # Aquí puedes añadir el código para realizar la Acción 3.
    elif opcion == "4":
        print("\nSaliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")

