from math import factorial

def all_permuted(array_length):
    subfactorial = 0
    for i in range(array_length + 1):
        subfactorial += ((-1)**i) * factorial(array_length) / factorial(i)
    return int(subfactorial)

# Example:
array_length = 4
result = all_permuted(array_length)
print(result)  # Output: 9
