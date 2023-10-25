def square_free_part(n):
    i = 2  # Comienza con el primer número primo
    square_free = 1  # Inicializa la parte libre de cuadrados con 1
    while i * i <= n:  # Mientras el cuadrado de i sea menor o igual a n
        if n % i == 0:  # Si i es un factor de n
            square_free *= i  # Multiplica la parte libre de cuadrados por i
            while n % i == 0:
                n //= i  # Divide n por i hasta que i ya no sea un factor
        i += 1  # Prueba el siguiente número (no es necesario verificar solo números primos, ya que los compuestos ya habrían sido cubiertos)
    if n > 1:
        square_free *= n  # Si n es un primo restante, multiplícalo en la parte libre de cuadrados
    return square_free

# Ejemplo de uso:
print(square_free_part(24))  # Output: 6
