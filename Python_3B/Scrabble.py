# Crear una lista de caracteres llamada "palabras" que representa
# una mano de Scrabble. Cada string contiene dos caracteres: el primer caracter es la letra de una ficha y el segundo el numero que representa los
# dos puntos de la ficha. Por ejemplo, el string "A5" representa la ficha con la letra A y un valor de 5 puntos.
# Crear un script que calcule el valor total de los puntos en una mano de sc rabble. El valor total sera la suma de los puntos de todas las ficahs de la mano.

mano_scrabble = ["A5", "B3", "C41", "H8", "D13"]

puntos = 0

for ficha in mano_scrabble:
    puntos = puntos + int(ficha[1:])

print("El numero total de puntos de tu mano es:", puntos)