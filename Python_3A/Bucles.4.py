# Crear un programa en el que se pregunte al usuario por
# una frase y una letra, y muestre por pantalla el numero de veces que aparece la letra en la frase

# Preguntamos la frase y la letra

frase = input("Pon una frase: ")
letra = input("Pon una letra para esta frase: ")
veces = 0

while letra in frase:
    veces = veces + 1
    
print(veces)
    
    