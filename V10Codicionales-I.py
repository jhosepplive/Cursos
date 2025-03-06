print("Esto es una evalucion")

nota_alumno= int(input("Ingrese un valor "))

def evalucion(nota_alumno):
	valoracion = "aprobado"
	if nota_alumno < 6:
		valoracion = "suspenso"
	return valoracion

print(evalucion(nota_alumno))
