def Login(nombre,password,intentos):
	intentos += 1
	if nombre == "usuario1" and password == "asdasd":
		return(True,intentos)
	else:
		return(False,intentos)

cuantasveces = 0

while True:
	usuario = input("Introduce tu usuario: ")
	clave = input("Introduce tu contraseña: ")
	entrar,cuantasveces = Login(usuario,clave,cuantasveces)
	if not entrar:
		print("Error. Nombre de usuario o contraseña incorrecta.")
	if entrar or cuantasveces == 3: 
		break
if entrar:
	print("Bienvenidos al sistema")
else: # He llegado a los tres intentos
	print("No has entrado en el sistema")


def main():

	cuantasveces = 0

	while True:
		usuario = input("Introduce tu usuario: ")
		clave = input("Introduce tu contraseña: ")
		entrar,cuantasveces = Login(usuario,clave,cuantasveces)
		if not entrar:
			print("Error. Nombre de usuario o contraseña incorrecta.")
		if entrar or cuantasveces == 3: 
			break
	if entrar:
		print("Bienvenidos al sistema")
	else: # He llegado a los tres intentos
		print("No has entrado en el sistema")
main()

# import math

# def areaPerimetroCircunferencia(radio):
# 	area=math.pi *radio * radio
# 	perimetro=2 * math.pi * radio
# 	return area,perimetro

# def mostrarResultados(rad,are,per):
# 	print(f"El área del cículo de {rad} es: {round(are,2)} centrimetros cuadrados")
# 	print(f"El perímetro de la circunferencia de radio {rad} es: {round(per,2)} centímetros")

# def main():
# 	radio=float(input("Introduce el radio en centímetros: "))
# 	a,p=areaPerimetroCircunferencia(radio)
# 	mostrarResultados(radio,a,p)
# main()

# Otro ejemplo 

def loginn(nombre , contraseña , intentos):
	intentos-=1
	if nombre=="usuario1" and contraseña=="asdasd":
		print("Se ha logeado perfectamente.....")
		return(True,intentos)
	else:
		print(f"Incorrecto! , Te quedan {intentos} intentos.")
		return(False,intentos)
def main():
	correcto=False
	intentos=3
	while correcto==False and intentos>0:
		nombre=input("Introduzca su usuario: ")
		password=input("Introduzca la contraseña: ")
		correcto , intentos = loginn(nombre,password,intentos)
main()