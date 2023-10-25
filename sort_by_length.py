def sort_by_length(arr):
    # La función sorted() de Python permite una personalización del ordenamiento
    # a través del argumento 'key'. En este caso, le estamos diciendo que ordene
    # las cadenas en el arreglo 'arr' según su longitud.
    return sorted(arr, key=len)

list = ["Telescopes", "Glasses", "Eyes", "Monocles"]

print(sort_by_length(list))