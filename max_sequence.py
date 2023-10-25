def max_sequence(arr):
    max_ending_here = max_so_far = 0

    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Ejemplo de uso
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_sequence(arr)
print(result)  # Debería imprimir 6
