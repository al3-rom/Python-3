# Pedir al user una palabra y luego mostrar por pantalla
# una a una las letras de la palabra introducida empezando por ultima

# Pedimos la palabra

palabra = input("Pon tu palabra: ")

# Mostramos una a una las letras de la palabra

for letra in reversed(palabra):
    print(letra)

    