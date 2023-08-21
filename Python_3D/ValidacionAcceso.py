# Crear un script que verifique si el nombre de usuario y la 
# contraseña ingresados son correctos y permita el acceso solo si ambos son correctos

nombres_user = ["juan123", "ana456", "pedro789"]

passwords = ["clave123", "clave456", "clave789"]

usuario = input("Ingrese su nombre de usuario: ")

password = input("Ingrese su contraseña: ")

credenciales = False

for i in range(len(nombres_user)):
    if nombres_user[i] == usuario and passwords[i] == password:
        credenciales = True
        
if credenciales:
    print("Bienvenido!")
else:
    print("Acceso denegado!")
  