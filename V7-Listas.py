familia = ["Jose" , "Wendy" , "Britt"] *5

familia2 =["Matilde" , "Victor", "Chicola"]*5


#La funcion append permite insertar un valo al final de una lista
familia.append("Lucia")

#La funcion insert  inserta el valor de una lista indicando la posicion del indice
familia.insert(2,"Sosa")

#La funcion extend te permite insertar mas valores a una lista
familia.extend(["Angel", "Lupe", "Tury", "Josue"])


#Elimina un valor de la lista
familia.remove("Tury")

#Elimina el ultimo valor de la lista
familia.pop()

#Debuelve el valor del indice almacenado, solo que en este esditor de codigo no me fuciona la funcion.
#familia(familia.index("Jose"))

#Imprime las  listas
print(familia)

#Imprime un valor de la lista dandole un indice
print(familia[1])

#Imprime el rango de 2 valores de la lista
print(familia[1:2])

#Concatena la 2 lista de familia y familia2
print(familia + familia2)