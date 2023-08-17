"""
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.

Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase. 

"""

estudiantes = ["Juan", "Maria", "Pedro"]

# Nuestra base de datos
database = [ ["Juan", [6.4,7.0,9.1]], 
            ["Maria", [8.2,9.8,6.5]],
            ["Pedro", [7.1,8.4,5.2]]
            ]

# Calcular la nota media de cada estudiante
for data in database:
    # Extraemos el nombre del estudiante
    nombre = data[0]
      # Extraemos la lista de notas
    notas = data[1]
    # Calculamos la media del estudiante
    media = sum(notas) / len(notas)
    print(f"La media de {nombre} es {media :.2f}")


# La nota media de toda la clase
total_notas = 0
num_notas = 0
for data in database:

    notas = data[1]

    total_notas = total_notas + sum(notas)
    num_notas = num_notas + len(notas)
    
    
media_clase = total_notas / num_notas
print(f"La nota media de la clase es:{media_clase} ")

    


