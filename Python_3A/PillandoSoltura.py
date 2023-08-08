# 1.Escribir una programa para encontrar los elementos duplicados de una lista,
#  añadirlos a nueva lista y borrarlos de la lista. Despues imprimir una lista con tan solo los elementos unicos
# 2.Unir dos listas y ordenarlas en orden ascendente 
# 3.Encontrar el segundo numero mas grande da la lista
# 4.Contar el numero de elementos mas grandes que un determinado numero dado por el usuario(supon una lista numerica)
# 5.Crear un script dado un numero introducido por el usuario o determinado al inicio del programa,
# realizar la suma de aquellos numeros que sean dividibles por este 
# 6.Pedir un numero al usuario y dada una lista encontrar el numero mas alto que es inferior al numero introducido
# o determinado al inicio del programa
# 7.Crear un script que extraiga los elementos comunes entre dos listas
# 8.Crear un script para contar el numero de apariciones de un elemento de una lista en dicha lista(P.e en la lista =[23,65,23] el numero de apariciones de 23 es 2 )
# 9.Escribir un programa que lea una lista de enteros y cree una nueva lista que contenga solo numeros positivos de la lista original
# 10.Tomar una lista de strings y crear una nueva lista que contenga el tamaño de los strings de la lista original
# 11.Crear un programa que dada una lista de strings, devuelva otra lista con los strings en mayuscula

# 1

lista = [1,2,3,4,5,6,3,7,8,9,8,10]
print("Lista original:", lista)
elementos_duplicados = []
elementos_unicos = []

for elemento in lista:
    #count para contar elementos
    if lista.count(elemento) > 1:
        if elemento not in elementos_duplicados:
         elementos_duplicados.append(elemento)
    else:
       elementos_unicos.append(elemento)

for elemento in elementos_duplicados:
   lista.remove(elemento)       
print("Elementso unicos son:", elementos_unicos)
print("Elementos duplicados:", elementos_duplicados)
print("Lista nueva:", lista)

print( "---------------") # Para separar los ejercicios!
# 2
lista1 = [3,4,1,5]
lista2 = [6,2,7,8]

lista_combinada = lista1 + lista2
lista_combinada.sort()
print(lista_combinada)


print( "---------------") # Para separar los ejercicios!

# 3
numbers = [3,4,1,5,6,2,7,8]
numbers.sort(reverse=True)
print(numbers[1])

print( "---------------") # Para separar los ejercicios!
# 4

numeros = [3,4,1,5,6,2,7,8]
numero_objetivo = 4
contador = 0
for num in numeros:
   if num > numero_objetivo:
      contador +=1
print(contador)

print( "---------------") # Para separar los ejercicios!
# 5

numeros = [3,4,1,5,6,2,7,8]

divisor = 3
resultado = 0
for num in numeros:
   if num % divisor == 0:
      resultado +=num
print(resultado)
print( "---------------") # Para separar los ejercicios!

# 6 

numeros = [3,4,1,5,6,2,7,8]
numero_objetivo = 4
numeros.sort()

for num in numeros:
   if num < numero_objetivo:
      resultado = num
print(resultado)
print( "---------------") # Para separar los ejercicios!

# 7

lista1 = [1,2,3,4,5,6]
lista2 = [4,5,6,7,8,9]

comunes =[]

for elemento in lista1:
   if elemento in lista2:
      comunes.append(elemento)
print("Elementos comunes", comunes)
print( "---------------") # Para separar los ejercicios!

# 8

numeros = [23,65,23]
objetivo = 23
print(numeros.count(objetivo))

#otro ejemplo:
#for elemento in numeros:
   #print(f"El elemento {elemento}, aparece {numeros.count(elemento)} veces en la lista")

print( "---------------") # Para separar los ejercicios!
# 9

lista_original = [-1,-2,-3,4,-5,6,-7,8,-9]
lista_positiva = []

for numero in lista_original:
   if numero > 0:
      lista_positiva.append(numero)
print("Lista original:", lista_original)
print("Lista positivos:", lista_positiva)
print( "---------------") # Para separar los ejercicios!

# 10
lista_strings = ["hola", "estas", "usando", "python"]
lista_longitudes = []

for string in lista_strings:
   longitud = len(string)
   lista_longitudes.append(longitud)
print("Lista de strings", lista_strings)
print("Lista de longitudes", lista_longitudes)
print( "---------------") # Para separar los ejercicios!

# 11

lista_strings = ["hola", "estas", "usando", "python"]
lista_mayuscula = []

for string in lista_strings:
   lista_mayuscula.append(string.upper())
print("Lista de strings", lista_strings)
print("Lista en matuscula", lista_mayuscula)
print( "---------------") # Para separar los ejercicios!