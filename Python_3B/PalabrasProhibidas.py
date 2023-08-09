# 1.Definir una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras
# 2.Filtrar las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
# aquella palabras que no tienen ninguna letra prohibida



# 1
lista_original = ["coche", "telefono", "cuchillo", "banana", "microfono"]
letras_prohibidas = ["a", "t", "l"]

# 2 
palabras_filtradas = [palabra for palabra in lista_original if all(letra not in palabra for letra in letras_prohibidas)]

         
            

print(palabras_filtradas)

