def solve(arr):
    # Crear un diccionario vacío para realizar un seguimiento de las últimas ocurrencias de cada elemento.
    last_occurrence = {}
    
    # Crear una lista vacía para almacenar el resultado.
    result = []
    
    # Recorrer la lista desde el final al principio.
    for i in range(len(arr) - 1, -1, -1):
        element = arr[i]
        
        # Si el elemento no está en el diccionario de últimas ocurrencias, agregarlo a la lista de resultados y al diccionario.
        if element not in last_occurrence:
            result.append(element)
            last_occurrence[element] = i
    
    # Invertir la lista de resultados para obtener el orden correcto.
    result.reverse()
    
    return result

input_list1 = [3, 4, 4, 3, 6, 3]
result1 = solve(input_list1)
print(result1)
# Salida esperada: [4, 6, 3]