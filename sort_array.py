"""
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    # Return a sorted array.
"""


def sort_array(source_array):
    # Crear una lista de los números impares en el array fuente, ordenados en forma ascendente
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])
    
    # Inicializar una lista para almacenar el resultado final
    result = []
    
    # Inicializar un índice para recorrer los números impares ordenados
    odd_index = 0
    
    # Iterar a través de cada número en el array fuente
    for num in source_array:
        if num % 2 != 0:
            # Si el número es impar, agregar el siguiente número impar ordenado
            # y actualizar el índice de números impares ordenados
            result.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            # Si el número es par, simplemente agregarlo al resultado
            result.append(num)
    
    # Devolver el resultado final
    return result

# Casos de prueba
print(sort_array([7, 1]))  # [1, 7]
print(sort_array([5, 8, 6, 3, 4]))  # [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

