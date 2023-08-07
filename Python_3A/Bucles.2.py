# Hacer un programa que almacene la cadena de caracteres contraseña en una variable
# preguntar al usuario por la contraseña hasta que introduzca la contraseña correcta


password = "secreto"


password_entrada = ""


while password_entrada != password:
    password_entrada = input("Introduzca la contraseña: ")
    if password_entrada != password:
        print("Contraseña incorrecta! Intentelo de nuevo!")
print("Contraseña es correcta! Bienvenido!")