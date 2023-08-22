"""
Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
imprimir la nota media de los alumnos junto con el DNI.
Supón ahora que tu input es un string como este:
"David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
de todos los alumnos en ese string. 

"""
# Lista de listas
base_datos = [["Alvaro", "Gomez", "87654372B", "64782", "1", "7.6", "5.4", "9.3"]]

# Definir la cadena de caracteres con la informacion de un alumno
cadena = "David Fernandez 12311267A 43527 2 2.1 4.6 3.4"

# convertir la cadena de entrada en una lista
datos_alumno = cadena.split() # split separara la cadena en una lista de valores individuales


# introducir la lista con los datos del alumno en la base de datos
base_datos.append(datos_alumno)


for alumno in base_datos:
    
    suma_notas = 0
    n_notas = 0

    dni = alumno[2] # extraemos el DNI del alumno
    # calculamos la media del alumno
    for i in range(5, len(alumno)):
        suma_notas = suma_notas + float(alumno[i]) 
        n_notas = n_notas + 1 # calculamos el numero total de notas del alumno

    nota_media = suma_notas / n_notas # calculamos la nota media del alumno

    print(f"El alumno con dni: {dni}, tiene una nota media de:{nota_media:.2f}") # :.2f-sirve para que nos muestra 2 decimales al final(ejemplo: 2.03211 = 2.03)

