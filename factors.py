def factors(number):
    if not isinstance(number, int) or number < 1:
        return -1
    
    factors = []
    
    for i in range(number, 0, -1):
        if number % i == 0:
            factors.append(i)
    
    return factors

# Ejemplo de uso:
input_number = 54
result = factors(input_number)
print(result)
