"""edad = 145

if 0 < edad < 100 :
	print("Las Edad es correcta ")
	
else :
	print("La edad es incorrecta ")
	"""
salario_presidente = int(input("Ingrese el salario del presidente "))
print("Salario presidente " + str(salario_presidente))

salario_director = int(input("Ingrese el salario del director "))
print("Salario del ditrctor " + str(salario_director))

salario_jefe_area = int(input("Ingrese el salario del jafe de area "))
print("Salario del jefe de area " + str(salario_jefe_area))

salario_administrativo = int(input("Ingrese el salario del administrativo "))
print("Salario del administrativo " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente :
	print("Todo va bien " , "\n")
else :
	print("Hay un error en el sistema" , "\n")