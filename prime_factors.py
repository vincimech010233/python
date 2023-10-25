"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

def prime_factors(n):
    assert n > 1, "El número debe ser mayor que 1."
    
    factors = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            exponent = 0
            while n % divisor == 0:
                n //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1 if divisor == 2 else 2
    
    factor_string = ""
    for factor, exponent in factors:
        if exponent == 1:
            factor_string += f"({factor})"
        else:
            factor_string += f"({factor}**{exponent})"
    
    return factor_string

# Pruebas automatizadas
assert prime_factors(86240) == "(2**5)(5)(7**2)(11)"
assert prime_factors(28) == "(2**2)(7)"
assert prime_factors(75) == "(3)(5**2)"
assert prime_factors(17) == "(17)"

print("Todas las pruebas pasaron correctamente.")
print(prime_factors(86240))