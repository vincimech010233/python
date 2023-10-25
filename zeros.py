"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""


def zeros(n):
    count = 0
    i = 5 # # Inicializamos i en 5, ya que estamos buscando factores de 5.
    while n // i > 0: # mientras n dividido por i sea mayor que 0.
        count += n // i # sumamos la cantidad de factores de 5
        i *= 5 # i por 5 para buscar factores de 5 en potencias superiores.
    return count

print(zeros(6))  
print(zeros(12))  
