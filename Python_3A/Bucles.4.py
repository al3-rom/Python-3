# Crear un programa en el que se pregunte al usuario por
# una frase y una letra, y muestre por pantalla el numero de veces que aparece la letra en la frase

# Preguntamos la frase y la letra

frase = input("Pon una frase: ")
letra = input("Pon una letra para esta frase: ")

# Bucle para recorrer la frase y 
# contar las apariciones de la letra
contador = 0

for caracter in frase:
    if caracter == letra:
        contador += 1
print("El numero de veces que aparece la letra en la frase es: ", contador)
    
    