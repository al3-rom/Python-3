# 1.Definir una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras
# 2.Filtrar las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
# aquella palabras que no tienen ninguna letra prohibida



# 1
lista_original = ["coche", "telefono", "cuchillo", "banana", "microfono"]
letras_prohibidas = ["a", "t", "l"]

# 2 
palabras_filtradas = []

for palabra in lista_original:
    incluir = True
    for letra_prohibida in letras_prohibidas:         
        if letra_prohibida in palabra:
            incluir = False
        
    if incluir:
        palabras_filtradas.append(palabra)
            

print(palabras_filtradas)

