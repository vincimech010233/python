def histogram(values, bin_width):
    # Paso 1: Inicialización
    if not values:
        return []
    max_value = max(values)
    bins = [0] * ((max_value // bin_width) + 1)
    
    # Paso 2: Conteo
    for value in values:
        bin_index = value // bin_width
        bins[bin_index] += 1
    
    # Paso 3: Retorno
    return bins

# Ejemplos de uso
print(histogram([1, 1, 0, 1, 3, 2, 6], 1))  # Output: [1, 3, 1, 1, 0, 0, 1]
print(histogram([1, 1, 0, 1, 3, 2, 6], 2))  # Output: [4, 2, 0, 1]
print(histogram([7], 1))  # Output: [0, 0, 0, 0, 0, 0, 0, 1]
