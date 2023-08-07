# 1.Crear una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
# de caracteres: manzana, platano, cereza, pera, higo, frambuesa y fresa

# 2.Usa la funcion len()-para imprimir la longitud de la lista de frutas

# 3.Acceder al objeto numero 3 de la lista e imprimir por consola

# 4.Modificar el segundo objeto de la lista y cambiarlo a mora

# 5.Añadir el string mango al final de la lista

# 6.Usar el metodo insert() y añadir el string (uva) al comienzo de la lista

# 7.Usar el bucle para recorrer la lista e imprimir cada fruta por la consola

# 8.Usar el metodo pop() para eliminar el ultimo de la lista y guardarlo en una variable llamada (ultima_fruta)

# 9.Realizar un bucle que recorra la lista e imprimir cada una de las frutas por consola

# 10.Modificar el script para que imprima tambien la longitud de cada nomnbre de fruta por consola

# 11.Modificar el script para que recorra la lista de frutas y solo imprima aquellos nombres que tengan mas de 5 caracteres

# 12.Usar el metodo remove() para borrar el string (cereza) de la lista

# 13.Usar el metodo clear() para vaciar la lista


#1
frutas=["manzana", "platano", "cereza", "pera", "higo", "frambuesa", "fresa"]
#2
print(len(frutas))
#3
print(frutas[2])
#4
frutas[1] = "mora"
#5
frutas.append("magona")
#6
frutas.insert(0, "uva")
#7
for fruta in frutas:
    print(fruta)
print(" /// ") #para separar con otras listas
#8
ultima_fruta = frutas.pop()
#9
for fruta in frutas:
    print(fruta)
print(" /// ") #para separar con otras listas
#10
for fruta in frutas:
    print(fruta)
    print(len(fruta))
print(" /// ") #para separar con otras listas
#11
for fruta in frutas:
    if len(fruta) > 5:
     print(fruta)
print(" /// ") #para separar con otras listas
#12
frutas.remove("cereza")
print(frutas)
print(" /// ") #para separar con otras listas
#13
frutas.clear()
print(frutas)