""" print("Programa de Becas ")

distancia_escuela = int(input("Introduce la distancia a la escuela en km " ))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el numeron de hermanos "))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario anual bruto "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000 :
	print("Tienes derecho a Beca ")
	
else :
	print("No tiene beca ")
"""
print("Asiganaturas: Matematicas , Informatica , Fisica ")

opcion = input("Ingresa una asignatura ")

asignatura = opcion.lower()

if asignaturas in ("Matematicas " , "Informatica " , "Fisica ") :
	print("Asignatura elegida " + asiganturas) 
	
else :
	print("La asignatura elegida no esta completada")
