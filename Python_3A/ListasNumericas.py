# 1.Crear una lista llamada "numeros" que contenga los siguientes numeros: [1,2,3,4,5,6,7,8,9,10]
# 2.Crear una nueva lista con los numeros pares de la lista anterior en orden inverso
# 3.Ecribir un bucle que recorra la lista "numeros" e imprima el cuadrado de cada numero por consola
# 4.Intentar rehacer los pasos 2 y 3 con el numero de lineas posible
# 5.Usar un metodo que te devuelva el numero mas pequeño de la lista e imprimirlo 
# 6.Hacer lo mismo con el numero mas alto
# 7.Sumar todos los elementos de la lista con y sin un bucle
# 8.Encontrar el indice correspondiente al numero 8 en la lista original y en la lista resultante tras el punto 2

# 1
#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))
print(numeros)
print( " / / / ") #Para separar las listas
# 2
pares_invertidos = []

for numero in reversed(numeros):
    if numero % 2 == 0:
        pares_invertidos.append(numero)
# [::-1] - para inverso(en vez de reversed)

print(pares_invertidos)
print( " / / / ") #Para separar las listas
# 3

for numero in numeros:
    print(numero**2)
print( " / / / ") #Para separar las listas

# 4
pares_invertidos = [numero for numero in numeros if numero % 2 == 0][::-1]
numero_cuadrados = [numero**2 for numero in numeros]
print(pares_invertidos, numero_cuadrados)
# 5
print(min(numeros)) #Numero minimo
print( " / / / ") #Para separar las listas
# 6
print(max(numeros))# Numero maximo
print( " / / / ") #Para separar las listas
# 7

# Con bucle
sumaTotal = 0
for numero in numeros:
    sumaTotal = sumaTotal + numero
print(sumaTotal)
print( " / / / ") #Para separar las listas

# Sin bucle
sumaTotal = sum(numeros)
print(sumaTotal)
print( " / / / ") #Para separar las listas

# 8 
indice_8_orig = numeros.index(8)
indice_8_invert = pares_invertidos.index(8)
print(indice_8_orig, ",",indice_8_invert)