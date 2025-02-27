familia = ["Jose" , "Wendy" , "Britt"]

#La funcion append permite insertar un valo al final de una lista
familia.append("Lucia")

#La funcion insert  inserta el valor de una lista indicando la posicion del indice
familia.insert(2,"Sosa")

#La funcion extend te permite insertar mas valores a una lista
familia.extend(["Angel", "Lupe", "Tury", "Josue"])

#Debuelve el valor del indice almacenado, solo que en este esditor de codigo no me fuciona la funcion.
familia(familia.index("Jose"))

#Imprime las  listas
print(familia)

#Imprime un valor de la lista dandole un indice
print(familia[1])

#Imprime el rango de 2 valores de la lista
print(familia[1:2])