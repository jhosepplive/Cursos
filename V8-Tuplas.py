
#Nota:Las tuplas no se pueden modificar ni devolver el indice

miTupla = ("Jose" , "Wendy","Britt" , "Lucia")

cumple = ("Jose " , 10 , "Oct" , 1991)

#Se declara una variable para guardar el nombre, dia, mes y año de la tupla cumple
nombre , dia , mes , Año= cumple 

miLista = ["Angel" , "Josue" , "Tury"]

#El metodo list convierta una tupla en lista
miList = list(miTupla)

#El metodo tuple comvierte una lista en tupla
miLista2 = tuple(miLista)

#Imprime los valores de la variable miTupla
print("Los valores de mi variable tupla son " ,miList ,"\n")

#Imptime los valores de la variable miLista
print("Los valores de la variable lista son" ,miLista2 , "\n")

#El metodo in devuelve si un elementonse encuentra dentro de una tupla
print("Jose" in miTupla , "\n")

#El metodo count devuelve cuantad veces se encuentra el valor en la tupla
print("El valor jose se encuentra almacenado",miTupla.count("Jose"), "\n")

#El metodo len devuelve la logitud de una tupla
print("La longitud de la tupla es de" ,len(miTupla) , "\n")

#Imprime los valores de la tupla mi cumple, almacenados en la variable nombre, mes, dia, año.
print("Los valores almacenados en las varoables son: " , cumple , "\n")

