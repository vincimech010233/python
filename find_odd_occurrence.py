def find_odd_occurrence(arr):
    count_dict = {}  # Diccionario para contar las ocurrencias de cada número

    # Contar las ocurrencias de cada número en el arreglo
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Buscar el número que aparece un número impar de veces
    for num, count in count_dict.items():
        if count % 2 != 0:
            return num

# Examples
print(find_odd_occurrence([7]))  # Debería devolver 7
print(find_odd_occurrence([0]))  # Debería devolver 0
print(find_odd_occurrence([1, 1, 2]))  # Debería devolver 2
print(find_odd_occurrence([0, 1, 0, 1, 0,]))  # Debería devolver 0
print(find_odd_occurrence([0, 1, 0, 1, 0, 1, 3, 1, 0, 1]))  # Debería devolver 1
print(find_odd_occurrence([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))  # Debería devolver 4

# Assert
assert find_odd_occurrence([7]) == 7
assert find_odd_occurrence([0]) == 0
assert find_odd_occurrence([1, 1, 2]) == 2
print("All tests passed!")