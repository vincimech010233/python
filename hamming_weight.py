def hamming_weight(n):
    count = 0
    while n:
        count += n & 1 # n & 1, obtienes 1 si el último bit de n es 1 y 0 si es 0.
        n >>= 1 # desplaza el número n un bit hacia la derecha
    return count

# Examples:
print(hamming_weight(10))  # Debería imprimir 2
print(hamming_weight(21))  # Debería imprimir 3


def custom_hamming_weight(n):
    # bin(n) devuelve una cadena que comienza con "0b", por lo que eliminamos esos dos primeros caracteres con [2:].
    binary_representation = bin(n)[2:]  
    count = 0
    for bit in binary_representation:
        if bit == '1':
            count += 1
    return count

# Examples:
print(custom_hamming_weight(10))  # Debería imprimir 2
