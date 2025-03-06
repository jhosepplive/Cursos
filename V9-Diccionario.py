#En este apartado podemos localizar un diccionario que tiene en su interior una lista y un subdiccionario.
midiccionario = {"Alemania" : "Berlin" , "Francia" : "Paris", "Reino unido" : "Londres", "España":"Madrid", "Fechas":{"Temporadas":["1992 , 1992 , 1993 , 1994" ] }}

milista = ["Jose" , "Wendy" , "Britt"]

#Desde un diccionario podemos agregar elementos a una lista
diccLista= {milista[0]:"Angel" , milista[1]:"Josue" , milista[2]:"Tury"}

midiccionario["Italia"] = "Lisboa"
#Accede a una clave del diccionario

#Imprimen la pareja de un elemento del doccionario
print("La clave de un elemento del diccionario es" , midiccionario["Alemania"] ,"\n")

#Imprime todas las claves del diccionario
print("Las claves de los diccionarios son" ,midiccionario , "\n")

#Sobrescribe un elemento del diccionario
midiccionario["Italia"] = "Roma"

#Imprime el diccionario con el nuevo valor sobrescrito Italia = Roma
print(midiccionario , "\n")

#Elima una una pareja del diccionario
del midiccionario["Reino unido"]

print(midiccionario , "\n")

#El metodo keys() devuele las claves pricipalrs del diccionario
print("Estas son las principales claves del diccionario", midiccionario.keys(), "\n")

# El metodo values() devuelve el valor de las claves del diccionario.
print("El valor de las claves del diccionario son las siguientes" , midiccionario.values(), "\n")

#El metodo len() devuelve la cantidad de valores que tiene un diccionario
print("La cantidad de valores del diccionario es de : " , len(midiccionario) , "\n")

#Con el ciclo for podemos recorrer e imprimir un diccionario
for i in midiccionario :
	print(i, "\n")

#Con este print imprimimos los elementos agregados a una lista mediante un diccionario.
print(diccLista)