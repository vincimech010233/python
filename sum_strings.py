"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""

def sumStrings(a, b):
    # Rellenar con ceros a la izquierda para igualar la longitud de las cadenas
    length = max(len(a), len(b))
    a = a.zfill(length)
    b = b.zfill(length)
    
    carry = 0
    result = []

    for i in range(length - 1, -1, -1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])

# Ejemplo de uso
num1 = '123456789012345678901234567890'
num2 = '987654321098765432109876543210'
result = sumStrings(num1, num2)
print(result)
