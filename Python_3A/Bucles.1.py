# Pedir al usuario un numero entero y mostar por pantalla una estructura
# como esta: 
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# Donde el valor de entrada es el numero de estrellas en el centro de la estructura

# Pedimos el numero y convertimos en un numero entero: ( int() )
num = int(input("Pon un numero: "))

# Hacemos el bucle
for i in range(1, num + 1):
    print("*"*i + " " * (num - i))
    
for i in range(num-1, 0, -1):
    print("*" * i + " " * (num - 1))

